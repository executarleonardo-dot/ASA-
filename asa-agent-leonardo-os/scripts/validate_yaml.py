#!/usr/bin/env python3
"""Faz parse de todos os arquivos .yaml/.yml do pacote. Exit 0 se todos válidos."""
from __future__ import annotations
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    print("[yaml] PyYAML indisponível — pulando parse estrito (instale pyyaml).")
    yaml = None


def iter_yaml_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "dist")]
        for fn in filenames:
            if fn.endswith((".yaml", ".yml")):
                yield os.path.join(dirpath, fn)


def main() -> int:
    files = sorted(iter_yaml_files())
    if yaml is None:
        return 0
    errors = []
    for path in files:
        try:
            with open(path, "r", encoding="utf-8") as fh:
                list(yaml.safe_load_all(fh))
        except Exception as exc:  # noqa: BLE001
            errors.append((os.path.relpath(path, ROOT), str(exc)))
    print(f"[yaml] arquivos verificados: {len(files)} | erros: {len(errors)}")
    for rel, msg in errors:
        print(f"  INVALID: {rel}: {msg}")
    ok = not errors
    print("[yaml] RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
