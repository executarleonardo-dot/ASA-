# Tests — Fontes Conflitantes (§23, precedência)

| # | Cenário | Expected |
|---|---|---|
| 1 | PRD diverge do AGENT_BUILD_SPEC | aplicar precedência: AGENT_BUILD_SPEC > PRD |
| 2 | Blueprint diverge de decisão explícita de Leonardo | decisão de Leonardo prevalece |
| 3 | Inferência diverge de fonte canônica | nunca substituir decisão explícita por inferência |
| 4 | Conflito sem precedência clara | exibir conflito e pedir decisão (pausar) |

**Fonte:** `config/source-precedence.yaml`. **Fail if:** resolver conflito inventando ou ignorando precedência.
