# Tests — Regressão

Conjunto mínimo a reexecutar a cada mudança, para preservar comportamento (SPEC §29).

| # | Invariante | Verificação |
|---|---|---|
| 1 | 3 etapas visíveis em todos os workflows/rotinas | `evals/workflow-three-steps.yaml` |
| 2 | trace em 100% das execuções | `evals/traceability.yaml` |
| 3 | ação externa sempre confirmada | `evals/safety.yaml` |
| 4 | 1 agente runtime + 3 Skills | `registries/agent-registry.yaml`, `skill-registry.yaml` |
| 5 | boundaries sem sobreposição | ADR-001 + skills |
| 6 | nenhum secret | `scripts/scan_secrets.py` |
| 7 | estrutura completa | `scripts/validate_structure.py` |

**Fail if:** qualquer invariante quebra após mudança.
