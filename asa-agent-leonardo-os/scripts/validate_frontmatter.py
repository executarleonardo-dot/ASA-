#!/usr/bin/env python3
"""Valida frontmatter YAML dos agentes e Skills.
- .claude/agents/*.md: frontmatter com name, description (tools opcional/lista).
- .claude/skills/*/SKILL.md: frontmatter com name, description.
Exit 0 se todos válidos."""
from __future__ import annotations
import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None


def parse_frontmatter(path: str):
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    if not text.startswith("---"):
        return None, "sem frontmatter (não inicia com ---)"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "frontmatter mal delimitado"
    block = parts[1]
    if yaml is None:
        # checagem mínima textual
        data = {}
        for line in block.splitlines():
            if ":" in line and not line.startswith(" "):
                k = line.split(":", 1)[0].strip()
                data[k] = True
        return data, None
    try:
        return yaml.safe_load(block) or {}, None
    except Exception as exc:  # noqa: BLE001
        return None, f"YAML inválido: {exc}"


def check(path: str, required, want_tools_list=False):
    data, err = parse_frontmatter(path)
    rel = os.path.relpath(path, ROOT)
    if err:
        return [f"{rel}: {err}"]
    problems = []
    for key in required:
        if key not in data or data.get(key) in (None, ""):
            problems.append(f"{rel}: campo obrigatório ausente/vazio: {key}")
    if want_tools_list and "tools" in data and yaml is not None:
        if not isinstance(data["tools"], list):
            problems.append(f"{rel}: 'tools' deve ser lista")
    return problems


def main() -> int:
    problems = []
    for path in sorted(glob.glob(os.path.join(ROOT, ".claude/agents/*.md"))):
        problems += check(path, ["name", "description"], want_tools_list=True)
    for path in sorted(glob.glob(os.path.join(ROOT, ".claude/skills/*/SKILL.md"))):
        problems += check(path, ["name", "description"])
    n = len(glob.glob(os.path.join(ROOT, ".claude/agents/*.md"))) + \
        len(glob.glob(os.path.join(ROOT, ".claude/skills/*/SKILL.md")))
    print(f"[frontmatter] componentes verificados: {n} | problemas: {len(problems)}")
    for p in problems:
        print(f"  {p}")
    ok = not problems
    print("[frontmatter] RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
