# GAP_REGISTER — ASA Agent / Gerador do Leonardo-OS

**Schema:** LEO-GAP-REGISTER-v2.0
**Atualizado em:** 2026-06-25 (integração do Follow-up Report v2.0 — ASA-FOLLOWUP-2026-06-25-v2.0.0)
**Regra:** apenas gaps reais. Ausência documental não é gap. Resoluções baseadas em insumos: `references/follow-up-v2/ASA_LEONARDO_OS_FOLLOW_UP_REPORT_v2.0.md` (S6) e extração da SSOT (S7).

> **Estado geral:** todas as Open Questions do BUILD_REPORT estão **resolvidas** (por evidência ou por política); as 9 lacunas do workbook receberam tratamento; os 7 gaps de runtime permanecem **abertos por natureza**, agora com **critério objetivo de fechamento**.

---

## 1. Open Questions (BUILD_REPORT §24) — RESOLVIDAS

| OQ | Tema | Status | Resolução (insumo S6 §19) |
|---|---|---|---|
| OQ-01 | commands_01_03_function | **CLOSED** | Router canônico com **11 rotas** e owners; catálogo ampliado por skill. Ver `registries/command-registry.yaml`. |
| OQ-02 | leonardo_s_alias | **CLOSED** | Separação canônica: **AGENT-LEONARDO-ORCHESTRATOR** (estado do projeto) × **SKILL-OS-PARTNER-ADMIN** (conta/admin). Ver `registries/alias-registry.yaml` + DECISION_LOG ADR-007. |
| OQ-03 | interview_name | **PROVISIONAL** | Nome operacional: etapa **COLLECT-OPERATING-CONTEXT** do `WF-ONBOARD-LEONARDO-OS`. Rotina D mantém `status: provisional`. |
| OQ-04 | design_plugins_duplication | **CLOSED** | Apenas **1 plugin** declarado (`PLUGIN-SMALL-BUSINESS`); variantes de Design System são **documentos**, não plugins. |
| OQ-05 | master_spreadsheet_writable_fields | **CLOSED_BY_POLICY** | Write policy EDITABLE/CONTROLLED/COMPUTED/LOCKED. Ver `config/write-policy.yaml`. |
| OQ-06 | admin_boundaries | **CLOSED** | Boundary OS Partner Admin (plano de controle) × Leonardo Orchestrator (plano de estado). DECISION_LOG ADR-001/ADR-007. |
| OQ-07 | deskos_qr | **DOCUMENTED_RUNTIME_OPEN** | Contrato QR abstrato definido; implementação/round-trip dependem de runtime → ver GR-06. |
| OQ-08 | autonomy_threshold | **CLOSED_BY_POLICY** | AUTO / CONFIRM / BLOCK formalizados. Ver `config/autonomy-policy.yaml`. |

---

## 2. Lacunas do workbook (S6 §19) — TRATADAS

| ID | Lacuna | Estado | Tratamento / critério |
|---|---|---|---|
| GAP-001 | Course Express sem arquivo próprio | PARTIAL | Criar Charter + Vision + BRD + MRD + PRD mínimo. Produto permanece **PROPOSED**. |
| GAP-002 | Education sem documentação dedicada | PARTIAL | Criar Program Charter; não promover a CONFIRMED sem aprovação de escopo/ofertas. |
| GAP-003 | Small Business / maturidade | PARTIAL | Separar Business Suite, GTM Showroom e Agency Kit; stage gate por evidência. |
| GAP-004 | Agent Factory | PARTIALLY_RESOLVED | Mapeado para `AGENT-CAPABILITY-BUILDER` + `WF-BUILD-MISSING-CAPABILITY`; falta documento dedicado (FUP-DEC-04). |
| GAP-005 | Neuro-Agent | OPEN_CONTROLLED | Módulo candidato; exige problema, boundary clínico zero, I/O, evals e decisão do owner. |
| GAP-006 | Setup Suite | RESOLVED_AS_CANDIDATE | OFFER-CANDIDATE apoiada por Setup OS + OS Partner Admin; validar WTP antes de produto. |
| GAP-007 | AI OS Reset | RESOLVED_AS_CANDIDATE | OFFER-CANDIDATE; definir JTBD, ICP, DoD, preço e experimento. |
| GAP-008 | Design System variants | PROVISIONAL_RESOLUTION | `SOT_DESING_SYSTEM` = SSOT provisória; outra variante = REFERENCE; diff semântico obrigatório (FUP-DEC-01). |
| GAP-009 | Contextos_adicionais_ | RESOLVED | Cluster primário C04; tag secundária C08 só em seções visuais (FUP-DEC-02). |

**Regra de promoção:** `PROPOSED → REVIEW_REQUIRED → CONFIRMED` exige owner, problema, ICP, escopo, boundary, BRD/MRD/PRD, dependências, riscos, experimento e DoD.

---

## 3. Gaps de runtime (`[GAP-RUNTIME]`) — ABERTOS POR NATUREZA, com critério de fechamento

| Gap | Tema | Critério objetivo de fechamento (S6 §19) |
|---|---|---|
| GR-01 | Environment capabilities | Executar Environment Resolver e registrar capacidades reais em `config/environment-capabilities.yaml`. |
| GR-02 | Installed skills | Confirmar importação, versão e disponibilidade de cada skill no Project. |
| GR-03 | Connectors/permissions | Testar autorização mínima e round-trip, sem credenciais no pacote. |
| GR-04 | End-to-end real case | Executar `TEST-LEONARDO-WORKFLOW-001` (`/day-zero`) com evidências. |
| GR-05 | Intent accuracy | Benchmark com intents, expected route e threshold; medir acurácia por rota. |
| GR-06 | QR / DESK-OS physical sync | Testar geração, leitura, ação e Recycle em dispositivo real. |
| GR-07 | Frontmatter acceptance | Importar no Claude.ai e validar campos aceitos/rejeitados com log. |

> Estes gaps **não podem** ser fechados no build local — exigem o runtime Claude.ai, conectores, permissões ou QR real. O roadmap (S6 §23) define Ciclos 1–5 para fechá-los.

---

## 4. Itens explicitamente **não** classificados como gap

- Ausência de repositório/branch/X-RAY — esperado (build local standalone).
- PRD/System Prompt/stack proprietário não estarem como arquivos separados — **incorporados/extraídos** e catalogados (registries + references).
- 10 skills + 5 agentes não materializados como SKILL.md próprios — são **stack proprietário existente de Leonardo (SSOT FILE-025)**; catalogados, não reinventados (evita duplicação/invenção).

---

## 5. Próxima ação sobre gaps

Aprovar/ajustar FUP-DEC-01..05 (S6 §18) e executar o Ciclo 1 do roadmap (import no Claude.ai + Environment Resolver) para iniciar o fechamento dos GR-01..07. Nenhum gap impede a entrega do pacote v2.0.0 (RC1).
