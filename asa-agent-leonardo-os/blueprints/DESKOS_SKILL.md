---
schema: LEO-BLUEPRINT-v1.0
id: LEO-SKILL-DESKOS-v1
name: DeskOS
type: runtime_skill
status: required
boundaries_ref: "DECISION_LOG.md ADR-001"
---

# Blueprint — DeskOS Skill

## Identity
- **id:** LEO-SKILL-DESKOS-v1 · **type:** runtime_skill · **status:** required.

## Role
Adaptador entre o **estado digital** do Leonardo-OS e a interface físico-digital **DESK-OS**.

## Goal
Converter workflows, status, próxima ação e evidências em uma **representação semanal de baixa carga cognitiva**.

## Scope (boundary — ADR-001)
**Deve conter:** mapa semanal; workflow atual; três etapas; status; próxima ação; entregável; bloqueio; handoff; Recycle; contrato para geração física; contrato QR (inicialmente abstrato).

**Não deve conter:** política central de roteamento; criação de agentes; decisão arquitetural do ASA; escrita automática em sistemas externos sem aprovação.

## Inputs / Outputs
- **Inputs:** execution_trace, workflow_plan, status, evidências.
- **Outputs:** `deskos_handoff` (`schemas/deskos-handoff.schema.yaml`), mapa semanal, Recycle.

## Contrato DeskOS handoff
Campos: handoff_id, date, workflow{id,name,stage{number,name}}, system_activity, user_action_required, next_gate, primary_deliverable, status, blocker, evidence_refs, recycle{classification, carry_forward, notes}. Status ∈ {preparing, executing, awaiting, validating, completed, blocked}.

## Contrato QR
**Abstrato (OQ-07).** Definir apenas o contrato; **não** implementar QR funcional na v1.

## Allowed tools / approval points
Leitura de estado/trace; geração de representação semanal. **Escrita automática em sistemas externos requer aprovação.**

## Quality criteria
Baixa carga cognitiva; 1 próxima ação; 3 etapas; mobile-first; sem rolagem horizontal.

## Failure handling / Stop conditions
Sem ação externa não aprovada. Parar no primeiro gate crítico.

## Examples
- **DO:** "Gere o handoff para o DeskOS" → `deskos_handoff` preenchido + Recycle.
- **DON'T:** decidir roteamento do ASA; escrever na Planilha sem confirmação.

## Implementação
`.claude/skills/deskos/SKILL.md`.

## Gaps
OQ-05 (escrita na Planilha), OQ-07 (QR), GR-06 (`[GAP-RUNTIME]` sync/QR/DeskOS físico).
