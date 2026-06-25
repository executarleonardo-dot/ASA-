---
schema: LEO-PRD-ASA-v1
document_type: prd
title: "PRD — ASA Agent: Gerador do Leonardo-OS"
status: normalized_from_build_spec
owner: "Leonardo Batista"
created_at: "2026-06-25"
language: "pt-BR"
derived_from:
  - "AGENT_BUILD_SPEC.md (LEO-AGENT-BUILD-SPEC-v1.0)"
  - "references/_sources/BRIEFING_LEONARDO_ADMIN_OS.md"
  - "references/_sources/PROJECT_OVERVIEW_CONTEXT.md"
note: >
  Documento normalizado a partir das seções de produto do AGENT_BUILD_SPEC,
  sem placeholder e sem invenção de dados. Em conflito, o AGENT_BUILD_SPEC prevalece.
---

# PRD — ASA Agent: Gerador do Leonardo-OS

## 1. Identidade do produto

| Campo | Valor |
|---|---|
| Nome do produto | ASA Agent — Gerador do Leonardo-OS |
| Nome operacional | ASA |
| Papel oficial | Agentic Systems Architect |
| Comando principal futuro | `/architect-agentic-system` |
| Comando alternativo | `/create-validate-agentic-system` |
| Owner / ICP 0 | Leonardo Batista |
| Build environment | Claude Code |
| Runtime v1 | Claude.ai Projects |
| Idioma | Português PT-BR (código/nomes técnicos em inglês permitidos) |
| Estado | Draft for Build |
| Restrição operacional | 25h/semana; 3 frentes; 1 workflow/dia; 1 entregável/dia |

## 2. Problema

Leonardo opera um ecossistema de Skills proprietárias, conectores, DESK-OS, memória, planilha master, projetos e workflows ponta a ponta, mas **não possui um orquestrador** que selecione e combine esses recursos de maneira adaptativa e rastreável.

### 2.1 Causas
- seleção manual de Skills;
- contexto fragmentado entre conversas;
- respostas generalistas;
- ausência de política explícita de roteamento;
- falta de registro da Skill escolhida, motivo e evidência;
- ausência de handoff consistente para DESK-OS e Recycle;
- sobreposição potencial entre Leonardo Admin Skill e ASA Admin Skill.

### 2.2 Efeitos
- retrabalho; reorganização manual de outputs; perda de contexto; inconsistência entre sessões; carga cognitiva elevada; dificuldade de transformar componentes em sistema operacional executável.

### 2.3 Job to Be Done
> Quando Leonardo apresentar uma tarefa, o ASA deve interpretar a intenção, selecionar o menor stack suficiente, compor o especialista temporário adequado, executar um workflow com três etapas visíveis, produzir um entregável verificável, registrar decisões e evidências e encaminhar o estado ao DESK-OS.

## 3. Goals

- **G1 — Especialização dinâmica:** compor um especialista temporário por tarefa (role, goal, skill principal, auxiliares, contexto, ferramentas, conectores, método, critérios, limites, stop conditions). O especialista existe apenas durante a execução.
- **G2 — Zero reorganização manual:** output utilizável sem reinterpretação/correção/reorganização.
- **G3 — Geração operacional do Leonardo-OS:** produzir e manter ASA Orchestrator + Leonardo Admin Skill + ASA Admin Skill + DeskOS Skill.
- **G4 — Adaptação nativa do Fugu:** orquestrar recursos Claude (Skills, Projects, Connectors, Memory, tools, artifacts, context), não múltiplos modelos externos.
- **G5 — Governança rastreável:** registrar por execução intenção, workflow, skill principal/auxiliares, ferramentas, conectores, motivo, decisões, gates, evidências, resultado e próxima ação.

## 4. Non-Goals
- roteamento multi-modelo externo na v1; mega-Skill monolítica; substituir julgamento humano em gates críticos; gravar conversas completas em memória; ações externas irreversíveis sem confirmação; aplicação autônoma fora do Claude.ai na v1; subagente runtime por microetapa; duplicar capacidades entre Skills; afirmar suporte a recurso não verificado pelo Environment Resolver.

## 5. Escopo da versão

**Dentro:** arquitetura modular; agente orquestrador; três Skills; três workflows; contratos YAML; templates de execução; rastreabilidade; testes; evals; documentação; empacotamento; registro de gaps; rotinas A–E como especificação P1; separação fixed core × variable profile.

**Fora imediato:** deploy em produção; gravação automática em conectores; criação de credenciais; instalação automática no Claude.ai; sincronização real com Planilha Master; QR router funcional; dashboard de observabilidade; chamadas a modelos externos; Agent SDK runtime.

## 6. Usuário principal

```yaml
user:
  name: Leonardo Batista
  role: [founder, product_owner, solo_worker, non_developer_power_user, low_code_builder, content_creator]
  location: "Santos, São Paulo, Brasil"
  timezone: "America/Sao_Paulo"
  language: "pt-BR"
  capacity:
    weekly_hours: 25
    best_focus_window: "primeiras 3 horas da manhã"
    max_parallel_fronts: 3
    max_visible_workflow_steps: 3
    max_primary_deliverables_per_day: 1
  interaction_preferences:
    - plain_text_tree
    - tables
    - yaml_for_execution
    - mobile_first
    - no_horizontal_scroll
    - next_action_only
    - low_cognitive_load
```

## 7. Componentes runtime (alvo G3)

1. **ASA Orchestrator Agent** — orquestra ponta a ponta com o menor stack suficiente.
2. **Leonardo Admin Skill** — contexto operacional de Leonardo.
3. **ASA Admin Skill** — engenharia/validação/evolução do sistema agêntico.
4. **DeskOS Skill** — adaptador estado → DESK-OS.

(Fronteiras detalhadas em `DECISION_LOG.md` ADR-001.)

## 8. Workflows
- **WF1 — BUILD:** DEFINIR → DESENVOLVER → ENTREGAR.
- **WF2 — COMMUNICATE:** EXTRAIR → PRODUZIR → PUBLICAR.
- **WF3 — OPERATE:** DISTRIBUIR → ANALISAR → RECICLAR.

Sempre **exatamente 3 etapas visíveis** com gates e evidências.

## 9. Success Metrics

**Leading:** reorganização manual/sessão = 0; outputs genéricos < 10%; P0 gates registrados = 100%; workflows com 3 etapas visíveis = 100%; intenção classificada ≤ 1 turno; execução com trace = 100%.

**Lagging:** tarefa real sem reinterpretação (semana 1); 4 blueprints validados (mês 1); template para outro ICP (mês 2–3); ≥3 novas Skills via ASA (mês 2).

## 10. Definition of Done (produto)
PEDIDO → INTERPRETADO → ROTEADO → EXECUTADO EM 3 ETAPAS → ENTREGÁVEL VERIFICÁVEL → REGISTRADO → DESKOS ATUALIZADO → RECYCLE PREPARADO.

## 11. Open Questions
Ver `GAP_REGISTER.md` (OQ-01 a OQ-08). Nenhuma impede a arquitetura; impedem apenas afirmar completude dos componentes afetados.
