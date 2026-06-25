# ASA Admin — Component Selection (referência)

Fonte: `AGENT_BUILD_SPEC` §8/§35 e `references/ASA_AGENT_BLUEPRINT_SOURCE.md`.

## Decision logic
```text
simple_stable_task     → skill
broad_context          → progressive_disclosure
isolated_specialty     → subagent
repeatable_sequence    → workflow
distributed_capability → plugin
external_integration   → MCP
deterministic_event    → hook
high_risk_action       → human_approval
```

## Princípios
- Começar simples; escalar só com evidência (testes).
- Minimizar custo de contexto e de tooling.
- Separar conhecimento (reference) de autonomia (agente).
- Função única por Skill; um agente não duplica responsabilidade de outro.

## Anti-padrões (Don't)
- subagente para tarefa trivial;
- carregar toda a documentação no SKILL.md;
- delegar sem contrato de entrada/saída;
- dois agentes donos da mesma decisão.

## Menor arquitetura por complexidade (SPEC §8 P-01)
```text
simples      → resposta direta ou 1 Skill
especializada→ 1 Skill + contexto selecionado
composta     → Planner + Skills + síntese
crítica      → Planner + execução + crítica + verificação + síntese
aberta       → decomposição adaptativa + gates humanos
```
