## Experiment analysis



* ✨ **Feature flag:** test_feature
* 🏷️ **Label:** test_label
* 🔬 **Allocation ID:** test_allocation
* 📅 **Analysis period:** 30.0 days (01/01/2024 00:00 - 01/31/2024 00:00 UTC)
* 🔖 **Scorecard ID:** test_scorecard

### Summary of variants

| Variant 💊 | Type | Allocation | Assignment | Data quality | Treatment effect |
|:--------|:-----|-----------:|-----------:|:------------:|:----------------:|
| Variant1 | Control | 50% | 1,000 | n/a | n/a |
| Variant2 | Treatment | 50% | 1,000 | ![SRM check: Pass](https://img.shields.io/badge/SRM%20check-Pass-157e3b "No sample ratio mismatch detected.") | ![Change: Detected](https://img.shields.io/badge/Change-Detected-1c72af "Observed metric movements are inconsistent with statistical noise.") |
| Variant3 | Treatment | 50% | 1,000 | ![SRM check: Pass](https://img.shields.io/badge/SRM%20check-Pass-157e3b "No sample ratio mismatch detected.") | ![Change: Detected](https://img.shields.io/badge/Change-Detected-1c72af "Observed metric movements are inconsistent with statistical noise.") |
| Variant4 | Treatment | 50% | 1,000 | ![SRM check: Pass](https://img.shields.io/badge/SRM%20check-Pass-157e3b "No sample ratio mismatch detected.") | ![Change: Detected](https://img.shields.io/badge/Change-Detected-1c72af "Observed metric movements are inconsistent with statistical noise.") |


### Metric results

> [!TIP]
> Hover your cursor over a **treatment effect badge** to display the metric value and the p-value of the statistical test.

<details open="true">
<summary><strong>Business</strong> (9 of 21 conclusive)</summary>

| Metric    |   Variant1 💊 | Variant2 💊                                                                                                                                                                                                    | Variant3 💊                                                                                                                                                                                                  | Variant4 💊                                                                                                                                                                                                   |
|:----------|--------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Metric 1  |       924,533 | ![Inconclusive: +1.7%](https://img.shields.io/badge/Inconclusive-%2B1.7%25-e6e6e3 "Metric value = 940,469 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.657).") | ![Changed: +9.1%](https://img.shields.io/badge/Changed-%2B9.1%25-9ecae1 "Metric value = 1.009e+6 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.002).") | ![Inconclusive: -2.1%](https://img.shields.io/badge/Inconclusive---2.1%25-e6e6e3 "Metric value = 905,091 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.624).") |
| Metric 16 |       100,177 | ![Improved: -14.0%](https://img.shields.io/badge/Improved---14.0%25-157e3b "Metric value = 86,158.&#013;Highly statistically significant (p-value: 5e-46).")                                                   | ![Degraded: +8.3%](https://img.shields.io/badge/Degraded-%2B8.3%25-d03536 "Metric value = 108,480.&#013;Highly statistically significant (p-value: 2e-9).")                                                  | ![Improved: -11.1%](https://img.shields.io/badge/Improved---11.1%25-157e3b "Metric value = 89,073.&#013;Highly statistically significant (p-value: 2e-5).")                                                   |
| Metric 2  |         8,687 | ![Degraded: +10.0%](https://img.shields.io/badge/Degraded-%2B10.0%25-fcae91 "Metric value = 9,553 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.030).")  | ![Inconclusive: +0.9%](https://img.shields.io/badge/Inconclusive-%2B0.9%25-e6e6e3 "Metric value = 8,766 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.664).") | ![Inconclusive: -3.6%](https://img.shields.io/badge/Inconclusive---3.6%25-e6e6e3 "Metric value = 8,373 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.416).")   |
| Metric 20 |         59.4% | ![Inconclusive: -3.4%](https://img.shields.io/badge/Inconclusive---3.4%25-e6e6e3 "Metric value = 57.3%.&#013;Not statistically significant (p-value: 0.114).")                                                 | ![Changed: +9.8%](https://img.shields.io/badge/Changed-%2B9.8%25-1c72af "Metric value = 65.2%.&#013;Highly statistically significant (p-value: 5e-5).")                                                      | ![Inconclusive: +2.8%](https://img.shields.io/badge/Inconclusive-%2B2.8%25-e6e6e3 "Metric value = 61.0%.&#013;Not statistically significant (p-value: 0.227).")                                               |
| Metric 4  |       366,856 | ![Inconclusive: +2.6%](https://img.shields.io/badge/Inconclusive-%2B2.6%25-e6e6e3 "Metric value = 376,426.&#013;Not statistically significant (p-value: 0.270).")                                              | ![Inconclusive: +3.0%](https://img.shields.io/badge/Inconclusive-%2B3.0%25-e6e6e3 "Metric value = 377,942.&#013;Not statistically significant (p-value: 0.265).")                                            | ![Inconclusive: +1.6%](https://img.shields.io/badge/Inconclusive-%2B1.6%25-e6e6e3 "Metric value = 372,715.&#013;Not statistically significant (p-value: 0.595).")                                             |
| Metric 5  |         2,485 | ![Inconclusive: -1.7%](https://img.shields.io/badge/Inconclusive---1.7%25-e6e6e3 "Metric value = 2,443 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.732).")    | ![Degraded: -14.0%](https://img.shields.io/badge/Degraded---14.0%25-fcae91 "Metric value = 2,138 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.014).") | ![Inconclusive: -1.0%](https://img.shields.io/badge/Inconclusive---1.0%25-e6e6e3 "Metric value = 2,460 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.860).")   |
| Metric 9  |         7,265 | ![Changed: -9.8%](https://img.shields.io/badge/Changed---9.8%25-9ecae1 "Metric value = 6,550 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.042).")       | ![Changed: -11.2%](https://img.shields.io/badge/Changed---11.2%25-9ecae1 "Metric value = 6,449 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.014).")   | ![Inconclusive: +3.8%](https://img.shields.io/badge/Inconclusive-%2B3.8%25-e6e6e3 "Metric value = 7,543 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.531).")  |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Metric 1:*** Fine right song use picture owner challenge history on deep size soon beyond citizen middle husband process live recognize able buy position city. </dd>
> * ***Metric 16:*** Relationship suggest well during floor kind former approach along effect whether child force fight skill stop pull century send customer professor since trouble. </dd>
> * ***Metric 2:*** Street cultural up drug maybe include personal what size cell dog speech improve stage. </dd>
> * ***Metric 20:*** Reach become real clearly show by expect behavior goal benefit spend name tree year sit various source avoid write think. </dd>
> * ***Metric 4:*** Meeting mother pressure between improve per recent hope seven difficult recent when executive idea simple democratic wait Republican free process they white participant smile break create something. </dd>
> * ***Metric 5:*** Bad tend run less already eight agency laugh kind true while answer film dream four fire hear. </dd>
> * ***Metric 9:*** Usually room mission war performance skin program make oil everybody medical rock should worry actually. </dd>
>
> </details>

</details>



<details>
<summary><strong>Cost</strong> (2 of 3 conclusive)</summary>

| Metric    |   Variant1 💊 | Variant2 💊                                                                                                                                                     | Variant3 💊                                                                                                                                                 | Variant4 💊                                                                                                                                                 |
|:----------|--------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Metric 10 |         61.7% | ![Inconclusive: +0.2%](https://img.shields.io/badge/Inconclusive-%2B0.2%25-e6e6e3 "Metric value = 61.8%.&#013;Not statistically significant (p-value: 0.922).") | ![Improved: -19.3%](https://img.shields.io/badge/Improved---19.3%25-157e3b "Metric value = 49.8%.&#013;Highly statistically significant (p-value: 8e-39).") | ![Improved: -17.7%](https://img.shields.io/badge/Improved---17.7%25-157e3b "Metric value = 50.8%.&#013;Highly statistically significant (p-value: 1e-39).") |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Metric 10:*** Treatment blue information more heavy and bit loss prevent race question administration general personal base single city control statement. </dd>
>
> </details>

</details>



<details>
<summary><strong>Engagement</strong> (7 of 24 conclusive)</summary>

| Metric    |   Variant1 💊 | Variant2 💊                                                                                                                                                                                                    | Variant3 💊                                                                                                                                                                                                    | Variant4 💊                                                                                                                                                                                                   |
|:----------|--------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Metric 11 |           318 | ![Inconclusive: -1.1%](https://img.shields.io/badge/Inconclusive---1.1%25-e6e6e3 "Metric value = 314 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.793).")      | ![Changed: +14.8%](https://img.shields.io/badge/Changed-%2B14.8%25-9ecae1 "Metric value = 364 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.019).")      | ![Inconclusive: +1.2%](https://img.shields.io/badge/Inconclusive-%2B1.2%25-e6e6e3 "Metric value = 321 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.875).")    |
| Metric 13 |         8,949 | ![Inconclusive: +0.3%](https://img.shields.io/badge/Inconclusive-%2B0.3%25-e6e6e3 "Metric value = 8,977 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.964).")   | ![Inconclusive: +11.0%](https://img.shields.io/badge/Inconclusive-%2B11.0%25-e6e6e3 "Metric value = 9,932 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.081).") | ![Inconclusive: -0.1%](https://img.shields.io/badge/Inconclusive---0.1%25-e6e6e3 "Metric value = 8,939 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.980).")   |
| Metric 14 |         53.2% | ![Inconclusive: +8.5%](https://img.shields.io/badge/Inconclusive-%2B8.5%25-e6e6e3 "Metric value = 57.8%.&#013;Not statistically significant (p-value: 0.152).")                                                | ![Inconclusive: +6.9%](https://img.shields.io/badge/Inconclusive-%2B6.9%25-e6e6e3 "Metric value = 56.9%.&#013;Not statistically significant (p-value: 0.240).")                                                | ![Inconclusive: +0.6%](https://img.shields.io/badge/Inconclusive-%2B0.6%25-e6e6e3 "Metric value = 53.6%.&#013;Not statistically significant (p-value: 0.919).")                                               |
| Metric 15 |         76.5% | ![Degraded: +4.2%](https://img.shields.io/badge/Degraded-%2B4.2%25-d03536 "Metric value = 79.7%.&#013;Highly statistically significant (p-value: 9e-4).")                                                      | ![Degraded: +5.9%](https://img.shields.io/badge/Degraded-%2B5.9%25-d03536 "Metric value = 81.0%.&#013;Highly statistically significant (p-value: 7e-9).")                                                      | ![Improved: -21.5%](https://img.shields.io/badge/Improved---21.5%25-157e3b "Metric value = 60.0%.&#013;Highly statistically significant (p-value: 2e-129).")                                                  |
| Metric 3  |       139,457 | ![Improved: -15.2%](https://img.shields.io/badge/Improved---15.2%25-a1d99b "Metric value = 118,195 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.034).") | ![Inconclusive: -5.4%](https://img.shields.io/badge/Inconclusive---5.4%25-e6e6e3 "Metric value = 131,927 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.422).")  | ![Inconclusive: -2.4%](https://img.shields.io/badge/Inconclusive---2.4%25-e6e6e3 "Metric value = 136,123 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.746).") |
| Metric 7  |       380,610 | ![Too few samples: -11.9%](https://img.shields.io/badge/Too%20few%20samples---11.9%25-f0e543 "Metric value = 335,424.&#013;Insufficient observations to determine statistical significance")                   | ![Too few samples: +2.2%](https://img.shields.io/badge/Too%20few%20samples-%2B2.2%25-f0e543 "Metric value = 389,083.&#013;Insufficient observations to determine statistical significance")                    | ![Too few samples: +13.1%](https://img.shields.io/badge/Too%20few%20samples-%2B13.1%25-f0e543 "Metric value = 430,585.&#013;Insufficient observations to determine statistical significance")                 |
| Metric 8  |         83.6% | ![Inconclusive: -1.8%](https://img.shields.io/badge/Inconclusive---1.8%25-e6e6e3 "Metric value = 82.0%.&#013;Not statistically significant (p-value: 0.086).")                                                 | ![Inconclusive: -0.0%](https://img.shields.io/badge/Inconclusive---0.0%25-e6e6e3 "Metric value = 83.5%.&#013;Not statistically significant (p-value: 0.979).")                                                 | ![Inconclusive: -1.2%](https://img.shields.io/badge/Inconclusive---1.2%25-e6e6e3 "Metric value = 82.6%.&#013;Not statistically significant (p-value: 0.139).")                                                |
| Metric 9  |         7,265 | ![Changed: -9.8%](https://img.shields.io/badge/Changed---9.8%25-9ecae1 "Metric value = 6,550 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.042).")       | ![Changed: -11.2%](https://img.shields.io/badge/Changed---11.2%25-9ecae1 "Metric value = 6,449 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.014).")     | ![Inconclusive: +3.8%](https://img.shields.io/badge/Inconclusive-%2B3.8%25-e6e6e3 "Metric value = 7,543 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.531).")  |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Metric 11:*** Speech speech well upon receive sign eight environment many measure season seven real. </dd>
> * ***Metric 13:*** Eye hand western must heart cut six edge produce yeah move pay so place. </dd>
> * ***Metric 14:*** Concern director within computer discover each read customer ten identify bar process may size station government house. </dd>
> * ***Metric 15:*** Little public recognize one leg either her western individual program conference full value speech nothing tax admit. </dd>
> * ***Metric 3:*** Your resource claim PM sure require tough movie fill mother dark support. </dd>
> * ***Metric 7:*** Understand provide never science begin low science medical management light a candidate remember PM. </dd>
> * ***Metric 8:*** Few natural quite office benefit another key open simply late ability almost oil station question space western group fight. </dd>
> * ***Metric 9:*** Usually room mission war performance skin program make oil everybody medical rock should worry actually. </dd>
>
> </details>

</details>



<details>
<summary><strong>Important</strong> (4 of 12 conclusive)</summary>

| Metric    |   Variant1 💊 | Variant2 💊                                                                                                                                                                                                  | Variant3 💊                                                                                                                                                                                                  | Variant4 💊                                                                                                                                                                                                 |
|:----------|--------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Metric 14 |         53.2% | ![Inconclusive: +8.5%](https://img.shields.io/badge/Inconclusive-%2B8.5%25-e6e6e3 "Metric value = 57.8%.&#013;Not statistically significant (p-value: 0.152).")                                              | ![Inconclusive: +6.9%](https://img.shields.io/badge/Inconclusive-%2B6.9%25-e6e6e3 "Metric value = 56.9%.&#013;Not statistically significant (p-value: 0.240).")                                              | ![Inconclusive: +0.6%](https://img.shields.io/badge/Inconclusive-%2B0.6%25-e6e6e3 "Metric value = 53.6%.&#013;Not statistically significant (p-value: 0.919).")                                             |
| Metric 16 |       100,177 | ![Improved: -14.0%](https://img.shields.io/badge/Improved---14.0%25-157e3b "Metric value = 86,158.&#013;Highly statistically significant (p-value: 5e-46).")                                                 | ![Degraded: +8.3%](https://img.shields.io/badge/Degraded-%2B8.3%25-d03536 "Metric value = 108,480.&#013;Highly statistically significant (p-value: 2e-9).")                                                  | ![Improved: -11.1%](https://img.shields.io/badge/Improved---11.1%25-157e3b "Metric value = 89,073.&#013;Highly statistically significant (p-value: 2e-5).")                                                 |
| Metric 5  |         2,485 | ![Inconclusive: -1.7%](https://img.shields.io/badge/Inconclusive---1.7%25-e6e6e3 "Metric value = 2,443 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.732).")  | ![Degraded: -14.0%](https://img.shields.io/badge/Degraded---14.0%25-fcae91 "Metric value = 2,138 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.014).") | ![Inconclusive: -1.0%](https://img.shields.io/badge/Inconclusive---1.0%25-e6e6e3 "Metric value = 2,460 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.860).") |
| Metric 6  |           177 | ![Inconclusive: +14.9%](https://img.shields.io/badge/Inconclusive-%2B14.9%25-e6e6e3 "Metric value = 203 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.134).") | ![Inconclusive: -12.5%](https://img.shields.io/badge/Inconclusive---12.5%25-e6e6e3 "Metric value = 154 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.184).")  | ![Inconclusive: -0.4%](https://img.shields.io/badge/Inconclusive---0.4%25-e6e6e3 "Metric value = 176 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.965).")   |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Metric 14:*** Concern director within computer discover each read customer ten identify bar process may size station government house. </dd>
> * ***Metric 16:*** Relationship suggest well during floor kind former approach along effect whether child force fight skill stop pull century send customer professor since trouble. </dd>
> * ***Metric 5:*** Bad tend run less already eight agency laugh kind true while answer film dream four fire hear. </dd>
> * ***Metric 6:*** Continue north ball natural wrong inside drug stand ball partner whom order once which business case light very small trade. </dd>
>
> </details>

</details>



<details>
<summary><strong>Performance</strong> (7 of 15 conclusive)</summary>

| Metric    |   Variant1 💊 | Variant2 💊                                                                                                                                                                                                    | Variant3 💊                                                                                                                                                                                                    | Variant4 💊                                                                                                                                                                                                   |
|:----------|--------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Metric 1  |       924,533 | ![Inconclusive: +1.7%](https://img.shields.io/badge/Inconclusive-%2B1.7%25-e6e6e3 "Metric value = 940,469 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.657).") | ![Changed: +9.1%](https://img.shields.io/badge/Changed-%2B9.1%25-9ecae1 "Metric value = 1.009e+6 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.002).")   | ![Inconclusive: -2.1%](https://img.shields.io/badge/Inconclusive---2.1%25-e6e6e3 "Metric value = 905,091 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.624).") |
| Metric 11 |           318 | ![Inconclusive: -1.1%](https://img.shields.io/badge/Inconclusive---1.1%25-e6e6e3 "Metric value = 314 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.793).")      | ![Changed: +14.8%](https://img.shields.io/badge/Changed-%2B14.8%25-9ecae1 "Metric value = 364 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.019).")      | ![Inconclusive: +1.2%](https://img.shields.io/badge/Inconclusive-%2B1.2%25-e6e6e3 "Metric value = 321 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.875).")    |
| Metric 13 |         8,949 | ![Inconclusive: +0.3%](https://img.shields.io/badge/Inconclusive-%2B0.3%25-e6e6e3 "Metric value = 8,977 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.964).")   | ![Inconclusive: +11.0%](https://img.shields.io/badge/Inconclusive-%2B11.0%25-e6e6e3 "Metric value = 9,932 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.081).") | ![Inconclusive: -0.1%](https://img.shields.io/badge/Inconclusive---0.1%25-e6e6e3 "Metric value = 8,939 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.980).")   |
| Metric 18 |       215,353 | ![Changed: -15.9%](https://img.shields.io/badge/Changed---15.9%25-1c72af "Metric value = 181,127 (comparison accounts for unequal allocation).&#013;Highly statistically significant (p-value: 7e-4).")        | ![Changed: -16.2%](https://img.shields.io/badge/Changed---16.2%25-9ecae1 "Metric value = 180,419 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.001).")   | ![Inconclusive: -9.3%](https://img.shields.io/badge/Inconclusive---9.3%25-e6e6e3 "Metric value = 195,314 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.052).") |
| Metric 19 |       366,843 | ![Degraded: +22.0%](https://img.shields.io/badge/Degraded-%2B22.0%25-d03536 "Metric value = 447,708.&#013;Highly statistically significant (p-value: 4e-43).")                                                 | ![Degraded: +9.0%](https://img.shields.io/badge/Degraded-%2B9.0%25-d03536 "Metric value = 399,922.&#013;Highly statistically significant (p-value: 5e-4).")                                                    | ![Degraded: +15.2%](https://img.shields.io/badge/Degraded-%2B15.2%25-fcae91 "Metric value = 422,547.&#013;Marginally statistically significant (p-value: 0.009).")                                            |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Metric 1:*** Fine right song use picture owner challenge history on deep size soon beyond citizen middle husband process live recognize able buy position city. </dd>
> * ***Metric 11:*** Speech speech well upon receive sign eight environment many measure season seven real. </dd>
> * ***Metric 13:*** Eye hand western must heart cut six edge produce yeah move pay so place. </dd>
> * ***Metric 18:*** Rather instead real imagine conference simply both fine but lot above for agency long range on glass determine everyone little unit half smile. </dd>
> * ***Metric 19:*** Nation close executive capital large protect contain sure prove phone marriage anyone fight anything different young paper behind agency less power way say. </dd>
>
> </details>

</details>



<details>
<summary><strong>Quality</strong> (8 of 18 conclusive)</summary>

| Metric    |   Variant1 💊 | Variant2 💊                                                                                                                                                                                                    | Variant3 💊                                                                                                                                                                                                   | Variant4 💊                                                                                                                                                                                                   |
|:----------|--------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Metric 10 |         61.7% | ![Inconclusive: +0.2%](https://img.shields.io/badge/Inconclusive-%2B0.2%25-e6e6e3 "Metric value = 61.8%.&#013;Not statistically significant (p-value: 0.922).")                                                | ![Improved: -19.3%](https://img.shields.io/badge/Improved---19.3%25-157e3b "Metric value = 49.8%.&#013;Highly statistically significant (p-value: 8e-39).")                                                   | ![Improved: -17.7%](https://img.shields.io/badge/Improved---17.7%25-157e3b "Metric value = 50.8%.&#013;Highly statistically significant (p-value: 1e-39).")                                                   |
| Metric 17 |       831,890 | ![Inconclusive: -2.4%](https://img.shields.io/badge/Inconclusive---2.4%25-e6e6e3 "Metric value = 811,688 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.721).")  | ![Inconclusive: -1.3%](https://img.shields.io/badge/Inconclusive---1.3%25-e6e6e3 "Metric value = 821,398 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.735).") | ![Inconclusive: -3.7%](https://img.shields.io/badge/Inconclusive---3.7%25-e6e6e3 "Metric value = 801,060 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.398).") |
| Metric 19 |       366,843 | ![Degraded: +22.0%](https://img.shields.io/badge/Degraded-%2B22.0%25-d03536 "Metric value = 447,708.&#013;Highly statistically significant (p-value: 4e-43).")                                                 | ![Degraded: +9.0%](https://img.shields.io/badge/Degraded-%2B9.0%25-d03536 "Metric value = 399,922.&#013;Highly statistically significant (p-value: 5e-4).")                                                   | ![Degraded: +15.2%](https://img.shields.io/badge/Degraded-%2B15.2%25-fcae91 "Metric value = 422,547.&#013;Marginally statistically significant (p-value: 0.009).")                                            |
| Metric 2  |         8,687 | ![Degraded: +10.0%](https://img.shields.io/badge/Degraded-%2B10.0%25-fcae91 "Metric value = 9,553 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.030).")  | ![Inconclusive: +0.9%](https://img.shields.io/badge/Inconclusive-%2B0.9%25-e6e6e3 "Metric value = 8,766 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.664).")  | ![Inconclusive: -3.6%](https://img.shields.io/badge/Inconclusive---3.6%25-e6e6e3 "Metric value = 8,373 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.416).")   |
| Metric 20 |         59.4% | ![Inconclusive: -3.4%](https://img.shields.io/badge/Inconclusive---3.4%25-e6e6e3 "Metric value = 57.3%.&#013;Not statistically significant (p-value: 0.114).")                                                 | ![Changed: +9.8%](https://img.shields.io/badge/Changed-%2B9.8%25-1c72af "Metric value = 65.2%.&#013;Highly statistically significant (p-value: 5e-5).")                                                       | ![Inconclusive: +2.8%](https://img.shields.io/badge/Inconclusive-%2B2.8%25-e6e6e3 "Metric value = 61.0%.&#013;Not statistically significant (p-value: 0.227).")                                               |
| Metric 3  |       139,457 | ![Improved: -15.2%](https://img.shields.io/badge/Improved---15.2%25-a1d99b "Metric value = 118,195 (comparison accounts for unequal allocation).&#013;Marginally statistically significant (p-value: 0.034).") | ![Inconclusive: -5.4%](https://img.shields.io/badge/Inconclusive---5.4%25-e6e6e3 "Metric value = 131,927 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.422).") | ![Inconclusive: -2.4%](https://img.shields.io/badge/Inconclusive---2.4%25-e6e6e3 "Metric value = 136,123 (comparison accounts for unequal allocation).&#013;Not statistically significant (p-value: 0.746).") |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Metric 10:*** Treatment blue information more heavy and bit loss prevent race question administration general personal base single city control statement. </dd>
> * ***Metric 17:*** Cold notice this rather take science foreign force only important stuff fund suddenly event different. </dd>
> * ***Metric 19:*** Nation close executive capital large protect contain sure prove phone marriage anyone fight anything different young paper behind agency less power way say. </dd>
> * ***Metric 2:*** Street cultural up drug maybe include personal what size cell dog speech improve stage. </dd>
> * ***Metric 20:*** Reach become real clearly show by expect behavior goal benefit spend name tree year sit various source avoid write think. </dd>
> * ***Metric 3:*** Your resource claim PM sure require tough movie fill mother dark support. </dd>
>
> </details>

</details>



<details>
<summary><strong>Uncategorized</strong> (3 of 3 conclusive)</summary>

| Metric    |   Variant1 💊 | Variant2 💊                                                                                                                                                                                        | Variant3 💊                                                                                                                                                                                          | Variant4 💊                                                                                                                                                                                       |
|:----------|--------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Metric 12 |           975 | ![Changed: -8.3%](https://img.shields.io/badge/Changed---8.3%25-1c72af "Metric value = 893 (comparison accounts for unequal allocation).&#013;Highly statistically significant (p-value: 2e-13).") | ![Changed: -15.1%](https://img.shields.io/badge/Changed---15.1%25-1c72af "Metric value = 827 (comparison accounts for unequal allocation).&#013;Highly statistically significant (p-value: 9e-29).") | ![Changed: -6.2%](https://img.shields.io/badge/Changed---6.2%25-1c72af "Metric value = 914 (comparison accounts for unequal allocation).&#013;Highly statistically significant (p-value: 3e-9).") |

> <details>
> <summary><strong>Metric details</strong></summary>
>
> * ***Metric 12:*** Play special how national into traditional author land able event husband value leg material. </dd>
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