# Taxonomy — ASA / Agentic Systems Architect

**Schema:** LEO-TAXONOMY-v1.0 · Derivado de AGENT_BUILD_SPEC (Apêndice A) e `references/ASA_AGENT_BLUEPRINT_SOURCE.md`.

## 1. Famílias de classificação

- **FUNCTION** — o que o agente executa.
- **SPECIALTIES** — em quais domínios possui competência.
- **CAPABILITIES** — quais operações concretas consegue realizar.
- **RESPONSIBILITIES** — por quais resultados e controles responde.

## 2. Funções do ASA

requirements engineering · knowledge architecture · interface architecture · agentic architecture · component selection · workflow architecture · orchestration and supervision · context engineering · prompt engineering · Skill engineering · plugin architecture · tool and MCP engineering · governance and permissions · security and safety · validation and evaluation · packaging and distribution · observability · lifecycle evolution.

## 3. Especialidades

multi-agent system design · Claude Code · Claude.ai · Skills · subagents · plugins · hooks · MCP · progressive disclosure · human-in-the-loop · least privilege · context isolation · semantic tagging · version control · test-driven decomposition · agent evaluation · failure recovery.

## 4. Capacidades (ciclo)

```text
diagnosticar → arquitetar → selecionar → decompor → delegar → construir →
integrar → validar → corrigir → empacotar → registrar → monitorar → evoluir
```

## 5. Intent taxonomy (Intent Classifier — SPEC §15)

```yaml
intent:
  domain: [build, communicate, operate]
  use_case: [diagnose, research, plan, write, build, review, administer, custom]
  complexity: [simple, compound, open]
  risk: [low, medium, high, critical]
```

## 6. Component selection (decision logic — Blueprint)

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

## 7. Master tags (referência do Blueprint)

- **Function tags:** #requirement-analysis #problem-framing #knowledge-architecture #interface-architecture #agentic-system-design #component-selection #workflow-design #agent-orchestration #context-management #prompt-architecture #skill-engineering #plugin-design #tool-integration #agent-governance #agent-security #artifact-validation #agent-observability #failure-recovery #memory-governance #artifact-packaging #system-evolution #delegation-design #completion-control
- **Capability tags:** #analyze #diagnose #classify #design #decompose #select #create #delegate #orchestrate #integrate #monitor #validate #secure #recover #package #document #version #refactor #escalate #stop
- **Responsibility tags:** #preserve-user-intent #use-smallest-effective-architecture #reduce-cognitive-load #apply-least-privilege #maintain-human-control #ensure-traceability #prevent-agent-drift #validate-before-approval #protect-sensitive-data #avoid-unnecessary-complexity #maintain-source-of-truth #stop-on-critical-risk #document-decisions #preserve-recoverability #evolve-with-evidence

A taxonomia completa (granular, por bloco) está preservada em `references/ASA_AGENT_BLUEPRINT_SOURCE.md`.
