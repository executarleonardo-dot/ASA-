#!/usr/bin/env python3
"""Scan de secrets no pacote (heurístico). Exit !=0 se algo suspeito for achado.
Ignora binários e o diretório de fontes preservadas (_sources) e .git/dist."""
from __future__ import annotations
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATTERNS = [
    ("AWS Access Key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("AWS Secret", re.compile(r"(?i)aws_secret_access_key\s*[:=]\s*['\"]?[A-Za-z0-9/+=]{40}")),
    ("Private Key", re.compile(r"-----BEGIN (RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----")),
    ("Generic API key assignment", re.compile(r"(?i)\b(api[_-]?key|secret|passwd|password|token)\b\s*[:=]\s*['\"][^'\"]{12,}['\"]")),
    ("Slack token", re.compile(r"xox[abprs]-[0-9A-Za-z-]{10,}")),
    ("GitHub token", re.compile(r"gh[pousr]_[0-9A-Za-z]{30,}")),
    ("Google API key", re.compile(r"AIza[0-9A-Za-z\-_]{35}")),
    ("Bearer token", re.compile(r"(?i)bearer\s+[A-Za-z0-9\-_.=]{20,}")),
]

# Placeholders aceitáveis: não contam como secret.
PLACEHOLDER_HINTS = ("placeholder", "example", "<", ">", "your_", "xxxx", "changeme", "_comment")

SKIP_DIRS = {".git", "dist", "_sources", "follow-up-v2"}
TEXT_EXT = (".md", ".yaml", ".yml", ".json", ".py", ".txt", ".toml", ".ini", ".cfg")


def iter_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(TEXT_EXT):
                yield os.path.join(dirpath, fn)


def looks_placeholder(line: str) -> bool:
    low = line.lower()
    return any(h in low for h in PLACEHOLDER_HINTS)


def main() -> int:
    findings = []
    n = 0
    for path in sorted(iter_files()):
        n += 1
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                for i, line in enumerate(fh, 1):
                    if looks_placeholder(line):
                        continue
                    for name, pat in PATTERNS:
                        if pat.search(line):
                            findings.append((os.path.relpath(path, ROOT), i, name))
        except Exception:  # noqa: BLE001
            continue
    print(f"[secrets] arquivos escaneados: {n} | achados: {len(findings)}")
    for rel, ln, name in findings:
        print(f"  SECRET? {rel}:{ln} [{name}]")
    ok = not findings
    print("[secrets] RESULT:", "PASS (nenhum secret)" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
