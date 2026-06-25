#!/usr/bin/env python3
"""Valida referências internas a caminhos do pacote em arquivos .md/.yaml.
Verifica:
  - links markdown [txt](path) relativos;
  - tokens em crase `path` que começam por um diretório conhecido do pacote.
Ignora URLs, wildcards e caminhos de exemplo/futuro (allowlist).
Exit 0 se nenhuma referência quebrada."""
from __future__ import annotations
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KNOWN_PREFIXES = (
    "config/", "schemas/", "workflows/", "blueprints/", "templates/",
    "references/", "registries/", "evals/", "tests/", "scripts/", ".claude/",
)

# Caminhos intencionalmente ausentes (exemplos/estrutura futura).
IGNORE = {
    ".claude/settings.json",   # gerado a partir do .example pelo usuário
    "core/", "profiles/leonardo/", "profiles/future-icp/",  # estrutura futura ADR-003
}

MD_LINK = re.compile(r"\]\(([^)]+)\)")
CODE_PATH = re.compile(r"`([^`]+)`")


def iter_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "dist", "_sources", "follow-up-v2")]
        for fn in filenames:
            if fn.endswith((".md", ".yaml", ".yml")):
                yield os.path.join(dirpath, fn)


def is_candidate(token: str) -> bool:
    token = token.strip()
    if not token or token in IGNORE:
        return False
    if token.startswith(("http://", "https://", "#", "mailto:")):
        return False
    if any(c in token for c in "<>*?| "):
        return False
    return token.startswith(KNOWN_PREFIXES)


def exists(token: str, base_dir: str) -> bool:
    cand_root = os.path.join(ROOT, token)
    cand_rel = os.path.join(base_dir, token)
    if token.endswith("/"):
        return os.path.isdir(cand_root) or os.path.isdir(cand_rel)
    return os.path.exists(cand_root) or os.path.exists(cand_rel)


def main() -> int:
    broken = []
    checked = 0
    for path in sorted(iter_files()):
        base_dir = os.path.dirname(path)
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
        tokens = set(MD_LINK.findall(text)) | set(CODE_PATH.findall(text))
        for tok in tokens:
            tok = tok.split("#", 1)[0].strip()
            if is_candidate(tok):
                checked += 1
                if not exists(tok, base_dir):
                    broken.append((os.path.relpath(path, ROOT), tok))
    print(f"[links] referências verificadas: {checked} | quebradas: {len(broken)}")
    for rel, tok in broken:
        print(f"  BROKEN: {rel} -> {tok}")
    ok = not broken
    print("[links] RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
