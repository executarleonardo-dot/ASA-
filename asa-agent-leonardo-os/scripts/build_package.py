#!/usr/bin/env python3
"""Empacota o pacote ASA em dist/asa-agent-leonardo-os-v1.0.0.zip e gera checksum SHA-256.
Exclui .git, dist e caches. Exit 0 em sucesso."""
from __future__ import annotations
import hashlib
import os
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = "1.0.0"
PKG_NAME = f"asa-agent-leonardo-os-v{VERSION}.zip"
DIST = os.path.join(ROOT, "dist")
EXCLUDE_DIRS = {".git", "dist", "__pycache__", ".obsidian"}


def iter_pkg_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fn in filenames:
            if fn.endswith(".pyc"):
                continue
            yield os.path.join(dirpath, fn)


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    os.makedirs(DIST, exist_ok=True)
    out = os.path.join(DIST, PKG_NAME)
    if os.path.exists(out):
        os.remove(out)
    count = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(iter_pkg_files()):
            arc = os.path.join("asa-agent-leonardo-os", os.path.relpath(path, ROOT))
            zf.write(path, arc)
            count += 1
    digest = sha256(out)
    checksum_path = out + ".sha256"
    with open(checksum_path, "w", encoding="utf-8") as fh:
        fh.write(f"{digest}  {PKG_NAME}\n")
    size = os.path.getsize(out)
    print(f"[package] arquivos: {count}")
    print(f"[package] zip: dist/{PKG_NAME} ({size} bytes)")
    print(f"[package] sha256: {digest}")
    print(f"[package] checksum: dist/{PKG_NAME}.sha256")
    # valida abertura
    with zipfile.ZipFile(out) as zf:
        bad = zf.testzip()
    if bad is not None:
        print(f"[package] FAIL: arquivo corrompido no zip: {bad}")
        return 1
    print("[package] RESULT: PASS (pacote abre)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
