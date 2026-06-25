---
name: create-validate-agentic-system
description: >-
  Comando alternativo do ASA. Cria e valida um sistema agêntico com ênfase em
  validação (evals, tests, gates) antes da entrega. Roteia para WF1 (BUILD) com
  foco na etapa de validação.
---

# /create-validate-agentic-system

> Alternativa a `/architect-agentic-system`, com ênfase em validação. Roteia para a **ASA Admin Skill**.

## Uso
`/create-validate-agentic-system <intenção>`

## Comportamento (3 etapas visíveis)
1. **DEFINIR** — requisitos + critérios de aceite.
2. **CONSTRUIR** — gerar componente.
3. **VALIDAR/ENTREGAR** — rodar evals/tests (`evals/`, `tests/`), aplicar gates, entregar com evidência.

## Roteamento
domain=build → WF1. `primary_skill: asa-admin`; auxiliares por dependência real.

## Guardrails
Evidência antes de aprovar; falha em critério crítico → reescrever; sem ação externa.

## Gaps
OQ-01 `[GAP]` (função histórica dos comandos não especificada).
