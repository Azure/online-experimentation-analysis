# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""Tests for formatting functions in the analysis.render module."""

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from analysis.render import (
    fmt_badge,
    fmt_hyperlink,
    fmt_image,
    fmt_metric_search,
    fmt_metric_table,
    fmt_metric_value,
    fmt_pvalue,
    fmt_reldiff,
    fmt_treatment_badge,
    strip_commit_hash,
)


@pytest.mark.parametrize(
    "value, metric_type, expected",
    [
        (np.nan, "EventCount", "--"),
        (np.inf, "EventCount", "∞"),
        (-np.inf, "EventCount", "-∞"),
        (0, "EventRate", "0%"),
        (50, "EventRate", "50.0%"),
        (100, "EventRate", "100%"),
        (0, "UserRate", "0%"),
        (50, "UserRate", "50.0%"),
        (100, "UserRate", "100%"),
        (0, "EventCount", "0"),
        (123, "EventCount", "123"),
        (1234, "EventCount", "1,234"),
        (1.234e6, "EventCount", "1.2M"),
        (2.345e9, "EventCount", "2.3B"),
        (3.456e12, "EventCount", "3.5T"),
        (4.567e15, "EventCount", "4.57e+15"),
        (123, "Sum", "123"),
        (1234, "Sum", "1,234"),
        (123.456, "Sum", "123.5"),
        (1234.56, "Sum", "1,235"),
        (12345.6, "Sum", "12,346"),
        (123456.7, "Sum", "123,457"),
        (1234567, "Sum", "1.235e+6"),
        (1.23456, "Sum", "1.235"),
        (0.000123456, "Sum", "0.0001235"),
        (0.0000123456, "Sum", "1.235e-5"),
    ],
)
def test_fmt_metric_value(value, metric_type, expected):
    """Test formatting of metric value."""
    assert fmt_metric_value(value, metric_type) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (np.nan, "--"),
        (np.inf, "+∞"),
        (-np.inf, "-∞"),
        (0, "0%"),
        (0.1234, "+12.3%"),
        (-0.1234, "-12.3%"),
        (2, "+200.0%"),
        (-1, "-100.0%"),
    ],
)
def test_fmt_reldiff(value, expected):
    """Test formatting of relative difference."""
    assert fmt_reldiff(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, "≈0"),
        (1.23e-10, "1e-10"),
        (0.000123, "1e-4"),
        (0.00123, "0.001"),
        (0.0123, "0.012"),
        (0.05, "0.050"),
        (0.1234, "0.123"),
        (1, "1.000"),
    ],
)
def test_fmt_pvalue(value, expected):
    """Test formatting of p-value."""
    assert fmt_pvalue(value) == expected


@pytest.mark.parametrize(
    "test_case, text, url, tooltip",
    [
        ("without-tooltip", "GitHub", "https://github.com", ""),
        ("with-tooltip", "GitHub", "https://github.com", "Visit GitHub"),
        ("quotes-tooltip", "GitHub", "https://github.com", 'Visit "GitHub"'),
        ("newline-tooltip", "GitHub", "https://github.com", "Visit\nGitHub"),
    ],
)
def test_fmt_hyperlink(test_case, text, url, tooltip, snapshot):
    """Test formatting of hyperlinks."""
    output = fmt_hyperlink(text, url, tooltip)

    snapshot.snapshot_dir = Path("tests", "snapshots", "fmt_hyperlink")
    snapshot.assert_match(output, f"{test_case}.md")


def test_fmt_image():
    """Test formatting of image markdown."""
    assert (
        fmt_image("https://example.com/image.png", "Alt text")
        == '![Alt text](https://example.com/image.png "")'
    )


@pytest.mark.parametrize(
    "test_case, label, message, color, tooltip",
    [
        ("improved-strong", "Improved", "+5.3%", "ImprovedStrong", ""),
        ("improved-weak", "Improved", "+5.3%", "ImprovedWeak", ""),
        ("degraded-strong", "Degraded", "+5.3%", "DegradedStrong", ""),
        ("degraded-weak", "Degraded", "+5.3%", "DegradedWeak", ""),
        ("changed-strong", "Changed", "+5.3%", "ChangedStrong", ""),
        ("changed-weak", "Changed", "+5.3%", "ChangedWeak", ""),
        ("inconclusive", "Inconclusive", "+5.3%", "Inconclusive", ""),
        ("warning", "Zero samples", "0%", "Warning", "My tooltip"),
        ("pass", "Test", "Passed", "Pass", ""),
        ("fail", "Test", "Failed", "Fail", ""),
        ("hex-color", "Hex", "Color", "#4C6CE4", ""),
        ("special-characters", "A_B", "C-D", "Pass", ""),
    ],
)
# pylint: disable-next=too-many-arguments
def test_fmt_badge(test_case, label, message, color, tooltip, snapshot):
    """Test formatting of badges."""
    output = fmt_badge(label, message, color, tooltip)

    snapshot.snapshot_dir = Path("tests", "snapshots", "fmt_badge")
    snapshot.assert_match(output, f"{test_case}.md")


@pytest.mark.parametrize(
    "test_case, row",
    [
        (
            "improved-strong",
            {
                "TreatmentEffect": "Improved",
                "PValue": 1.23e-6,
                "MetricType": "EventCount",
                "RelativeDifference": 0.053,
                "TreatmentMetricValue": 4567,
            },
        ),
        (
            "degraded-weak",
            {
                "TreatmentEffect": "Degraded",
                "PValue": 0.023,
                "MetricType": "EventRate",
                "RelativeDifference": 1.23,
                "TreatmentMetricValue": 56.7,
            },
        ),
        (
            "inconclusive",
            {
                "TreatmentEffect": "Inconclusive",
                "PValue": 0.456,
                "MetricType": "Average",
                "RelativeDifference": -0.543,
                "TreatmentMetricValue": 12345.6789,
            },
        ),
        (
            "too-few-samples",
            {
                "TreatmentEffect": "Too few samples",
                "PValue": 0.049,
                "MetricType": "Average",
                "RelativeDifference": -0.543,
                "TreatmentMetricValue": 12345.6789,
            },
        ),
        (
            "zero-samples",
            {
                "TreatmentEffect": "Zero samples",
                "PValue": 1,
                "MetricType": "Sum",
                "RelativeDifference": 0,
                "TreatmentMetricValue": 0,
            },
        ),
    ],
)
def test_fmt_treatment_badge(test_case, row, snapshot):
    """Test formatting of badges."""
    output = fmt_treatment_badge(pd.Series(row))

    snapshot.snapshot_dir = Path("tests", "snapshots", "fmt_treatment_badge")
    snapshot.assert_match(output, f"{test_case}.md")


@pytest.mark.parametrize(
    "test_case, data",
    [
        (
            "single-metric-single-treatment",
            {
                "MetricId": ["Metric1"],
                "MetricDisplayName": ["Metric 1"],
                "MetricType": ["EventCount"],
                "TreatmentVariant": ["VariantB"],
                "TreatmentMetricValue": [123],
                "ControlVariant": ["VariantA"],
                "ControlMetricValue": [456],
                "PValue": [0.0123],
                "TreatmentEffect": ["Improved"],
                "RelativeDifference": [0.123],
            },
        ),
        (
            "multi-metric-single-treatment",
            {
                "MetricId": ["Metric1", "Metric2", "Metric3"],
                "MetricDisplayName": ["Metric 1", "Metric 2", "Metric 3"],
                "MetricType": ["EventCount", "EventRate", "Sum"],
                "TreatmentVariant": ["VariantB", "VariantB", "VariantB"],
                "TreatmentMetricValue": [123, 50.23, 456],
                "ControlVariant": ["VariantA", "VariantA", "VariantA"],
                "ControlMetricValue": [456, 76.54, 789],
                "PValue": [0.0123, 0.0456, 0.0789],
                "TreatmentEffect": ["Improved", "Degraded", "Inconclusive"],
                "RelativeDifference": [0.123, 0.456, 0.789],
            },
        ),
        (
            "single-metric-multi-treatment",
            {
                "MetricId": ["Metric1", "Metric1", "Metric1"],
                "MetricDisplayName": ["Metric 1", "Metric 1", "Metric 1"],
                "MetricType": ["EventCount", "EventCount", "EventCount"],
                "TreatmentVariant": ["VariantB", "VariantC", "VariantD"],
                "TreatmentMetricValue": [123, 234, 345],
                "ControlVariant": ["VariantA", "VariantA", "VariantA"],
                "ControlMetricValue": [456, 456, 456],
                "PValue": [0.0123, 0.0234, 0.345],
                "TreatmentEffect": ["Improved", "Degraded", "Inconclusive"],
                "RelativeDifference": [0.123, 0.234, 0.345],
            },
        ),
        (
            "multi-metric-multi-treatment",
            {
                "MetricId": ["Metric1", "Metric1", "Metric2", "Metric2"],
                "MetricDisplayName": ["Metric 1", "Metric 1", "Metric 2", "Metric 2"],
                "MetricType": ["EventCount", "EventCount", "EventRate", "EventRate"],
                "TreatmentVariant": ["VariantB", "VariantC", "VariantB", "VariantC"],
                "TreatmentMetricValue": [123, 234, 50.23, 60.34],
                "ControlVariant": ["VariantA", "VariantA", "VariantA", "VariantA"],
                "ControlMetricValue": [456, 456, 76.54, 76.54],
                "PValue": [0.0123, 0.0234, 0.456, 0.0467],
                "TreatmentEffect": ["Improved", "Degraded", "Inconclusive", "Degraded"],
                "RelativeDifference": [0.123, 0.234, 0.345, 0.456],
            },
        ),
    ],
)
def test_fmt_metric_table(test_case, data, snapshot):
    """Test formatting of metric table."""
    output = fmt_metric_table(pd.DataFrame(data))

    snapshot.snapshot_dir = Path("tests", "snapshots", "fmt_metric_table")
    snapshot.assert_match(output, f"{test_case}.md")


def test_strip_commit_hash():
    """Test stripping the optional commit hash from the metric description."""
    with_hash = "Metric description Commit hash: 123456789"
    without_hash = "Metric description"

    assert strip_commit_hash(with_hash) == "Metric description"
    assert strip_commit_hash(without_hash) == "Metric description"


def test_fmt_metric_search_enabled(monkeypatch):
    """Test formatting of metric search hyperlink."""
    monkeypatch.setenv("GITHUB_SERVER_URL", "https://github.com")
    monkeypatch.setenv("GITHUB_REPOSITORY", "org/repo")

    output = fmt_metric_search("MetricId", "Search")
    url = 'https://github.com/org/repo/search?q="MetricId"+path%3A*.json'
    expected = fmt_hyperlink("Search", url)

    assert output == expected


def test_fmt_metric_search_diabled(monkeypatch):
    """Test formatting of metric search hyperlink."""
    monkeypatch.delenv("GITHUB_REPOSITORY", raising=False)

    assert fmt_metric_search("MetricId") == ""
