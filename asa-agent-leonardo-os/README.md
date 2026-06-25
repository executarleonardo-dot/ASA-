# ASA Agent — Gerador do Leonardo-OS

**Versão:** 2.0.0 (RC1) · **Estado:** Ready for Controlled Runtime Validation · **Build:** Claude Code · **Runtime v1:** Claude.ai Projects · **Idioma:** PT-BR

> **v2.0.0** integra o **Follow-up Report v2.0**: resolve as 8 Open Questions, trata as 9 lacunas do workbook e cataloga o stack proprietário real (10 skills, 5 agentes, 11 rotas, 9 workflows). Ver `FOLLOW_UP_INTEGRATION_REPORT.md` e `references/follow-up-v2/`. Os 7 gaps de runtime (GR-01..07) permanecem abertos por natureza, com critério de fechamento.

O **ASA (Agentic Systems Architect)** é o orquestrador do **Leonardo-OS**: interpreta uma intenção, seleciona o menor stack suficiente, compõe um especialista temporário, executa um workflow em **3 etapas visíveis**, produz um entregável verificável, registra decisões/evidências e encaminha o estado ao DESK-OS.

## Arquitetura runtime v1

```text
ASA Orchestrator (1 agente)
├── Leonardo Admin Skill   → contexto operacional de Leonardo
├── ASA Admin Skill        → engenharia do sistema agêntico
└── DeskOS Skill           → adaptador estado → DESK-OS
3 workflows: WF1 BUILD · WF2 COMMUNICATE · WF3 OPERATE
```

A construção (Claude Code) usa 4 subagentes **build-time** (architect, agent-engineer, skill-engineer, quality/governance auditor) que **não** fazem parte do runtime.

## Estrutura

```text
asa-agent-leonardo-os/
├── AGENT_BUILD_SPEC.md      # contrato canônico de build
├── CLAUDE.md                # instruções para Claude Code
├── README.md / CHANGELOG.md / SECURITY.md / LICENSE_POLICY.md
├── GAP_REGISTER.md / DECISION_LOG.md / BUILD_REPORT.md
├── .claude/                 # agents, skills, commands, hooks, settings.example.json
├── config/                  # governance, routing, autonomy, memory, capabilities, precedence
├── schemas/                 # contratos YAML
├── workflows/               # WF1/WF2/WF3 + routines/ A–E
├── blueprints/              # 4 especificações canônicas
├── templates/               # agent/skill/workflow/output/decision/handoff/gap
├── references/              # PRD, System Prompt, Blueprint source, taxonomy, glossary, source-map, _sources/
├── registries/              # agent/skill/command/connector/project/alias
├── evals/ · tests/ · scripts/
└── dist/                    # pacote empacotado
```

## Como instalar no Claude.ai (runtime v1)

> Instalação **manual** por Leonardo. O build não instala nem testa automaticamente no Claude.ai (`[GAP-RUNTIME]`).

1. Criar um Project no Claude.ai.
2. Importar o conteúdo de `.claude/skills/` como Skills (Leonardo Admin, ASA Admin, DeskOS).
3. Importar `.claude/agents/asa-orchestrator.md` como o agente orquestrador.
4. Adicionar `references/` ao Project Knowledge.
5. Rodar o **Environment Resolver** (preencher `config/environment-capabilities.yaml`) antes do primeiro uso real.
6. Validar 1 caso real ponta a ponta (ver `tests/happy-path/`).

## Validação local

```bash
python3 scripts/validate_structure.py
python3 scripts/validate_yaml.py
python3 scripts/validate_frontmatter.py
python3 scripts/validate_links.py
python3 scripts/scan_secrets.py
python3 scripts/run_evals.py
python3 scripts/build_package.py    # gera dist/asa-agent-leonardo-os-v1.0.0.zip + checksum
```

## Governança

`never_invent_missing_data` · `external_action_requires_confirmation` · `least_privilege` · sem credenciais · sem deploy. Ver `SECURITY.md` e `config/governance.yaml`.

## Status e gaps

Ver `BUILD_REPORT.md` (gates BUILD-G1..G5) e `GAP_REGISTER.md` (OQ-01..OQ-08 + `[GAP-RUNTIME]`).
