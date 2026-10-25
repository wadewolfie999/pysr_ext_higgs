# HP run-num1 recorded-output snapshot

Package version **0.1.0** · Curated **2026-10-25** · Export labels **v5.3.0**.

This package captures the 17-row winner logger and indexes all available expression exports and saved plots from `HP_output`. It contains 188 copied artifacts (87,287,372 bytes), stored in the sibling expression directories. No checkpoint is required to read the exported expressions.

- [Exact logger snapshot](logger.csv): unchanged eight-column CSV, including original source paths.
- [Batch manifest](manifest.json): complete entry inventory, counts, ledger hash, and preparation reference.
- [Validation record](verification.json): copy checks, structural checks, identity checks, and preservation results.
- [Repository overview](../../README.md).
- [Wiki publication sources](../../wiki/Home.md) and [Project Registry](../../wiki/Project-Registry.md).

## Reading the record

Expression exports and manifests are in `../<Expression_ID>/`; plots, where present, are in its `plots/` subdirectory. Each manifest maps original source paths to curated files and records SHA-256 hashes. The logger paths intentionally remain unchanged and refer to local source collections, not the curated layout.

The featured entries are `TEMP_4_0141` (recorded AUC leader) and `TEMP_19_044` (simpler comparison). The catalogue ranks this batch by the full-precision recorded test AUC. Plots are unavailable for `TEMP_1_0202` and `TEMP_2_070`. `TEMP_8` and `TEMP_9` have no finalized logger rows; no cause is assigned here.

The inspected v5.3.0 pipeline ranks candidate expressions by `test_auc`; that score is part of selection and is not an untouched final-test estimate. Total AUC is descriptive. Saved validation-subset figures reuse one fixed expression across six subsets, with no refitting. The SD band is not a confidence interval. Figure labels remain as recorded; other full-precision split AUCs are not supplied by this logger.

These are preserved recorded outputs. No predictions, AUCs, or figures were recalculated and no model was retrained for this catalogue. The original generating commit, training-data fingerprint, split membership, run date, and run-specific selection invocation are not established by the winner CSV. Exported expressions return raw, uncalibrated scores.

The preparation commit identifies the checkout used to curate these copies. It does not establish the generating commit, original training data, or original split membership. The separate historical snapshot from `output/TEMP_6/TEMP_6_038/` is preserved without revision.

## Version record

README: **0.3.1 → 0.4.0**, for the substantial replacement of featured results and public links. Wiki Home and Project Registry: **0.1.0 → 0.2.0**, for the expanded catalogue. This batch and its new expression manifests start at **0.1.0**. The existing historical snapshot remains **0.1.0**; science code remains **v5.3.0**. Source files retain their original content and version labels.

## Publication sequence

This is a local prepared update. No commits, pushes, or live wiki edits are part of curation. The new wiki artifact links currently target `main` as draft publication locations and will resolve only after the repository update is published. Existing historical links remain pinned to their original commit.

After publication is explicitly requested, publish repository artifacts first, replace only the new wiki artifact `main` references with the resulting repository commit SHA, then publish `wiki/Home.md` and `wiki/Project-Registry.md` to the separate wiki repository. Verify live page anchors, image loads, and downloads afterwards. Do not replace the preparation reference with the publication commit or alter historical links.
