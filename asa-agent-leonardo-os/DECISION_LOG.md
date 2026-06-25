# DECISION_LOG — ASA Agent / Gerador do Leonardo-OS

**Schema:** LEO-DECISION-LOG-v1.0
**Gerado em:** 2026-06-25
**Build:** Claude Code local · **Runtime v1:** Claude.ai Projects

Registro cronológico de decisões de construção e Architecture Decision Records (ADR). Precedência aplicada: Segurança/Governança → Decisões de Leonardo → CMD → AGENT_BUILD_SPEC → PRD → System Prompt → Blueprint → Inferência.

---

## Parte A — Correções de ambiente (do CMD MASTER STANDALONE)

| # | Decisão | Motivo | Fonte |
|---|---|---|---|
| D-01 | Build é **local** no Claude Code, sem repositório preexistente obrigatório. | CMD remove `repository`, `branch`, `github_required`. | CMD §"Correções obrigatórias" |
| D-02 | **Não** usar/procurar X-RAY. | Proibição explícita. | CMD §Proibições |
| D-03 | Runtime v1 = **Claude.ai Projects**. | Ambiente operacional declarado. | CMD §Ambiente / SPEC §1 |
| D-04 | Pacote gerado em `asa-agent-leonardo-os/` (subdiretório do repo da branch). | CMD: `./asa-agent-leonardo-os/`. Branch designada exige commit/push. | CMD §Diretório obrigatório + instruções de branch |
| D-05 | Fontes embutidas extraídas sem placeholder; **nenhuma busca externa**. | `source_policy.embedded_only`. | CMD §source_policy |
| D-06 | Ausência documental **não** é gap. | Regra explícita. | CMD item 7 |
| D-07 | Planilha Master (`.xlsx`) preservada como binário, **não parseada**. | Não inventar campos (OQ-05); least data. | SPEC §6.2 / governança |
| D-08 | Sem subagentes Claude Code spawnados para construir (build inline). | Não solicitado; menor arquitetura. | Instrução do usuário / SPEC §2 |

---

## Parte B — Architecture Boundary Records (ADR)

### ADR-001 — Fronteiras das 3 Skills runtime (resolve OQ-06)

**Decisão:** aplicar as fronteiras do AGENT_BUILD_SPEC §11. Cada Skill tem responsabilidade única e não sobrepõe as demais.

| Skill | Administra | NÃO contém |
|---|---|---|
| **Leonardo Admin** | Contexto operacional de Leonardo: identidade, preferências, limites cognitivos, projetos ativos, priorização, briefing/week open/closing, decisões e handoffs humanos. | Engenharia de agentes, criação de Skills, arquitetura de plugins, testes técnicos, política central de roteamento. |
| **ASA Admin** | O **sistema agêntico**: requirements, arquitetura de agentes/Skills, context/prompt engineering, evals, testes, packaging, versioning, gap detection, blueprints, refactoring, observability. | Agenda pessoal, briefing diário pessoal, rotina semanal, conteúdo físico do DeskOS, administração geral do negócio. |
| **DeskOS** | Adaptador estado digital → interface físico-digital DESK-OS: mapa semanal, workflow atual, 3 etapas, status, próxima ação, entregável, bloqueio, handoff, Recycle, contrato QR abstrato. | Política central de roteamento, criação de agentes, decisão arquitetural do ASA, escrita automática em sistemas externos sem aprovação. |

**Critério anti-overlap:** se uma capacidade puder caber em duas Skills, decidir pelo *owner do resultado*: contexto/operação de Leonardo → Leonardo Admin; engenharia do sistema → ASA Admin; representação semanal/handoff físico → DeskOS.

### ADR-002 — Um único agente runtime

**Decisão:** o runtime v1 tem **exatamente 1 agente orquestrador** (ASA Orchestrator). Nenhum subagente runtime por microetapa (mitiga R-02). Os 4 subagentes (`asa-build-architect`, `asa-agent-engineer`, `asa-skill-engineer`, `asa-quality-governance-auditor`) são **build-time** e não fazem parte obrigatória do runtime.

### ADR-003 — Fixed core × Variable profile

**Decisão:** separar o que é universal (fixed core) do que é específico de Leonardo (variable profile), preparando reuso para outros ICPs.

- **Fixed core:** governança, context cascade, intent classifier, specialist composer, workflow planner, interface de 3 etapas, gates, trace, quality evaluator, failure handling, stop conditions, source precedence.
- **Variable profile:** identidade, empresa, projetos, prioridades, Skills instaladas, connectors, rotinas, vocabulário, layout DeskOS, memória, UIDs, autonomia autorizada.

Estrutura futura prevista: `core/` (ASA universal) + `profiles/leonardo/` + `profiles/future-icp/`. Na v1 o profile de Leonardo vive na Leonardo Admin Skill e nos registries.

### ADR-004 — Cascata de contexto normalizada para 9 camadas (0–8)

**Decisão:** o spec menciona "8 camadas" mas enumera 9. Normalizar para camadas **0–8** (Constituição, Identidade, Ambiente, Projeto, Caso de uso, Problema, Especialista temporário, Workflow, Estado), conforme SPEC §10. Implementado em `schemas/context.schema.yaml` e no ASA Orchestrator.

### ADR-005 — Política de autonomia provisória por risco (resolve OQ-08 provisoriamente)

**Decisão:** até OQ-08 ser decidida por Leonardo, aplicar `config/autonomy-policy.yaml`:
- baixo risco + reversível → pode prosseguir com suposições explícitas;
- risco médio → confirmar se houver ambiguidade material;
- alto/crítico → sempre confirmar;
- escrita externa → sempre confirmar.

### ADR-006 — Frontmatter e formato dos componentes

**Decisão:** agentes em `.claude/agents/*.md` e Skills em `SKILL.md` usam YAML frontmatter na convenção atual do Claude Code (`name`, `description`, e p/ agentes `tools`). A aceitação exata de campos é `[GAP-RUNTIME]` (GR-07) e deve ser confirmada no import. Núcleo das Skills mantido enxuto; conteúdo extenso em `references/`.

---

## Parte C — Plano de geração dos 4 blueprints

Ordem (SPEC §31 Fase 2). Cada blueprint segue o contrato do spec e referencia os schemas correspondentes.

1. **ASA_ORCHESTRATOR_AGENT.md** — identidade LEO-AGENT-ASA-ORCHESTRATOR-v1; role/goal/responsabilidades (§11.1); arquitetura lógica do runtime (§9); cascata de contexto (§10); specialist composer (§16); intent classifier (§15); 3 workflows; gates; trace (§19); handoff DeskOS (§20); output contract (§21); governança (§18); failure handling (§23); stop conditions (§37).
2. **LEONARDO_ADMIN_SKILL.md** — LEO-SKILL-LEONARDO-ADMIN-v1; boundary ADR-001; rotinas A/B/C; inputs/outputs (§11.2).
3. **ASA_ADMIN_SKILL.md** — LEO-SKILL-ASA-ADMIN-v1; boundary ADR-001; pipeline diagnosticar→arquitetar→delegar→executar→monitorar→validar→corrigir→empacotar→evoluir (§11.3); taxonomia (Apêndice A / blueprint).
4. **DESKOS_SKILL.md** — LEO-SKILL-DESKOS-v1; boundary ADR-001; contrato DeskOS handoff (§20); QR abstrato (OQ-07).

Cada blueprint é a especificação canônica; os arquivos executáveis correspondentes ficam em `.claude/agents/asa-orchestrator.md` e `.claude/skills/*/SKILL.md`.

---

## Parte D — Decisões de implementação (inferências registradas)

| # | Decisão | Tipo |
|---|---|---|
| D-09 | Schemas escritos em YAML descritivo (campos + tipo + obrigatoriedade), não JSON-Schema estrito, para legibilidade humana e validação leve. | `[INFERÊNCIA]` |
| D-10 | Scripts de validação em Python 3 stdlib (sem dependências externas) para rodar offline. | `[INFERÊNCIA]` |
| D-11 | Pacote versionado; checksum SHA-256 (v1.0.0 build inicial; v2.0.0 após integração do follow-up). | SPEC §25/§34 |
| D-12 | Rotina E (Analytics) e Rotina D (Interview) especificadas com `status: provisional` (OQ-03). | SPEC §14 |

---

## Parte E — Integração do Follow-up Report v2.0 (ASA-FOLLOWUP-2026-06-25-v2.0.0)

Insumo autoritativo: `references/follow-up-v2/ASA_LEONARDO_OS_FOLLOW_UP_REPORT_v2.0.md` (S6), extração SSOT (S7). Precedência: **decisões de Leonardo > AGENT_BUILD_SPEC**, portanto o follow-up reconcilia/atualiza decisões do build inicial.

### Decisões de follow-up adotadas (S6 §18)

| ID | Decisão | Status |
|---|---|---|
| FUP-DEC-01 | `SOT_DESING_SYSTEM` = SSOT provisória do Design System; `Desing_System_.txt` = REFERENCE. Definitiva só após diff semântico (552 registros/variante). | adotada (provisional) |
| FUP-DEC-02 | `Contextos_adicionais_` = cluster primário **C04** (Architecture/System); C08 apenas em seções visuais. | adotada |
| FUP-DEC-03 | **Setup Suite** e **AI OS Reset** = ofertas candidatas, não produtos confirmados. | adotada |
| FUP-DEC-04 | **Agent Factory** = capability implementada por `AGENT-CAPABILITY-BUILDER` + `WF-BUILD-MISSING-CAPABILITY`; documento dedicado ainda obrigatório. | adotada (partial) |
| FUP-DEC-05 | **Write policy** e **autonomy policy** passam a contrato de governança. | adotada → `config/write-policy.yaml`, `config/autonomy-policy.yaml` |

### ADR-007 — Boundary OS Partner Admin × Leonardo Orchestrator (resolve OQ-02/OQ-06)

A sobreposição "Leonardo S" × "Leonardo Admin" é resolvida por **dois planos**:

```text
OS PARTNER ADMIN (plano de controle)      LEONARDO ORCHESTRATOR (plano de estado)
├── conta e projetos                      ├── estado canônico do projeto
├── documentação e arquitetura            ├── fase e gate
├── administração de negócio              ├── decisões e tracker
├── validação e packaging                 ├── roteamento de intenção
└── release                               └── próximas ações
```

`AGENT-LEONARDO-ORCHESTRATOR` (master router) é powered by `SKILL-LEONARDO-ORCHESTRATOR` + `SKILL-OS-PARTNER-ADMIN`. Ver `registries/agent-registry.yaml`.

### ADR-008 — Catalogar (não reinventar) o stack proprietário

O follow-up revela o stack real de Leonardo: **10 skills proprietárias (SSOT FILE-025), 5 agentes canônicos, 11 rotas de comando, 9 workflows**. Estes **já existem** no ecossistema de Leonardo e são extraídos da SSOT, não construídos por este pacote. Decisão: **catalogá-los** em `registries/` e `references/follow-up-v2/`, preservando a v1 (1 orquestrador + 3 Skills) como implementação de referência, com mapeamento explícito (ADR-009). Materializar SKILL.md de cada um seria inventar/duplicar a SSOT → proibido.

### ADR-009 — Mapeamento v1 (implementado) → stack canônico (catalogado)

| Componente v1 (este pacote) | Equivalente canônico (S6) |
|---|---|
| agente `asa-orchestrator` | `AGENT-LEONARDO-ORCHESTRATOR` (master router) |
| skill `leonardo-admin` | `SKILL-OS-PARTNER-ADMIN` + `SKILL-LEONARDO-ORCHESTRATOR` (control/state) |
| skill `asa-admin` | `SKILL-META-TEMPLATE-SPECIALIST` + `SKILL-AGENTIC-PROBLEM-SOLVING` (programa ASA) |
| skill `deskos` | `SKILL-DESK-OS` (DESK-OS-Full-Stack-Skill) |
| WF1/WF2/WF3 (3 etapas visíveis) | interface de superfície dos 9 workflows operacionais (S6 §10) |

A v1 permanece válida como o "menor conjunto suficiente"; o catálogo canônico é a referência de expansão para os Ciclos de runtime.

### Write policy (FUP-DEC-05) — resumo

- **EDITABLE:** `classification_status/status`, `documentation_status`, `next_action`, `review_required`, owner, due date, notas de validação.
- **CONTROLLED:** `authority_status`, parent/relation, SSOT — só owner/governança.
- **COMPUTED:** contagens, KPIs, cobertura, fórmulas, indicadores.
- **LOCKED/IMMUTABLE:** `source_file`, `source_hash`, `source_locator`, conteúdo bruto, IDs publicados, decisões aprovadas, evidências de validação.

### Autonomy policy (FUP-DEC-05) — resumo

- **AUTO:** leitura, classificação reversível, geração local, testes estáticos, documentação, propostas.
- **CONFIRM:** ação externa, publicação, envio, alteração de SSOT, exclusão, credenciais, dados privados, decisão que muda produto.
- **BLOCK:** exposição de segredo, alegação de execução não verificada, ação destrutiva sem backup, violação de guardrail.
