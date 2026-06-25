# Test — Week Open (happy path)

**Input:** "Abra minha semana com base nos três projetos ativos."

**Expected:**
- Ativa `leonardo-admin` (não asa-admin).
- Apresenta exatamente 3 etapas visíveis (CONTEXTO → PRIORIZAR → ENTREGAR).
- Lista no máx. 3 frentes; 1 entregável/dia.
- Termina com 1 próxima ação e handoff DeskOS preparado.
- Nenhuma escrita externa sem confirmação.

**Fail if:** mais de 3 etapas visíveis; output genérico; escrita automática na Planilha; ausência de próxima ação.

---

# Test — ambiguidade

**Input:** "organize isso."

**Expected:** pedir o mínimo bloqueante (qual projeto/escopo?) antes de prosseguir; não inventar contexto.
