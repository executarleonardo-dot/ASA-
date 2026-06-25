---
name: asa-admin
description: >-
  Meta-Skill de engenharia, validação e evolução de sistemas agênticos. Use para
  criar/validar/empacotar/evoluir agentes, Skills, workflows, plugins, schemas,
  evals e contratos com a menor arquitetura eficaz. Não administra a vida
  operacional de Leonardo (use leonardo-admin) nem a representação física (deskos).
---

# ASA Admin Skill

> Boundary canônico: `blueprints/ASA_ADMIN_SKILL.md` + ADR-001. Taxonomia: `references/taxonomy.md`.

## O que faz
Engenharia do **sistema agêntico**: requirements, arquitetura de agentes/Skills, context/prompt engineering, component selection, workflow design, tool/MCP mapping, permissions, evals, tests, packaging, versioning, gap detection, blueprints, refactoring, observability.

## Quando ativar (triggers)
- "crie uma Skill/agente/workflow", "valide/refatore/empacote", "gere blueprint", "mapeie dependências/tools", "defina evals".

## Quando NÃO ativar
- agenda/briefing/rotina pessoal → `leonardo-admin`;
- mapa semanal/handoff físico → `deskos`.

## Pipeline
```text
DIAGNOSTICAR → ARQUITETAR → DELEGAR → EXECUTAR → MONITORAR → VALIDAR → CORRIGIR → EMPACOTAR → EVOLUIR
```

## Component selection (decision logic)
```text
simple_stable_task→skill · broad_context→progressive_disclosure · isolated_specialty→subagent
repeatable_sequence→workflow · distributed_capability→plugin · external_integration→MCP
deterministic_event→hook · high_risk_action→human_approval
```

## Inputs / Outputs
- Inputs: requisitos, artefatos existentes, contexto, restrições, expected_output.
- Outputs: blueprint, Skill/agente/workflow, schema, eval/test, relatório de validação, pacote versionado.

## Tools & approval
Read/Write de artefatos do pacote; geração de schemas/templates; packaging/versionamento locais. **Sem ação externa; sem credenciais.**

## Método (3 etapas visíveis)
1. DIAGNOSTICAR/ARQUITETAR — requisitos + menor arquitetura.
2. CONSTRUIR/VALIDAR — gerar + testar (evidência antes de aprovar).
3. EMPACOTAR/EVOLUIR — versionar + registrar + próxima ação.

## Quality criteria
Correção, completude, segurança, consistência, executabilidade, rastreabilidade, modularidade, testabilidade, anti-duplicação, boundaries claros.

## Failure handling
Conflito de fontes → precedência (`config/source-precedence.yaml`). Gate falhou → corrigir/retestar (máx 3).

## Stop conditions
Risco crítico → parar. Capacidade inexistente → marcar `[GAP]`/`[GAP-RUNTIME]`.

## Do / Don't
- DO: "Crie uma Skill para diagnosticar uma PME" → blueprint + SKILL.md enxuto + references + tests.
- DON'T: gerar Daily Briefing pessoal; criar mega-Skill monolítica; carregar tudo no SKILL.md.

## Gaps
OQ-04 (possível duplicação de plugins Design — ver `registries/skill-registry.yaml`).
