# Research repository cleanup and Wiki correction — blueprint v0.1.0

Approved 2026-10-26. Target: `/Users/vaheedgorgeen/libs/train-symexpr-bsm`.

## Goal and settled decisions

Deliver a reviewable, reproducible repository with exactly four retained winners: EXP_6_072, ELEM_7_0198, L2HL_1_050, L2HL_2_0235, in logger order. Keep test-AUC selection and all selected IDs. L2HingeLoss is the owner's preferred objective, not a proven statistically superior loss. Withdraw all other results from current claims while preserving history and raw local evidence.

## Evidence and worktree

Back up edited sources, notebook, runtime logger, four parent runs and 16 curve children, then verify hashes before editing. Preserve all 223 pre-existing result-file deletions. Curate unchanged winner exports, standard plots, parent candidate tables and two saved fitted-curve images. Version manifests and the batch snapshot at 0.1.0; distinguish source paths, curated asset paths, current reproduction, and unknown historical provenance. Preserve raw numeric decimal strings.

The root logger remains local and mutable; ignore it and remove it from tracking only at the authorized Git checkpoint. Keep raw outputs, checkpoints, environments, and old local drafts ignored. Track the chosen blueprint, verification artifact and focused tests.

## Workflow changes

Support both eight- and nine-column loggers, optional curve paths, atomic replacement and one winner per run. Add a no-checkpoint selected-expression reader for raw runs and curated manifests. Default script and notebook to curated L2HL_1_050; save regenerated figures only to a separate ignored inspection destination. Preserve do_split and test-AUC ranking.

Consolidate notebook curve fitting into one helper. RUN_CURVE_FITS defaults False; PySR loading/fitting occurs only in the enabled branch. Display preserved images by default. Future opted-in curves retain numerical tables, model settings, selected children and lineage; missing historical arrays remain unavailable. Future training records actual split identities, signed labels, weights, configuration, dataset and source hashes before fitting.

## Documentation and versions

Update README to 0.5.0, Wiki Home and Registry to 0.3.0, and add Method and Limitations 0.1.0. Align code at 5.6.0 and notebook artifact at 4.6.0. Explain owner withdrawal, the regression/margin loss distinction, valid negative raw scores, test selection scores, and the three different diagnostic types. Preserve copied export version labels. Canonical Wiki sources remain wiki/.

## Acceptance and authority

Use the existing environment and standard-library test runner. Prove logger compatibility/failure preservation; all retained predictions/AUCs and artifact hashes; portable offline inspection without ignored runs or PySR; zero default fits; stub-only curve orchestration; metadata, CSV, version/link consistency, and git diff --check. Review rendered README/Wiki and images.

No real training, branch, commit, push, PR, or Wiki publication is authorized. Deliver the verified review-ready diff. An empty git status requires separately authorized commits. If publication is later requested, synchronize the separate Wiki checkout, publish repository assets, then pin and publish Wiki links, and verify public results.

Version 0.1.0 is the first saved approved blueprint. Historical baseline: main 35ff005, four modified files, 223 deleted tracked result files, no staged changes.
