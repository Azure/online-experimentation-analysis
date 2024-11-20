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

## Sample workflows

| Trigger event                                                                                                                                                                                                                                                                               | Analysis results storage         | Workflow file                      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------- | :--------------------------------- |
| [Scheduled](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule) + [manual dispatch](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow) | Directory of GitHub repository   | [Link](samples/commit-dir.yaml)    |
| [Scheduled](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule) + [manual dispatch](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/manually-running-a-workflow) | GitHub Wiki                      | [Link](samples/commit-wiki.yaml)   |
| Trigger comment in GitHub Issue                                                                                                                                                                                                                                                             | Response comment in GitHub Issue | [Link](samples/issue-comment.yaml) |

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
