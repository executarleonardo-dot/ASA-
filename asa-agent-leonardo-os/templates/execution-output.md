# Template — Output de execução (contrato fixo §21)

```text
RESUMO     : <o que foi feito, 1–2 linhas>
DECISÃO    : <decisão tomada e por quê>
ARTEFATOS  : <lista de artefatos/links>
VALIDAÇÃO  : <gates avaliados + resultado>
RISCOS     : <riscos e gaps [GAP]/[GAP-RUNTIME]>
PRÓXIMA AÇÃO: <uma única próxima ação>
```

## Interface mínima
```text
WORKFLOW    : [WF1 | WF2 | WF3] — nome
ETAPA ATUAL: [1 | 2 | 3] — nome
SISTEMA     : atividade atual
PRECISA     : ação de Leonardo ou "Nenhuma ação"
PRÓXIMO     : gate ou entregável
STATUS      : Preparando | Executando | Aguardando | Validando | Concluído | Bloqueado
```

Regra: mostrar **uma** próxima ação; não apresentar backlog completo por padrão.
