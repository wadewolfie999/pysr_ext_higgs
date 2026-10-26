# PySR in Extended Higgs Sector Models

Symbolic-regression classification using the mass features mchi1 and mchipm1 (GeV) and the binary reference target exclusion. The expression returns a continuous, uncalibrated score.

## Current expression

The current user-facing result is L2HL_1_050.

| Record | Value |
|---|---|
| Objective | L2HingeLoss() |
| Complexity | 50 |
| Current validation ROC-AUC | 0.9726962005193153 |
| Recorded test ROC-AUC | 0.9615986120334543; used as the original expression-selection score |

The validation value is a current reproduction on the reconstructed split, not a recovered historical validation result. Original split membership is unknown. The recorded test AUC is a selection score, not an independent final-test estimate.

![Preserved ROC curve for L2HL_1_050.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/roc_curve.png)

[Project Registry](wiki/Project-Registry.md) · [Method and limitations](wiki/Method-and-Limitations.md) · [Expression files and manifest](results/L2HL_1_050/manifest.json)

## Inspect the saved expression

From the repository root, in the existing environment:

~~~bash
.venv/bin/python plot_sr.py
~~~

This evaluates the fixed expression and displays its diagnostics. It does not load a checkpoint, start PySR or Julia, fit a model, or save plots by default. Curated inspection stops if the current dataset fingerprint differs from the one in the expression manifest.

The notebook also supports saved-result inspection. Keep its curve-fit switch disabled for that path. If enabled, its curve workflow fits fresh diagnostic models; these runs are separate from evaluating the fixed expression and write to ignored directories under output/curve_diagnostics/.

## Expression artifacts

The expression’s binary plots are served from the immutable L2HL_1_050 directory at [logs.reshub.lol](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/). To download and verify those files into the local cache:

~~~bash
.venv/bin/python fetch_artifacts.py --expression L2HL_1_050
~~~

Each download is checked against the committed byte count and SHA-256 before it replaces a cached file. Downloads are explicit; ordinary inspection never fetches files automatically. Raw logs, checkpoints, environment files, and backups are not served.

## Data and evaluation

The current dataset has 12,280 rows and SHA-256 c8c8063c84a10143b6369f444a037ef5695ff13f5eef6f9bf00dc86880c3937a. The reconstructed split uses seed 42 and contains 7,368 training, 1,228 validation, and 3,684 test rows. Current reproduction of L2HL_1_050 matches its recorded test AUC and exported NumPy predictions. This does not authenticate the original split membership or establish independent performance.

## Environment and new runs

The inspected environment uses Python 3.13.7 and PySR 2.7.0. A new-machine installation has not been verified in this revision.

~~~bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
~~~

Review main.py before running a new training search:

~~~bash
.venv/bin/python main.py
~~~

Future runs record their actual split row IDs, labels, weights, model parameters, dataset hash, and source hashes before fitting. Training is separate from inspecting the saved expression.

## Repository sources

- results/L2HL_1_050/: the current expression exports, candidate table, and manifest; binary plots are optional local cache.
- output/ and HP_output/: ignored local runs and checkpoints.
- wiki/: canonical editable sources for the GitHub Wiki.

Previous catalogue revisions remain historical records in Git history. The current README and Wiki present L2HL_1_050 as the current expression.

<sub>README v0.7.0 · Expression record v0.1.0.</sub>
