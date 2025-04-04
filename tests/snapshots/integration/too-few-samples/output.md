## Experiment analysis



* ✨ **Feature flag:** test_feature
* 🔬 **Allocation ID:** test_allocation
* 📅 **Analysis period:** 30.0 days (01/01/2024 00:00 - 01/31/2024 00:00 UTC)
* 🔖 **Scorecard ID:** test_scorecard

### Summary of variants

| Variant 💊 | Type | Allocation | Assignment | Data quality | Treatment effect |
|:--------|:-----|-----------:|-----------:|:------------:|:----------------:|
| Variant1 | Control | 50% | 5 | n/a | n/a |
| Variant2 | Treatment | 50% | 6 | ![Data quality: Too few samples](https://img.shields.io/badge/Data%20quality-Too%20few%20samples-f0e543 "Not enough assigned users for reliable SRM analysis.") | ![Change: Detected](https://img.shields.io/badge/Change-Detected-1c72af "Observed metric movements are inconsistent with statistical noise.") |
| Variant3 | Treatment | 50% | 7 | ![Data quality: Too few samples](https://img.shields.io/badge/Data%20quality-Too%20few%20samples-f0e543 "Not enough assigned users for reliable SRM analysis.") | ![Change: Undetected](https://img.shields.io/badge/Change-Undetected-e6e6e3 "Observed metric movements are consistent with statistical noise.&#013;Either the experiment is underpowered or had limited impact on the metrics.") |
| Variant4 | Treatment | 50% | 8 | ![SRM check: Pass](https://img.shields.io/badge/SRM%20check-Pass-157e3b "No sample ratio mismatch detected.") | ![Change: Detected](https://img.shields.io/badge/Change-Detected-1c72af "Observed metric movements are inconsistent with statistical noise.") |


### Metric results

> [!TIP]
> Hover your cursor over a **treatment effect badge** to display the metric value and the p-value of the statistical test.

<details open="true">
<summary><strong>Important</strong> (2 of 3 conclusive)</summary>

| Metric   |   Variant1 💊 | Variant2 💊                                                                                                                                                  | Variant3 💊                                                                                                                                                    | Variant4 💊                                                                                                                                                  |
|:---------|--------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Metric 1 |         50.8% | ![Improved: +51.0%](https://img.shields.io/badge/Improved-%2B51.0%25-157e3b "Metric value = 76.7%.&#013;Highly statistically significant (p-value: 6e-60).") | ![Inconclusive: -3.3%](https://img.shields.io/badge/Inconclusive---3.3%25-e6e6e3 "Metric value = 49.2%.&#013;Not statistically significant (p-value: 0.273).") | ![Improved: +39.2%](https://img.shields.io/badge/Improved-%2B39.2%25-157e3b "Metric value = 70.7%.&#013;Highly statistically significant (p-value: 1e-35).") |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Metric 1:*** Wish fight pressure since task see hair artist lot prepare heavy meeting necessary pretty issue not ago pass wonder former degree ago matter foreign as. </dd>
>
> </details>

</details>



<details>
<summary><strong>Performance</strong> (2 of 3 conclusive)</summary>

| Metric   |   Variant1 💊 | Variant2 💊                                                                                                                                                  | Variant3 💊                                                                                                                                                    | Variant4 💊                                                                                                                                                  |
|:---------|--------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Metric 1 |         50.8% | ![Improved: +51.0%](https://img.shields.io/badge/Improved-%2B51.0%25-157e3b "Metric value = 76.7%.&#013;Highly statistically significant (p-value: 6e-60).") | ![Inconclusive: -3.3%](https://img.shields.io/badge/Inconclusive---3.3%25-e6e6e3 "Metric value = 49.2%.&#013;Not statistically significant (p-value: 0.273).") | ![Improved: +39.2%](https://img.shields.io/badge/Improved-%2B39.2%25-157e3b "Metric value = 70.7%.&#013;Highly statistically significant (p-value: 1e-35).") |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Metric 1:*** Wish fight pressure since task see hair artist lot prepare heavy meeting necessary pretty issue not ago pass wonder former degree ago matter foreign as. </dd>
>
> </details>

</details>

---

### Guide

<details>
<summary><strong>Treatment effect badges</strong></summary>

Each treatment column displays the impact of the treatment variant upon the metric value, relative to the control variant. For example, "+5.3%" means the metric value is 5.3% higher in the treatment variant than the control variant. The experiment analysis checks whether the observed treatment effect could be explained by random noise in the data.

* If not statistically significant, we display the badge: ![Inconclusive: +5.3%](https://img.shields.io/badge/Inconclusive-%2B5.3%25-e6e6e3 "Not statistically significant.")
* If statistically significant, the badge color reflects the desired direction of the metric and the strength of confidence:

| Observed treatment effect | Marginal confidence<br />(p-value ≤ 0.05) | High confidence<br />(p-value ≤ 0.001) |
|:--------------------------|:------------------------------------------|:---------------------------------------|
| Against the desired direction | ![Degraded: +5.3%](https://img.shields.io/badge/Degraded-%2B5.3%25-fcae91 "Marginally statistically significant.") | ![Degraded: +5.3%](https://img.shields.io/badge/Degraded-%2B5.3%25-d03536 "Highly statistically significant.") |
| Matches the desired direction | ![Improved: +5.3%](https://img.shields.io/badge/Improved-%2B5.3%25-a1d99b "Marginally statistically significant.") | ![Improved: +5.3%](https://img.shields.io/badge/Improved-%2B5.3%25-157e3b "Highly statistically significant.") |
| Desired direction is neutral | ![Changed: +5.3%](https://img.shields.io/badge/Changed-%2B5.3%25-9ecae1 "Marginally statistically significant.") | ![Changed: +5.3%](https://img.shields.io/badge/Changed-%2B5.3%25-1c72af "Highly statistically significant.") |

</details>