---
schema: LEO-ROUTINE-v1.0
id: D
name: Interview
owner: "ASA seleciona Skill adequada"
status: provisional
related_gap: OQ-03
source: "AGENT_BUILD_SPEC §14"
---

# Rotina D — Interview (provisional)

> `[GAP]` OQ-03: "Interview" pode não ser o nome oficial. Mantido com `status: provisional` até validação de Leonardo.

- **trigger:** "entreviste-me", coleta estruturada de requisitos/contexto.
- **inputs:** objetivo da entrevista, tópico, restrições.
- **required_context:** camadas 4 (caso de uso), 5 (problema).
- **allowed_tools:** leitura; sem ação externa.
- **confirmation_points:** persistir respostas em memória.

## 3 etapas visíveis
```
1. ENQUADRAR  — objetivo e escopo da entrevista
2. COLETAR    — perguntas mínimas necessárias (sem inventar)
3. SINTETIZAR — requisitos/contexto estruturados
```

## gates
```yaml
gate_id: D-G1
pass_when: [objective_clear, minimal_questions_only, structured_synthesis]
fail_when: [leading_questions, invented_data]
```

## output
síntese estruturada (requisitos/contexto) pronta para WF1/WF2/WF3.

## evidence
trace_id + lista de respostas com fonte.

## failure behavior
ambiguidade → perguntar o mínimo; não preencher lacuna com invenção.

## state update
nenhuma escrita persistente sem confirmação.

## next action
encaminhar síntese ao workflow adequado.
