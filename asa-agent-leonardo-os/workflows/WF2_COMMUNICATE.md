---
schema: LEO-WORKFLOW-v1.0
id: WF2
name: COMMUNICATE
visible_steps: 3
source: "AGENT_BUILD_SPEC §13.2"
---

# WF2 — COMMUNICATE

## Gatilhos
transformar resultado validado em conteúdo · case · narrativa · publicação.

## Interface visível
```
1. EXTRAIR
2. PRODUZIR
3. PUBLICAR
```

## Etapa 1 — EXTRAIR
Identificar caso documentável a partir de resultado validado; coletar evidências.
```yaml
gate_id: WF2-G1
name: case_extracted
pass_when: [documentable_case_exists, source_result_is_validated, evidence_collected]
```

## Etapa 2 — PRODUZIR
Construir narrativa e conteúdo final; validar narrativa.
```yaml
gate_id: WF2-G2
name: content_validated
pass_when: [narrative_validated, final_content_ready, anti_genericity_pass]
```

## Etapa 3 — PUBLICAR
Publicar **somente após confirmação**; registrar destino; preparar métricas/feedback.
```yaml
gate_id: WF2-G3
name: published_or_confirmed
pass_when: [publication_confirmed_by_leonardo, destination_registered, metrics_feedback_prepared]
fail_when: [published_without_confirmation]
```

## DoD
caso documentável · narrativa validada · conteúdo final · publicação só após confirmação · link/destino registrado · métricas e feedback preparados.

## Nota de governança
Publicar/enviar = ação externa → confirmação obrigatória (`config/governance.yaml`).
