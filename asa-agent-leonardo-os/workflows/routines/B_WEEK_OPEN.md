---
schema: LEO-ROUTINE-v1.0
id: B
name: Week Open
owner: [leonardo-admin, deskos]
status: specify_and_test
source: "AGENT_BUILD_SPEC §14"
---

# Rotina B — Week Open

- **trigger:** "abra minha semana", segunda-feira / início de ciclo.
- **inputs:** projetos ativos (máx 3), capacidade semanal (25h), pendências carregadas, prioridades.
- **required_context:** camadas 1, 3, 7 (workflow), 8 (estado).
- **allowed_tools:** leitura de Project Knowledge / Planilha; geração de handoff DeskOS.
- **confirmation_points:** escrita externa, alteração de memória, escrita na Planilha.

## 3 etapas visíveis
```
1. CONTEXTO    — confirmar 3 frentes da semana
2. PRIORIZAR   — 1 entregável/dia, foco matinal
3. ENTREGAR    — plano semanal + handoff DeskOS
```

## gates
```yaml
gate_id: B-G1
pass_when: [max_three_fronts, daily_primary_deliverable_mapped, deskos_handoff_prepared, next_action_defined]
fail_when: [more_than_three_fronts, no_handoff]
```

## output
plano semanal + `deskos_handoff` (status: preparing).

## evidence
trace_id + handoff_id.

## failure behavior
mais de 3 frentes → reduzir/escalar decisão a Leonardo. Dado ausente → `[GAP]`.

## state update
estado semanal preparado; carry_forward de pendências marcado no Recycle.

## next action
primeira ação da semana (foco matinal do dia 1).
