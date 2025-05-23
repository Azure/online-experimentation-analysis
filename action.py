# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""GitHub Action to retrieve the latest analysis results for an online experiment
of an Azure App Configuration feature flag
"""

import os
import sys
import uuid
from datetime import timedelta
from typing import Optional

from azure.identity import DefaultAzureCredential

from analysis import AnalysisResults, LogAnalyticsWorkspace, latest_analysis, summarize

GITHUB_OUTPUT = os.getenv("GITHUB_OUTPUT")
GITHUB_STEP_SUMMARY = os.getenv("GITHUB_STEP_SUMMARY")

SUBSCRIPTION_ID = os.getenv("SUBSCRIPTION_ID")
RESOURCE_GROUP = os.getenv("RESOURCE_GROUP")
LOGANALYTICS_WORKSPACE = os.getenv("LOGANALYTICS_WORKSPACE")
APPCONFIG_FEATURE_FLAG = os.getenv("APPCONFIG_FEATURE_FLAG")
APPCONFIG_LABEL = os.getenv("APPCONFIG_LABEL")
METRIC_CATEGORY_ORDER = [
    x.strip() for x in os.getenv("METRIC_CATEGORY_ORDER", "").split(",") if x.strip()
]
LOOKBACK_DAYS = int(os.getenv("LOOKBACK_DAYS", "30"))
GHA_SUMMARY = os.getenv("GHA_SUMMARY", "true").lower() not in ["false", "0", "no", "n"]


# pylint: disable-next=too-many-arguments
def main(
    subscription_id: str,
    resource_group: str,
    log_analytics_workspace: str,
    feature_flag: str,
    label: str,
    category_order: list[str],
    lookback_days: int,
) -> tuple[Optional[AnalysisResults], str]:
    """Retrieve the latest analysis of an experiment and summarize the results.

    Parameters
    ----------
    subscription_id: str
        Azure subscription ID.
    resource_group: str
        Azure resource group name.
    log_analytics_workspace: str
        Azure Log Analytics workspace name.
    feature_flag: str
        Azure App Configuration feature flag name.
    label: str
        Azure App Configuration label.
    category_order: list[str]
        Specify the order that metric categories are displayed in the summary.
        Unspecified categories are appended in alphabetical order, followed by
        an 'Uncategorized' category.
    lookback_days: int
        Number of days to look back for the analysis.

    Returns
    -------
    tuple[Optional[AnalysisResults], str]
        Tuple of the analysis results and the summary markdown string.
    """
    workspace = LogAnalyticsWorkspace(
        subscription_id=subscription_id,
        resource_group=resource_group,
        workspace=log_analytics_workspace,
    )

    result = latest_analysis(
        DefaultAzureCredential(),
        workspace=workspace,
        feature_flag=feature_flag,
        label=label,
        allocation_id=None,
        timespan=timedelta(days=lookback_days),
    )

    if result is None:
        summary = f"Analysis unavailable for feature flag '{feature_flag}''"
        if label:
            summary += f" with label '{label}'"
    else:
        summary = summarize(result, category_order=category_order, workspace=workspace)

    return result, summary


def set_github_output(name: str, value: str):
    """Write multiline string to GitHub Actions output variable"""
    if GITHUB_OUTPUT:
        delim = str(uuid.uuid4())
        with open(GITHUB_OUTPUT, "a", encoding="utf-8") as f:
            f.write(f"{name}<<{delim}\n{value}\n{delim}\n")


if __name__ == "__main__":
    if not SUBSCRIPTION_ID:
        raise ValueError("Missing input: subscription-id")
    if not RESOURCE_GROUP:
        raise ValueError("Missing input: resource-group")
    if not LOGANALYTICS_WORKSPACE:
        raise ValueError("Missing input: log-analytics-workspace")
    if not APPCONFIG_FEATURE_FLAG:
        raise ValueError("Missing input: app-configuration-feature-flag")
    if not APPCONFIG_LABEL:
        APPCONFIG_LABEL = ""  # default to no label

    results, summary_md = main(
        subscription_id=SUBSCRIPTION_ID,
        resource_group=RESOURCE_GROUP,
        log_analytics_workspace=LOGANALYTICS_WORKSPACE,
        feature_flag=APPCONFIG_FEATURE_FLAG,
        label=APPCONFIG_LABEL,
        category_order=METRIC_CATEGORY_ORDER,
        lookback_days=LOOKBACK_DAYS,
    )

    # if analysis not found, exit gracefully (may be expected)
    if results is None:
        label_str = f" with label '{APPCONFIG_LABEL}'" if APPCONFIG_LABEL else ""
        title = f"Analysis unavailable: {APPCONFIG_FEATURE_FLAG} '{label_str}'"
        msg = (
            f"Can't find analysis results for feature flag '{APPCONFIG_FEATURE_FLAG}'"
            " {label_str}. Is the first analysis still pending?"
        )

        # highlight within GitHub Action annotations
        print(f"::warning title={title}::{msg}")
        sys.exit(0)

    if results.scorecard.empty:
        raise ValueError("Found analysis results but unable to download metric data")

    set_github_output("allocation-id", results.analysis.allocation_id)
    set_github_output("scorecard-id", results.analysis.scorecard_id)
    set_github_output("analysis-start-time", results.analysis.start_time.isoformat())
    set_github_output("analysis-end-time", results.analysis.end_time.isoformat())
    set_github_output("summary-md", summary_md)

    if GHA_SUMMARY and GITHUB_STEP_SUMMARY:
        with open(GITHUB_STEP_SUMMARY, "a", encoding="utf-8") as fp:
            fp.write(summary_md)
