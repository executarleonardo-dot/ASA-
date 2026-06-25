---
schema: LEO-WORKFLOW-v1.0
id: WF3
name: OPERATE
visible_steps: 3
source: "AGENT_BUILD_SPEC §13.3"
---

# WF3 — OPERATE

## Gatilhos
distribuir · analisar · decidir · reciclar.

## Interface visível
```
1. DISTRIBUIR
2. ANALISAR
3. RECICLAR
```

## Etapa 1 — DISTRIBUIR
Definir audiência e canal; **ação externa confirmada** antes de distribuir.
```yaml
gate_id: WF3-G1
name: distribution_confirmed
pass_when: [audience_defined, channel_defined, external_action_confirmed]
fail_when: [external_action_without_confirmation]
```

## Etapa 2 — ANALISAR
Analisar respostas/dados; tomar decisão.
```yaml
gate_id: WF3-G2
name: analysis_done
pass_when: [responses_or_data_analyzed, decision_made]
```

## Etapa 3 — RECICLAR
Atualizar backlog/memória/SOP **conforme autorização**; preparar novo ciclo.
```yaml
gate_id: WF3-G3
name: recycle_prepared
pass_when: [backlog_memory_sop_updated_as_authorized, next_cycle_prepared]
fail_when: [memory_written_without_confirmation]
```

## DoD
audiência/canal definidos · ação externa confirmada · respostas/dados analisados · decisão tomada · backlog/memória/SOP atualizados conforme autorização · novo ciclo preparado.
