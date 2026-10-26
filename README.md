# PySR in Extended Higgs Sector Models

Symbolic-regression classification using the two mass features `mchi1` and `mchipm1` (GeV), with `exclusion` as the binary reference target. Expressions return continuous, uncalibrated scores.

**Earlier results withdrawn.** The owner has withdrawn every result outside the four retained expression IDs. Earlier published artifacts remain in Git history: [17-expression HP catalogue](https://github.com/wadewolfie999/pysr_ext_higgs/tree/dc77738e4ac520701ca35ac218a2bb8dbbd63284/results) and [historical TEMP_6_038 snapshot](https://github.com/wadewolfie999/pysr_ext_higgs/tree/036ab03beca29d1d2cfe9e8466d49123b03dfa77/results/TEMP_6_038).

The owner reports that an omitted `elementwise_loss` left earlier work using PySR's default squared-error objective, rather than the intended margin-classification objective. This is the owner's reason for withdrawal; the cause has not been authenticated separately for every historical run. Negative raw scores alone do not falsify a classifier's ranking. `L2HingeLoss()` is the owner's preferred loss for current work, not a demonstrated statistically superior objective.

## Retained results

| Retained expression | Saved loss | Complexity | Recorded test AUC (selection score) | Fitted curves |
|---|---|---:|---:|---|
| [EXP_6_072](results/EXP_6_072/manifest.json) | `LogitMarginLoss()` | 72 | 0.9637619186481049 | Unavailable |
| [ELEM_7_0198](results/ELEM_7_0198/manifest.json) | `LogitMarginLoss()` | 198 | 0.9644941298130999 | Unavailable |
| [L2HL_1_050](results/L2HL_1_050/manifest.json) | `L2HingeLoss()` | 50 | 0.9615986120334543 | Available |
| [L2HL_2_0235](results/L2HL_2_0235/manifest.json) | `L2HingeLoss()` | 235 | 0.9442093320165948 | Available |

The selected IDs and recorded decimal values are preserved. **Test AUC remains the selection metric by the owner's decision**, so it is not an untouched final-test estimate. Loss values from different objectives are not directly comparable.

![Preserved ROC figure for L2HL_1_050, the default saved expression.](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/L2HL_1_050/plots/roc_curve.png)

[Local results catalogue](wiki/Project-Registry.md) · [Method and limitations](wiki/Method-and-Limitations.md) · [Batch snapshot](results/current-runs-v0.1.0/README.md) · [Batch manifest](results/current-runs-v0.1.0/manifest.json)

## Public artifacts and optional local cache

The curated artifact package is served at [logs.reshub.lol](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/). Arvancloud manages public HTTPS and renewal; Caddy serves the public-file origin. Published version directories are immutable. PNG/PDF binaries live there and in ignored local cache; Git keeps code, candidate tables, expression source exports, and checksum manifests. Historical files already committed remain in Git history.

To explicitly download and verify the default expression's binary artifacts:

```bash
.venv/bin/python fetch_artifacts.py --expression L2HL_1_050
```

The command checks each file's committed byte count and SHA-256 before atomically replacing a cached file. Valid cached files require no network. An interrupted or invalid download leaves prior local bytes intact. Raw logs, checkpoints, environment files and backups are not served.

## Inspect saved results without training

From the repository root in the existing environment:

```bash
.venv/bin/python plot_sr.py
```

The default is the tracked curated `L2HL_1_050` expression. This path uses no checkpoint, PySR import, Julia startup, or fitting. It evaluates the fixed expression, displays four diagnostics, and saves nothing by default. In `plot_sr.py`, `RUN_SOURCE` can also name a raw run directory; set its matching `EXPRESSION_ID` explicitly. For curated inputs, a changed dataset fingerprint stops inspection.

`plot.ipynb` uses the same reader and default expression. Ordinary Run All evaluates the fixed expression and displays checksum-verified cached L2HL curve images, or links to the hosted images when they are not cached. It never downloads automatically. Keep `RUN_CURVE_FITS = False` for saved-result inspection. Setting it to `True` explicitly starts **16 new diagnostic searches**, eight per parent, and requires the corresponding local parent checkpoints. New tables, figures, settings, and child lineage go to fresh ignored directories under `output/curve_diagnostics/`.

Explicitly enabled offline plot saving uses `.temp/inspection/<Expression_ID>/`. Source evidence and curated results are protected from being used as the regeneration destination.

## Environment and setup

The inspected working environment uses **Python 3.13.7** and **PySR 2.7.0**; dependencies are recorded in `requirements.txt`. A new-machine installation has not been tested in this revision. With Python 3.13 available, the setup commands are:

```bash
git clone https://github.com/wadewolfie999/pysr_ext_higgs.git
cd pysr_ext_higgs
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Saved-result inspection needs the Python plotting/evaluation libraries. Training and explicitly enabled curve fitting additionally initialize PySR's Julia environment. The owner's separate Linux setup used Julia 1.11.9; that is not a verified cross-platform requirement. Exporting a new winner PDF requires `pdflatex` on PATH.

## Start a new training run

Review the configuration in `main.py` before executing:

```bash
.venv/bin/python main.py
```

This command starts a new search. The current configuration uses `L2HingeLoss()`, signed training labels `2*y-1`, balanced training weights, and test-AUC expression selection. Evaluation retains labels 0 and 1. Each new run writes its actual split row IDs, labels, weights, model parameters, dataset hash, and source hashes to `output/<RUN_ID>/run_metadata.json` before fitting.

## Evidence and repository layout

- `results/<Expression_ID>/`: committed candidate tables, expression source exports, and manifests; PNG/PDF files are optional ignored cache of the public artifact package.
- `results/current-runs-v0.1.0/`: retained logger snapshot, batch manifest, and explicitly reconstructed current split record.
- `output/` and `HP_output/`: ignored local runs and checkpoints. The root `.run_num1_logger.csv` is the mutable runtime ledger; the versioned batch is the durable catalogue record.
- `wiki/`: canonical Wiki publication sources. Other ignored local documentation drafts are not maintained in parallel.

Current reproduction on 12,280 observations matches all four recorded test AUCs exactly; exported NumPy predictions match the selected saved equations. The reconstructed split has 7,368 training, 1,228 validation, and 3,684 test rows. This does not authenticate original training membership or establish independent performance. Original numerical arrays for the two saved fitted-curve images were not serialized.

## Verification and publication status

```bash
PYTHONDONTWRITEBYTECODE=1 MPLBACKEND=Agg .venv/bin/python -m unittest discover -s tests -v
```

Tests use a stub for fitting orchestration; no real model fitting is part of this cleanup. [Accepted blueprint](docs/research-cleanup-blueprint-v0.1.0.md). [Verification record](docs/research-cleanup-verification-v0.1.0.json).

The curated artifact endpoint is published and independently checksum-verified. This repository contains the v5.7.0 workflow and the canonical sources for the [public Wiki](https://github.com/wadewolfie999/pysr_ext_higgs/wiki). The catalogue uses immutable artifact URLs; earlier catalogue entries remain withdrawn and accessible through pinned historical commits. [Deployment and rollback procedure](deployment/logs-reshub/0.1.0/README.md) · [Acceptance record](deployment/logs-reshub/0.1.0/verification-v0.1.0.json).

<sub>README v0.6.1 · Code release v5.7.0 · Notebook artifact v4.7.0 · Retained batch v0.1.0.</sub>
