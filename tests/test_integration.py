# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""Integration snapshot tests for the analysis summary."""

import json
from pathlib import Path

import pandas as pd
import pytest

from analysis import download, latest_analysis, summarize
from analysis.results import SCHEMA_SCORECARD

PARENT_DIR = Path("tests", "snapshots", "integration")
CASE_DIRS = [p for p in PARENT_DIR.iterdir() if p.is_dir()]


def read_analysis(path: Path) -> pd.DataFrame:
    """Read the analysis metadata from a JSON file."""
    metadata = json.loads(path.read_text())
    dtypes = {
        "ScorecardId": str,
        "FeatureName": str,
        "Label": str,
        "AllocationId": str,
        "AnalysisStartTime": str,
        "AnalysisEndTime": str,
        "Variants": str,
    }

    if metadata is None:
        df = pd.DataFrame({col: pd.Series(dtype=dt) for col, dt in dtypes.items()})
    else:
        assert metadata.keys() == dtypes.keys()
        metadata["Variants"] = json.dumps(metadata["Variants"])
        df = pd.DataFrame(metadata, index=[0])

    df["AnalysisStartTime"] = pd.to_datetime(df["AnalysisStartTime"])
    df["AnalysisEndTime"] = pd.to_datetime(df["AnalysisEndTime"])

    return df


def read_scorecard(path: Path) -> pd.DataFrame:
    """Read the analysis metric data from a CSV file."""
    dtypes = SCHEMA_SCORECARD
    try:
        return pd.read_csv(path, dtype=dtypes)
    except pd.errors.EmptyDataError:
        return pd.DataFrame({col: pd.Series(dtype=dt) for col, dt in dtypes.items()})


@pytest.fixture(name="case_dir")
def fixture_case_dir(request, monkeypatch):
    """Fixture for an integration test case directory.

    This fixture mocks the analysis.log_analytics.query_df function to read fake
    experiment analysis results from files in the test case directory.
    """
    _case_dir: Path = request.param
    analysis_file = _case_dir.joinpath("analysis.json")
    scorecard_file = _case_dir.joinpath("scorecard.csv")

    # pylint: disable-next=unused-argument
    def mock_query_df(credential, workspace, query, *, timespan) -> pd.DataFrame:
        if "OEWExperimentScorecards" in query:
            df = read_analysis(analysis_file)
        elif "OEWExperimentScorecardMetricPairs" in query:
            df = read_scorecard(scorecard_file)
        else:
            raise ValueError("Unrecognized query")

        return df

    monkeypatch.delenv("GITHUB_REPOSITORY", raising=False)
    monkeypatch.setattr(download, "query_df", mock_query_df)
    return _case_dir


@pytest.mark.parametrize("case_dir", CASE_DIRS, indirect=True)
def test_summarize(case_dir, snapshot):
    """Integration snapshot test for the analysis summary."""
    _ = None
    result = latest_analysis(_, _, feature_flag=_, label=_, allocation_id=_, timespan=_)
    summary = summarize(result)

    snapshot.snapshot_dir = case_dir
    snapshot.assert_match(summary, "output.md")
