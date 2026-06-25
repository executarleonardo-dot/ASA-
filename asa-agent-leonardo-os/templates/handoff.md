# Template — Handoff DeskOS

```yaml
deskos_handoff:
  handoff_id: ""
  date: ""
  workflow: { id: "", name: "", stage: { number: 1, name: "" } }
  system_activity: ""
  user_action_required: ""      # ou "Nenhuma ação"
  next_gate: ""
  primary_deliverable: ""
  status: preparing             # preparing|executing|awaiting|validating|completed|blocked
  blocker: ""
  evidence_refs: []
  recycle: { classification: "", carry_forward: false, notes: "" }
```

Nota: QR permanece **abstrato** (OQ-07). Escrita externa requer confirmação.
