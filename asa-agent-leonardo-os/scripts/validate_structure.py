#!/usr/bin/env python3
"""Valida que a árvore obrigatória do AGENT_BUILD_SPEC §25 existe.
Saída: lista de arquivos esperados/criados/faltando. Exit 0 se nada faltar."""
from __future__ import annotations
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXPECTED = [
    "AGENT_BUILD_SPEC.md", "CLAUDE.md", "README.md", "CHANGELOG.md",
    "BUILD_REPORT.md", "GAP_REGISTER.md", "DECISION_LOG.md", "SECURITY.md",
    "LICENSE_POLICY.md",
    ".claude/agents/asa-orchestrator.md",
    ".claude/agents/asa-build-architect.md",
    ".claude/agents/asa-agent-engineer.md",
    ".claude/agents/asa-skill-engineer.md",
    ".claude/agents/asa-quality-governance-auditor.md",
    ".claude/skills/leonardo-admin/SKILL.md",
    ".claude/skills/leonardo-admin/README.md",
    ".claude/skills/asa-admin/SKILL.md",
    ".claude/skills/asa-admin/README.md",
    ".claude/skills/deskos/SKILL.md",
    ".claude/skills/deskos/README.md",
    ".claude/commands/architect-agentic-system.md",
    ".claude/commands/create-validate-agentic-system.md",
    ".claude/commands/wf1-build.md",
    ".claude/commands/wf2-communicate.md",
    ".claude/commands/wf3-operate.md",
    ".claude/hooks/README.md",
    ".claude/settings.example.json",
    "config/environment-capabilities.yaml", "config/governance.yaml",
    "config/routing-policy.yaml", "config/autonomy-policy.yaml",
    "config/memory-policy.yaml", "config/source-precedence.yaml",
    "config/write-policy.yaml",
    "workflows/WORKFLOW_LIBRARY.md",
    "FOLLOW_UP_INTEGRATION_REPORT.md",
    "references/follow-up-v2/ASA_LEONARDO_OS_FOLLOW_UP_REPORT_v2.0.md",
    "schemas/request.schema.yaml", "schemas/context.schema.yaml",
    "schemas/environment-manifest.schema.yaml", "schemas/intent.schema.yaml",
    "schemas/temporary-specialist.schema.yaml", "schemas/workflow-plan.schema.yaml",
    "schemas/execution-trace.schema.yaml", "schemas/deskos-handoff.schema.yaml",
    "schemas/quality-report.schema.yaml", "schemas/blueprint.schema.yaml",
    "workflows/WF1_BUILD.md", "workflows/WF2_COMMUNICATE.md", "workflows/WF3_OPERATE.md",
    "workflows/routines/A_DAILY_BRIEFING.md", "workflows/routines/B_WEEK_OPEN.md",
    "workflows/routines/C_WEEK_CLOSING.md", "workflows/routines/D_INTERVIEW.md",
    "workflows/routines/E_ANALYTICS.md",
    "blueprints/ASA_ORCHESTRATOR_AGENT.md", "blueprints/LEONARDO_ADMIN_SKILL.md",
    "blueprints/ASA_ADMIN_SKILL.md", "blueprints/DESKOS_SKILL.md",
    "templates/agent-template.md", "templates/skill-template.md",
    "templates/workflow-template.md", "templates/specialist-composition.yaml",
    "templates/execution-output.md", "templates/decision-record.md",
    "templates/handoff.md", "templates/gap-record.md",
    "references/PRD_LEO_PRD_ASA_v1.md", "references/LEONARDO_ADMIN_OS_SYSTEM_PROMPT.md",
    "references/ASA_AGENT_BLUEPRINT_SOURCE.md", "references/taxonomy.md",
    "references/glossary.md", "references/source-map.yaml",
    "registries/agent-registry.yaml", "registries/skill-registry.yaml",
    "registries/command-registry.yaml", "registries/connector-registry.yaml",
    "registries/project-registry.yaml", "registries/alias-registry.yaml",
    "evals/intent-classification.yaml", "evals/routing.yaml",
    "evals/anti-genericity.yaml", "evals/safety.yaml",
    "evals/specialist-composition.yaml", "evals/workflow-three-steps.yaml",
    "evals/traceability.yaml",
    "scripts/validate_structure.py", "scripts/validate_yaml.py",
    "scripts/validate_links.py", "scripts/validate_frontmatter.py",
    "scripts/scan_secrets.py", "scripts/run_evals.py", "scripts/build_package.py",
    "dist/.gitkeep",
]

EXPECTED_DIRS = [
    ".claude/skills/leonardo-admin/references",
    ".claude/skills/leonardo-admin/templates",
    ".claude/skills/leonardo-admin/tests",
    ".claude/skills/asa-admin/references",
    ".claude/skills/asa-admin/templates",
    ".claude/skills/asa-admin/tests",
    ".claude/skills/deskos/references",
    ".claude/skills/deskos/templates",
    ".claude/skills/deskos/tests",
    "tests/happy-path", "tests/incomplete-input", "tests/ambiguous-input",
    "tests/unavailable-tool", "tests/external-action", "tests/conflicting-sources",
    "tests/high-risk", "tests/regression",
]


def main() -> int:
    missing = [p for p in EXPECTED if not os.path.isfile(os.path.join(ROOT, p))]
    missing_dirs = [d for d in EXPECTED_DIRS if not os.path.isdir(os.path.join(ROOT, d))]
    created = len(EXPECTED) - len(missing)
    print(f"[structure] expected files: {len(EXPECTED)} | present: {created} | missing: {len(missing)}")
    print(f"[structure] expected dirs:  {len(EXPECTED_DIRS)} | missing: {len(missing_dirs)}")
    for p in missing:
        print(f"  MISSING FILE: {p}")
    for d in missing_dirs:
        print(f"  MISSING DIR : {d}")
    ok = not missing and not missing_dirs
    print("[structure] RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
