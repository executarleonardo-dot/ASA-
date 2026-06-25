# DeskOS — Contrato QR (abstrato)

**Status:** abstract · **Gap:** OQ-07 / GR-06 (`[GAP-RUNTIME]`)

Na v1, o QR é apenas um **contrato**, não uma funcionalidade. Não gerar QR real, não resolver roteamento por QR, não integrar com app físico.

```yaml
qr_contract:
  status: abstract
  intent: "apontar para o estado atual do workflow / próxima ação"
  payload_fields:    # definição abstrata; não serializar/gerar
    - handoff_id
    - workflow_id
    - stage_number
    - next_action_ref
  rendering: "[GAP] definir no momento da implementação física"
  generation: "[GAP-RUNTIME] requer integração externa autorizada"
```

Quando Leonardo decidir o timing do QR (antes/depois da v1), atualizar este contrato e remover o status `abstract`.
