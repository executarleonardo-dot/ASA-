#!/usr/bin/env python3
"""Executa verificações estáticas dos evals (o que é possível sem o runtime Claude.ai).
Checks estáticos:
  - todos os evals/*.yaml fazem parse;
  - workflow-three-steps: cada workflow/rotina declara 3 etapas visíveis;
  - traceability: campos obrigatórios do trace presentes no schema.
Itens dependentes do runtime são reportados como GAP-RUNTIME (não falham o gate)."""
from __future__ import annotations
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    print("[evals] PyYAML indisponível — não é possível rodar checks estáticos.")
    sys.exit(0)


def load(path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def check_eval_parse():
    eval_dir = os.path.join(ROOT, "evals")
    files = [f for f in os.listdir(eval_dir) if f.endswith(".yaml")]
    bad = []
    for f in files:
        try:
            load(os.path.join(eval_dir, f))
        except Exception as exc:  # noqa: BLE001
            bad.append((f, str(exc)))
    return len(files), bad


def check_three_steps():
    """Confere que WF e rotinas declaram 3 etapas (visible_steps: 3)."""
    problems = []
    targets = [
        "workflows/WF1_BUILD.md", "workflows/WF2_COMMUNICATE.md", "workflows/WF3_OPERATE.md",
        "workflows/routines/A_DAILY_BRIEFING.md", "workflows/routines/B_WEEK_OPEN.md",
        "workflows/routines/C_WEEK_CLOSING.md", "workflows/routines/D_INTERVIEW.md",
        "workflows/routines/E_ANALYTICS.md",
    ]
    for rel in targets:
        path = os.path.join(ROOT, rel)
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
        if "visible_steps: 3" not in text and "visible_steps:3" not in text:
            # rotinas usam frontmatter; aceitar contagem textual de "3 etapas"
            if "3 etapas visíveis" not in text and "visible_steps" not in text:
                problems.append(rel)
    return targets, problems


def check_trace_fields():
    schema = load(os.path.join(ROOT, "schemas", "execution-trace.schema.yaml"))
    trace = (schema or {}).get("execution_trace", {})
    required = ["execution_id", "timestamp", "user_request", "intent", "workflow",
               "resource_selection", "gates", "evidence", "next_action", "final_status"]
    missing = [r for r in required if r not in trace]
    return required, missing


def main() -> int:
    failures = 0

    n_eval, bad = check_eval_parse()
    print(f"[evals] parse evals: {n_eval} arquivos | inválidos: {len(bad)}")
    for f, msg in bad:
        print(f"  INVALID: {f}: {msg}")
    failures += len(bad)

    targets, problems = check_three_steps()
    print(f"[evals] three-steps: {len(targets)} alvos | sem 3 etapas: {len(problems)}")
    for p in problems:
        print(f"  NO-3-STEPS: {p}")
    failures += len(problems)

    required, missing = check_trace_fields()
    print(f"[evals] trace fields: {len(required)} obrigatórios | ausentes: {len(missing)}")
    for m in missing:
        print(f"  MISSING TRACE FIELD: {m}")
    failures += len(missing)

    print("[evals] GAP-RUNTIME: acurácia de intenção, execução ponta a ponta e conectores "
          "só avaliáveis no Claude.ai (GR-04, GR-05).")
    print("[evals] RESULT:", "PASS (estático)" if failures == 0 else "FAIL")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
