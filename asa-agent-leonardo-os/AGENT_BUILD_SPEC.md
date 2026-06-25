---
schema: LEO-AGENT-BUILD-SPEC-v1.0
document_type: agent_build_spec
title: "ASA Agent — Gerador do Leonardo-OS"
status: draft_for_build
owner: "Leonardo Batista"
product_owner: "Leonardo Batista"
created_at: "2026-06-25"
language: "pt-BR"
source_of_truth:
  primary:
    - "PRD — ASA Agent: Gerador do Leonardo-OS — LEO-PRD-ASA-v1"
    - "LEONARDO ADMIN OS — SYSTEM PROMPT — LEO-ADMIN-OS-SP-v1.0"
    - "ASA AGENTE BLUE PRINT.md"
  architectural_reference:
    - "Sakana Fugu Architecture adaptada ao ecossistema Claude"
target_environments:
  build: "Claude Code"
  runtime_v1: "Claude.ai Projects"
  future:
    - "Claude Code plugin"
    - "Agent SDK"
version: "1.0.0"
classification: internal
build_mode: scaffold_and_validate
external_action_requires_confirmation: true
never_invent_missing_data: true
---

# AGENT_BUILD_SPEC — ASA Agent: Gerador do Leonardo-OS

## 0. Instrução executiva ao Claude Code

Leia este documento integralmente como **contrato de construção**.

Sua função é transformar esta especificação em um pacote funcional, modular, validável e documentado para o **ASA Agent**, cujo ambiente operacional v1 é o Claude.ai.

Não produza apenas exemplos, recomendações ou pseudocódigo. Gere a estrutura de arquivos definida neste documento, preencha o conteúdo implementável, marque lacunas como `[GAP]`, execute validações locais possíveis e produza um relatório final de construção.

### Regra de precedência

Em caso de conflito, aplicar esta ordem:

```text
SEGURANÇA E GOVERNANÇA
        ↓
DECISÕES EXPLÍCITAS DE LEONARDO
        ↓
ESTE AGENT_BUILD_SPEC
        ↓
PRD LEO-PRD-ASA-v1
        ↓
SYSTEM PROMPT LEO-ADMIN-OS-SP-v1.0
        ↓
BLUEPRINT ASA AGENTE
        ↓
INFERÊNCIAS DE IMPLEMENTAÇÃO
```

Nunca substituir uma decisão explícita por inferência.

---

# 1. Identidade do projeto

| Campo | Valor |
|---|---|
| Nome do produto | ASA Agent — Gerador do Leonardo-OS |
| Nome operacional | ASA |
| Papel oficial | Agentic Systems Architect |
| Comando principal futuro | `/architect-agentic-system` |
| Comando alternativo | `/create-validate-agentic-system` |
| Owner | Leonardo Batista |
| ICP inicial | Leonardo Batista — ICP 0 |
| Build environment | Claude Code |
| Runtime v1 | Claude.ai Projects |
| Idioma | Português PT-BR |
| Código e nomes técnicos | Inglês permitido |
| Estado | Draft for Build |
| Restrição operacional | 25h/semana; 3 frentes; 1 workflow/dia; 1 entregável/dia |

---

# 2. Tese arquitetural

O ASA não será uma persona monolítica com todo o contexto de Leonardo incorporado.

O sistema será composto por:

```text
ASA RUNTIME V1
│
├── 1 agente orquestrador
│   └── ASA Orchestrator Agent
│
├── 3 Skills operacionais
│   ├── Leonardo Admin Skill
│   ├── ASA Admin Skill
│   └── DeskOS Skill
│
├── recursos sob demanda
│   ├── Project Knowledge
│   ├── Memory
│   ├── Connectors / MCP
│   ├── templates
│   ├── schemas
│   └── registros
│
└── 3 workflows convergentes
    ├── WF1 — Build
    ├── WF2 — Communicate
    └── WF3 — Operate
```

O **menor conjunto suficiente** deve ser ativado em cada tarefa.

### Separação build-time × runtime

```text
CLAUDE CODE — BUILD-TIME
│
├── analisa a especificação
├── gera arquivos
├── cria agentes auxiliares de construção
├── valida schemas
├── executa testes
└── empacota o produto
        │
        ▼
CLAUDE.AI — RUNTIME V1
│
├── recebe intenção
├── resolve ambiente e contexto
├── compõe especialista temporário
├── planeja 3 etapas visíveis
├── executa com Skills e conectores
├── valida
└── registra e encaminha ao DeskOS
```

Os subagentes de Claude Code definidos neste documento são **agentes de construção e auditoria**, não agentes obrigatórios do runtime v1.

---

# 3. Problema

Leonardo opera um ecossistema composto por Skills proprietárias, conectores, DESK-OS, memória, planilha master, projetos e workflows ponta a ponta, mas não possui um orquestrador que selecione e combine esses recursos de maneira adaptativa e rastreável.

## 3.1 Causas

- seleção manual de Skills;
- contexto fragmentado entre conversas;
- respostas generalistas;
- ausência de política explícita de roteamento;
- falta de registro da Skill escolhida, motivo e evidência;
- ausência de handoff consistente para DESK-OS e Recycle;
- sobreposição potencial entre Leonardo Admin Skill e ASA Admin Skill.

## 3.2 Efeitos

- retrabalho;
- reorganização manual de outputs;
- perda de contexto;
- inconsistência entre sessões;
- carga cognitiva elevada;
- dificuldade para transformar componentes em sistema operacional executável.

## 3.3 Job to Be Done

> Quando Leonardo apresentar uma tarefa, o ASA deve interpretar a intenção, selecionar o menor stack suficiente, compor o especialista temporário adequado, executar um workflow com três etapas visíveis, produzir um entregável verificável, registrar decisões e evidências e encaminhar o estado ao DESK-OS.

---

# 4. Goals

## G1 — Especialização dinâmica

Compor um especialista temporário por tarefa, contendo:

- role;
- goal;
- Skill principal;
- Skills auxiliares;
- contexto selecionado;
- ferramentas;
- conectores;
- método;
- critérios de qualidade;
- limites;
- stop conditions.

O especialista temporário existe apenas durante a execução atual.

## G2 — Zero reorganização manual

O output deve ser utilizável sem que Leonardo precise reinterpretar, corrigir ou reorganizar manualmente.

## G3 — Geração operacional do Leonardo-OS

Produzir e manter:

1. ASA Orchestrator Agent;
2. Leonardo Admin Skill;
3. ASA Admin Skill;
4. DeskOS Skill.

## G4 — Adaptação nativa do Fugu

Orquestrar recursos Claude, e não múltiplos modelos externos:

- Skills;
- Projects;
- Connectors;
- Memory;
- tools;
- artifacts;
- context.

## G5 — Governança rastreável

Registrar por execução:

- intenção classificada;
- workflow escolhido;
- Skill principal;
- Skills auxiliares;
- ferramentas;
- conectores;
- motivo da seleção;
- decisões;
- gates;
- evidências;
- resultado;
- próxima ação.

---

# 5. Non-Goals

- não implementar roteamento multi-modelo externo na v1;
- não criar mega-Skill monolítica;
- não substituir julgamento humano em gates críticos;
- não gravar conversas completas em memória;
- não executar ações externas irreversíveis sem confirmação;
- não implementar aplicação autônoma fora do Claude.ai na v1;
- não criar um subagente runtime para cada microetapa;
- não duplicar capacidades entre Skills;
- não afirmar suporte a recurso que o Environment Resolver não verificou.

---

# 6. Escopo da versão

## 6.1 Dentro do escopo

- arquitetura modular;
- agente orquestrador;
- três Skills;
- três workflows;
- contratos YAML;
- templates de execução;
- rastreabilidade;
- testes;
- evals;
- documentação;
- empacotamento;
- registro de gaps;
- rotinas A–E como especificação P1;
- separação fixed core × variable profile.

## 6.2 Fora do escopo imediato

- deploy em produção;
- gravação automática em conectores;
- criação de credenciais;
- instalação automática no Claude.ai;
- sincronização real com Planilha Master;
- QR router funcional;
- dashboard de observabilidade;
- chamadas para modelos externos;
- Agent SDK runtime.

---

# 7. Usuário principal

```yaml
user:
  name: Leonardo Batista
  role:
    - founder
    - product_owner
    - solo_worker
    - non_developer_power_user
    - low_code_builder
    - content_creator
  location: "Santos, São Paulo, Brasil"
  timezone: "America/Sao_Paulo"
  language: "pt-BR"
  capacity:
    weekly_hours: 25
    best_focus_window: "primeiras 3 horas da manhã"
    max_parallel_fronts: 3
    max_visible_workflow_steps: 3
    max_primary_deliverables_per_day: 1
  interaction_preferences:
    - plain_text_tree
    - tables
    - yaml_for_execution
    - mobile_first
    - no_horizontal_scroll
    - next_action_only
    - low_cognitive_load
```

---

# 8. Princípios de arquitetura

## P-01 — Menor arquitetura eficaz

```text
Tarefa simples
└── resposta direta ou 1 Skill

Tarefa especializada
└── 1 Skill + contexto selecionado

Tarefa composta
└── Planner + Skills + síntese

Tarefa crítica
└── Planner + execução + crítica + verificação + síntese

Tarefa aberta
└── decomposição adaptativa + gates humanos
```

## P-02 — Separar conhecimento de autonomia

- referência contém conhecimento;
- Skill contém procedimento;
- agente decide, delega e supervisiona;
- connector executa ação externa;
- schema controla estrutura;
- evaluator verifica qualidade.

## P-03 — Progressive disclosure

O usuário vê no máximo três etapas. O pipeline interno pode ser completo.

## P-04 — Contexto em cascata

Recuperar apenas o contexto necessário para a tarefa atual.

## P-05 — Transparência

O roteamento deve ser explicável e registrável.

## P-06 — Human-in-the-loop proporcional ao risco

Quanto maior o impacto, irreversibilidade ou incerteza, maior o nível de confirmação.

## P-07 — Evidência antes de conclusão

Arquivo criado não significa produto validado. Registro não significa execução confirmada.

---

# 9. Arquitetura lógica do runtime

```text
SOLICITAÇÃO
│
▼
ENVIRONMENT RESOLVER
│   ├── capacidades disponíveis
│   ├── Skills instaladas
│   ├── conectores
│   ├── permissões
│   └── gaps
│
▼
CONTEXT RESOLVER
│   └── cascata de contexto
│
▼
INTENT CLASSIFIER
│   ├── domínio
│   ├── caso de uso
│   ├── complexidade
│   └── risco
│
▼
SPECIALIST COMPOSER
│   ├── role
│   ├── goal
│   ├── skills
│   ├── tools
│   ├── method
│   └── quality criteria
│
▼
WORKFLOW PLANNER
│   ├── exatamente 3 etapas visíveis
│   ├── gates
│   ├── evidências
│   └── entregável
│
▼
EXECUTION ROUTER
│   ├── Leonardo Admin Skill
│   ├── ASA Admin Skill
│   ├── DeskOS Skill
│   ├── connectors
│   └── references
│
▼
QUALITY EVALUATOR
│
▼
STATE + TRACE REGISTRY
│
▼
HANDOFF
│   ├── output
│   ├── evidence
│   ├── DeskOS state
│   ├── Recycle
│   └── next action
```

---

# 10. Cascata de contexto

A especificação original declara “8 camadas”, mas enumera Constituição, Identidade, Ambiente, Projeto, Caso de Uso, Problema, Especialista Temporário, Workflow e Estado. Isso totaliza **9 camadas numeradas de 0 a 8**.

A implementação deve normalizar assim:

| Camada | Nome | Variabilidade |
|---:|---|---|
| 0 | Constituição | fixa |
| 1 | Identidade operacional | fixa |
| 2 | Ambiente | semiestável; verificar por sessão |
| 3 | Projeto | variável |
| 4 | Caso de uso | variável |
| 5 | Problema | variável |
| 6 | Especialista temporário | dinâmico |
| 7 | Workflow | dinâmico |
| 8 | Estado | dinâmico |

```yaml
context_resolution_order:
  - layer: 0
    id: constitution
  - layer: 1
    id: operational_identity
  - layer: 2
    id: environment
  - layer: 3
    id: project
  - layer: 4
    id: use_case
  - layer: 5
    id: problem
  - layer: 6
    id: temporary_specialist
  - layer: 7
    id: workflow
  - layer: 8
    id: state
```

---

# 11. Catálogo de componentes runtime

## 11.1 ASA Orchestrator Agent

### Identidade

```yaml
id: LEO-AGENT-ASA-ORCHESTRATOR-v1
name: ASA Orchestrator
type: runtime_agent
role: Agentic Systems Architect
status: required
```

### Role

Orquestrar operações ponta a ponta dentro do ecossistema Leonardo-OS, usando o menor stack suficiente e preservando rastreabilidade.

### Goal

Transformar qualquer solicitação de Leonardo em resultado executável, verificável e registrado, por meio de três etapas visíveis, gates e handoff.

### Responsabilidades

- resolver ambiente;
- resolver contexto;
- classificar intenção;
- selecionar workflow;
- compor especialista temporário;
- selecionar Skills;
- controlar ferramentas e conectores;
- aplicar gates;
- solicitar confirmação;
- avaliar output;
- registrar trace;
- preparar DeskOS handoff;
- encerrar ou pausar conforme stop conditions.

### Não responsabilidades

- armazenar toda biografia de Leonardo;
- incorporar conteúdo integral de todas as Skills;
- executar ação externa sem confirmação;
- substituir uma Skill especializada;
- fabricar dados;
- declarar teste não executado como aprovado.

### Inputs

```yaml
request:
  raw_input: ""
  workflow_type: ""
  project_uid: ""
  urgency: ""
  expected_output: ""

context:
  active_project: ""
  active_phase: ""
  previous_workflow_id: ""
  available_assets: []
  blockers: []

constraints:
  time_available: ""
  fronts_in_progress: 0
  tools_restricted: []

missing_data: []
```

### Outputs

```yaml
execution_result:
  workflow_id: ""
  workflow_type: ""
  current_stage: ""
  status: ""
  decision: ""
  temporary_specialist: {}
  selected_resources: []
  artifacts: []
  validation: []
  risks: []
  gaps: []
  evidence: []
  deskos_handoff: {}
  next_action: ""
```

---

## 11.2 Leonardo Admin Skill

```yaml
id: LEO-SKILL-LEONARDO-ADMIN-v1
name: Leonardo Admin
type: runtime_skill
status: required
```

### Fronteira de responsabilidade proposta

A Leonardo Admin Skill administra o **contexto operacional de Leonardo**.

### Deve conter

- identidade operacional;
- preferências;
- limites cognitivos;
- projetos ativos;
- regras de priorização;
- fonte de verdade;
- administração pessoal e empresarial;
- Daily Briefing;
- Week Open;
- Week Closing;
- decisões e handoffs humanos;
- interface de execução para Leonardo.

### Não deve conter

- engenharia de agentes;
- criação de Skills;
- arquitetura de plugins;
- testes técnicos de pacotes;
- política central de roteamento do ASA.

### Role

Especialista administrativo e operacional personalizado para Leonardo.

### Goal

Transformar contexto pessoal e empresarial em prioridades, decisões, rotinas e registros executáveis.

### Inputs

- estado semanal;
- agenda;
- projetos;
- pendências;
- capacidade;
- prioridades;
- decisões;
- status de workflows.

### Outputs

- briefing diário;
- abertura semanal;
- fechamento semanal;
- plano operacional;
- decisão administrativa;
- atualização estruturada para DeskOS.

---

## 11.3 ASA Admin Skill

```yaml
id: LEO-SKILL-ASA-ADMIN-v1
name: ASA Admin
type: runtime_skill
status: required
```

### Fronteira de responsabilidade proposta

A ASA Admin Skill administra o **sistema agêntico**, não a vida operacional de Leonardo.

### Deve conter

- requirements engineering;
- arquitetura de agentes;
- arquitetura de Skills;
- context engineering;
- component selection;
- workflow design;
- prompt engineering;
- tool/MCP mapping;
- permissions;
- evals;
- tests;
- packaging;
- versioning;
- gap detection;
- blueprint generation;
- refactoring;
- observability specification.

### Não deve conter

- agenda pessoal;
- briefing diário pessoal;
- rotina semanal de Leonardo;
- conteúdo físico do DeskOS;
- administração geral do negócio que não envolva o sistema agêntico.

### Role

Meta-Skill de engenharia, validação e evolução de sistemas agênticos.

### Goal

Criar, validar, empacotar e evoluir agentes, Skills, workflows, plugins e contratos com a menor arquitetura eficaz.

### Pipeline

```text
DIAGNOSTICAR
    ↓
ARQUITETAR
    ↓
DELEGAR
    ↓
EXECUTAR
    ↓
MONITORAR
    ↓
VALIDAR
    ↓
CORRIGIR
    ↓
EMPACOTAR
    ↓
EVOLUIR
```

---

## 11.4 DeskOS Skill

```yaml
id: LEO-SKILL-DESKOS-v1
name: DeskOS
type: runtime_skill
status: required
```

### Role

Adaptador entre o estado digital do Leonardo-OS e a interface físico-digital DESK-OS.

### Goal

Converter workflows, status, próxima ação e evidências em uma representação semanal de baixa carga cognitiva.

### Deve conter

- mapa semanal;
- workflow atual;
- três etapas;
- status;
- próxima ação;
- entregável;
- bloqueio;
- handoff;
- Recycle;
- contrato para geração física;
- contrato QR, inicialmente abstrato.

### Não deve conter

- política central de roteamento;
- criação de agentes;
- decisão arquitetural do ASA;
- escrita automática em sistemas externos sem aprovação.

---

# 12. Subagentes de construção no Claude Code

Estes agentes existem para construir e auditar o pacote. Não são parte obrigatória do runtime v1.

## 12.1 Build Architect

```yaml
name: asa-build-architect
purpose: converter o PRD e esta spec em arquitetura de arquivos
tools: [Read, Glob, Grep, Write, Edit]
permission_mode: plan_first
```

Responsabilidades:

- inventariar fontes;
- detectar conflitos;
- definir boundaries;
- produzir architecture decision records;
- gerar plano;
- impedir overengineering.

## 12.2 Skill Engineer

```yaml
name: asa-skill-engineer
purpose: criar as três Skills e seus recursos
tools: [Read, Glob, Grep, Write, Edit]
permission_mode: normal
```

Responsabilidades:

- criar SKILL.md;
- separar core de references;
- criar inputs/outputs;
- criar exemplos;
- criar failure handling;
- validar progressive disclosure.

## 12.3 Agent Engineer

```yaml
name: asa-agent-engineer
purpose: criar o ASA Orchestrator e os contratos de composição
tools: [Read, Glob, Grep, Write, Edit]
permission_mode: normal
```

Responsabilidades:

- criar prompt do agente;
- definir tools e Skills;
- implementar roteamento declarativo;
- criar specialist composer;
- criar stop conditions.

## 12.4 Quality and Governance Auditor

```yaml
name: asa-quality-governance-auditor
purpose: auditar segurança, consistência, testes e rastreabilidade
tools: [Read, Glob, Grep]
permission_mode: read_only
```

Responsabilidades:

- auditoria independente;
- anti-genericidade;
- segurança;
- validação de schemas;
- testes negativos;
- relatório PASS/FAIL;
- não corrigir silenciosamente o próprio trabalho auditado.

---

# 13. Workflows runtime

## 13.1 WF1 — BUILD

### Gatilhos

- criar;
- desenvolver;
- arquitetar;
- validar;
- refatorar;
- empacotar;
- gerar Skill;
- gerar agente;
- gerar workflow;
- gerar template;
- gerar produto.

### Interface visível

```text
1. DEFINIR
2. DESENVOLVER
3. ENTREGAR
```

### Etapa 1 — Definir

Internamente:

- capturar problema;
- recuperar contexto;
- identificar solução;
- verificar duplicação;
- delimitar escopo;
- criar briefing;
- definir critérios.

Gate:

```yaml
gate_id: WF1-G1
name: briefing_approved
pass_when:
  - problem_is_clear
  - user_is_defined
  - expected_output_is_defined
  - scope_is_bounded
  - resources_are_mapped
  - acceptance_criteria_exist
fail_when:
  - goal_is_generic
  - user_is_unknown
  - equivalent_solution_already_exists
  - critical_dependencies_are_missing
```

### Etapa 2 — Desenvolver

Internamente:

- projetar arquitetura;
- mapear dependências;
- recuperar referências;
- selecionar menor stack;
- construir arquivos;
- integrar;
- testar;
- corrigir;
- retestar.

Gate:

```yaml
gate_id: WF1-G2
name: component_validated
pass_when:
  - structure_is_complete
  - instructions_are_executable
  - critical_tests_pass
  - guardrails_are_active
  - dependencies_are_documented
  - original_problem_is_solved
```

### Etapa 3 — Entregar

Internamente:

- revisar;
- documentar;
- empacotar;
- salvar;
- registrar;
- comunicar;
- produzir handoff.

Gate:

```yaml
gate_id: WF1-G3
name: delivery_completed
pass_when:
  - final_package_exists
  - package_opens
  - version_is_registered
  - documentation_is_included
  - destination_is_accessible_or_marked_gap
  - handoff_exists
  - next_action_exists
```

---

## 13.2 WF2 — COMMUNICATE

### Interface visível

```text
1. EXTRAIR
2. PRODUZIR
3. PUBLICAR
```

### DoD

- caso documentável;
- narrativa validada;
- conteúdo final;
- publicação somente após confirmação;
- link ou destino registrado;
- métricas e feedback preparados.

---

## 13.3 WF3 — OPERATE

### Interface visível

```text
1. DISTRIBUIR
2. ANALISAR
3. RECICLAR
```

### DoD

- audiência e canal definidos;
- ação externa confirmada;
- respostas ou dados analisados;
- decisão tomada;
- backlog/memória/SOP atualizados conforme autorização;
- novo ciclo preparado.

---

# 14. Rotinas A–E

| ID | Rotina | Owner principal | Status v1 |
|---|---|---|---|
| A | Daily Briefing | Leonardo Admin Skill | especificar e testar |
| B | Week Open | Leonardo Admin + DeskOS | especificar e testar |
| C | Week Closing | Leonardo Admin + DeskOS | especificar e testar |
| D | Interview | ASA seleciona Skill adequada | nome sujeito a validação |
| E | Analytics | ASA + Skill analítica selecionada | especificar |

Cada rotina deve possuir:

- trigger;
- inputs;
- required_context;
- allowed_tools;
- confirmation_points;
- 3 visible steps;
- gates;
- output;
- evidence;
- failure behavior;
- state update;
- next action.

---

# 15. Intent Classifier

## 15.1 Taxonomia

```yaml
intent:
  domain:
    - build
    - communicate
    - operate
  use_case:
    - diagnose
    - research
    - plan
    - write
    - build
    - review
    - administer
    - custom
  complexity:
    - simple
    - compound
    - open
  risk:
    - low
    - medium
    - high
    - critical
```

## 15.2 Regras

```text
criação ou desenvolvimento
→ WF1

resultado validado que deve virar conteúdo
→ WF2

distribuição, análise, decisão ou reciclagem
→ WF3

tarefa simples sem especialização
→ resposta direta

padrão repetível
→ command ou Skill

contexto isolado / raciocínio especializado
→ Skill ou especialista temporário

ação externa
→ connector + confirmação

alto risco
→ gate humano obrigatório
```

## 15.3 Confidence

Até OQ-08 ser resolvida:

```yaml
autonomy_threshold:
  status: GAP
  temporary_policy:
    low_risk_and_reversible: may_proceed_with_explicit_assumptions
    medium_risk: confirm_if_material_ambiguity
    high_or_critical_risk: always_confirm
    external_write: always_confirm
```

---

# 16. Specialist Composer

## 16.1 Contrato

```yaml
temporary_specialist:
  id: ""
  task_id: ""
  role: ""
  goal: ""
  domain: ""
  use_case: ""
  primary_skill: ""
  auxiliary_skills: []
  references: []
  tools: []
  connectors: []
  method: []
  constraints: []
  quality_criteria: []
  guardrails: []
  stop_conditions: []
  rationale:
    selected_because: []
    rejected_alternatives: []
  lifetime: task_only
```

## 16.2 Regras

- nunca reutilizar sem adaptação um especialista de domínio diferente;
- nunca carregar todo o stack;
- selecionar uma Skill principal;
- adicionar auxiliares somente por dependência real;
- registrar por que cada recurso foi selecionado;
- registrar alternativas rejeitadas quando relevantes;
- destruir ou arquivar o especialista após a tarefa;
- converter em Skill permanente apenas se o padrão for reutilizável e aprovado.

---

# 17. Environment Resolver

O Environment Resolver deve verificar capacidades reais, nunca presumir.

## 17.1 Manifesto esperado

```yaml
environment_manifest:
  checked_at: ""
  runtime: ""
  account_plan: ""
  model:
    available: []
    selected: ""
  projects:
    available: null
  memory:
    available: null
    write_requires_confirmation: true
  skills:
    installed: []
  connectors:
    active: []
    unavailable: []
  artifacts:
    available: null
  permissions:
    external_write: confirmation_required
    destructive_action: confirmation_required
  gaps: []
```

## 17.2 Regra crítica

Capacidades descritas em documentos históricos devem ser consideradas **declarações não verificadas** até a inspeção do ambiente.

O build deve incluir um arquivo de compatibilidade para mapear capacidades confirmadas no momento da instalação.

---

# 18. Governança

## 18.1 Regras inegociáveis

```yaml
governance:
  never_invent_missing_data: true
  external_action_requires_confirmation: true
  distinguish_fact_hypothesis_gap: true
  never_claim_unverified_execution: true
  memory_write_requires_confirmation: true
  destructive_action_requires_confirmation: true
  least_privilege: true
  max_correction_attempts: 3
```

## 18.2 Labels epistemológicas

- `[FATO]`
- `[INFERÊNCIA]`
- `[HIPÓTESE]`
- `[GAP]`
- `[LACUNA]`

## 18.3 Confirmação obrigatória

- publicar;
- enviar;
- entregar a cliente;
- escrever em Linear;
- escrever em Drive;
- escrever em GitHub;
- escrever em Gmail;
- escrever em Notion;
- alterar memória;
- ação financeira;
- remoção;
- overwrite;
- deploy;
- operação irreversível.

---

# 19. Estado e rastreabilidade

## 19.1 Execution Trace

```yaml
execution_trace:
  execution_id: ""
  timestamp: ""
  user_request: ""
  environment_snapshot_id: ""
  context_layers_used: []
  intent:
    domain: ""
    use_case: ""
    complexity: ""
    risk: ""
    confidence: null
  workflow:
    id: ""
    stages: []
  specialist:
    id: ""
    role: ""
  resource_selection:
    primary_skill: ""
    auxiliary_skills: []
    tools: []
    connectors: []
    selection_rationale: []
  decisions: []
  approvals: []
  gates: []
  artifacts: []
  evidence: []
  gaps: []
  errors: []
  retries: []
  result_classification: ""
  deskos_handoff_id: ""
  next_action: ""
  final_status: ""
```

## 19.2 Classificação pós-execução

```yaml
result_classification:
  transient:
    destination: chat
  project_specific:
    destination: project_knowledge
  permanent_preference:
    destination: memory
    requires_confirmation: true
  reusable_procedure:
    destination: skill_backlog
    requires_validation: true
```

---

# 20. Contrato DeskOS

```yaml
deskos_handoff:
  handoff_id: ""
  date: ""
  workflow:
    id: ""
    name: ""
    stage:
      number: 1
      name: ""
  system_activity: ""
  user_action_required: ""
  next_gate: ""
  primary_deliverable: ""
  status: preparing
  blocker: ""
  evidence_refs: []
  recycle:
    classification: ""
    carry_forward: false
    notes: ""
```

Valores de status:

- preparing;
- executing;
- awaiting;
- validating;
- completed;
- blocked.

---

# 21. Output contract

Todo output runtime deve incluir:

```text
RESUMO
DECISÃO
ARTEFATOS
VALIDAÇÃO
RISCOS
PRÓXIMA AÇÃO
```

## 21.1 Interface mínima

```text
WORKFLOW    : [WF1 | WF2 | WF3] — nome
ETAPA ATUAL: [1 | 2 | 3] — nome
SISTEMA     : atividade atual
PRECISA     : ação de Leonardo ou "Nenhuma ação"
PRÓXIMO     : gate ou entregável
STATUS      : Preparando | Executando | Aguardando | Validando | Concluído | Bloqueado
```

## 21.2 Regra de usabilidade

Mostrar uma única próxima ação. Não apresentar backlog completo por padrão.

---

# 22. Quality Criteria

## 22.1 Anti-genericidade

Todo output deve responder “sim” a:

1. usa contexto específico de Leonardo?
2. considera projetos, stack e restrições?
3. mudaria materialmente para outro usuário?
4. explicita limites e gaps?
5. apresenta próxima ação específica?

Falha em qualquer item crítico implica reescrita.

## 22.2 Critérios técnicos

- correção;
- completude;
- segurança;
- consistência;
- executabilidade;
- rastreabilidade;
- modularidade;
- testabilidade;
- legibilidade;
- progressive disclosure;
- ausência de duplicação;
- boundaries claros.

## 22.3 Definition of Done funcional

```text
PEDIDO
  ↓
INTERPRETADO
  ↓
ROTEADO
  ↓
EXECUTADO EM 3 ETAPAS
  ↓
ENTREGÁVEL VERIFICÁVEL
  ↓
REGISTRADO
  ↓
DESKOS ATUALIZADO
  ↓
RECYCLE PREPARADO
```

---

# 23. Failure Handling

```text
DETECTAR
  ↓
CLASSIFICAR
  ↓
ESCOLHER AÇÃO
  ├── perguntar mínimo bloqueante
  ├── assumir explicitamente
  ├── usar fallback
  ├── corrigir
  ├── retestar
  ├── escalar
  └── abortar
  ↓
REGISTRAR
```

| Falha | Ação |
|---|---|
| dado crítico ausente | perguntar mínimo necessário |
| dado não crítico ausente | marcar GAP e prosseguir com suposição explícita |
| conflito de fontes | exibir conflito e aplicar precedência ou pedir decisão |
| ferramenta indisponível | fallback manual ou bloquear |
| gate falhou | corrigir e retestar, máximo 3 |
| risco crítico | parar imediatamente |
| baixa confiança | declarar inferência e confirmar conforme risco |
| loop | parar no limite e escalar |
| ação externa não aprovada | não executar |

---

# 24. Open Questions e decisões provisórias

| ID | Questão | Bloqueante | Decisão provisória |
|---|---|---:|---|
| OQ-01 | Funções dos Commands 01–03 | sim | criar placeholders sem inventar função |
| OQ-02 | UID Leonardo S × Leonardo Admin | sim | tratar Leonardo Admin como nome canônico; preservar alias em registry |
| OQ-03 | Interview é nome oficial? | não | manter `Interview` com status provisional |
| OQ-04 | Dois plugins Design | não | marcar possível duplicação |
| OQ-05 | Campos graváveis na Planilha Master | sim | toda escrita requer confirmação; leitura permitida |
| OQ-06 | Fronteiras Leonardo Admin × ASA Admin | sim | aplicar boundaries desta spec |
| OQ-07 | QR DeskOS antes/depois da v1 | não | implementar contrato abstrato, não resolver QR |
| OQ-08 | Threshold de autonomia | sim | aplicar policy provisória baseada em risco |

Nenhuma OQ bloqueante deve impedir a criação da arquitetura e dos arquivos. Deve impedir apenas afirmações de completude nos componentes afetados.

---

# 25. Arquivos que o Claude Code deve gerar

```text
asa-agent-leonardo-os/
│
├── AGENT_BUILD_SPEC.md
├── CLAUDE.md
├── README.md
├── CHANGELOG.md
├── BUILD_REPORT.md
├── GAP_REGISTER.md
├── DECISION_LOG.md
├── SECURITY.md
├── LICENSE_POLICY.md
│
├── .claude/
│   ├── agents/
│   │   ├── asa-orchestrator.md
│   │   ├── asa-build-architect.md
│   │   ├── asa-agent-engineer.md
│   │   ├── asa-skill-engineer.md
│   │   └── asa-quality-governance-auditor.md
│   │
│   ├── skills/
│   │   ├── leonardo-admin/
│   │   │   ├── SKILL.md
│   │   │   ├── README.md
│   │   │   ├── references/
│   │   │   ├── templates/
│   │   │   └── tests/
│   │   │
│   │   ├── asa-admin/
│   │   │   ├── SKILL.md
│   │   │   ├── README.md
│   │   │   ├── references/
│   │   │   ├── templates/
│   │   │   └── tests/
│   │   │
│   │   └── deskos/
│   │       ├── SKILL.md
│   │       ├── README.md
│   │       ├── references/
│   │       ├── templates/
│   │       └── tests/
│   │
│   ├── commands/
│   │   ├── architect-agentic-system.md
│   │   ├── create-validate-agentic-system.md
│   │   ├── wf1-build.md
│   │   ├── wf2-communicate.md
│   │   └── wf3-operate.md
│   │
│   ├── hooks/
│   │   └── README.md
│   │
│   └── settings.example.json
│
├── config/
│   ├── environment-capabilities.yaml
│   ├── governance.yaml
│   ├── routing-policy.yaml
│   ├── autonomy-policy.yaml
│   ├── memory-policy.yaml
│   └── source-precedence.yaml
│
├── schemas/
│   ├── request.schema.yaml
│   ├── context.schema.yaml
│   ├── environment-manifest.schema.yaml
│   ├── intent.schema.yaml
│   ├── temporary-specialist.schema.yaml
│   ├── workflow-plan.schema.yaml
│   ├── execution-trace.schema.yaml
│   ├── deskos-handoff.schema.yaml
│   ├── quality-report.schema.yaml
│   └── blueprint.schema.yaml
│
├── workflows/
│   ├── WF1_BUILD.md
│   ├── WF2_COMMUNICATE.md
│   ├── WF3_OPERATE.md
│   └── routines/
│       ├── A_DAILY_BRIEFING.md
│       ├── B_WEEK_OPEN.md
│       ├── C_WEEK_CLOSING.md
│       ├── D_INTERVIEW.md
│       └── E_ANALYTICS.md
│
├── blueprints/
│   ├── ASA_ORCHESTRATOR_AGENT.md
│   ├── LEONARDO_ADMIN_SKILL.md
│   ├── ASA_ADMIN_SKILL.md
│   └── DESKOS_SKILL.md
│
├── templates/
│   ├── agent-template.md
│   ├── skill-template.md
│   ├── workflow-template.md
│   ├── specialist-composition.yaml
│   ├── execution-output.md
│   ├── decision-record.md
│   ├── handoff.md
│   └── gap-record.md
│
├── references/
│   ├── PRD_LEO_PRD_ASA_v1.md
│   ├── LEONARDO_ADMIN_OS_SYSTEM_PROMPT.md
│   ├── ASA_AGENT_BLUEPRINT_SOURCE.md
│   ├── taxonomy.md
│   ├── glossary.md
│   └── source-map.yaml
│
├── registries/
│   ├── agent-registry.yaml
│   ├── skill-registry.yaml
│   ├── command-registry.yaml
│   ├── connector-registry.yaml
│   ├── project-registry.yaml
│   └── alias-registry.yaml
│
├── evals/
│   ├── intent-classification.yaml
│   ├── routing.yaml
│   ├── anti-genericity.yaml
│   ├── safety.yaml
│   ├── specialist-composition.yaml
│   ├── workflow-three-steps.yaml
│   └── traceability.yaml
│
├── tests/
│   ├── happy-path/
│   ├── incomplete-input/
│   ├── ambiguous-input/
│   ├── unavailable-tool/
│   ├── external-action/
│   ├── conflicting-sources/
│   ├── high-risk/
│   └── regression/
│
├── scripts/
│   ├── validate_structure.py
│   ├── validate_yaml.py
│   ├── validate_links.py
│   ├── validate_frontmatter.py
│   ├── scan_secrets.py
│   ├── run_evals.py
│   └── build_package.py
│
└── dist/
    └── .gitkeep
```

---

# 26. Conteúdo obrigatório do CLAUDE.md

O `CLAUDE.md` deve instruir Claude Code a:

- ler este spec;
- preservar source files;
- operar plan-first;
- não inventar;
- usar menor arquitetura;
- separar runtime e build-time;
- manter boundaries;
- não executar ações externas;
- validar antes de concluir;
- registrar gaps;
- executar scripts;
- gerar BUILD_REPORT;
- não marcar P0 como completo quando OQ bloqueante impedir validação;
- não criar credenciais;
- não hardcode secrets;
- não ocultar falhas.

---

# 27. Requisitos dos arquivos de agentes

Cada `.claude/agents/*.md` deve conter frontmatter compatível com a versão instalada do Claude Code e, no corpo:

- identity;
- role;
- goal;
- scope;
- inputs;
- outputs;
- allowed tools;
- denied actions;
- workflow;
- decision rules;
- quality criteria;
- guardrails;
- failure handling;
- stop conditions;
- examples;
- handoff contract.

O build deve consultar a documentação local/atual antes de assumir campos de frontmatter.

---

# 28. Requisitos das Skills

Cada Skill deve:

- ter função única e boundary explícito;
- possuir `SKILL.md`;
- manter o núcleo conciso;
- mover conteúdo extenso para `references/`;
- incluir templates;
- incluir exemplos Do/Don’t;
- incluir testes;
- declarar dependências;
- declarar tools;
- declarar approval points;
- declarar outputs;
- declarar stop conditions;
- evitar contexto oculto;
- ser utilizável isoladamente quando aplicável.

---

# 29. Test Plan

## 29.1 Happy path

1. “Crie uma Skill para diagnosticar uma PME.”
2. “Transforme o produto validado em case.”
3. “Analise o feedback e decida o próximo ciclo.”
4. “Abra minha semana com base nos três projetos ativos.”
5. “Gere o handoff para o DeskOS.”

## 29.2 Input incompleto

- pedido sem expected_output;
- project UID ausente;
- ativo referenciado inexistente;
- prazo ausente;
- ferramenta citada não disponível.

## 29.3 Ambiguidade

- “organize isso”;
- “crie o agente”;
- “publique” sem canal;
- “atualize a planilha” sem campos.

## 29.4 Safety

- escrever em GitHub sem confirmação;
- enviar Gmail sem confirmação;
- apagar arquivo;
- sobrescrever registro;
- persistir memória;
- manipular credenciais;
- declarar deploy inexistente.

## 29.5 Anti-genericidade

Comparar outputs para:

- Leonardo;
- professor;
- advogado;
- PME genérica.

O output de Leonardo deve mudar materialmente.

## 29.6 Routing

Target inicial:

```yaml
intent_classification_accuracy:
  target: 0.90
  sample_minimum: 30
```

## 29.7 Three-step constraint

Todos os workflows apresentados ao usuário devem possuir exatamente três etapas visíveis.

---

# 30. Success Metrics

## Leading

| Métrica | Target |
|---|---:|
| reorganização manual por sessão | 0 |
| outputs genéricos | <10% |
| P0 gates registrados | 100% |
| workflows com 3 etapas visíveis | 100% |
| intenção classificada | ≤1 turno |
| execução com trace | 100% |

## Lagging

| Métrica | Target |
|---|---|
| tarefa real sem reinterpretação | semana 1 |
| 4 blueprints validados | mês 1 |
| template para outro ICP | mês 2–3 |
| novas Skills via ASA | ≥3 no mês 2 |

---

# 31. Sequência de construção

## Fase 1 — Inventário e normalização

- copiar fontes para `references/`;
- criar source map;
- registrar aliases;
- registrar OQs;
- detectar duplicações;
- produzir ADR boundaries.

## Fase 2 — Blueprints

- ASA Orchestrator;
- Leonardo Admin;
- ASA Admin;
- DeskOS.

## Fase 3 — Schemas e policies

- request;
- environment;
- intent;
- specialist;
- workflow;
- trace;
- handoff;
- governance;
- autonomy.

## Fase 4 — Implementação Claude Code

- agentes build-time;
- agente runtime;
- Skills;
- commands;
- templates;
- registries.

## Fase 5 — Testes e evals

- happy path;
- negative;
- safety;
- routing;
- anti-genericity;
- traceability.

## Fase 6 — Package

- README;
- changelog;
- build report;
- package;
- checksum;
- dist.

---

# 32. Gates de construção

## BUILD-G1 — Sources normalized

PASS:

- fontes preservadas;
- source map criado;
- conflicts registrados;
- OQs registradas.

## BUILD-G2 — Architecture approved by spec

PASS:

- boundaries explícitos;
- um agente runtime;
- três Skills;
- subagentes apenas build-time;
- fixed core separado de variable profile.

## BUILD-G3 — Components generated

PASS:

- arquivos obrigatórios existem;
- schemas válidos;
- links internos válidos;
- frontmatter válido.

## BUILD-G4 — Tests passed

PASS:

- safety;
- routing;
- 3 steps;
- anti-genericity;
- traceability.

## BUILD-G5 — Package ready

PASS:

- README completo;
- build report;
- gap register;
- nenhum secret;
- pacote abre;
- checksum gerado.

---

# 33. Build instructions para Claude Code

```text
1. Leia AGENT_BUILD_SPEC.md e todas as fontes em references/.
2. Inventarie arquivos e preserve originais.
3. Crie GAP_REGISTER.md e DECISION_LOG.md antes de construir.
4. Verifique a versão e os recursos reais do Claude Code.
5. Gere a árvore de diretórios.
6. Crie CLAUDE.md.
7. Crie os quatro blueprints.
8. Crie os agentes build-time.
9. Crie o ASA Orchestrator.
10. Crie as três Skills.
11. Crie schemas, policies, registries e templates.
12. Crie workflows e rotinas.
13. Crie testes e evals.
14. Crie scripts de validação.
15. Execute validações possíveis localmente.
16. Corrija falhas, no máximo três ciclos por gate.
17. Gere BUILD_REPORT.md com PASS, FAIL, GAP e evidências.
18. Empacote somente quando BUILD-G1 a BUILD-G5 permitirem.
```

### Regra de não bloqueio

Não peça esclarecimentos antes de gerar a arquitetura quando a informação ausente puder ser representada por `[GAP]`.

Pergunte ou pare somente quando:

- a ausência impedir uma decisão segura;
- houver ação externa;
- houver conflito crítico sem precedência;
- houver risco irreversível;
- a implementação exigiria inventar capacidade.

---

# 34. Required BUILD_REPORT

```yaml
build_report:
  build_id: ""
  generated_at: ""
  environment:
    claude_code_version: ""
    capabilities_verified: []
  files:
    expected: 0
    created: 0
    missing: []
  gates:
    BUILD_G1: ""
    BUILD_G2: ""
    BUILD_G3: ""
    BUILD_G4: ""
    BUILD_G5: ""
  tests:
    passed: []
    failed: []
    skipped: []
  gaps: []
  risks: []
  security_scan: ""
  package:
    path: ""
    checksum: ""
  next_action: ""
```

---

# 35. Fixed core × variable profile

## Fixed core

- governança;
- context cascade;
- intent classifier;
- specialist composer;
- workflow planner;
- 3-step interface;
- gates;
- trace;
- quality evaluator;
- failure handling;
- stop conditions;
- source precedence.

## Variable profile

- identidade;
- empresa;
- projetos;
- prioridades;
- Skills instaladas;
- connectors;
- rotinas;
- vocabulário;
- DeskOS layout;
- memória;
- UIDs;
- autonomia autorizada.

Estrutura futura:

```text
core/
└── universal ASA

profiles/
├── leonardo/
└── future-icp/
```

---

# 36. Riscos

| ID | Risco | Mitigação |
|---|---|---|
| R-01 | mega-Skill | boundaries e references |
| R-02 | excesso de subagentes | um agente runtime |
| R-03 | duplicação Leonardo/ASA Admin | fronteiras desta spec |
| R-04 | capacidade Claude presumida | Environment Resolver |
| R-05 | escrita externa indevida | confirmation gate |
| R-06 | output genérico | anti-genericity eval |
| R-07 | trace excessivo | schema conciso e IDs |
| R-08 | carga cognitiva | 3 etapas e 1 próxima ação |
| R-09 | OQs bloqueantes | GAP register |
| R-10 | spec desatualizada | capability compatibility layer |

---

# 37. Stop Conditions do build

## Concluir quando

- estrutura gerada;
- quatro blueprints criados;
- um agente runtime criado;
- três Skills criadas;
- subagentes build-time criados;
- schemas válidos;
- testes críticos executados;
- gaps documentados;
- build report criado;
- pacote produzido ou bloqueio explicitado.

## Pausar quando

- ação externa for necessária;
- ferramenta exigir credencial;
- risco crítico;
- conflito sem precedência;
- três tentativas falharem.

## Abortar quando

- houver risco de exposição de segredo;
- fonte estiver corrompida sem backup;
- Leonardo solicitar parada;
- build exigir capacidade inexistente sem fallback.

---

# 38. Definition of Done do AGENT_BUILD_SPEC

Este documento é considerado implementado quando:

- os quatro blueprints existem;
- o ASA executa ao menos um caso real em teste;
- o roteamento é registrado;
- o especialista temporário é composto;
- três etapas são apresentadas;
- um entregável é produzido;
- gates são avaliados;
- evidence trace é criado;
- DeskOS handoff é gerado;
- gaps bloqueantes continuam explícitos;
- nenhuma ação externa ocorre sem confirmação.

---

# 39. Próxima ação do Claude Code

```text
Executar a Fase 1 — Inventário e Normalização.

Saída obrigatória:
1. SOURCE_MAP;
2. GAP_REGISTER;
3. DECISION_LOG inicial;
4. árvore de arquivos;
5. Architecture Boundary Record;
6. plano de geração dos quatro blueprints.
```

Não iniciar integração externa. Não criar credenciais. Não realizar deploy.

---

# Apêndice A — Taxonomia funcional do ASA

## Funções

- requirements engineering;
- knowledge architecture;
- interface architecture;
- agentic architecture;
- component selection;
- workflow architecture;
- orchestration and supervision;
- context engineering;
- prompt engineering;
- Skill engineering;
- plugin architecture;
- tool and MCP engineering;
- governance and permissions;
- security and safety;
- validation and evaluation;
- packaging and distribution;
- observability;
- lifecycle evolution.

## Especialidades

- multi-agent system design;
- Claude Code;
- Claude.ai;
- Skills;
- subagents;
- plugins;
- hooks;
- MCP;
- progressive disclosure;
- human-in-the-loop;
- least privilege;
- context isolation;
- semantic tagging;
- version control;
- test-driven decomposition;
- agent evaluation;
- failure recovery.

## Capacidades

```text
diagnosticar
→ arquitetar
→ selecionar
→ decompor
→ delegar
→ construir
→ integrar
→ validar
→ corrigir
→ empacotar
→ registrar
→ monitorar
→ evoluir
```

---

# Apêndice B — Comando de bootstrap

```text
Leia integralmente o AGENT_BUILD_SPEC.md.

Trate-o como contrato de construção do ASA Agent — Gerador do Leonardo-OS.

Execute primeiro a Fase 1:
- inventário;
- normalização;
- source map;
- gap register;
- decision log;
- architecture boundaries;
- plano dos quatro blueprints.

Depois gere todos os arquivos definidos na árvore obrigatória.

Regras:
- preserve as fontes;
- não invente dados;
- não execute ações externas;
- não crie credenciais;
- não use mais componentes do que o necessário;
- diferencie runtime v1 de build-time;
- use um agente runtime e três Skills;
- marque toda lacuna como [GAP];
- valide antes de concluir;
- produza BUILD_REPORT.md;
- pare no primeiro gate crítico.
```
