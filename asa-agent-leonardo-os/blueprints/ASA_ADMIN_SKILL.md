---
schema: LEO-BLUEPRINT-v1.0
id: LEO-SKILL-ASA-ADMIN-v1
name: ASA Admin
type: runtime_skill
status: required
boundaries_ref: "DECISION_LOG.md ADR-001"
---

# Blueprint — ASA Admin Skill

## Identity
- **id:** LEO-SKILL-ASA-ADMIN-v1 · **type:** runtime_skill · **status:** required.

## Role
Meta-Skill de **engenharia, validação e evolução de sistemas agênticos**.

## Goal
Criar, validar, empacotar e evoluir agentes, Skills, workflows, plugins e contratos com a **menor arquitetura eficaz**.

## Scope (boundary — ADR-001)
**Deve conter:** requirements engineering; arquitetura de agentes; arquitetura de Skills; context engineering; component selection; workflow design; prompt engineering; tool/MCP mapping; permissions; evals; tests; packaging; versioning; gap detection; blueprint generation; refactoring; observability specification.

**Não deve conter:** agenda pessoal; briefing diário pessoal; rotina semanal de Leonardo; conteúdo físico do DeskOS; administração geral do negócio que não envolva o sistema agêntico.

## Pipeline
```text
DIAGNOSTICAR → ARQUITETAR → DELEGAR → EXECUTAR → MONITORAR →
VALIDAR → CORRIGIR → EMPACOTAR → EVOLUIR
```

## Component selection (decision logic)
```text
simple_stable_task→skill · broad_context→progressive_disclosure · isolated_specialty→subagent
repeatable_sequence→workflow · distributed_capability→plugin · external_integration→MCP
deterministic_event→hook · high_risk_action→human_approval
```

## Inputs / Outputs
- **Inputs:** requisitos, artefatos existentes, contexto, restrições, expected_output.
- **Outputs:** blueprint, Skill/agente/workflow, schema, eval/test, relatório de validação, pacote versionado.

## Allowed tools / approval points
Read/Write de artefatos do pacote; geração de schemas/templates; **empacotamento e versionamento** locais. Sem ação externa; sem credenciais.

## Quality criteria
Correção, completude, segurança, consistência, executabilidade, rastreabilidade, modularidade, testabilidade, anti-duplicação, boundaries claros. **Evidência antes de aprovação.**

## Failure handling / Stop conditions
Conflito de fontes → precedência ou decisão. Gate falhou → corrigir/retestar (máx 3). Risco crítico → parar.

## Examples
- **DO:** "Crie uma Skill para diagnosticar uma PME" → blueprint + SKILL.md enxuto + references + tests.
- **DON'T:** gerar o Daily Briefing pessoal (isso é Leonardo Admin); criar mega-Skill monolítica.

## Implementação
`.claude/skills/asa-admin/SKILL.md`. Taxonomia completa: `references/taxonomy.md` e `references/ASA_AGENT_BLUEPRINT_SOURCE.md`.

## Gaps
OQ-04 (possível duplicação de plugins Design).
