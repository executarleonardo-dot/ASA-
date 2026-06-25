# DeskOS Skill

Skill runtime que converte estado digital em **representação semanal** para a interface DESK-OS. Núcleo em `SKILL.md`; contrato/QR em `references/`; modelo em `templates/`; casos em `tests/`.

- **Boundary:** `blueprints/DESKOS_SKILL.md` / ADR-001.
- **Contrato:** `schemas/deskos-handoff.schema.yaml`.
- **QR:** abstrato (OQ-07).
- **Não contém:** roteamento, criação de agentes, administração pessoal.

## Estrutura
```
deskos/
├── SKILL.md
├── README.md
├── references/   # contrato + QR abstrato
├── templates/    # handoff semanal
└── tests/        # geração de handoff
```
