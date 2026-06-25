# Changelog — ASA Agent / Gerador do Leonardo-OS

Formato: [Keep a Changelog](https://keepachangelog.com/) · Versionamento: [SemVer](https://semver.org/).

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
