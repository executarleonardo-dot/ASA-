---
schema: LEO-ROUTINE-v1.0
id: C
name: Week Closing
owner: [leonardo-admin, deskos]
status: specify_and_test
source: "AGENT_BUILD_SPEC §14"
---

# Rotina C — Week Closing

- **trigger:** "feche minha semana", fim de ciclo / sexta-feira.
- **inputs:** workflows da semana, entregáveis produzidos, pendências, bloqueios.
- **required_context:** camadas 7 (workflow), 8 (estado).
- **allowed_tools:** leitura de trace/estado; geração de handoff DeskOS + Recycle.
- **confirmation_points:** escrita em memória/Planilha, decisão de carry_forward que altere prioridades.

## 3 etapas visíveis
```
1. REVISAR    — o que foi concluído vs. planejado
2. CLASSIFICAR— Recycle (manter/descartar/carregar)
3. ENCERRAR   — fechamento + handoff + preparo do próximo ciclo
```

## gates
```yaml
gate_id: C-G1
pass_when: [week_reviewed, recycle_classified, deskos_handoff_updated, next_cycle_seeded]
fail_when: [no_recycle_classification]
```

## output
fechamento semanal + `deskos_handoff` (status: completed) + Recycle.

## evidence
trace_id + handoff_id + lista de entregáveis com evidência.

## failure behavior
itens sem evidência → marcar `[GAP]`/`[LACUNA]`, não declarar concluído.

## state update
Recycle aplicado; carry_forward definido para Week Open seguinte.

## next action
semente do próximo ciclo (1 próxima ação).
