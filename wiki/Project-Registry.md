# Retained results

**Wiki revision v0.4.1 · Updated 2026-10-26.** The four retained expressions below link to curated files at `logs.reshub.lol` under immutable versioned paths.

**Earlier results withdrawn.** The owner has withdrawn every result outside the four retained expression IDs. Earlier published artifacts remain in Git history: [17-expression HP catalogue](https://github.com/wadewolfie999/pysr_ext_higgs/tree/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results) and [historical TEMP_6_038 snapshot](https://github.com/wadewolfie999/pysr_ext_higgs/tree/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038).

The owner reports that an omitted `elementwise_loss` left earlier work using PySR's default squared-error objective, rather than the intended margin-classification objective. This is the owner's reason for withdrawal; the cause has not been authenticated separately for every historical run. Negative raw scores alone do not falsify a classifier's ranking. `L2HingeLoss()` is the owner's preferred loss for current work, not a demonstrated statistically superior objective.

## Current list

| Retained expression | Saved loss | Complexity | Recorded test AUC (selection score) | Fitted curves |
|---|---|---:|---:|---|
| [EXP_6_072](#user-content-exp_6_072) | `LogitMarginLoss()` | 72 | 0.9637619186481049 | Unavailable |
| [ELEM_7_0198](#user-content-elem_7_0198) | `LogitMarginLoss()` | 198 | 0.9644941298130999 | Unavailable |
| [L2HL_1_050](#user-content-l2hl_1_050) | `L2HingeLoss()` | 50 | 0.9615986120334543 | Available |
| [L2HL_2_0235](#user-content-l2hl_2_0235) | `L2HingeLoss()` | 235 | 0.9442093320165948 | Available |

The table preserves logger order. `L2HingeLoss()` is the owner's preferred objective; `ELEM_7_0198` has the highest recorded test selection score among these four entries. Neither fact establishes a controlled comparison of losses. [Method and limitations](Method-and-Limitations).

The downloadable expression files, standard figures, and hall-of-fame CSVs are unchanged copies. The additional train/validation/total values below are explicitly **current reproductions** on the fingerprinted current dataset and reconstructed split, not recovered original split provenance.

## EXP_6_072

| Record | Value |
|---|---|
| Parent run | `EXP_6` |
| Saved loss | `LogitMarginLoss()` |
| Complexity | 72 |
| Recorded objective value | 0.2468033104265783 |
| Recorded test AUC — selection score | 0.9637619186481049 |
| Original export label | `5.3.1` |

![Preserved EXP_6_072 ROC figure.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/plots/roc_curve.png)

[ROC PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/plots/roc_curve.pdf) · [SymPy](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/expression_sympy.txt) · [NumPy module](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/expression_lambda.py) · [TeX](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/expression.tex) · [Expression PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/expression.pdf) · [Candidate table](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/hall_of_fame.csv) · [Manifest and checksums](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/manifest.json)

| Current reproduction | ROC-AUC |
|---|---:|
| Training | 0.9624913313353541 |
| Validation | 0.9754782470457316 |
| Test — selection score | 0.9637619186481049 |
| Total — descriptive | 0.9641399722107414 |

<details>
<summary>Additional preserved fixed-expression figures</summary>

![EXP_6_072 raw scores and reference labels at observed mass pairs.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/plots/mass_plane.png)

[Mass-plane PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/plots/mass_plane.pdf)

![EXP_6_072 raw score scan with charged mass fixed at 2000 GeV.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/plots/mass_scan_1d.png)

[Scan PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/plots/mass_scan_1d.pdf)

![EXP_6_072 fixed-expression validation subset variability, with no refitting.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/plots/subset_variability.png)

[Subset PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/EXP_6_072/plots/subset_variability.pdf). Six subsets reuse one expression. Their SD band is not a confidence interval.

</details>

Fitted validation/learning curves are unavailable for this entry. No substitute curves were generated.

## ELEM_7_0198

| Record | Value |
|---|---|
| Parent run | `ELEM_7` |
| Saved loss | `LogitMarginLoss()` |
| Complexity | 198 |
| Recorded objective value | 0.2421791821480971 |
| Recorded test AUC — selection score | 0.9644941298130999 |
| Original export label | `5.3.1` |

![Preserved ELEM_7_0198 ROC figure.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/plots/roc_curve.png)

[ROC PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/plots/roc_curve.pdf) · [SymPy](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/expression_sympy.txt) · [NumPy module](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/expression_lambda.py) · [TeX](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/expression.tex) · [Expression PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/expression.pdf) · [Candidate table](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/hall_of_fame.csv) · [Manifest and checksums](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/manifest.json)

| Current reproduction | ROC-AUC |
|---|---:|
| Training | 0.9631089813491995 |
| Validation | 0.9763437726317277 |
| Test — selection score | 0.9644941298130999 |
| Total — descriptive | 0.9648159331081483 |

<details>
<summary>Additional preserved fixed-expression figures</summary>

![ELEM_7_0198 raw scores and reference labels at observed mass pairs.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/plots/mass_plane.png)

[Mass-plane PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/plots/mass_plane.pdf)

![ELEM_7_0198 raw score scan with charged mass fixed at 2000 GeV.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/plots/mass_scan_1d.png)

[Scan PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/plots/mass_scan_1d.pdf)

![ELEM_7_0198 fixed-expression validation subset variability, with no refitting.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/plots/subset_variability.png)

[Subset PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/ELEM_7_0198/plots/subset_variability.pdf). Six subsets reuse one expression. Their SD band is not a confidence interval.

</details>

Fitted validation/learning curves are unavailable for this entry. No substitute curves were generated.

## L2HL_1_050

| Record | Value |
|---|---|
| Parent run | `L2HL_1` |
| Saved loss | `L2HingeLoss()` |
| Complexity | 50 |
| Recorded objective value | 0.3425168330019069 |
| Recorded test AUC — selection score | 0.9615986120334543 |
| Original export label | `5.3.1` |

![Preserved L2HL_1_050 ROC figure.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/roc_curve.png)

[ROC PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/roc_curve.pdf) · [SymPy](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/expression_sympy.txt) · [NumPy module](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/expression_lambda.py) · [TeX](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/expression.tex) · [Expression PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/expression.pdf) · [Candidate table](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/hall_of_fame.csv) · [Manifest and checksums](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/manifest.json)

| Current reproduction | ROC-AUC |
|---|---:|
| Training | 0.9573333839771221 |
| Validation | 0.9726962005193153 |
| Test — selection score | 0.9615986120334543 |
| Total — descriptive | 0.9601292032444535 |

<details>
<summary>Additional preserved fixed-expression figures</summary>

![L2HL_1_050 raw scores and reference labels at observed mass pairs.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/mass_plane.png)

[Mass-plane PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/mass_plane.pdf)

![L2HL_1_050 raw score scan with charged mass fixed at 2000 GeV.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/mass_scan_1d.png)

[Scan PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/mass_scan_1d.pdf)

![L2HL_1_050 fixed-expression validation subset variability, with no refitting.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/subset_variability.png)

[Subset PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/subset_variability.pdf). Six subsets reuse one expression. Their SD band is not a confidence interval.

</details>

### Saved fitted-model diagnostics for L2HL_1

![Saved validation and learning curves for parent L2HL_1.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/valid-learn-curve.png)

[Full-size preserved image](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/valid-learn-curve.png). Eight fresh child fits produced this image: complexity limits 10, 15, 20, 25, then training fractions 0.25, 0.50, 0.75, 1.0 with maxsize 280. These child models use PySR's `model_selection='best'`, separately from this parent winner's test-AUC selection. The manifest records all eight child IDs and local source hashes. Original numerical curve arrays were not serialized; a single fit per point supplies no uncertainty estimate.

## L2HL_2_0235

| Record | Value |
|---|---|
| Parent run | `L2HL_2` |
| Saved loss | `L2HingeLoss()` |
| Complexity | 235 |
| Recorded objective value | 0.3923035167578615 |
| Recorded test AUC — selection score | 0.9442093320165948 |
| Original export label | `5.3.1` |

![Preserved L2HL_2_0235 ROC figure.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/plots/roc_curve.png)

[ROC PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/plots/roc_curve.pdf) · [SymPy](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/expression_sympy.txt) · [NumPy module](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/expression_lambda.py) · [TeX](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/expression.tex) · [Expression PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/expression.pdf) · [Candidate table](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/hall_of_fame.csv) · [Manifest and checksums](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/manifest.json)

| Current reproduction | ROC-AUC |
|---|---:|
| Training | 0.9417812482386989 |
| Validation | 0.9580705844947273 |
| Test — selection score | 0.9442093320165948 |
| Total — descriptive | 0.9441207569756248 |

<details>
<summary>Additional preserved fixed-expression figures</summary>

![L2HL_2_0235 raw scores and reference labels at observed mass pairs.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/plots/mass_plane.png)

[Mass-plane PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/plots/mass_plane.pdf)

![L2HL_2_0235 raw score scan with charged mass fixed at 2000 GeV.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/plots/mass_scan_1d.png)

[Scan PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/plots/mass_scan_1d.pdf)

![L2HL_2_0235 fixed-expression validation subset variability, with no refitting.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/plots/subset_variability.png)

[Subset PDF](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/plots/subset_variability.pdf). Six subsets reuse one expression. Their SD band is not a confidence interval.

</details>

### Saved fitted-model diagnostics for L2HL_2

![Saved validation and learning curves for parent L2HL_2.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/valid-learn-curve.png)

[Full-size preserved image](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_2_0235/valid-learn-curve.png). Eight fresh child fits produced this image: complexity limits 10, 15, 20, 25, then training fractions 0.25, 0.50, 0.75, 1.0 with maxsize 280. These child models use PySR's `model_selection='best'`, separately from this parent winner's test-AUC selection. The manifest records all eight child IDs and local source hashes. Original numerical curve arrays were not serialized; a single fit per point supplies no uncertainty estimate.

## Provenance and withdrawn records

[Retained batch manifest](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/current-runs-v0.1.0/manifest.json) · [Logger snapshot](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/current-runs-v0.1.0/logger.csv) · [Current reconstructed row identities](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/current-runs-v0.1.0/current-reproduction-splits.json)

Each curated manifest distinguishes source paths from portable asset paths, preserves original export labels, and records SHA-256 hashes. Current reproduction uses dataset hash `c8c8063c84a10143b6369f444a037ef5695ff13f5eef6f9bf00dc86880c3937a`, split seed 42, and 7,368/1,228/3,684 train/validation/test rows. Exact score reproduction does not authenticate original training membership.

<details>
<summary>Withdrawn published expressions — historical downloads only</summary>

These 18 entries are outside the current retained list. Their 223 previously tracked files remain available through Git history, and are removed from the current working catalogue.

| Withdrawn expression | Historical manifest |
|---|---|
| `TEMP_10_0479` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_10_0479/manifest.json) |
| `TEMP_11_071` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_11_071/manifest.json) |
| `TEMP_12_064` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_12_064/manifest.json) |
| `TEMP_13_068` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_13_068/manifest.json) |
| `TEMP_14_044` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_14_044/manifest.json) |
| `TEMP_15_068` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_15_068/manifest.json) |
| `TEMP_16_079` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_16_079/manifest.json) |
| `TEMP_17_052` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_17_052/manifest.json) |
| `TEMP_18_064` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_18_064/manifest.json) |
| `TEMP_19_044` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_19_044/manifest.json) |
| `TEMP_1_0202` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_1_0202/manifest.json) |
| `TEMP_2_070` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_2_070/manifest.json) |
| `TEMP_3_065` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_3_065/manifest.json) |
| `TEMP_4_0141` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_4_0141/manifest.json) |
| `TEMP_5_059` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_5_059/manifest.json) |
| `TEMP_6_0138` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_6_0138/manifest.json) |
| `TEMP_6_038` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038/manifest.json) |
| `TEMP_7_082` | [Archived record](https://github.com/wadewolfie999/pysr_ext_higgs/blob/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results/TEMP_7_082/manifest.json) |

</details>

[Home](Home) · [Method and limitations](Method-and-Limitations)

<sub>Page v0.4.1 · Previous v0.4.0 · Retained batch v0.1.0.</sub>
