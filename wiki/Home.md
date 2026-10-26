# PySR classification research

**Wiki revision v0.5.0 · Code release v5.7.0 · Updated 2026-10-26.**

The current Project Registry focuses on one expression: L2HL_1_050, a symbolic classifier using the mass features mchi1 and mchipm1 (GeV) with exclusion as its binary reference target.

## Start here

- [Current expression and its saved artifacts](Project-Registry)
- [Method, validation, and limitations](Method-and-Limitations)
- [Setup and saved-result inspection](https://github.com/wadewolfie999/pysr_ext_higgs/blob/main/README.md)

The current reconstructed validation AUC for the fixed expression is 0.9726962005193153. This is a reproduction on the current dataset split; original split membership is not known. The recorded test AUC was used as the original selection score and is not an independent final-test estimate.

## Workflow

1. Inspect the saved expression with plot_sr.py; this does not train a model.
2. Use main.py only when deliberately starting a new search.
3. Keep curve fitting disabled for saved-result inspection. Fitted curves, when explicitly enabled, use fresh diagnostic models and do not evaluate the fixed expression.
4. Use the Project Registry for the current result record and artifact links.

The repository’s wiki/ directory contains the canonical editable sources. Previous catalogue revisions remain historical records and are not the current registry.

<sub>Page v0.5.0 · Previous v0.4.1 · Code release v5.7.0.</sub>
