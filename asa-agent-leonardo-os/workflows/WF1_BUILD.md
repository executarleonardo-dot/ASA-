---
schema: LEO-WORKFLOW-v1.0
id: WF1
name: BUILD
visible_steps: 3
source: "AGENT_BUILD_SPEC §13.1"
---

# WF1 — BUILD

## Gatilhos
criar · desenvolver · arquitetar · validar · refatorar · empacotar · gerar Skill/agente/workflow/template/produto.

## Interface visível
```
1. DEFINIR
2. DESENVOLVER
3. ENTREGAR
```

## Etapa 1 — DEFINIR
Interno: capturar problema; recuperar contexto; identificar solução; verificar duplicação; delimitar escopo; criar briefing; definir critérios.
```yaml
gate_id: WF1-G1
name: briefing_approved
pass_when: [problem_is_clear, user_is_defined, expected_output_is_defined, scope_is_bounded, resources_are_mapped, acceptance_criteria_exist]
fail_when: [goal_is_generic, user_is_unknown, equivalent_solution_already_exists, critical_dependencies_are_missing]
```

## Etapa 2 — DESENVOLVER
Interno: projetar arquitetura; mapear dependências; recuperar referências; selecionar menor stack; construir; integrar; testar; corrigir; retestar.
```yaml
gate_id: WF1-G2
name: component_validated
pass_when: [structure_is_complete, instructions_are_executable, critical_tests_pass, guardrails_are_active, dependencies_are_documented, original_problem_is_solved]
```

## Etapa 3 — ENTREGAR
Interno: revisar; documentar; empacotar; salvar; registrar; comunicar; produzir handoff.
```yaml
gate_id: WF1-G3
name: delivery_completed
pass_when: [final_package_exists, package_opens, version_is_registered, documentation_is_included, destination_is_accessible_or_marked_gap, handoff_exists, next_action_exists]
```

## Evidência / Trace
Registrar em `schemas/execution-trace.schema.yaml`. Handoff via `schemas/deskos-handoff.schema.yaml`.
