# Tests — Happy Path (§29.1)

| # | Input | Expected route | Skill principal | DoD |
|---|---|---|---|---|
| 1 | "Crie uma Skill para diagnosticar uma PME." | WF1 | asa-admin | blueprint + SKILL.md + tests; 3 etapas; trace |
| 2 | "Transforme o produto validado em case." | WF2 | asa-admin/orchestrator | conteúdo final; publicar só após confirmação |
| 3 | "Analise o feedback e decida o próximo ciclo." | WF3 | leonardo-admin + analítica | decisão + Recycle |
| 4 | "Abra minha semana com base nos três projetos ativos." | WF1/Rotina B | leonardo-admin (+deskos) | plano semanal + handoff |
| 5 | "Gere o handoff para o DeskOS." | WF3 | deskos | deskos_handoff válido |

**Invariantes:** 3 etapas visíveis; 1 próxima ação; trace 100%; nenhuma ação externa sem confirmação.
