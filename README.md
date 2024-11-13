# Online Experimentation Analysis

> [!IMPORTANT]
> This GitHub Action is under beta release and is subject to the [Azure AI Private Preview Terms - Online Experimentation](private-preview-terms.md).

This GitHub Action downloads the latest analysis results for your online experiment, so you can review how feature flag variants cause key metrics to change.
The analysis results are summarized as a GitHub Flavored Markdown document for an enriched user experience.

## Inputs

| Name                           | Required? | Description                                                                                                                                                                                                                                                |
| :----------------------------- | :-------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| subscription-id                |   true    | The subscription ID of the Log Analytics workspace.                                                                                                                                                                                                        |
| resource-group                 |   true    | The resource group of the Log Analytics workspace.                                                                                                                                                                                                         |
| log-analytics-workspace        |   true    | The name of the Log Analytics workspace.                                                                                                                                                                                                                   |
| app-configuration-feature-flag |   true    | The App Configuration feature flag of the experiment.                                                                                                                                                                                                      |
| metric-tags-order              |   false   | The analysis summary displays metrics grouped by their tags. This input specifies the display order of metric tags as a comma separated list. Unspecified tags are appended in alphabetical order, followed by the group of untagged metrics. Default: ''. |
| lookback-days                  |   false   | The number of previous days to search the Log Analytics workspace for the latest analysis results. Default: 30.                                                                                                                                            |
| github-actions-summary         |   false   | If the analysis summary should be displayed in the GitHub Action job summary. Default: true.                                                                                                                                                               |

## Outputs

| Name                | Description                                                        |
| :------------------ | :----------------------------------------------------------------- |
| analysis-start-time | The start time of the analysis (ISO 8601 format).                  |
| analysis-end-time   | The end time of the analysis (ISO 8601 format).                    |
| summary-md          | Summary of the analysis results (GitHub Flavored Markdown format). |

## Sample workflow

The following GitHub Actions workflow reads the list of running experiments from a JSON file storing the Azure App Configuration feature flags.
It then executes the Online Experimentation Analysis action for every feature flag in this list, summarizing the latest analysis results for each experiment.
The workflow is scheduled to run daily or it can be manually triggered by the [Run workflow button](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow?tool=webui).
When triggering manually, you can specify a single feature flag to analyze (instead of analyzing all running experiments).

```yaml
# File: .github/workflows/analyze-experiments.yml

name: Analyze Experiments
on:
  # analyze running experiments (daily at 12:30 AM UTC)
  schedule:
    - cron: "30 0 * * *"
  # analyze specific experiment (manually via UI)
  workflow_dispatch:
    inputs:
      app-configuration-feature-flag:
        description: "The App Configuration feature flag. By default, analyze all running experiments."
        required: false
        type: string

# Update for your setup
env:
  APP_CONFIGURATION_FILE: .config/feature-flags.json
  METRIC_TAGS_ORDER: "Important, Cost, Performance"

jobs:
  list-experiments:
    name: List experiments
    runs-on: ubuntu-latest
    outputs:
      feature-flags: ${{ steps.write.outputs.feature-flags }}

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Read running experiments from config file
        if: github.event_name == 'schedule' || (github.event_name == 'workflow_dispatch' && github.event.inputs.app-configuration-feature-flag == '')
        run: echo "FEATURE_FLAGS=$(jq -c '[.feature_management.feature_flags[] | select(.enabled and .allocation.percentile) | .id]' ${{ env.APP_CONFIGURATION_FILE }})" >> $GITHUB_ENV

      - name: Propagate specified feature flag
        if: github.event_name == 'workflow_dispatch' && github.event.inputs.app-configuration-feature-flag != ''
        run: echo "FEATURE_FLAGS=[\"${{ github.event.inputs.app-configuration-feature-flag }}\"]" >> $GITHUB_ENV

      - name: Export list
        id: write
        run: echo "feature-flags=$FEATURE_FLAGS" >> "$GITHUB_OUTPUT"

  analysis:
    name: Analysis of ${{ matrix.feature-flag }}
    runs-on: ubuntu-latest
    needs: list-experiments
    permissions:
      id-token: write
      contents: read
    strategy:
      fail-fast: false
      matrix:
        feature-flag: ${{ fromJson(needs.list-experiments.outputs.feature-flags) }}

    steps:
      - name: Azure login using Federated Credentials
        uses: azure/login@v2
        with:
          client-id: ${{ vars.AZURE_CLIENT_ID }}
          tenant-id: ${{ vars.AZURE_TENANT_ID }}
          subscription-id: ${{ vars.AZURE_SUBSCRIPTION_ID }}

      - name: Download experiment analysis results
        id: results
        uses: azure/online-experimentation-analysis@v1-beta
        with:
          subscription-id: ${{ vars.AZURE_SUBSCRIPTION_ID }}
          resource-group: ${{ vars.AZURE_RESOURCE_GROUP }}
          log-analytics-workspace: ${{ vars.AZURE_LOG_ANALYTICS_WORKSPACE }}
          app-configuration-feature-flag: ${{ matrix.feature-flag }}
          metric-tags-order: ${{ env.METRIC_TAGS_ORDER }}
```

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
