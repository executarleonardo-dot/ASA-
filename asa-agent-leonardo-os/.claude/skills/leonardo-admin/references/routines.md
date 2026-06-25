# Leonardo Admin — Rotinas (referência)

Esta Skill é **owner** das rotinas A, B e C. Especificação canônica em `workflows/routines/`.

| ID | Rotina | Co-owner | Status | Spec |
|---|---|---|---|---|
| A | Daily Briefing | — | specify_and_test | `workflows/routines/A_DAILY_BRIEFING.md` |
| B | Week Open | DeskOS | specify_and_test | `workflows/routines/B_WEEK_OPEN.md` |
| C | Week Closing | DeskOS | specify_and_test | `workflows/routines/C_WEEK_CLOSING.md` |

Rotinas D (Interview, provisional — OQ-03) e E (Analytics) são roteadas pelo ASA para a Skill adequada e **não** pertencem exclusivamente à Leonardo Admin.

## Estrutura comum de cada rotina
trigger · inputs · required_context · allowed_tools · confirmation_points · 3 etapas visíveis · gates · output · evidence · failure behavior · state update · next action.

## Invariantes
- Sempre 3 etapas visíveis e 1 próxima ação.
- Escrita externa/memória → confirmação.
- Baixa carga cognitiva (mobile-first, sem rolagem horizontal).
