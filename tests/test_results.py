"""Tests for the analysis.results module."""

from datetime import datetime

import pandas as pd
import pytest

from analysis.results import AnalysisMetadata, AnalysisResults, VariantMetadata

args_control = {
    "variant": "A",
    "is_control": True,
    "allocated_pct": 50.0,
    "assigned_users": 999,
    "is_srm": False,
    "is_tea": False,
}
args_treatment = {
    "variant": "B",
    "is_control": False,
    "allocated_pct": 50.0,
    "assigned_users": 1001,
    "is_srm": False,
    "is_tea": True,
}
args_metadata = {
    "feature_flag": "test_feature",
    "allocation_id": "test_allocation",
    "scorecard_id": "test_scorecard",
    "start_time": datetime(2024, 1, 1),
    "end_time": datetime(2024, 1, 31),
}
data_scorecard = {
    "MetricId": ["metric_1"],
    "MetricDisplayName": ["Metric 1"],
    "MetricDescription": ["Description 1"],
    "MetricKind": ["Average"],
    "MetricLifecycle": ["Active"],
    "MetricTags": ["tag_1"],
    "DesiredDirection": ["Increase"],
    "TreatmentVariant": ["A"],
    "TreatmentCount": [1001],
    "TreatmentMetricValue": [0.1],
    "TreatmentMetricValueNormalized": [0.1],
    "TreatmentStandardErrorNormalized": [0.01],
    "ControlVariant": ["B"],
    "ControlCount": [999],
    "ControlMetricValue": [0.05],
    "ControlMetricValueNormalized": [0.05],
    "ControlStandardErrorNormalized": [0.005],
    "PValue": [0.01],
    "TreatmentEffect": ["Improved"],
    "RelativeDifference": [1.0],
}


def test_variant_metadata():
    """Test initialization of a valid VariantMetadata object."""
    variant = VariantMetadata(**args_control)
    assert variant.variant == "A"
    assert variant.is_control is True
    assert variant.allocated_pct == 50.0
    assert variant.assigned_users == 999
    assert variant.is_srm is False
    assert variant.is_tea is False


def test_analysis_metadata():
    """Test initialization of a valid AnalysisMetadata object."""
    variant_control = VariantMetadata(**args_control)
    variant_treatment = VariantMetadata(**args_treatment)
    metadata = AnalysisMetadata(
        **args_metadata, variants=[variant_control, variant_treatment]
    )
    assert metadata.feature_flag == "test_feature"
    assert metadata.allocation_id == "test_allocation"
    assert metadata.scorecard_id == "test_scorecard"
    assert metadata.start_time == datetime(2024, 1, 1)
    assert metadata.end_time == datetime(2024, 1, 31)
    assert metadata.variants == [variant_control, variant_treatment]
    assert metadata.is_any_srm is False


def test_is_any_srm():
    """Test the is_any_srm property of AnalysisMetadata."""
    variant_control = VariantMetadata(**args_control)
    variant_treatment = VariantMetadata(**args_treatment | {"is_srm": True})
    metadata = AnalysisMetadata(
        **args_metadata, variants=[variant_control, variant_treatment]
    )
    assert metadata.is_any_srm is True


def test_analysis_results():
    """Test initialization of a valid AnalysisResults object."""
    variant_control = VariantMetadata(**args_control)
    variant_treatment = VariantMetadata(**args_treatment)
    metadata = AnalysisMetadata(
        **args_metadata, variants=[variant_control, variant_treatment]
    )
    df_scorecard = pd.DataFrame(data_scorecard)
    results = AnalysisResults(analysis=metadata, scorecard=df_scorecard)

    dtype_coerce = {"TreatmentCount": int, "ControlCount": int}
    assert results.analysis == metadata
    assert results.scorecard.equals(df_scorecard.astype(dtype_coerce))


def test_analysis_results_missing_column():
    """Test that AnalysisResults raises an error for missing columns."""
    variant_control = VariantMetadata(**args_control)
    variant_treatment = VariantMetadata(**args_treatment)
    metadata = AnalysisMetadata(
        **args_metadata, variants=[variant_control, variant_treatment]
    )
    df_scorecard = pd.DataFrame(data_scorecard)
    df_scorecard.drop(columns=["MetricId"], inplace=True)

    with pytest.raises(ValueError):
        AnalysisResults(analysis=metadata, scorecard=df_scorecard)


def test_analysis_results_extra_column():
    """Test that AnalysisResults drops extra columns."""
    variant_control = VariantMetadata(**args_control)
    variant_treatment = VariantMetadata(**args_treatment)
    metadata = AnalysisMetadata(
        **args_metadata, variants=[variant_control, variant_treatment]
    )
    df_scorecard = pd.DataFrame(data_scorecard)
    results = AnalysisResults(
        analysis=metadata, scorecard=df_scorecard.assign(ExtraColumn=0)
    )

    dtype_coerce = {"TreatmentCount": int, "ControlCount": int}
    assert results.scorecard.equals(df_scorecard.astype(dtype_coerce))
