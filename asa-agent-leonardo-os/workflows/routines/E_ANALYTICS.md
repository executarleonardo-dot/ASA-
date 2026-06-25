---
schema: LEO-ROUTINE-v1.0
id: E
name: Analytics
owner: "ASA + Skill analítica selecionada"
status: specify
source: "AGENT_BUILD_SPEC §14"
---

# Rotina E — Analytics

- **trigger:** "analise o feedback", "métricas", "decida o próximo ciclo".
- **inputs:** dados/respostas coletados, métricas-alvo, período.
- **required_context:** camadas 5 (problema), 8 (estado).
- **allowed_tools:** leitura de dados; sem escrita externa sem confirmação.
- **confirmation_points:** decisões que disparem ação externa; escrita em memória/SOP.

## 3 etapas visíveis
```
1. COLETAR   — consolidar dados/feedback
2. ANALISAR  — extrair sinais e comparar com alvo
3. DECIDIR   — recomendação + próxima ação (decisão de Leonardo se alto risco)
```

## gates
```yaml
gate_id: E-G1
pass_when: [data_consolidated, signals_extracted, recommendation_with_evidence]
fail_when: [conclusion_without_evidence, unverified_claim]
```

## output
relatório analítico + recomendação + próxima ação.

## evidence
trace_id + fontes de dados + cálculos.

## failure behavior
dado insuficiente → declarar `[GAP]`; não afirmar resultado não verificado.

## state update
backlog/SOP atualizados conforme autorização (WF3 RECICLAR).

## next action
decisão do próximo ciclo (1 próxima ação).
