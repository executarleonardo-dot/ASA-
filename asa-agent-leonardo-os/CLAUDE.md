# CLAUDE.md — Instruções de operação para Claude Code

Este pacote é o **ASA Agent — Gerador do Leonardo-OS**. Leia o `AGENT_BUILD_SPEC.md` como contrato de construção antes de qualquer mudança.

## Regras obrigatórias

1. **Ler o spec** — `AGENT_BUILD_SPEC.md` e as fontes em `references/` (incluindo `references/_sources/`).
2. **Preservar source files** — nunca sobrescrever `references/_sources/*` nem `references/ASA_AGENT_BLUEPRINT_SOURCE.md`.
3. **Operar plan-first** — planejar antes de gerar; impedir overengineering.
4. **Não inventar** — `never_invent_missing_data: true`. Distinguir `[FATO]` / `[INFERÊNCIA]` / `[HIPÓTESE]` / `[GAP]` / `[LACUNA]`.
5. **Menor arquitetura eficaz** — 1 agente runtime + 3 Skills; subagentes apenas build-time.
6. **Separar runtime de build-time** — `.claude/skills/*` e `.claude/agents/asa-orchestrator.md` são runtime v1; os demais agentes são build-time.
7. **Manter boundaries** — respeitar ADR-001 (Leonardo Admin × ASA Admin × DeskOS).
8. **Não executar ações externas** — sem publicar, enviar, escrever em conectores, deploy ou instalar no Claude.ai.
9. **Validar antes de concluir** — rodar `scripts/validate_*.py` e `scripts/scan_secrets.py`.
10. **Registrar gaps** — manter `GAP_REGISTER.md` atualizado; ausência documental não é gap.
11. **Executar scripts** — usar `scripts/run_evals.py` e `scripts/build_package.py` quando os gates permitirem.
12. **Gerar BUILD_REPORT** — `BUILD_REPORT.md` por último, com PASS/FAIL/GAP e evidências.
13. **Não marcar P0 como completo** quando uma OQ bloqueante impedir validação do componente.
14. **Não criar credenciais** e **não hardcode secrets**.
15. **Não ocultar falhas** — reportar fielmente.

## Precedência em conflitos

```
Segurança e Governança → Decisões explícitas de Leonardo → CMD MASTER STANDALONE →
AGENT_BUILD_SPEC → PRD (LEO-PRD-ASA-v1) → System Prompt (LEO-ADMIN-OS-SP-v1.0) →
ASA Blueprint → Inferências de implementação
```

## Mapa rápido do pacote

- `blueprints/` — especificação canônica dos 4 componentes runtime.
- `.claude/agents/` — 1 agente runtime (`asa-orchestrator.md`) + 4 build-time.
- `.claude/skills/` — `leonardo-admin/`, `asa-admin/`, `deskos/`.
- `config/` — governança, roteamento, autonomia, memória, capacidades, precedência.
- `schemas/` — contratos (request, context, intent, specialist, workflow, trace, handoff, etc.).
- `workflows/` — WF1/WF2/WF3 + `routines/` A–E.
- `evals/`, `tests/`, `scripts/` — validação local.
- `registries/` — catálogos de agents, skills, commands, connectors, projects, aliases.

## Antes de assumir frontmatter

Consulte a documentação/versão atual do Claude Code antes de assumir campos de frontmatter de agentes/Skills (ver `GAP_REGISTER.md` GR-07). Confirmar no momento do import no Claude.ai.
