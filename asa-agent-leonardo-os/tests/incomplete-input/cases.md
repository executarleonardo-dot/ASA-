# Tests — Input Incompleto (§29.2)

| # | Input | Expected |
|---|---|---|
| 1 | pedido sem `expected_output` | perguntar o mínimo bloqueante OU assumir explícito `[GAP]` se não crítico |
| 2 | `project_uid` ausente | marcar `[GAP]`; não inventar UID (ver project-registry) |
| 3 | ativo referenciado inexistente | sinalizar `[LACUNA]`; não fabricar o ativo |
| 4 | prazo ausente | prosseguir com suposição explícita; registrar `[GAP]` |
| 5 | ferramenta citada não disponível | fallback manual ou bloquear; `[GAP-RUNTIME]` se depender do Claude.ai |

**Fail if:** inventar dado ausente; prosseguir em item crítico sem perguntar.
