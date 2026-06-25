---
name: wf3-operate
description: >-
  Executa o Workflow 3 — OPERATE: DISTRIBUIR → ANALISAR → RECICLAR. Use para
  distribuição, análise, decisão e reciclagem. Ações externas e atualização de
  backlog/memória/SOP somente após confirmação.
---

# /wf3-operate

> Workflow canônico: `workflows/WF3_OPERATE.md`. 3 etapas visíveis + gates.

## Interface visível
```
1. DISTRIBUIR
2. ANALISAR
3. RECICLAR
```

## DoD
audiência/canal definidos · ação externa confirmada · respostas/dados analisados · decisão tomada · backlog/memória/SOP atualizados conforme autorização · novo ciclo preparado.

## Guardrails
3 etapas; ação externa e escrita em memória → confirmação; trace 100%.
