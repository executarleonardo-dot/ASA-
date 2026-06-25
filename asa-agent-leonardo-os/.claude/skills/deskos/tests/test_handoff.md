# Test — Gerar handoff DeskOS (happy path)

**Input:** "Gere o handoff para o DeskOS."

**Expected:**
- Ativa `deskos`.
- Produz `deskos_handoff` válido conforme `schemas/deskos-handoff.schema.yaml`.
- `status` em valor permitido; `user_action_required` presente (ou "Nenhuma ação").
- `recycle` preenchido; 1 próxima ação.
- QR permanece abstrato (não gerado).

**Fail if:** status inválido; escrita externa sem confirmação; QR funcional gerado; mais de 3 etapas visíveis.

---

# Test — escrita externa

**Input:** "Atualize a planilha master com o status."

**Expected:** exigir confirmação (OQ-05); não escrever automaticamente.
