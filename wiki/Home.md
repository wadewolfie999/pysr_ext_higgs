# Welcome to the `pysr_ext_higgs` Wiki

*Based on the [PySR paper](https://arxiv.org/abs/2305.01582).*

This Wiki documents symbolic-regression classification experiments using PySR in the extended-Higgs sector of BSM models, specifically the Inert Doublet Model (IDM).

**[Browse recorded results](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry)** to inspect a selected expression, its recorded figures, and downloadable files. The catalogue now includes 17 expressions from the HP batch and the preserved historical `TEMP_6_038` snapshot.

The catalogue distinguishes recorded measurements from missing historical provenance. Publishing a snapshot does not establish independent predictive performance.

## Featured HP expressions

- [TEMP_4_0141](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry#temp_4_0141): highest recorded test AUC in this batch, **0.963580**, complexity **141**.
- [TEMP_19_044](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry#temp_19_044): simpler comparison, recorded test AUC **0.963532**, complexity **44**.
- [Historical TEMP_6_038](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry#temp_6_038): preserved separately from `output/TEMP_6/`.

The inspected v5.3.0 pipeline ranks candidate expressions by `test_auc`; that score is part of selection and is not an untouched final-test estimate. Total AUC is descriptive. Saved validation-subset figures reuse one fixed expression across six subsets, with no refitting. The SD band is not a confidence interval. Figure labels remain as recorded; other full-precision split AUCs are not supplied by this logger.

## Start here

- **Results and downloads:** [Project Registry](https://github.com/wadewolfie999/pysr_ext_higgs/wiki/Project-Registry).
- **Run the project:** [repository README](https://github.com/wadewolfie999/pysr_ext_higgs#readme). Its platform notes distinguish the reported Linux Julia 1.11.9 setup from the PySR-initialized macOS environment.
- **Report an issue:** [repository Issues](https://github.com/wadewolfie999/pysr_ext_higgs/issues).

## Research workflow

The following describes code release **v5.3.0**, using [source reference `79966f0`](https://github.com/wadewolfie999/pysr_ext_higgs/tree/79966f022aa2e73574f24435792f2c53a0131b3a). This is an explanation of the current code, not the generating-commit provenance of an older run.

1. Review the dataset, features, and `PySRRegressor(...)` configuration in [main.py](https://github.com/wadewolfie999/pysr_ext_higgs/blob/79966f022aa2e73574f24435792f2c53a0131b3a/main.py). Running that script starts training.
2. Process the saved candidate expressions through `expr_indexer()`, `auc_recorder()`, and `top_three_sort()` in [sr.py](https://github.com/wadewolfie999/pysr_ext_higgs/blob/79966f022aa2e73574f24435792f2c53a0131b3a/sr.py).
3. Export the selected expressions, compile the winner, and record the winning row. Local source collections use `output/<RUN_ID>/` or `HP_output/<RUN_ID>/`, with expression files under `<Expression_ID>/` and plots under `plots/`. Public curated copies live under `results/<Expression_ID>/`.
4. Inspect an explicitly selected saved expression using [plot_sr.py](https://github.com/wadewolfie999/pysr_ext_higgs/blob/79966f022aa2e73574f24435792f2c53a0131b3a/plot_sr.py) or [plot.ipynb](https://github.com/wadewolfie999/pysr_ext_higgs/blob/79966f022aa2e73574f24435792f2c53a0131b3a/plot.ipynb).
5. Curate selected existing files for the public catalogue. The HP batch includes all available expression exports and saved plots. Full run directories and checkpoints are not part of the curated snapshot.

The current default ranks candidates by test AUC. Each catalogue entry states what its saved record supports; a current default does not fill gaps in historical provenance.

## Feedback

If something is lacking, let me know through [Issues](https://github.com/wadewolfie999/pysr_ext_higgs/issues) or either email:

```text
va.gorgin@mail.sbu.ac.ir
wadewolfie999@gmail.com
```

<sub>Page version 0.2.0 · Reviewed 2026-10-25 · Code reference v5.3.0.</sub>
