# Leonardo Admin Skill

Skill runtime que administra o **contexto operacional de Leonardo**. Núcleo em `SKILL.md`; conhecimento estável em `references/`; modelos em `templates/`; casos em `tests/`.

- **Boundary:** `blueprints/LEONARDO_ADMIN_SKILL.md` / ADR-001.
- **Owner de rotinas:** A (Daily Briefing), B (Week Open), C (Week Closing).
- **Não contém:** engenharia de agentes (asa-admin), representação física (deskos).

## Estrutura
```
leonardo-admin/
├── SKILL.md
├── README.md
├── references/   # boundary + rotinas detalhadas
├── templates/    # week-open, daily-briefing
└── tests/        # casos happy/ambíguo
```
