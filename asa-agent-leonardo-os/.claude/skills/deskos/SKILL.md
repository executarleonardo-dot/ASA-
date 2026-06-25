---
name: deskos
description: >-
  Adaptador entre o estado digital do Leonardo-OS e a interface físico-digital
  DESK-OS. Use para converter workflow/status/próxima ação/evidências em uma
  representação semanal de baixa carga cognitiva e gerar o handoff. Não decide
  roteamento (orchestrator), não cria agentes (asa-admin), não administra a
  rotina pessoal (leonardo-admin).
---

# DeskOS Skill

> Boundary canônico: `blueprints/DESKOS_SKILL.md` + ADR-001. Contrato: `schemas/deskos-handoff.schema.yaml`.

## O que faz
Converte estado digital em **representação semanal** (mapa semanal, workflow atual, 3 etapas, status, próxima ação, entregável, bloqueio, handoff, Recycle) com baixa carga cognitiva.

## Quando ativar (triggers)
- "gere o handoff", "atualize o DeskOS", "mapa da semana", "status para o desk", "prepare o Recycle".

## Quando NÃO ativar
- decisão de roteamento/arquitetura → orchestrator/asa-admin;
- priorização/briefing pessoal → leonardo-admin.

## Inputs / Outputs
- Inputs: execution_trace, workflow_plan, status, evidências.
- Outputs: `deskos_handoff` (schema), mapa semanal, Recycle.

## Contrato de handoff
Campos: handoff_id, date, workflow{id,name,stage}, system_activity, user_action_required, next_gate, primary_deliverable, status, blocker, evidence_refs, recycle. Status ∈ {preparing, executing, awaiting, validating, completed, blocked}.

## Contrato QR
**Abstrato (OQ-07).** Apenas o contrato; **sem** QR funcional na v1.

## Tools & approval
Leitura de estado/trace; geração de representação. **Escrita automática em sistemas externos requer aprovação.**

## Método (3 etapas visíveis)
1. COLETAR — ler trace/workflow/status.
2. CONVERTER — montar mapa semanal + handoff.
3. ENTREGAR — handoff + Recycle + próxima ação.

## Quality criteria
Baixa carga cognitiva; 1 próxima ação; 3 etapas; mobile-first; sem rolagem horizontal.

## Failure handling / Stop conditions
Sem ação externa não aprovada. Parar no primeiro gate crítico.

## Do / Don't
- DO: "Gere o handoff para o DeskOS" → `deskos_handoff` preenchido + Recycle.
- DON'T: decidir roteamento; escrever na Planilha sem confirmação.

## Gaps
OQ-05 (escrita na Planilha), OQ-07 (QR), GR-06 (`[GAP-RUNTIME]` sync/QR/DeskOS físico).
