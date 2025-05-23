# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""Download analysis results from a Log Analytics workspace"""

import json
import logging
from datetime import datetime, timedelta
from typing import Optional

import pandas as pd
from jinja2 import Template
from scipy.stats import false_discovery_control

from .log_analytics import LogAnalyticsWorkspace, query_df
from .results import AnalysisMetadata, AnalysisResults, VariantMetadata

QUERY_ANALYSIS = """
OEWExperimentScorecards
| where FeatureName == '{{ feature_flag }}' and Label == '{{ label }}'
{% if allocation_id %}| where AllocationId == '{{ allocation_id }}'{% endif %}
| summarize arg_max(TimeGenerated, *) by ScorecardId
| summarize arg_max(TimeGenerated, *) by AnalysisEndTime
| summarize arg_max(AnalysisEndTime, *)
| project ScorecardId, FeatureName, Label, AllocationId, AnalysisStartTime, AnalysisEndTime, 
          Variants=Insights.Assignment
| where FeatureName == '{{ feature_flag }}' and Label == '{{ label }}'
""".strip()

QUERY_SCORECARD = """
OEWExperimentScorecardMetricPairs
| where ScorecardId == '{{ scorecard_id }}'
| summarize arg_max(TimeGenerated, *) by ScorecardId, MetricId, TreatmentVariant, ControlVariant
""".strip()


def treatment_effect_assessment(df: pd.DataFrame) -> bool:
    """Overall assessment of whether a treatment effect was detected"""
    df_evaluated = df.loc[
        lambda df: ~df["MetricCategories"].str.contains("__Internal__")
        & ~df["TreatmentEffect"].isin(["Zero samples", "Too few samples"])
        & (df["TreatmentStandardErrorNormalized"] > 0)
        & (df["ControlStandardErrorNormalized"] > 0)
        & (df["PValue"] < 1)
        & (df["PValue"] >= 0)
    ]

    pvalues = df_evaluated["PValue"].to_numpy()

    if len(pvalues) > 0:
        pvalue_bh = false_discovery_control(pvalues, method="bh").min()
        return pvalue_bh <= 0.05
    return False


def extract_metadata(df: pd.DataFrame) -> Optional[AnalysisMetadata]:
    """Extract metadata from the scorecard record in Log Analytics."""
    if df.empty:
        return None

    config = df.iloc[0].to_dict()
    try:
        variants = json.loads(config["Variants"])
    except (KeyError, json.JSONDecodeError):
        logging.warning("Variant metadata are unavailable")
        variants = []

    return AnalysisMetadata(
        feature_flag=config["FeatureName"],
        label=config["Label"],
        allocation_id=config["AllocationId"],
        scorecard_id=config["ScorecardId"],
        start_time=config["AnalysisStartTime"].to_pydatetime(),
        end_time=config["AnalysisEndTime"].to_pydatetime(),
        variants=[
            VariantMetadata(
                variant=x["Variant"],
                is_control=x["IsControlVariant"],
                allocated_pct=x["VariantAssignmentPercentage"],
                assigned_users=x["AssignmentUserCount"],
                is_srm=x["SampleRatioMismatchPValue"] <= 0.0005,
                is_tea=False,  # populate later based on metric data
            )
            for x in variants
        ],
    )

# pylint: disable=too-many-arguments
def latest_analysis(
    credential,
    workspace: LogAnalyticsWorkspace,
    *,
    feature_flag: str,
    label: str,
    allocation_id: Optional[str],
    timespan: timedelta | tuple[datetime, timedelta] | tuple[datetime, datetime]
) -> Optional[AnalysisResults]:
    """Retrieve results for the latest analysis of an experiment.

    Parameters
    ----------
    credential: azure.core.credentials.TokenCredential
        Microsoft Entra ID token for Azure SDK authentication.
    workspace: LogAnalyticsWorkspace
        Azure Log Analytics workspace storing analysis results.
    feature_flag: str
        Azure App Configuration feature flag name.
    label: str
        Azure App Configuration label
    allocation_id: Optional[str]
        Allocation ID for the experiment. If unspecified, the latest experiment is selected.
    timespan: timedelta | tuple[datetime, timedelta] | tuple[datetime, datetime]
        Time range to search for the experiment.
    """
    # find the latest experiment analysis (latest allocation + date range)
    query = Template(QUERY_ANALYSIS).render(
        feature_flag=feature_flag, label=label, allocation_id=allocation_id
    )
    df_analysis = query_df(credential, workspace, query, timespan=timespan)
    analysis = extract_metadata(df_analysis)
    if analysis is None:
        return None

    # retrieve precomputed scorecard
    query = Template(QUERY_SCORECARD).render(scorecard_id=analysis.scorecard_id)
    df_scorecard = query_df(credential, workspace, query, timespan=timespan)
    results = AnalysisResults(analysis, df_scorecard)

    # update 'is_tea' for each variant
    for variant in results.analysis.variants:
        scorecard_variant = results.scorecard.loc[
            results.scorecard["TreatmentVariant"] == variant.variant
        ]
        variant.is_tea = treatment_effect_assessment(scorecard_variant)

    return results
