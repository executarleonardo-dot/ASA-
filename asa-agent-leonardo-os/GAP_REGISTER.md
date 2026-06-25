# GAP_REGISTER — ASA Agent / Gerador do Leonardo-OS

**Schema:** LEO-GAP-REGISTER-v1.0
**Gerado em:** 2026-06-25
**Regra:** apenas gaps de decisão reais e gaps de runtime. **Ausência documental não é gap** — todas as fontes estão incorporadas no CMD e no PROJECT.zip.

## Legenda

- `[GAP]` — decisão real pendente (Open Question) que impede afirmar completude de um componente afetado.
- `[GAP-RUNTIME]` — só pode ser resolvido com instalação/inspeção/teste no Claude.ai; não bloqueia o build local.

---

## 1. Gaps de decisão (Open Questions do AGENT_BUILD_SPEC §24)

| ID | Gap | Bloqueante | Componentes afetados | Decisão provisória aplicada |
|---|---|---|---|---|
| OQ-01 | `[GAP]` Funções dos Commands 01–03 não especificadas | sim | `.claude/commands/architect-agentic-system.md`, `create-validate-agentic-system.md` | Criar comandos com função derivada do spec (WF1/arquitetura). Não inventar funções inexistentes; marcar seções não definidas como `[GAP]`. |
| OQ-02 | `[GAP]` UID "Leonardo S" × "Leonardo Admin" | sim | `registries/alias-registry.yaml`, Leonardo Admin Skill | Nome canônico = **Leonardo Admin**; alias "Leonardo S" preservado no alias-registry. |
| OQ-03 | `[GAP]` "Interview" é nome oficial da Rotina D? | não | `workflows/routines/D_INTERVIEW.md` | Manter `Interview` com `status: provisional`. |
| OQ-04 | `[GAP]` Dois plugins "Design" (possível duplicação) | não | `registries/skill-registry.yaml` | Marcar possível duplicação; nenhuma Skill Design criada na v1 (fora do conjunto de 3 Skills). |
| OQ-05 | `[GAP]` Campos graváveis na Planilha Master | sim | `registries/connector-registry.yaml`, DeskOS Skill | Toda escrita requer confirmação; leitura permitida. Planilha preservada como binário sem parsing. |
| OQ-06 | `[GAP]` Fronteiras Leonardo Admin × ASA Admin | sim | as 3 Skills, `DECISION_LOG.md` (ADR-001) | Aplicar boundaries do spec §11.2/§11.3/§11.4 (ver ADR-001). |
| OQ-07 | `[GAP]` QR DeskOS antes/depois da v1 | não | DeskOS Skill, `templates/handoff.md` | Implementar contrato QR **abstrato**; não resolver QR funcional. |
| OQ-08 | `[GAP]` Threshold de autonomia | sim | `config/autonomy-policy.yaml`, Intent Classifier | Aplicar policy provisória baseada em risco (§15.3). |

**Efeito das OQ bloqueantes:** não impedem a criação da arquitetura nem dos arquivos. Impedem apenas afirmar *completude funcional* dos componentes marcados até decisão de Leonardo.

---

## 2. Gaps de runtime (`[GAP-RUNTIME]` — exigem o Claude.ai)

| ID | Gap | Por que não pode ser resolvido no build local |
|---|---|---|
| GR-01 | `[GAP-RUNTIME]` Capacidades reais do ambiente (Projects, Memory, Connectors, Artifacts) | Exige inspeção do Environment Resolver na conta Claude.ai do Leonardo. |
| GR-02 | `[GAP-RUNTIME]` Skills realmente instaladas e ativas | Só verificável após import no Project. |
| GR-03 | `[GAP-RUNTIME]` Conectores/MCP ativos e suas permissões | Depende da configuração da conta. |
| GR-04 | `[GAP-RUNTIME]` Execução de ≥1 caso real ponta a ponta (DoD §38) | Requer runtime Claude.ai; não simulável localmente. |
| GR-05 | `[GAP-RUNTIME]` Acurácia de classificação de intenção ≥0.90 (≥30 amostras) | Requer execução do modelo no runtime. |
| GR-06 | `[GAP-RUNTIME]` Sincronização real com Planilha Master / DeskOS físico / QR | Fora do escopo v1; exige integração externa autorizada. |
| GR-07 | `[GAP-RUNTIME]` Versão e campos de frontmatter aceitos pela instância Claude | Frontmatter gerado conforme convenção atual; confirmar no import. |

---

## 3. Itens explicitamente **não** classificados como gap

- Ausência de repositório/branch/X-RAY preexistente — esperado (build local standalone).
- Ausência de PRD/System Prompt como arquivos separados — **incorporados** no AGENT_BUILD_SPEC e normalizados em `references/`.
- Ausência de credenciais/secrets — proibido criar (governança).

---

## 4. Próxima ação sobre gaps

Os gaps bloqueantes (OQ-01, OQ-02, OQ-05, OQ-06, OQ-08) e os `[GAP-RUNTIME]` devem ser revisados por Leonardo antes de declarar P0 completo. Nenhum deles impede a entrega do pacote scaffold validado localmente.
