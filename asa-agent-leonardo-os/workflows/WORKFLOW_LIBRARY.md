---
schema: LEO-WORKFLOW-LIBRARY-v1.0
updated_by: "Follow-up v2.0 §10"
---

# Workflow Library (catálogo canônico)

Os 9 workflows operacionais do ecossistema (Follow-up v2.0 §10). Cada um expõe **exatamente 3 etapas visíveis** ao usuário (consistente com WF1/WF2/WF3 deste pacote). Catalogados — a materialização/execução real é runtime (GR-04).

| Workflow ID | Prio | Finalidade | Sequência (owner skills) | DoD |
|---|---|---|---|---|
| WF-ONBOARD-LEONARDO-OS | P0 | Construir/atualizar macro-personalização | SETUP-OS → COGNITIVE-TRIGGER → OS-PARTNER-ADMIN | Contexto validado; agentes/skills/tools/workflows/comandos/exclusões e requisitos DESK-OS definidos. |
| WF-START-WEEK | P0 | Gerar superfície operacional semanal | LEONARDO-ORCHESTRATOR → COGNITIVE-TRIGGER → DESK-OS | ≤3 workflows ativos, 3 etapas cada, 1 entregável/workflow, QR ligado a ação real. |
| WF-SOLVE-COMPLEX-PROBLEM | P0 | Resolver problema ambíguo | COGNITIVE-TRIGGER → AGENTIC-PROBLEM-SOLVING → LEONARDO-ORCHESTRATOR | Problema definido, estratégia justificada, stop condition, avaliação. |
| WF-VALIDATE-PRODUCT-HYPOTHESIS | P0 | Validar hipótese produto/mercado | AGENTIC-PROBLEM-SOLVING → PLUGIN-SMALL-BUSINESS → OS-PARTNER-ADMIN | Hipótese falsificável, experimento mínimo, métricas/thresholds, decisão de gate. |
| WF-BUILD-MISSING-CAPABILITY | P1 | Criar especialista/skill/comando ausente | META-TEMPLATE-SPECIALIST → AGENTIC-PROBLEM-SOLVING → CMD-01-PPS | Capacidade distinta, contratos, progressive disclosure, evals, pacote versionado. |
| WF-CREATE-PROJECT-ORCHESTRATOR | P2 | Corpus → orquestrador standalone | STANDALONE-ORCHESTRATOR-TEMPLATE → META-TEMPLATE-SPECIALIST → CMD-01-PPS | Fonte canônica, mapa MECE, fases, gates, decisões, tracker, skill standalone. |
| WF-OPERATE-EDITORIAL-SPRINT | P1 | Planejar/produzir/medir conteúdo | EDITORIAL-OS → COGNITIVE-TRIGGER → EDITORIAL-OS | Sprint, ativo, relatório de qualidade, analytics, próxima ação. |
| WF-PACKAGE-RELEASE | P1 | Release rastreável | OS-PARTNER-ADMIN → CMD-01-PPS → LEONARDO-ORCHESTRATOR | Repo normalizado, metadados, audit log, ZIP, decisão de release. |
| WF-CLOSE-AND-RECYCLE-WEEK | P0 | Reconciliar e preparar próximo ciclo | DESK-OS → LEONARDO-ORCHESTRATOR → DESK-OS | Concluídos, carry-over, decisões, tracker, seed da próxima semana. |

## Mapeamento para a interface de 3 etapas (WF1/WF2/WF3)
- **Build** (criar/desenvolver): WF-BUILD-MISSING-CAPABILITY, WF-CREATE-PROJECT-ORCHESTRATOR, WF-PACKAGE-RELEASE → família **WF1**.
- **Communicate** (conteúdo): WF-OPERATE-EDITORIAL-SPRINT → família **WF2**.
- **Operate** (semana/decisão/reciclagem): WF-START-WEEK, WF-CLOSE-AND-RECYCLE-WEEK, WF-SOLVE-COMPLEX-PROBLEM, WF-VALIDATE-PRODUCT-HYPOTHESIS, WF-ONBOARD-LEONARDO-OS → família **WF3**.

## Contrato obrigatório de workflow (§10)
1. ID verbal · 2. Trigger · 3. Input contract · 4. **3 etapas visíveis** · 5. Output contract · 6. DoD · 7. Owner skill · 8. Failure mode · 9. Evidência de gate.

> OQ-03: a etapa **COLLECT-OPERATING-CONTEXT** de `WF-ONBOARD-LEONARDO-OS` é o nome operacional da "Interview" (Rotina D, provisional).
