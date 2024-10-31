"""Functions to interact with a Log Analytics workspace"""

import json
import logging
from dataclasses import dataclass
from urllib.parse import quote

import pandas as pd
from azure.core.exceptions import HttpResponseError
from azure.monitor.query import LogsQueryClient, LogsQueryStatus

from .results import AnalysisMetadata


@dataclass
class LogAnalyticsWorkspace:
    """A Log Analytics workspace"""

    subscription_id: str
    resource_group: str
    workspace: str

    @property
    def resource_id(self) -> str:
        """Fully-qualified resource name for the Log Analytics workspace"""
        resource_type = "Microsoft.OperationalInsights/workspaces"
        return (
            f"/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group}"
            f"/providers/{resource_type}/{self.workspace}"
        )


def query_df(
    credential, workspace: LogAnalyticsWorkspace, query: str, *, timespan
) -> pd.DataFrame:
    """Download the results of a Log Analytics query as a pandas DataFrame."""
    client = LogsQueryClient(credential)

    try:
        response = client.query_resource(
            workspace.resource_id, query, timespan=timespan
        )

        if response.status == LogsQueryStatus.SUCCESS:
            data = response.tables
        else:
            logging.warning(response.partial_error)
            data = response.partial_data
    except HttpResponseError as err:
        logging.error(err)
        raise

    return pd.DataFrame(data=data[0].rows, columns=data[0].columns)


def _blade_url(
    base_url: str, *, extension: str, view: str, blade_inputs: dict[str, str]
):
    url = base_url + f"/#blade/{extension}/{view}"
    for k, v in blade_inputs.items():
        url += f'/{k}/{quote(v, safe="")}'
    return url


def analysis_workbook_url(
    workspace: LogAnalyticsWorkspace, analysis: AnalysisMetadata
) -> str:
    """Generate URL to the Experiment Analysis workbook under the Log Analytics
    workspace resource, passing workbook parameters for the specific analysis.
    """
    workbook_name = "Experiment Analysis"
    workbook_params = {
        "Workspace": workspace.resource_id,
        "TimeRange": {
            # Time range of this analysis is known, but there might be later analyses.
            # Best effort is a long time range (90 days) and recognize the URL becomes stale.
            "durationMs": 7776000000
        },
        "FeatureName": analysis.feature_flag,
        "AllocationId": analysis.allocation_id,
    }

    return _blade_url(
        "https://portal.azure.com",
        extension="AppInsightsExtension",
        view="WorkbookViewerBlade",
        blade_inputs={
            "ComponentId": workspace.resource_id,
            "ConfigurationId": f"Community-Workbooks/Online Experimentation/{workbook_name}",
            "WorkbookTemplateName": workbook_name,
            "NotebookParams": json.dumps(workbook_params),
        },
    )
