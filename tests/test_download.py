# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""Tests for the analysis.download module."""

import json
from datetime import datetime

import pandas as pd

from analysis.download import extract_metadata


def test_extract_metadata():
    """Test extracting metadata from a valid scorecard record."""
    # fmt: off
    df = pd.DataFrame({
        "ScorecardId": ["test_scorecard"],
        "FeatureName": ["test_feature"],
        "AllocationId": ["test_allocation"],
        "AnalysisStartTime": [pd.Timestamp("2023-01-01 00:00:00")],
        "AnalysisEndTime": [pd.Timestamp("2023-01-02 00:00:00")],
        "Variants": [json.dumps([
            {
                "Variant": "A",
                "IsControlVariant": True,
                "VariantAssignmentPercentage": 50.0,
                "AssignmentUserCount": 999,
                "SampleRatioMismatchPValue": 1.0
            },
            {
                "Variant": "B",
                "IsControlVariant": False,
                "VariantAssignmentPercentage": 50.0,
                "AssignmentUserCount": 1001,
                "SampleRatioMismatchPValue": 0.00001
            }
        ])]
    })
    # fmt: on

    metadata = extract_metadata(df)

    assert metadata is not None
    assert metadata.feature_flag == "test_feature"
    assert metadata.allocation_id == "test_allocation"
    assert metadata.scorecard_id == "test_scorecard"
    assert metadata.start_time == datetime(2023, 1, 1)
    assert metadata.end_time == datetime(2023, 1, 2)
    assert len(metadata.variants) == 2

    variant_a = metadata.variants[0]
    assert variant_a.variant == "A"
    assert variant_a.is_control
    assert variant_a.allocated_pct == 50.0
    assert variant_a.assigned_users == 999
    assert not variant_a.is_srm
    assert not variant_a.is_tea

    variant_b = metadata.variants[1]
    assert variant_b.variant == "B"
    assert not variant_b.is_control
    assert variant_b.allocated_pct == 50.0
    assert variant_b.assigned_users == 1001
    assert variant_b.is_srm
    assert not variant_b.is_tea


def test_extract_metadata_unavailable():
    """Test extracting metadata when scorecard unavailable."""
    df = pd.DataFrame()
    metadata = extract_metadata(df)
    assert metadata is None


def test_extract_metadata_invalid_variants():
    """Test extracting metadata with invalid variant metadata."""
    # fmt: off
    df = pd.DataFrame({
        "ScorecardId": ["test_scorecard"],
        "FeatureName": ["test_feature"],
        "AllocationId": ["test_allocation"],
        "AnalysisStartTime": [pd.Timestamp("2023-01-01 00:00:00")],
        "AnalysisEndTime": [pd.Timestamp("2023-01-02 00:00:00")],
        "Variants": ["invalid_json"]
    })
    # fmt: on

    metadata = extract_metadata(df)

    assert metadata is not None
    assert metadata.feature_flag == "test_feature"
    assert metadata.allocation_id == "test_allocation"
    assert metadata.scorecard_id == "test_scorecard"
    assert metadata.start_time == datetime(2023, 1, 1)
    assert metadata.end_time == datetime(2023, 1, 2)
    assert len(metadata.variants) == 0
