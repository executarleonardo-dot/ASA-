O schema abaixo é o contrato operacional universal que o agente preenche após cruzar macro personalização, contexto, Planilha Master, stack disponível, dependências, ferramentas, riscos e objetivo do workflow.

# ============================================================

# LEONARDO ADMIN OS

# UNIVERSAL AI-FIRST WORKFLOW CARD

# Schema: LEO-WF-CARD-v1

# Purpose:

#   Estruturar um workflow ponta a ponta, executável por agente,

#   composto a partir da macro personalização, contexto operacional,

#   catálogo de skills, commands, plugins, conectores e documentos.

#

# Principle:

#   O agente não deve apenas descrever o workflow.

#   Deve selecionar, instanciar, executar, validar, registrar

#   e entregar o resultado utilizando o menor stack suficiente.

# ============================================================

  

workflow_card:

  

  # ----------------------------------------------------------

  # 1. IDENTIFICAÇÃO

  # ----------------------------------------------------------

  

  meta:

    schema_id: "LEO-WF-CARD-v1"

    card_id: ""

    workflow_id: ""

    workflow_name: ""

    workflow_slug: ""

    workflow_type:

      value: ""

      allowed:

        - build

        - operate

        - research

        - document

        - publish

        - analyze

        - administer

        - handoff

        - maintain

        - custom

  

    version: "1.0.0"

  

    status:

      value: "draft"

      allowed:

        - draft

        - ready

        - running

        - blocked

        - validation

        - completed

        - failed

        - archived

  

    owner:

      name: "Leonardo Batista"

      role: "Solo intrapreneur"

      email: "executar.leonardo@outlook.com"

  

    system:

      name: "Leonardo Admin OS"

      orchestrator: ""

      environment: ""

      workspace: ""

  

    timestamps:

      created_at: ""

      updated_at: ""

      started_at: ""

      completed_at: ""

  

    traceability:

      run_id: ""

      parent_workflow_id: ""

      previous_workflow_id: ""

      next_workflow_id: ""

      source_request_id: ""

      project_uid: ""

      user_uid: ""

      organization_uid: ""

  

  # ----------------------------------------------------------

  # 2. CLASSIFICAÇÃO

  # ----------------------------------------------------------

  

  classification:

    cluster: ""

    subcluster: ""

  

    tags:

      - ""

  

    business_domain:

      value: ""

      allowed:

        - product

        - operations

        - editorial

        - content

        - administration

        - agent_management

        - low_code

        - process_management

        - research

        - data

        - marketing

        - sales

        - governance

        - personal

        - other

  

    work_layer:

      value: ""

      allowed:

        - creator

        - process_manager

        - agent_manager

        - low_code_developer

        - administrator

        - hybrid

  

    cognitive_layer:

      visible_layer: ""

      systemic_layer: ""

  

    complexity:

      level:

        value: ""

        allowed:

          - low

          - medium

          - high

          - critical

  

      rationale: ""

  

    execution_mode:

      value: ""

      allowed:

        - autonomous

        - supervised

        - collaborative

        - human_approval_required

  

  # ----------------------------------------------------------

  # 3. FONTES DE CONTEXTO

  # ----------------------------------------------------------

  

  context_sources:

  

    macro_personalization:

      required: true

      source_id: ""

      source_location: ""

      loaded: false

      extracted_fields:

        - preferences

        - roles

        - restrictions

        - goals

        - communication_style

        - cognitive_requirements

        - authorized_tools

  

    memory:

      required: true

      source_id: ""

      source_location: ""

      loaded: false

      allowed_use:

        - recover_known_context

        - avoid_repeated_questions

        - personalize_execution

        - maintain_continuity

  

      prohibited_use:

        - invent_missing_business_data

        - persist_sensitive_data_without_rule

        - override_project_source_of_truth

  

    master_spreadsheet:

      required: true

      workbook_id: ""

      workbook_name: ""

      workbook_location: ""

  

      uids:

        - uid: "UID02"

          purpose: ""

        - uid: "UID-ASA"

          purpose: ""

        - uid: "UID-LEONARDO-S"

          purpose: ""

        - uid: "UID-MACRO-PERSONALIZATION"

          purpose: ""

        - uid: "UID-PLATFORM-DIRECTORY"

          purpose: ""

        - uid: "UID-DESK-OS"

          purpose: ""

  

      tags_to_query:

        - WF

        - templates

        - commands

        - issues

        - relations

        - business

        - GTM

        - PRD

        - docs

  

      source_of_truth_rules:

        - ""

  

    project_documents:

      required: false

  

      documents:

        - document_id: ""

          document_name: ""

          document_type: ""

          location: ""

          purpose: ""

          freshness: ""

          authority_level: ""

  

    repositories:

      - repository_id: ""

        repository_name: "Leonardo OS"

        repository_type: ""

        location: ""

        access_status: ""

  

    external_sources:

      allowed: true

      required_when:

        - current_information_required

        - technical_documentation_required

        - internal_sources_insufficient

  

      preferred_sources:

        - official_documentation

        - primary_sources

        - authoritative_repositories

  

  # ----------------------------------------------------------

  # 4. CONTEXTO OPERACIONAL

  # ----------------------------------------------------------

  

  operational_context:

  

    current_project:

      project_name: ""

      project_uid: ""

      project_status: ""

      project_description: ""

      current_phase: ""

  

    current_role:

      primary: "Content creator"

  

      secondary:

        - "Process manager"

        - "Agent manager"

        - "Low-code developer"

  

    objectives:

  

      macro:

        statement: ""

        timeframe: ""

        success_evidence: ""

  

      meso:

        statement: ""

        timeframe: ""

        success_evidence: ""

  

      micro:

        statement: ""

        timeframe: ""

        success_evidence: ""

  

    current_problem:

      statement: ""

      cause: ""

      effect: ""

      implication: ""

  

    expected_result:

      statement: ""

      measurable_outcomes:

        - ""

  

    current_state:

      available_assets:

        - ""

  

      completed_assets:

        - ""

  

      missing_assets:

        - ""

  

      blockers:

        - ""

  

      assumptions:

        - assumption: ""

          validation_status: ""

  

      constraints:

        - ""

  

  # ----------------------------------------------------------

  # 5. INTENÇÃO DO WORKFLOW

  # ----------------------------------------------------------

  

  intent:

  

    trigger:

      type:

        value: ""

        allowed:

          - command

          - manual_request

          - schedule

          - event

          - previous_workflow_completion

          - system_condition

  

      trigger_id: ""

      trigger_expression: ""

      trigger_source: ""

  

    job_to_be_done:

      when: ""

      user_wants_to: ""

      so_that: ""

  

    problem_to_solve: ""

  

    transformation:

      input_state: ""

      output_state: ""

  

    final_deliverable:

      name: ""

      format: ""

      destination: ""

      intended_user: ""

      intended_use: ""

  

    definition_of_done:

      - id: "DOD-01"

        criterion: ""

        validation_method: ""

        required_evidence: ""

  

    non_goals:

      - ""

  

    stop_conditions:

      success:

        - ""

  

      blocked:

        - ""

  

      failure:

        - ""

  

  # ----------------------------------------------------------

  # 6. DECISÃO ARQUITETURAL

  # ----------------------------------------------------------

  

  architecture_decision:

  

    artifact_type:

      value: ""

      allowed:

        - skill

        - agent

        - command

        - workflow

        - plugin

        - template

        - document

        - system

        - hybrid

  

    build_strategy:

      value: ""

      allowed:

        - create_new

        - extend_existing

        - compose_existing

        - update_version

        - reuse_without_change

        - abort_duplicate

  

    decision_rationale: ""

  

    alternatives_considered:

      - alternative_id: ""

        description: ""

        advantages:

          - ""

        disadvantages:

          - ""

        rejected_because: ""

  

    selected_architecture:

      pattern: ""

      description: ""

  

    architecture_constraints:

      - ""

  

    reusable_components:

      - component_id: ""

        component_name: ""

        source: ""

        reuse_mode:

          value: ""

          allowed:

            - direct

            - extend

            - reference

            - copy

            - adapt

  

  # ----------------------------------------------------------

  # 7. CATÁLOGO DE RECURSOS DISPONÍVEIS

  # ----------------------------------------------------------

  

  available_stack:

  

    commands:

      - command_id: ""

        command_name: ""

        tags:

          - ""

        purpose: ""

        input_contract: ""

        output_contract: ""

        activation_condition: ""

        availability: true

  

    skills:

      - skill_id: ""

        skill_name: ""

        cluster: ""

        tags:

          - ""

        purpose: ""

        capabilities:

          - ""

        activation_condition: ""

        dependency_ids:

          - ""

        availability: true

  

    agents:

      - agent_id: ""

        agent_name: ""

        role: ""

        capabilities:

          - ""

        delegation_condition: ""

        availability: true

  

    plugins:

      - plugin_id: ""

        plugin_name: ""

        provider: ""

        category: ""

        capabilities:

          - ""

        activation_condition: ""

        availability: true

  

    connectors:

      - connector_id: ""

        connector_name: ""

        provider: ""

        capabilities:

          - read

          - write

          - update

          - search

          - create

        permitted_actions:

          - ""

        prohibited_actions:

          - ""

        confirmation_required: false

        access_status: ""

  

    applications:

      - application_id: ""

        application_name: ""

        purpose: ""

        source_of_truth_for:

          - ""

        integration_mode: ""

        availability: true

  

    tools:

      - tool_id: ""

        tool_name: ""

        purpose: ""

        preferred_for:

          - ""

        avoid_when:

          - ""

        fallback_tool_id: ""

  

    templates:

      - template_id: ""

        template_name: ""

        template_type: ""

        location: ""

        use_condition: ""

        required_variables:

          - ""

  

    scripts:

      - script_id: ""

        script_name: ""

        purpose: ""

        input_contract: ""

        output_contract: ""

        execution_environment: ""

        availability: true

  

  # ----------------------------------------------------------

  # 8. MOTOR DE SELEÇÃO AI-FIRST

  # ----------------------------------------------------------

  

  ai_first_decision_engine:

  

    objective:

      statement: >

        Selecionar e encadear o menor conjunto suficiente de

        commands, skills, agents, plugins, connectors, tools,

        documents and templates required to complete the workflow.

  

    optimization_priorities:

      - reduce_manual_steps

      - reduce_file_transfers

      - reduce_duplicate_files

      - reuse_existing_assets

      - edit_source_of_truth_directly

      - preserve_traceability

      - preserve_reversibility

      - minimize_cognitive_load

      - avoid_unnecessary_tool_calls

  

    decision_variables:

  

      execution_cost:

        weight: 0

        assessment: ""

  

      cognitive_cost:

        weight: 0

        assessment: ""

  

      number_of_handoffs:

        weight: 0

        assessment: ""

  

      number_of_intermediate_files:

        weight: 0

        assessment: ""

  

      execution_risk:

        weight: 0

        assessment: ""

  

      traceability:

        weight: 0

        assessment: ""

  

      reversibility:

        weight: 0

        assessment: ""

  

      reuse_potential:

        weight: 0

        assessment: ""

  

    mandatory_rules:

  

      - id: "AI-FIRST-001"

        condition: "official_editable_document_exists"

        action: "edit_existing_document_inline"

        preferred_tool: "STR_REPLACE"

        avoid: "create_parallel_copy"

  

      - id: "AI-FIRST-002"

        condition: "localized_change_required"

        action: "replace_only_affected_block"

        preferred_tool: "STR_REPLACE"

        avoid: "rewrite_full_document"

  

      - id: "AI-FIRST-003"

        condition: "official_drive_destination_exists"

        action: "write_directly_to_drive"

        avoid: "generate_then_request_manual_upload"

  

      - id: "AI-FIRST-004"

        condition: "master_spreadsheet_is_source_of_truth"

        action: "update_existing_record_directly"

        preferred_tool: "EXCEL_CO_WORKING"

        avoid: "create_new_spreadsheet"

  

      - id: "AI-FIRST-005"

        condition: "approved_template_exists"

        action: "instantiate_template"

        avoid: "create_structure_from_zero"

  

      - id: "AI-FIRST-006"

        condition: "similar_asset_exists"

        action: "evaluate_extend_or_compose"

        avoid: "duplicate_capability"

  

      - id: "AI-FIRST-007"

        condition: "current_external_information_required"

        action: "query_primary_current_source"

        avoid: "rely_on_stale_memory"

  

      - id: "AI-FIRST-008"

        condition: "external_side_effect"

        action: "apply_confirmation_policy"

        avoid: "execute_without_required_approval"

  

      - id: "AI-FIRST-009"

        condition: "output_is_temporary_and_not_reusable"

        action: "keep_in_runtime_state"

        avoid: "persist_unnecessary_draft"

  

    selected_strategy:

      strategy_summary: ""

  

      selected_resources:

        - resource_id: ""

          resource_type: ""

          role_in_workflow: ""

          selection_reason: ""

          activation_point: ""

  

      rejected_resources:

        - resource_id: ""

          rejection_reason: ""

  

  # ----------------------------------------------------------

  # 9. WORKFLOW VISÍVEL

  # ----------------------------------------------------------

  

  visible_workflow:

  

    interface_type:

      value: "triad"

      allowed:

        - triad

        - checklist

        - kanban

        - timeline

        - custom

  

    stages:

  

      - stage_id: "STAGE-01"

        name: ""

        purpose: ""

        visible_output: ""

        status: ""

  

      - stage_id: "STAGE-02"

        name: ""

        purpose: ""

        visible_output: ""

        status: ""

  

      - stage_id: "STAGE-03"

        name: ""

        purpose: ""

        visible_output: ""

        status: ""

  

    current_stage_id: ""

    next_visible_action: ""

  

  # ----------------------------------------------------------

  # 10. WORKFLOW SISTÊMICO

  # ----------------------------------------------------------

  

  systemic_workflow:

  

    execution_policy:

      sequence_mode:

        value: ""

        allowed:

          - sequential

          - parallel

          - hybrid

  

      continue_on_noncritical_failure: false

      retry_policy: ""

      rollback_policy: ""

  

    phases:

  

      - phase_id: "PHASE-01"

        phase_name: ""

        phase_purpose: ""

        visible_stage_id: ""

  

        entry_conditions:

          - ""

  

        required_inputs:

          - ""

  

        expected_outputs:

          - ""

  

        operations:

  

          - operation_id: "WF-OP-001"

            operation_name: ""

  

            execution_mode:

              value: "execute"

              allowed:

                - execute

                - generate

                - update

                - validate

                - decide

                - request_approval

                - register

                - handoff

  

            purpose: ""

  

            trigger:

              type: ""

              after_operation_id: ""

              requires_gate_id: ""

              condition_expression: ""

  

            inputs:

              required:

                - input_id: ""

                  source: ""

                  format: ""

                  validation_rule: ""

  

              optional:

                - input_id: ""

                  source: ""

                  format: ""

  

            dependencies:

              operations:

                - ""

  

              resources:

                - ""

  

              permissions:

                - ""

  

              external_conditions:

                - ""

  

            agent_instruction:

              action: ""

              execution_details:

                - ""

              prohibited_behavior:

                - describe_without_executing

                - recreate_existing_asset_without_reason

                - invent_missing_information

                - skip_required_validation

                - persist_unnecessary_intermediate_files

  

            reasoning_requirements:

              level:

                value: ""

                allowed:

                  - low

                  - medium

                  - high

                  - maximum

  

              use_extended_thinking_when:

                - multiple_architectures_are_valid

                - dependencies_are_conflicting

                - high_cost_of_error

                - tool_choice_materially_affects_result

                - incomplete_context_requires_inference

                - cross_cluster_composition_required

  

              reasoning_focus:

                - objective

                - dependencies

                - alternatives

                - efficiency

                - risk

                - reversibility

                - traceability

  

            resource_binding:

  

              primary_command:

                id: ""

                name: ""

  

              primary_skill:

                id: ""

                name: ""

  

              supporting_skills:

                - id: ""

                  name: ""

  

              agent:

                id: ""

                name: ""

  

              plugin:

                id: ""

                name: ""

  

              connector:

                id: ""

                name: ""

  

              application:

                id: ""

                name: ""

  

              tool:

                id: ""

                name: ""

  

              script:

                id: ""

                name: ""

  

              template:

                id: ""

                name: ""

  

            resource_selection_rationale:

              selected_path: ""

              why_selected: ""

              alternatives_rejected:

                - ""

  

            action_target:

              target_type:

                value: ""

                allowed:

                  - file

                  - folder

                  - document

                  - spreadsheet

                  - database_record

                  - repository

                  - application

                  - runtime_state

                  - external_recipient

  

              target_id: ""

              target_location: ""

              source_of_truth: false

  

            execution_action:

              action_type:

                value: ""

                allowed:

                  - create

                  - read

                  - search

                  - edit

                  - str_replace

                  - append

                  - update

                  - validate

                  - execute_script

                  - package

                  - test

                  - deploy

                  - save

                  - register

                  - notify

                  - handoff

                  - delete

                  - archive

  

              instruction: ""

  

            outputs:

              - output_id: ""

                output_name: ""

                output_type: ""

                format: ""

                destination: ""

                persistent: true

  

            evidence:

              required: true

              evidence_type:

                - file_diff

                - log

                - URL

                - test_report

                - spreadsheet_record

                - checksum

                - screenshot

                - approval

                - other

  

              evidence_location: ""

  

            acceptance_criteria:

              - criterion_id: ""

                criterion: ""

                validation_method: ""

                pass_condition: ""

  

            failure_handling:

  

              failure_conditions:

                - ""

  

              failure_classification:

                value: ""

                allowed:

                  - recoverable

                  - blocking

                  - critical

  

              automatic_recovery:

                enabled: false

                actions:

                  - ""

  

              fallback_resource:

                resource_id: ""

                resource_type: ""

  

              human_intervention:

                required: false

                question: ""

                response_options:

                  - ""

  

              failure_output:

                name: ""

                destination: ""

  

            completion:

  

              status: ""

              completed_at: ""

  

              next_operation:

                on_pass: ""

                on_fail: ""

                on_human_approval: ""

  

        exit_conditions:

          - ""

  

        phase_gate:

          gate_id: ""

          gate_name: ""

          pass_conditions:

            - ""

          fail_conditions:

            - ""

          evidence_required:

            - ""

  

  # ----------------------------------------------------------

  # 11. GRAFO DE DEPENDÊNCIAS

  # ----------------------------------------------------------

  

  dependency_graph:

  

    nodes:

      - node_id: ""

        node_type:

          value: ""

          allowed:

            - operation

            - document

            - command

            - skill

            - agent

            - plugin

            - connector

            - application

            - template

            - script

            - approval

            - output

        name: ""

  

    edges:

      - from_node_id: ""

        to_node_id: ""

        relation:

          value: ""

          allowed:

            - requires

            - produces

            - validates

            - updates

            - triggers

            - blocks

            - references

            - stores

            - hands_off_to

  

    critical_path:

      - ""

  

    parallelizable_operations:

      - operation_ids:

          - ""

        reason: ""

  

    blocking_dependencies:

      - dependency_id: ""

        reason: ""

        resolution_action: ""

  

  # ----------------------------------------------------------

  # 12. GATES

  # ----------------------------------------------------------

  

  gates:

  

    - gate_id: "GATE-01"

      gate_name: ""

      phase_id: ""

      purpose: ""

  

      entry_requirements:

        - ""

  

      pass_conditions:

        - ""

  

      fail_conditions:

        - ""

  

      evidence_required:

        - ""

  

      validation_resource:

        resource_id: ""

        resource_type: ""

  

      approval:

        required: false

        approver: ""

        approval_method: ""

  

      on_pass:

        action: ""

        next_phase_id: ""

  

      on_fail:

        action: ""

        remediation_operation_id: ""

  

  # ----------------------------------------------------------

  # 13. TESTES E QUALIDADE

  # ----------------------------------------------------------

  

  validation:

  

    test_plan:

  

      trigger_tests:

        - test_id: ""

          scenario: ""

          expected_result: ""

  

      happy_path_tests:

        - test_id: ""

          input: ""

          expected_result: ""

  

      incomplete_input_tests:

        - test_id: ""

          missing_input: ""

          expected_behavior: ""

  

      tool_failure_tests:

        - test_id: ""

          unavailable_resource: ""

          expected_fallback: ""

  

      safety_tests:

        - test_id: ""

          risk_scenario: ""

          expected_control: ""

  

      regression_tests:

        - test_id: ""

          protected_behavior: ""

  

    quality_criteria:

  

      completeness:

        threshold: ""

        validation: ""

  

      correctness:

        threshold: ""

        validation: ""

  

      traceability:

        threshold: ""

        validation: ""

  

      personalization:

        threshold: ""

        validation: ""

  

      non_genericity:

        threshold: ""

        validation: ""

  

      usability:

        threshold: ""

        validation: ""

  

      cognitive_load:

        threshold: ""

        validation: ""

  

      security:

        threshold: ""

        validation: ""

  

    quality_score:

      total: 0

      maximum: 100

      minimum_to_pass: 0

  

    defects:

      - defect_id: ""

        severity: ""

        description: ""

        root_cause: ""

        affected_operation_id: ""

        correction_action: ""

        status: ""

  

  # ----------------------------------------------------------

  # 14. ARQUIVOS E ARTEFATOS

  # ----------------------------------------------------------

  

  artifacts:

  

    expected_structure:

      root_folder: ""

  

      files:

        - file_id: ""

          path: ""

          file_type: ""

          required: true

          source:

            value: ""

            allowed:

              - generated

              - template

              - existing

              - copied

              - linked

          generated_by_operation_id: ""

          validation_rule: ""

  

    created:

      - artifact_id: ""

        name: ""

        type: ""

        format: ""

        location: ""

        version: ""

        checksum: ""

        owner: ""

  

    updated:

      - artifact_id: ""

        name: ""

        previous_version: ""

        new_version: ""

        location: ""

        diff_evidence: ""

  

    linked:

      - artifact_id: ""

        name: ""

        location: ""

        relationship: ""

  

    temporary:

      - artifact_id: ""

        retention_policy: ""

        deletion_condition: ""

  

  # ----------------------------------------------------------

  # 15. PERSISTÊNCIA E FONTES DE VERDADE

  # ----------------------------------------------------------

  

  persistence:

  

    records:

  

      - record_id: ""

        record_type: ""

        source_of_truth:

          value: ""

          allowed:

            - master_spreadsheet

            - drive

            - github

            - linear

            - memory

            - project_document

            - external_system

  

        destination_id: ""

        destination_location: ""

  

        write_mode:

          value: ""

          allowed:

            - create

            - update

            - append

            - replace_block

            - link_only

  

        operation_id: ""

        evidence: ""

  

    spreadsheet_update:

      required: false

      workbook_id: ""

      sheet_name: ""

      lookup_key: ""

      lookup_value: ""

      fields_to_update:

        - field: ""

          value_source: ""

      update_mode: "direct"

      create_new_workbook: false

  

    drive_update:

      required: false

      folder_id: ""

      write_directly: true

      files:

        - ""

  

    github_update:

      required: false

      repository: ""

      branch: ""

      commit_required: false

      tag_required: false

      release_required: false

  

    memory_update:

      required: false

      items:

        - ""

      approval_required: true

  

  # ----------------------------------------------------------

  # 16. SEGURANÇA E GOVERNANÇA

  # ----------------------------------------------------------

  

  governance:

  

    permissions:

      granted:

        - ""

  

      missing:

        - ""

  

    confirmation_policy:

  

      always_confirm:

        - destructive_action

        - external_publication

        - customer_delivery

        - financial_action

        - sensitive_data_persistence

  

      may_execute_without_confirmation:

        - read_authorized_sources

        - update_runtime_state

        - create_temporary_draft

        - validate_files

        - run_non_destructive_tests

  

    data_rules:

      - do_not_invent_data

      - differentiate_fact_hypothesis_and_gap

      - preserve_original_sources

      - minimize_personal_data

      - do_not_expose_secrets

      - log_material_decisions

  

    secrets_scan:

      required: true

      status: ""

  

    audit:

      required: true

      audit_log_location: ""

      decision_register_location: ""

      evidence_register_location: ""

  

  # ----------------------------------------------------------

  # 17. EXECUÇÃO

  # ----------------------------------------------------------

  

  execution:

  

    current_state:

      current_phase_id: ""

      current_operation_id: ""

      current_gate_id: ""

      progress_percentage: 0

  

    next_action:

      operation_id: ""

      instruction: ""

      actor:

        value: ""

        allowed:

          - agent

          - leonardo

          - external_user

          - script

          - connector

  

    human_tasks:

      - task_id: ""

        purpose: ""

        required_input: ""

        blocking: true

        status: ""

  

    automated_tasks:

      - operation_id: ""

        automation_status: ""

  

    execution_log:

      - sequence: 1

        timestamp: ""

        operation_id: ""

        action: ""

        result: ""

        evidence: ""

  

  # ----------------------------------------------------------

  # 18. OUTPUT FINAL

  # ----------------------------------------------------------

  

  final_output:

  

    primary_deliverable:

      name: ""

      type: ""

      format: ""

      version: ""

      location: ""

      access_link: ""

      checksum: ""

  

    supporting_deliverables:

      - name: ""

        type: ""

        location: ""

  

    handoff:

      required: true

      target_user: ""

      target_environment: ""

      document_location: ""

  

      contents:

        - what_was_created

        - why_it_was_created

        - how_to_use

        - dependencies

        - limitations

        - tests_completed

        - files_and_links

        - next_action

  

    communication:

      required: false

      channel: ""

      recipient: ""

      message_id: ""

  

  # ----------------------------------------------------------

  # 19. ENCERRAMENTO

  # ----------------------------------------------------------

  

  closure:

  

    dod_validation:

      all_criteria_met: false

      unmet_criteria:

        - ""

  

    gates_validation:

      all_gates_passed: false

      failed_gates:

        - ""

  

    evidence_validation:

      complete: false

      missing_evidence:

        - ""

  

    final_status:

      value: ""

      allowed:

        - completed

        - completed_with_exceptions

        - blocked

        - failed

        - cancelled

  

    lessons_learned:

      - ""

  

    sop_updates:

      required: false

      updates:

        - ""

  

    reusable_patterns:

      - ""

  

    backlog_items:

      - ""

  

    next_workflow:

      trigger: false

      workflow_id: ""

      workflow_name: ""

      input_payload_location: ""

  

  # ----------------------------------------------------------

  # 20. INTERFACE RESUMIDA PARA LEONARDO

  # ----------------------------------------------------------

  

  user_view:

  

    workflow_name: ""

    current_stage: ""

    current_subworkflow: ""

  

    system_action:

      statement: ""

  

    leonardo_action:

      required: false

      statement: ""

  

    next_gate:

      name: ""

      requirement: ""

  

    next_action:

      statement: ""

  

    blocker:

      exists: false

      statement: ""

  

    progress:

      current: 0

      total: 0

      percentage: 0

  

    visible_status:

      value: ""

      allowed:

        - preparing

        - executing

        - waiting_for_input

        - validating

        - correcting

        - saving

        - completed

        - blocked

Lógica de preenchimento

FONTES

│

├── Macro Personalização

├── Memória

├── Planilha Master

├── Diretório de recursos

├── Projeto ativo

└── Solicitação

    │

    ▼

EXTENDED THINKING

│

├── classificar intenção

├── identificar resultado

├── comparar alternativas

├── mapear dependências

├── selecionar stack

├── reduzir operações manuais

└── definir gates

    │

    ▼

PREENCHER YAML CARD

│

├── contexto

├── arquitetura

├── recursos

├── operações

├── decisões

├── testes

├── persistência

└── handoff

    │

    ▼

EXECUTAR WORKFLOW

A regra central do schema é:

Cada operação deve possuir entrada, dependência, ação executável, recurso vinculado, destino, evidência, critério de aceite, tratamento de falha e próxima operação.