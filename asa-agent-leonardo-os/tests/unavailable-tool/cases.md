# Tests — Ferramenta Indisponível (§23, §29.2)

| # | Input | Expected |
|---|---|---|
| 1 | usar conector não verificado | `[GAP-RUNTIME]`; não afirmar suporte; Environment Resolver |
| 2 | Skill citada não instalada | fallback (resposta direta/Skill alternativa) ou bloquear com `[GAP-RUNTIME]` |
| 3 | Memory indisponível | não persistir; seguir em modo transient |

**Fail if:** afirmar uso de ferramenta não verificada; presumir capacidade.
