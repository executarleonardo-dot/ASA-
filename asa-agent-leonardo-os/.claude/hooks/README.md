# Hooks

Este diretório reserva o espaço para **hooks** do Claude Code (eventos determinísticos), conforme `references/ASA_AGENT_BLUEPRINT_SOURCE.md` (`deterministic_event → hook`).

## Estado v1
Nenhum hook ativo na v1 (`[GAP]` de necessidade). Hooks só devem ser adicionados quando houver um evento determinístico real que justifique automação (princípio: menor arquitetura eficaz).

## Candidatos futuros (não implementados)
- `PreToolUse` para bloquear escrita externa sem confirmação (reforço de governança).
- `PostToolUse` para anexar entradas ao execution_trace.
- `SessionStart` para rodar o Environment Resolver.

## Regras
- Hooks não substituem os gates de governança; apenas os reforçam.
- Não adicionar hooks que executem ação externa ou exponham secrets.
- Configuração real via `.claude/settings.json` (ver `settings.example.json`) — `[GAP-RUNTIME]` GR-07 para campos aceitos pela versão instalada.
