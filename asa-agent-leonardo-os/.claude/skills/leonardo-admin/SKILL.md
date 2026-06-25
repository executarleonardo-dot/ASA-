---
name: leonardo-admin
description: >-
  Administra o contexto operacional de Leonardo (pessoal e empresarial):
  identidade, preferências, limites cognitivos, projetos ativos, priorização,
  Daily Briefing, Week Open, Week Closing, decisões e handoffs humanos. Use
  quando a tarefa for operar a rotina/administração de Leonardo — não para
  engenharia de agentes (use asa-admin) nem representação física (use deskos).
---

# Leonardo Admin Skill

> Boundary canônico: `blueprints/LEONARDO_ADMIN_SKILL.md` + `DECISION_LOG.md` ADR-001.

## O que faz
Transforma contexto pessoal/empresarial em **prioridades, decisões, rotinas e registros executáveis**, com baixa carga cognitiva e **1 próxima ação**.

## Quando ativar (triggers)
- "abra/feche minha semana", "briefing", "minhas prioridades", "status dos projetos", "decisão administrativa", "plano operacional do dia".

## Quando NÃO ativar
- engenharia de Skills/agentes/plugins → `asa-admin`;
- mapa físico/QR/handoff semanal renderizado → `deskos`.

## Inputs
estado semanal · agenda · projetos · pendências · capacidade (25h/sem, 3 frentes) · prioridades · decisões · status de workflows.

## Outputs
briefing diário · abertura semanal · fechamento semanal · plano operacional · decisão administrativa · atualização estruturada para DeskOS.

## Rotinas (owner)
- A — Daily Briefing → `references/routines.md` / `workflows/routines/A_DAILY_BRIEFING.md`
- B — Week Open (com DeskOS) → `workflows/routines/B_WEEK_OPEN.md`
- C — Week Closing (com DeskOS) → `workflows/routines/C_WEEK_CLOSING.md`

## Tools & approval
Leitura de Project Knowledge e Planilha Master (somente leitura). **Toda escrita externa ou em memória requer confirmação** (`config/governance.yaml`).

## Método (3 etapas visíveis)
1. CONTEXTO — recuperar estado/projetos/capacidade.
2. PRIORIZAR — aplicar regras (foco matinal, 1 entregável/dia, 3 frentes).
3. ENTREGAR — plano/briefing + próxima ação + handoff DeskOS.

## Quality criteria
Anti-genericidade (usa contexto específico de Leonardo); 3 etapas; 1 próxima ação; mobile-first.

## Failure handling
Dado crítico ausente → perguntar o mínimo. Não-crítico → `[GAP]` + suposição explícita.

## Stop conditions
Ação externa/escrita → confirmar. Parar no primeiro gate crítico.

## Do / Don't
- DO: "Abra minha semana com base nos 3 projetos ativos" → Week Open + handoff.
- DON'T: projetar arquitetura de agentes; publicar conteúdo (isso é WF2/orchestrator).

## Referências
`references/` (boundary, rotinas). Templates em `templates/`. Testes em `tests/`.

## Gaps
OQ-02 (alias "Leonardo S" → ver `registries/alias-registry.yaml`); OQ-05 (campos graváveis da Planilha).
