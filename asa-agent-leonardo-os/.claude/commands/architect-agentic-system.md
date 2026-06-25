---
name: architect-agentic-system
description: >-
  Comando principal do ASA. Arquiteta um sistema agêntico ponta a ponta a partir
  de uma intenção: diagnostica, escolhe a menor arquitetura, gera componentes
  (Skill/agente/workflow), valida e documenta. Roteia para WF1 (BUILD).
---

# /architect-agentic-system

> Função primária derivada do `AGENT_BUILD_SPEC` e do Blueprint (Agentic Systems Architect). Roteia para a **ASA Admin Skill** via WF1.

## Uso
`/architect-agentic-system <intenção>`

## Comportamento (3 etapas visíveis)
1. **DIAGNOSTICAR/ARQUITETAR** — requisitos, escopo, menor arquitetura (`asa-admin` + component selection).
2. **CONSTRUIR/VALIDAR** — gerar componentes + testes (evidência antes de aprovar).
3. **EMPACOTAR/EVOLUIR** — versionar, registrar trace, próxima ação.

## Roteamento
domain=build → WF1. Especialista temporário com `primary_skill: asa-admin`.

## Guardrails
Sem ação externa/credenciais; confirmação para escrita; 3 etapas; 1 próxima ação.

## Gaps
OQ-01 `[GAP]`: a função histórica dos "Commands 01–03" não foi especificada; este comando implementa a função canônica do ASA (arquitetar sistema agêntico). Não inventar funções adicionais.
