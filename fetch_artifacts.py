"""Version v5.7.0: explicitly fetch checksum-verified public binary artifacts."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
from tempfile import NamedTemporaryFile
from urllib.parse import quote, urlparse
from urllib.request import urlopen

PROJECT_DIR = Path(__file__).resolve().parent
BASE_URL = "https://logs.reshub.lol/pysr-ext-higgs/0.1.0"
BINARY_SUFFIXES = {".png", ".pdf"}


def _manifest(expression_id, project_dir):
    if not re.fullmatch(r"[A-Za-z0-9_-]+", expression_id):
        raise ValueError("Provide a curated Expression_ID.")
    results = (Path(project_dir) / "results").resolve()
    folder = results / expression_id
    if folder.is_symlink() or not folder.resolve().is_relative_to(results):
        raise ValueError("Curated folder must remain inside results/.")
    record = json.loads((folder / "manifest.json").read_text())
    if record["expression_id"] != expression_id:
        raise ValueError("Expression_ID does not match the committed manifest.")
    return folder, record


def _target(folder, asset):
    relative = PurePosixPath(asset["path"])
    if relative.is_absolute() or ".." in relative.parts or "\\" in asset["path"]:
        raise ValueError("Artifact path must remain inside its curated folder.")
    target = folder.joinpath(*relative.parts)
    if target.is_symlink() or not target.resolve().is_relative_to(folder.resolve()):
        raise ValueError("Artifact path must not escape through a symlink.")
    if (not isinstance(asset["bytes"], int) or isinstance(asset["bytes"], bool) or asset["bytes"] < 1
            or not re.fullmatch(r"[a-f0-9]{64}", asset["sha256"])):
        raise ValueError("Manifest must supply a positive byte count and SHA-256.")
    return target


def _matches(path, asset):
    if not path.is_file() or path.stat().st_size != asset["bytes"]:
        return False
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest() == asset["sha256"]


def artifact_url(expression_id, relative_path, *, base_url=BASE_URL):
    """Return an immutable public URL; this function performs no network access."""
    relative = PurePosixPath(relative_path)
    if (not re.fullmatch(r"[A-Za-z0-9_-]+", expression_id) or relative.is_absolute()
            or ".." in relative.parts or "\\" in relative_path):
        raise ValueError("Provide an expression ID and a safe relative artifact path.")
    return base_url.rstrip("/") + "/" + quote(expression_id, safe="") + "/" + quote(relative.as_posix(), safe="/")


def cached_artifact(expression_id, relative_path, *, project_dir=PROJECT_DIR):
    """Return a verified cached file or None, without downloading anything."""
    folder, manifest = _manifest(expression_id, project_dir)
    matches = [asset for asset in manifest["files"] if asset["path"] == relative_path]
    if len(matches) != 1:
        raise ValueError("Artifact is absent or duplicated in the manifest.")
    target = _target(folder, matches[0])
    return target if _matches(target, matches[0]) else None


def fetch_expression(expression_id, *, project_dir=PROJECT_DIR, base_url=BASE_URL, timeout=30):
    """Fetch PNG/PDF files atomically; an invalid download never replaces a cache."""
    parsed = urlparse(base_url)
    if parsed.scheme != "https" and not (parsed.scheme == "http" and parsed.hostname in {"127.0.0.1", "localhost", "::1"}):
        raise ValueError("Use HTTPS for public downloads; HTTP is allowed only for local tests.")
    folder, manifest = _manifest(expression_id, project_dir)
    assets = [asset for asset in manifest["files"] if PurePosixPath(asset["path"]).suffix.lower() in BINARY_SUFFIXES]
    targets = [_target(folder, asset) for asset in assets]
    if len(set(targets)) != len(targets):
        raise ValueError("Manifest contains duplicate binary paths.")
    for asset, target in zip(assets, targets):
        if _matches(target, asset):
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = None
        try:
            digest, size = hashlib.sha256(), 0
            with NamedTemporaryFile(mode="wb", dir=target.parent, suffix=".part", delete=False) as stream:
                temporary = Path(stream.name)
                with urlopen(artifact_url(expression_id, asset["path"], base_url=base_url), timeout=timeout) as response:
                    while chunk := response.read(65536):
                        size += len(chunk)
                        if size > asset["bytes"]:
                            raise ValueError(f"Oversized artifact: {asset['path']}")
                        digest.update(chunk)
                        stream.write(chunk)
                if size != asset["bytes"] or digest.hexdigest() != asset["sha256"]:
                    raise ValueError(f"Artifact size/checksum mismatch: {asset['path']}")
                stream.flush()
                os.fsync(stream.fileno())
            temporary.replace(target)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
    return targets


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expression", default="L2HL_1_050", help="Curated Expression_ID; defaults to L2HL_1_050")
    args = parser.parse_args(argv)
    try:
        files = fetch_expression(args.expression)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Artifact download failed: {error}\n")
    print(f"Verified {len(files)} cached PNG/PDF files for {args.expression}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
