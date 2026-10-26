# Retained results snapshot — v0.1.0

Exactly four expressions are retained, in logger order. See `manifest.json` for their curated manifests and the withdrawal inventory.

`logger.csv` preserves recorded decimal strings and original repository-root-relative source paths. Only path whitespace and unavailable curve placeholders were normalized. Those source paths are provenance; portable downloads use each expression manifest's `files[].path`, relative to that manifest.

Copied artifacts retain their original bytes and export versions. Separate current-data metrics reproduce all four recorded test AUCs; reconstructed split membership does not authenticate historical training membership. Test AUC remains a selection score.

The two saved refitted-curve images have eight child runs each. Original numerical curve tables were not serialized. The manifest records their lineage and local source hashes without pretending the raw checkpoints are public.

This snapshot is prepared locally and is not a publication record. Raw runs and checkpoints remain local and ignored.
