"""Results from an online experimentation analysis"""

from dataclasses import dataclass
from datetime import datetime

import pandas as pd

SCHEMA_SCORECARD = {
    "MetricId": str,
    "MetricDisplayName": str,
    "MetricDescription": str,
    "MetricKind": str,
    "MetricLifecycle": str,
    "MetricTags": str,
    "DesiredDirection": str,
    "TreatmentVariant": str,
    "TreatmentCount": int,
    "TreatmentMetricValue": float,
    "TreatmentMetricValueNormalized": float,
    "TreatmentStandardErrorNormalized": float,
    "ControlVariant": str,
    "ControlCount": int,
    "ControlMetricValue": float,
    "ControlMetricValueNormalized": float,
    "ControlStandardErrorNormalized": float,
    "PValue": float,
    "TreatmentEffect": str,
    "RelativeDifference": float,
}


@dataclass
class VariantMetadata:
    """Metadata for a variant in an experiment analysis"""

    variant: str
    """Name of the variant"""
    is_control: bool
    """Whether this is the control variant"""
    allocated_pct: float
    """Percentage of users allocated to this variant"""
    assigned_users: int
    """Number of users assigned to this variant"""
    is_srm: bool
    """Whether the sample ratio mismatch test is significant"""
    is_tea: bool
    """Whether the treatment effect is statistically significant"""


@dataclass
class AnalysisMetadata:
    """Metadata for an experiment analysis"""

    feature_flag: str
    """Name of the feature flag"""
    allocation_id: str
    """ID of the allocation"""
    scorecard_id: str
    """ID of the scorecard"""
    start_time: datetime
    """Start time of the analysis"""
    end_time: datetime
    """End time of the analysis"""
    variants: list[VariantMetadata]
    """Metadata for each variant"""

    @property
    def is_any_srm(self) -> bool:
        """Whether any variant has a significant sample ratio mismatch"""
        return any(x.is_srm for x in self.variants)


@dataclass
class AnalysisResults:
    """Results of an experiment analysis"""

    analysis: AnalysisMetadata
    """Metadata for the experiment analysis"""
    scorecard: pd.DataFrame
    """Comparison of metric values between control and treatment groups"""

    def __post_init__(self):
        cols_expected = list(SCHEMA_SCORECARD.keys())
        cols_missing = set(cols_expected) - set(self.scorecard.columns)
        if cols_missing:
            raise ValueError(
                f'Missing columns in scorecard: {", ".join(sorted(cols_missing))}'
            )

        self.scorecard = (
            self.scorecard[cols_expected]
            .loc[lambda df: df["MetricId"] != ""]
            .astype(SCHEMA_SCORECARD)
        )
