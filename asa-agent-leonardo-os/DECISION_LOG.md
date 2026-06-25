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
| D-11 | Pacote versionado `v1.0.0`; nome `asa-agent-leonardo-os-v1.0.0.zip`; checksum SHA-256. | SPEC §25/§34 |
| D-12 | Rotina E (Analytics) e Rotina D (Interview) especificadas com `status: provisional` (OQ-03). | SPEC §14 |
