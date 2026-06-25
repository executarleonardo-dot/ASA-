---
schema: LEO-ROUTINE-v1.0
id: A
name: Daily Briefing
owner: leonardo-admin
status: specify_and_test
source: "AGENT_BUILD_SPEC §14"
---

# Rotina A — Daily Briefing

- **trigger:** "briefing", "meu dia", início do dia (foco matinal).
- **inputs:** agenda do dia, projetos ativos, pendências, capacidade restante.
- **required_context:** camadas 1 (identidade), 3 (projeto), 8 (estado).
- **allowed_tools:** leitura de Project Knowledge / Planilha (somente leitura).
- **confirmation_points:** qualquer escrita externa ou em memória.

## 3 etapas visíveis
```
1. CONTEXTO   — recuperar agenda, projetos, pendências
2. PRIORIZAR  — 1 entregável primário do dia + foco matinal
3. ENTREGAR   — briefing + próxima ação única
```

## gates
```yaml
gate_id: A-G1
pass_when: [context_recovered, single_primary_deliverable_defined, next_action_defined]
fail_when: [generic_briefing, no_next_action]
```

## output
briefing diário (RESUMO/DECISÃO/PRÓXIMA AÇÃO) com baixa carga cognitiva.

## evidence
trace_id + referência ao estado consultado.

## failure behavior
dado crítico ausente → perguntar mínimo; não-crítico → `[GAP]` + suposição explícita.

## state update
atualizar estado do dia (sem escrita externa sem confirmação).

## next action
1 próxima ação concreta para a manhã.
