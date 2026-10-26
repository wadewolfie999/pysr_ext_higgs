# Public curated-artifact deployment

Deployment record v0.1.0 · Initial publication · 2026-10-26

The public package is [pysr-ext-higgs/0.1.0](https://logs.reshub.lol/pysr-ext-higgs/0.1.0/). [Verification](verification-v0.1.0.json) records trusted HTTPS, full file checksums, redirects, directory navigation, response boundaries, and the existing ResHub routes. [Package manifest](package-manifest-v0.1.0.json) pins all 62 source files: 23,338,354 bytes, including 38 PNG/PDF files totaling 22,836,460 bytes. The hosted copy also contains the package manifest itself.

## Ownership and transport

Use **Arvancloud-managed HTTPS** for this hosting workflow, as directed by the owner. Arvancloud owns the visitor certificate and automatic renewal. The existing valid managed certificate covers `*.reshub.lol`. Only the `logs` A record is proxied; its origin stays `95.38.182.130`, with a per-record HTTP origin override. The root and mail records retain their prior values and proxy settings. Existing domain-wide edge HTTPS and HTTP redirection were already enabled and were retained.

Caddy serves `/var/lib/reshub-logs` using the isolated [site configuration](logs.reshub.caddy). It accepts only GET and HEAD and supplies a basic file index. Visitor-to-edge traffic uses HTTPS; edge-to-origin traffic uses HTTP. This origin is exclusively for the approved public research files. It must never contain credentials, environment files, checkpoints, console logs, or private backups. Fixed-expression offline inspection depends on committed candidate tables and the existing dataset, not this service.

The original direct-Caddy certificate attempt was not accepted: the VPS could not reach Let's Encrypt, and ZeroSSL registration returned a regional-service restriction. No ZeroSSL account credentials or private keys were added to this repository. A local certificate-contact email is not a dependency of the deployed Arvancloud-managed certificate.

## Package and repository boundaries

Published versions are immutable by publication procedure: never overwrite `0.1.0`; use a new version directory for changed bytes. Hosting preserves the original expression export versions, selected IDs, scientific values, manifests, and lineage. Some hosted manifests retain prepublication status labels from the frozen curation snapshot; the deployment verification record establishes current hosting status and does not reconstruct historical scientific provenance.

Git retains the downloader, code, small candidate tables, expression source exports, and checksum manifests. PNG/PDF files remain optional ignored local cache. Historical committed files remain in Git history. To explicitly fetch and verify one expression:

```bash
.venv/bin/python fetch_artifacts.py --expression L2HL_1_050
```

The downloader verifies the committed SHA-256 and byte count before installing each file atomically. A failed or interrupted download preserves prior cache bytes. A valid cache requires no network. Notebook inspection never downloads automatically; missing curve images are represented by their public links. Curve fitting remains disabled by default.

## Publication procedure

For a future approved version, build an allowlisted package outside the public root. Reject symlinks and unsafe paths. Record source SHA-256 and byte counts, copy through SSH to a private staging directory, and verify every staged file before atomically moving the complete package into a new public version directory. Refuse an existing destination. The initial private staging location was `/var/lib/reshub-logs-incoming/endpoint-v0.1.0-20261026`; the public release is `/var/lib/reshub-logs/pysr-ext-higgs/0.1.0`.

Before changing Caddy, back up the exact active configuration, confirm its expected hashes, validate the candidate with `caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile`, and reload only after validation succeeds. Recheck existing ResHub routes. Do not expose staging directories or install an upload application.

The initial configuration backup is `/var/backups/reshub-logs/20261026T010304Z`. The direct-HTTPS-to-Arvancloud-origin change is backed up at `/var/backups/reshub-logs/20261026T105453Z-arvan`; the GET/HEAD restriction change is backed up at `/var/backups/reshub-logs/20261026T105726Z-arvan`. Backups are private on the VPS. The verification record pins the active configuration hashes.

Before excluding binaries from future Git tracking, fetch every public file over trusted HTTPS and compare it with the pinned source checksum. Test directory navigation, HTTP redirection, valid and invalid byte ranges, unsupported methods, and missing/private paths. Verify the explicit downloader in an empty temporary cache. Update editable README/Wiki sources only with verified versioned URLs; publishing those source revisions is a separate Git/Wiki action.

## Rollback and recovery

Do not execute rollback as a routine check. To withdraw the endpoint, remove only the `logs` DNS record in Arvancloud and invalidate its cached public paths if immediate withdrawal is required. Keep the immutable release and private backups for recovery. DNS caches can retain prior answers until their TTL expires. Turning off the proxy alone is not a working HTTPS rollback: the origin deliberately serves HTTP.

To remove the origin route, first compare the current configuration hashes with the verification record. Remove only `import /etc/caddy/logs.reshub.caddy` from `/etc/caddy/Caddyfile`, validate, then reload. Restore the previous file if validation/reload fails. Restore a complete historical Caddyfile only if the current hash matches the exact installed version and no later changes would be lost. Do not change the root ResHub or mail routes.

To recover service, restore the scoped HTTP origin configuration, validate/reload, then restore `logs` with proxy enabled and the HTTP origin override. Verify trusted HTTPS and all published checksums again. Neither a successful reload nor a browser page alone proves complete recovery.

## Versions

The endpoint/cache workflow adds capabilities while preserving saved-expression inspection: code 5.6.0 → 5.7.0; notebook 4.6.0 → 4.7.0; README 0.5.0 → 0.6.0; Wiki Home/Registry 0.3.0 → 0.4.0; Method and Limitations 0.1.0 → 0.2.0. New deployment, package-manifest, and verification records start at 0.1.0. Copied research exports keep their original version labels.
