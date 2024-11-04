# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""Render analysis results as a markdown summary"""

import json
import os
from pathlib import Path
from typing import Optional
from urllib.parse import quote

import numpy as np
import pandas as pd
from jinja2 import Environment, FileSystemLoader

from .log_analytics import LogAnalyticsWorkspace, analysis_workbook_url
from .results import AnalysisResults

SS_THRESHOLD = 0.05
HSS_THRESHOLD = 0.001
TAG_UNTAGGED = "Untagged"

DARK_GREEN = "157e3b"
PALE_GREEN = "a1d99b"
DARK_RED = "d03536"
PALE_RED = "fcae91"
DARK_BLUE = "1c72af"
PALE_BLUE = "9ecae1"
PALE_YELLOW = "f0e543"
PALE_GREY = "e6e6e3"


def fmt_metric_value(x: np.float64, kind: str) -> str:
    """Format a metric value"""
    if np.isnan(x):
        out = "--"
    elif np.isinf(x):
        sign = "" if x > 0 else "-"
        out = f"{sign}∞"

    elif kind in ["EventRate", "UserRate"]:
        dp = 0 if x == 0 or np.isclose(x, 100) else 1
        out = format(x / 100.0, f".{dp}%")

    elif kind in ["EventCount", "UserCount"]:
        if x >= 1e15:
            out = format(x, ".2e")
        elif x >= 1e12:
            out = f"{x / 1e12:.1f}T"
        elif x >= 1e9:
            out = f"{x / 1e9:.1f}B"
        elif x >= 1e6:
            out = f"{x / 1e6:.1f}M"
        else:
            out = format(int(x), ",d")

    # Sum, Average, Percentile, etc
    else:
        if np.fabs(x) >= 10_000 and np.fabs(x) < 1e6:
            out = format(x, ",.0f")
        else:
            out = format(x, ",.4g").replace("e+0", "e+").replace("e-0", "e-")

    return out


def fmt_reldiff(x: np.float64) -> str:
    """Format a relative difference as a percentage"""
    if np.isnan(x):
        out = "--"
    elif np.isinf(x):
        sign = "+" if x > 0 else "-"
        out = f"{sign}∞"
    elif x == 0:
        out = "0%"
    else:
        out = format(x, "+.1%")

    return out


def fmt_pvalue(x: np.float64) -> str:
    """Format a p-value"""
    if x <= 0:
        return "≈0"

    spec = ".0e" if x < 0.001 else ".3f"
    return format(x, spec).replace("e-0", "e-")


def fmt_hyperlink(text: str, url: str, tooltip: str = "") -> str:
    """Markdown to render a hyperlink"""
    tooltip = tooltip.replace("\n", "&#013;").replace('"', "&quot;")
    return f'[{text}]({url} "{tooltip}")'


def fmt_image(url: str, alt_text: str, tooltip: str = "") -> str:
    """Markdown to render an image"""
    return "!" + fmt_hyperlink(alt_text, url, tooltip)


def fmt_badge(label: str, message: str, color: str, tooltip: str = "") -> str:
    """Markdown to render a badge

    Parameters
    ----------
    label : str
        Left-hand side of the badge.
    message : str
        Right-hand side of the badge.
    color : str
        Badge color. Accepts hex, rgb, hsl, hsla, css named color, or a preset:
            - ImprovedStrong: dark green
            - ImprovedWeak: pale green
            - DegradedStrong: dark red
            - DegradedWeak: pale red
            - ChangedStrong: dark blue
            - ChangedWeak: pale blue
            - Inconclusive: pale grey
            - Warning: pale yellow
            - Pass: dark green
            - Fail: dark red
    tooltip : str, optional
        Tooltip. Default: standard message for color presets, otherwise none.
    """
    if not tooltip:
        if color.endswith("Strong"):
            tooltip = "Highly statistically significant."
        elif color.endswith("Weak"):
            tooltip = "Marginally statistically significant."
        elif color == "Inconclusive":
            tooltip = "Not statistically significant."

    match color:
        case "ImprovedStrong":
            color = DARK_GREEN
        case "ImprovedWeak":
            color = PALE_GREEN
        case "DegradedStrong":
            color = DARK_RED
        case "DegradedWeak":
            color = PALE_RED
        case "ChangedStrong":
            color = DARK_BLUE
        case "ChangedWeak":
            color = PALE_BLUE
        case "Inconclusive":
            color = PALE_GREY
        case "Warning":
            color = PALE_YELLOW
        case "Pass":
            color = DARK_GREEN
        case "Fail":
            color = DARK_RED
        case _:
            # support custom colors
            pass

    def escape(s: str) -> str:
        return quote(s, safe="").replace("-", "--").replace("_", "__")

    badge_content = "-".join(map(escape, [label, message, color]))
    url = f"https://img.shields.io/badge/{badge_content}"
    alt_text = f"{label}: {message}"

    return fmt_image(url, alt_text, tooltip)


def fmt_treatment_badge(row: pd.Series) -> str:
    """Format a treatment effect as a badge"""
    effect = row["TreatmentEffect"]
    pvalue = row["PValue"]
    kind = row["MetricKind"]
    reldiff = row["RelativeDifference"]
    value = row["TreatmentMetricValue"]

    if effect in ["Improved", "Degraded", "Changed"]:
        if pvalue <= HSS_THRESHOLD:
            color = f"{effect}Strong"
            tooltip_stat = "Highly statistically significant"
        elif pvalue <= SS_THRESHOLD:
            color = f"{effect}Weak"
            tooltip_stat = "Marginally statistically significant"
        else:
            color = "Warning"
            tooltip_stat = "Unexpected classification"
        tooltip_stat += f" (p-value: {fmt_pvalue(pvalue)})."
    elif effect == "Inconclusive":
        if pvalue > SS_THRESHOLD:
            color = effect
            tooltip_stat = "Not statistically significant"
        else:
            color = "Warning"
            tooltip_stat = "Unexpected classification"
        tooltip_stat += f" (p-value: {fmt_pvalue(pvalue)})."
    elif effect == "Too few samples":
        color = "Warning"
        tooltip_stat = "Insufficient observations to determine statistical significance"
    elif effect == "Zero samples":
        color = "Warning"
        tooltip_stat = (
            "Zero observations might indicate a problem with "
            "the metric definition or data collection"
        )
    else:
        color = PALE_GREY
        tooltip_stat = ""

    tooltip_value = f"Metric value = {fmt_metric_value(value, kind)}"
    if kind in ["EventCount", "UserCount", "Sum"]:
        tooltip_value += " (analysis accounts for unequal allocation)"
    tooltip_value += "."

    tooltip = "\n".join([tooltip_value, tooltip_stat])
    return fmt_badge(effect, fmt_reldiff(reldiff), color, tooltip)


def fmt_metric_table(df: pd.DataFrame) -> str:
    """Format a DataFrame of metric results as a markdown table"""
    if df.empty:
        return ""

    control_variant = str(df["ControlVariant"].iloc[0])

    def fmt_control_value(row: pd.Series):
        return fmt_metric_value(row["ControlMetricValue"], row["MetricKind"])

    return (
        pd.DataFrame(
            {
                "MetricId": df["MetricId"],
                "Metric": df["MetricDisplayName"],
                control_variant: df.apply(fmt_control_value, axis=1),
                "TreatmentVariant": df["TreatmentVariant"],
                "TreatmentBadge": df.apply(fmt_treatment_badge, axis=1),
            }
        )
        .pivot(
            index=["MetricId", "Metric", control_variant],
            columns="TreatmentVariant",
            values="TreatmentBadge",
        )
        .reset_index()
        .drop(columns="MetricId")
        .rename(columns=lambda x: x if x == "Metric" else x + " 💊")
        .sort_values("Metric")
        .to_markdown(index=False, colalign=("left", "right"))
    )


def fmt_metric_search(
    metric_id: str, text: str = "Search for metric definition."
) -> str:
    """Format a hyperlink to search for a metric configuration on GitHub"""
    server_url = os.getenv("GITHUB_SERVER_URL", "https://github.com")
    repo = os.getenv("GITHUB_REPOSITORY")

    if repo:
        url = f'{server_url}/{repo}/search?q="{metric_id}"+path%3A*.json'
        return fmt_hyperlink(text, url)

    return ""


def summarize(
    results: AnalysisResults,
    tags_order: Optional[list[str]] = None,
    workspace: Optional[LogAnalyticsWorkspace] = None,
) -> str:
    """Render experiment analysis results as a markdown summary"""
    if results.scorecard.empty:
        return "No metric results found in the analysis."

    env = Environment(loader=FileSystemLoader(Path(__file__).parent))

    template = env.get_template("summary-ab.md.jinja")
    template.globals.update(fmt_metric_table=fmt_metric_table)
    template.globals.update(fmt_metric_search=fmt_metric_search)
    template.globals.update(fmt_badge=fmt_badge)

    def parse_tags(tags_json: str) -> list[str]:
        try:
            tags_list = list(json.loads(tags_json))
        except json.JSONDecodeError:
            tags_list = []

        return tags_list if len(tags_list) > 0 else [TAG_UNTAGGED]

    # explode metric tags + hide internal metrics
    df_processed = (
        results.scorecard.assign(
            MetricTags=lambda df: df["MetricTags"].apply(parse_tags)
        )
        .explode("MetricTags")
        .rename(columns={"MetricTags": "MetricTag"})
        .loc[lambda df: ~df["MetricTag"].str.startswith("__")]
        .sort_values("MetricDisplayName")
    )

    # show requested tag order, then others alphabetically, then untagged
    if tags_order is None:
        tags_order = []
    tags_observed = set(df_processed["MetricTag"].to_list())
    tags_order = [tag for tag in tags_order if tag in tags_observed]
    tags_order += sorted(tags_observed - set(tags_order) - {TAG_UNTAGGED})
    if TAG_UNTAGGED in tags_observed:
        tags_order.append(TAG_UNTAGGED)

    if workspace is not None:
        url_workbook = analysis_workbook_url(workspace, results.analysis)
    else:
        url_workbook = None

    return template.render(
        df_scorecard=df_processed,
        analysis=results.analysis,
        url_workbook=url_workbook,
        tags_order=tags_order,
    )
