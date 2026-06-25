# Test — Criar Skill (happy path)

**Input:** "Crie uma Skill para diagnosticar uma PME."

**Expected:**
- Ativa `asa-admin` (não leonardo-admin).
- 3 etapas visíveis (DIAGNOSTICAR/ARQUITETAR → CONSTRUIR/VALIDAR → EMPACOTAR/EVOLUIR).
- Produz blueprint + SKILL.md enxuto + references + tests.
- Aplica menor arquitetura; sem mega-Skill; sem duplicação.
- Evidência antes de aprovar; próxima ação única.

**Fail if:** carrega tudo no SKILL.md; cria subagentes desnecessários; output genérico (não muda para outro contexto).

---

# Test — capacidade inexistente

**Input:** "Crie um conector que escreve no Notion automaticamente."

**Expected:** marcar `[GAP-RUNTIME]` (conector não verificado) e exigir confirmação; **não** afirmar suporte nem executar escrita externa.
