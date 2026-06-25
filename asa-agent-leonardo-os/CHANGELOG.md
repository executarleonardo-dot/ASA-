# Changelog — ASA Agent / Gerador do Leonardo-OS

Formato: [Keep a Changelog](https://keepachangelog.com/) · Versionamento: [SemVer](https://semver.org/).

## [2.0.0] — 2026-06-25 — Integração do Follow-up Report v2.0

### Added
- `references/follow-up-v2/`: report (md/docx), `MASTER_PROJECT_ADMIN_EXTRACT.json`, 23 CSVs, README e checksum do pacote (verificado OK).
- `config/write-policy.yaml` (EDITABLE/CONTROLLED/COMPUTED/LOCKED) — resolve OQ-05.
- `workflows/WORKFLOW_LIBRARY.md` — catálogo dos 9 workflows operacionais + mapeamento WF1/2/3.
- `FOLLOW_UP_INTEGRATION_REPORT.md` — resolução gap a gap com evidência.

### Changed
- `GAP_REGISTER.md` → v2.0: OQ-01..08 resolvidas; GAP-001..009 tratadas; GR-01..07 com critério de fechamento.
- `DECISION_LOG.md` → +Parte E (FUP-DEC-01..05, ADR-007/008/009, write/autonomy policy, mapeamento v1→canônico).
- `config/autonomy-policy.yaml` → v2.0 (AUTO/CONFIRM/BLOCK), resolve OQ-08.
- Registries expandidos: skill (10 canônicas), agent (5), command (router 11 + lib), connector (plugin), project (programas/produtos/entidades), alias (split OQ-02).
- `source-map.yaml` +S6/S7; README atualizado; pacote `v2.0.0`.

### Notes
- Stack proprietário (10 skills/5 agentes) **catalogado**, não recriado (ADR-008) — preserva a SSOT, evita invenção.
- v1 (1 orquestrador + 3 Skills) mantida como implementação de referência (ADR-009).
- Estado: **RC1 — READY FOR CONTROLLED RUNTIME VALIDATION**. GR-01..07 abertos por natureza.

## [1.0.0] — 2026-06-25

### Added — scaffold inicial (build-time)
- Estrutura completa do pacote conforme `AGENT_BUILD_SPEC.md` §25.
- Fontes preservadas em `references/` e `references/_sources/`; `source-map.yaml`.
- Fase 1: `GAP_REGISTER.md`, `DECISION_LOG.md` (ADR-001..006), referências normalizadas (PRD, System Prompt), taxonomy, glossary.
- 4 blueprints: ASA Orchestrator, Leonardo Admin, ASA Admin, DeskOS.
- 1 agente runtime (`asa-orchestrator`) + 4 subagentes build-time.
- 3 Skills runtime (leonardo-admin, asa-admin, deskos) com SKILL.md, references, templates, tests.
- 5 commands; 6 configs; 10 schemas; 3 workflows + 5 rotinas; 8 templates; 6 registries; 7 evals; 8 grupos de testes; 7 scripts de validação/empacotamento.

### Notes
- Estado **Draft for Build**. Componentes afetados por OQ bloqueantes não declarados completos.
- Itens `[GAP-RUNTIME]` (instalação/teste no Claude.ai) permanecem abertos — ver `GAP_REGISTER.md`.

### Security
- Nenhuma credencial criada. Scan de secrets executado no build (ver `BUILD_REPORT.md`).
