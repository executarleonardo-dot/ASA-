# BUILD_REPORT — ASA Agent / Gerador do Leonardo-OS

**Schema:** LEO-BUILD-REPORT-v1.0

```yaml
build_report:
  build_id: ASA-BUILD-2026-06-25-v1.0.0
  generated_at: "2026-06-25"
  environment:
    build_tool: "Claude Code (local)"
    git_version: "2.43.0"
    python_version: "3.11.15"
    runtime_v1: "Claude.ai Projects (não instalado/testado neste build)"
    capabilities_verified:
      - filesystem_local
      - python3_stdlib
      - pyyaml_6.0.1
      - zip_sha256
  files:
    expected: 90        # arquivos da árvore obrigatória (validate_structure)
    created: 90
    total_in_package: 119   # inclui references/_sources/* preservados; exclui dist/ (saída de build)
    missing: []
  gates:
    BUILD_G1: PASS      # fontes preservadas + source-map + OQs/conflitos registrados
    BUILD_G2: PASS      # boundaries explícitos + 1 agente runtime + 3 Skills + subagentes build-time + fixed core/variable profile
    BUILD_G3: PASS      # estrutura, YAML, frontmatter e links internos válidos
    BUILD_G4: PARTIAL   # testes estáticos/locais PASS; testes exclusivos do Claude.ai = [GAP-RUNTIME]
    BUILD_G5: PASS      # README + BUILD_REPORT + gap register + scan sem secrets + pacote abre + checksum
  tests:
    passed:
      - validate_structure
      - validate_yaml
      - validate_frontmatter
      - validate_links
      - scan_secrets
      - run_evals (estático: parse, three-steps, trace fields)
    failed: []
    skipped:
      - intent_classification_accuracy   # [GAP-RUNTIME] GR-05 (Claude.ai)
      - end_to_end_real_case             # [GAP-RUNTIME] GR-04 (Claude.ai)
      - connector_round_trip             # [GAP-RUNTIME] GR-03
  gaps:
    decision:
      - OQ-01 commands_01_03_function
      - OQ-02 leonardo_s_alias (resolvido: canonical=Leonardo Admin)
      - OQ-03 interview_name (provisional)
      - OQ-04 design_plugins_duplication
      - OQ-05 master_spreadsheet_writable_fields
      - OQ-06 admin_boundaries (resolvido por ADR-001)
      - OQ-07 deskos_qr (contrato abstrato)
      - OQ-08 autonomy_threshold (policy provisória)
    runtime:
      - GR-01 environment_capabilities
      - GR-02 installed_skills
      - GR-03 connectors_permissions
      - GR-04 end_to_end_execution
      - GR-05 intent_accuracy
      - GR-06 sync_qr_deskos_physical
      - GR-07 frontmatter_fields_accepted
  risks:
    - id: R-04
      desc: "capacidade Claude presumida"
      mitigation: "Environment Resolver + config/environment-capabilities.yaml (não verificado)"
    - id: R-09
      desc: "OQs bloqueantes"
      mitigation: "GAP_REGISTER; componentes afetados não declarados completos"
    - id: R-10
      desc: "spec/frontmatter desatualizado"
      mitigation: "confirmar campos no import (GR-07)"
  security_scan: "PASS — nenhum secret; nenhuma credencial criada; .xlsx preservado sem parsing"
  package:
    path: "dist/asa-agent-leonardo-os-v1.0.0.zip"
    checksum_file: "dist/asa-agent-leonardo-os-v1.0.0.zip.sha256"
    checksum: "ver sidecar .sha256 (gerado por scripts/build_package.py)"
  next_action: >
    Leonardo: revisar OQs bloqueantes (OQ-01, OQ-05, OQ-08) e, quando aprovado,
    importar manualmente .claude/skills/* e .claude/agents/asa-orchestrator.md em um
    Project do Claude.ai, rodar o Environment Resolver e validar 1 caso real (GR-04).
```

## Resumo

- **Estrutura:** árvore obrigatória (§25) gerada integralmente; 90/90 arquivos esperados presentes; 17/17 diretórios.
- **Fontes:** preservadas em `references/` e `references/_sources/` (incl. `.xlsx` binário não parseado); `source-map.yaml` registra origem (CMD + PROJECT.zip), sem busca externa.
- **Arquitetura:** 1 agente runtime (`asa-orchestrator`) + 3 Skills (leonardo-admin, asa-admin, deskos) + 4 subagentes build-time; boundaries em ADR-001; fixed core × variable profile em ADR-003.
- **Validações locais:** YAML, frontmatter, links internos, scan de secrets e evals estáticos → PASS.
- **Limite honesto:** nenhuma instalação ou teste real no Claude.ai foi feito (`[GAP-RUNTIME]`). Nenhuma ação externa, deploy ou credencial.

## Gates de build (detalhe)

| Gate | Resultado | Evidência |
|---|---|---|
| BUILD-G1 Sources normalized | PASS | `references/source-map.yaml`, `GAP_REGISTER.md`, `DECISION_LOG.md` |
| BUILD-G2 Architecture approved | PASS | ADR-001/002/003; `registries/agent-registry.yaml`, `skill-registry.yaml` |
| BUILD-G3 Components generated | PASS | `validate_structure/yaml/frontmatter/links` PASS |
| BUILD-G4 Tests passed | PARTIAL | `run_evals` estático PASS; runtime = `[GAP-RUNTIME]` |
| BUILD-G5 Package ready | PASS | `scan_secrets` PASS; `dist/*.zip` abre; checksum em sidecar |

## Como reproduzir as validações

```bash
cd asa-agent-leonardo-os
python3 scripts/validate_structure.py
python3 scripts/validate_yaml.py
python3 scripts/validate_frontmatter.py
python3 scripts/validate_links.py
python3 scripts/scan_secrets.py
python3 scripts/run_evals.py
python3 scripts/build_package.py   # gera dist/asa-agent-leonardo-os-v1.0.0.zip + .sha256
```
