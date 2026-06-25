---
name: wf1-build
description: >-
  Executa o Workflow 1 — BUILD: DEFINIR → DESENVOLVER → ENTREGAR. Use para criar,
  desenvolver, arquitetar, validar, refatorar, empacotar ou gerar Skill/agente/
  workflow/template/produto.
---

# /wf1-build

> Workflow canônico: `workflows/WF1_BUILD.md`. 3 etapas visíveis + gates.

## Interface visível
```
1. DEFINIR
2. DESENVOLVER
3. ENTREGAR
```

## Gates
- WF1-G1 briefing_approved
- WF1-G2 component_validated
- WF1-G3 delivery_completed

## Guardrails
3 etapas; gates obrigatórios; confirmação para ação externa; trace 100%.
