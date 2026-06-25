# FOLLOW-UP REPORT — ASA Agent / Gerador do Leonardo-OS

**Schema:** `LEO-BUILD-FOLLOWUP-v2.0`  
**Build acompanhado:** `ASA-BUILD-2026-06-25-v1.0.0`  
**Follow-up ID:** `ASA-FOLLOWUP-2026-06-25-v2.0.0`  
**Fonte de verdade:** `MASTER_PROJECT_ADMIN.xlsx`  
**Fontes de suporte:** `README_ARCHITECTURE.md`, `VALIDATION_REPORT.md`, `AUDIT_REPORT.md`  
**Data-base:** 25 de junho de 2026  
**Owner:** Leonardo Batista  
**Estado proposto:** `READY_FOR_CONTROLLED_RUNTIME_VALIDATION`

> Regra de honestidade: este relatório encerra pendências documentais apenas quando há evidência no workbook. Pendências de instalação, permissões, execução real, conectores e QR permanecem como testes de runtime.

```yaml
build_followup:
  id: ASA-FOLLOWUP-2026-06-25-v2.0.0
  parent_build: ASA-BUILD-2026-06-25-v1.0.0
  source_of_truth: MASTER_PROJECT_ADMIN.xlsx
  source_scope:
    physical_files: 56
    source_documents: 54
    excluded_index_artifacts: 2
    workbooks: 8
    workbook_sheets_extracted: 97
    items_master: 163
    programs: 6
    products: 7
    strategic_entities: 22
    decisions: 13
    gaps: 9
    validation_gates: 10
  embedded_runtime_catalog:
    proprietary_skills: 10
    declared_plugins: 1
    core_agents: 5
    canonical_workflows: 9
    canonical_command_routes: 11
  status:
    documentary_governance: PASS
    local_build: PASS
    runtime_validation: PENDING
```


# 1. Executive Summary


O workbook consolidou a administração do ecossistema Leonardo em 23 abas e transformou 54 documentos-fonte e 97 abas de oito workbooks em um registro operacional único. O inventário contém **163 itens**: **37 CONFIRMED**, **109 PROPOSED** e **17 REVIEW_REQUIRED**. A documentação está classificada em **147 PRESENT**, **4 PARTIAL** e **12 MISSING**.

O follow-up confirma a arquitetura de programas irmãos, mantém o `MASTER_PROJECT_ADMIN.xlsx` como SSOT administrativo, extrai o stack proprietário completo e converte lacunas em quatro classes:

1. **Resolvida por evidência:** já há fonte, decisão ou classificação suficiente.
2. **Resolvida por política:** o relatório formaliza boundary, write policy ou autonomia.
3. **Parcialmente resolvida:** o conceito está definido, mas falta documento dedicado.
4. **Runtime obrigatório:** somente instalação/teste no Claude.ai ou integração real pode encerrar.

**Decisão executiva:** o pacote está pronto para uma validação controlada de runtime, mas não para declarar produção. O próximo gate real é importar o orquestrador e as skills, executar o Environment Resolver e validar um caso de ponta a ponta.


# 2. Project Snapshot e Delta do Build

| Campo | Valor |
| --- | --- |
| Projeto | PROJECT-LEONARDO-ECOSYSTEM |
| Build pai | ASA-BUILD-2026-06-25-v1.0.0 |
| Follow-up | ASA-FOLLOWUP-2026-06-25-v2.0.0 |
| Fase | Pós-Gate 0 / Materialização |
| Programa prioritário | PROGRAM-DESK-OS |
| Produto prioritário | PRODUCT-DESK-OS |
| Estado documental | PASS |
| Estado do build local | PASS |
| Estado do runtime | PENDING |
| Próxima decisão | Executar validação real do Claude.ai sem alterar a SSOT |

**Delta frente ao BUILD_REPORT original**

- O catálogo proprietário foi extraído da SSOT `LEONARDO_MACRO_PERSONALIZATION___PROPRIETARY_SKILL_STACK.md`.
- O boundary OS Partner Admin × Leonardo Orchestrator foi confirmado.
- O plugin Small Business foi separado das skills e recebeu gate de disponibilidade.
- As OQs foram reconciliadas em resolução, política provisória ou teste de runtime.
- As nove lacunas do workbook receberam decisão de tratamento e critério de fechamento.
- O report passa a ter rastreabilidade por aba, arquivo, hash, item e entidade.


# 3. Inventário Consolidado

| Objeto | Quantidade | Evidência |
| --- | --- | --- |
| Arquivos físicos | 56 | 06_FILE_INDEX |
| Documentos-fonte em escopo | 54 | 06_FILE_INDEX |
| Artefatos de índice excluídos | 2 | 06_FILE_INDEX |
| Workbooks processados | 8 | AUDIT_REPORT / 06_FILE_INDEX |
| Abas extraídas | 97 | 22_VALIDATION V2 |
| Itens no ITEMS_MASTER | 163 | 05_ITEMS_MASTER |
| File roots | 54 | 05_ITEMS_MASTER |
| Sheet items | 97 | 05_ITEMS_MASTER |
| Itens de contexto fornecido | 12 | 05_ITEMS_MASTER |
| Programas | 6 | 03_PROGRAMS |
| Produtos | 7 | 04_PRODUCTS |
| Entidades estratégicas | 22 | 19_STRATEGIC_ENTITIES |
| Decisões | 13 | 17_DECISIONS |
| Lacunas | 9 | 18_GAPS_REVIEW |

**Distribuição dos 163 itens por autoridade**

| Authority | Quantidade |
| --- | --- |
| APPROVED | 1 |
| DRAFT | 14 |
| DUPLICATE_COPY | 1 |
| REFERENCE | 5 |
| SSOT | 1 |
| SUPERSEDED | 11 |
| WORKING | 130 |

**Distribuição por cluster**

| Cluster | Quantidade |
| --- | --- |
| C01 | 3 |
| C02 | 11 |
| C03 | 5 |
| C04 | 54 |
| C05 | 11 |
| C06 | 11 |
| C07 | 8 |
| C08 | 5 |
| C09 | 24 |
| C10 | 6 |
| C11 | 10 |
| C12 | 15 |

# 4. Programs

| ID | Programa | Produtos | Autoridade | Classificação | Escopo |
| --- | --- | --- | --- | --- | --- |
| PRG-ASA | PROGRAM-ASA | PRODUCT-ASA | CONFIRMED | CONFIRMED | Arquitetura de sistemas agenticos, orquestracao, agentes, avaliacao, first principles. |
| PRG-TDAH | PROGRAM-TDAH | PRODUCT-TDAH-OS, PRODUCT-COPILOTO-TDAH | CONFIRMED | CONFIRMED | Sistemas operacionais cognitivos neuroinclusivos para ICP TDAH. |
| PRG-DESK-OS | PROGRAM-DESK-OS | PRODUCT-DESK-OS | CONFIRMED | CONFIRMED | Sistema fisico-digital A4, workflows, QR contextual, produto comercial. |
| PRG-LEONARDO-OS | PROGRAM-LEONARDO-OS | PRODUCT-LEONARDO-OS | CONFIRMED | CONFIRMED | Sistema operacional pessoal e empresarial; stack proprietario de skills; orquestrador. |
| PRG-EDUCATION | PROGRAM-EDUCATION | PRODUCT-COURSE-EXPRESS | DRAFT | PROPOSED | Programa de educacao; Course Express e trilhas. Inserido como proposto. |
| PRG-SMALL-BUSINESS | PROGRAM-SMALL-BUSINESS | PRODUCT-BUSINESS-SUITE | DRAFT | PROPOSED | Programa Small Business; Business Suite, GTM Showroom, Agency Kit. Inserido como proposto. |

**Decisão de governança:** ASA, TDAH, DESK-OS e Leonardo-OS são programas confirmados. Education e Small Business permanecem programas propostos, pois foram introduzidos por contexto fornecido e não possuem corpus dedicado suficiente. Leonardo-OS é programa irmão, não raiz hierárquica.


# 5. Products

| ID | Produto | Programa | Autoridade | Classificação | Documentação | Escopo |
| --- | --- | --- | --- | --- | --- | --- |
| PRD-ASA | PRODUCT-ASA | PRG-ASA | WORKING | CONFIRMED | PARTIAL | Arquitetura, metodos e ativos agenticos. |
| PRD-TDAH-OS | PRODUCT-TDAH-OS | PRG-TDAH | WORKING | CONFIRMED | PARTIAL | Sistema operacional cognitivo, 1 workflow/dia, 3 etapas, ICP TDAH. |
| PRD-COPILOTO-TDAH | PRODUCT-COPILOTO-TDAH | PRG-TDAH | WORKING | CONFIRMED | PARTIAL | Copiloto operacional, ciclos de 72h, proxima acao, evidencias. |
| PRD-DESK-OS | PRODUCT-DESK-OS | PRG-DESK-OS | WORKING | CONFIRMED | PRESENT | Produto autonomo comercializavel fisico-digital. |
| PRD-LEONARDO-OS | PRODUCT-LEONARDO-OS | PRG-LEONARDO-OS | WORKING | CONFIRMED | PARTIAL | Operacao pessoal de Leonardo; integra DESK-OS, ASA e macro-personalizacao. |
| PRD-COURSE-EXPRESS | PRODUCT-COURSE-EXPRESS | PRG-EDUCATION | DRAFT | PROPOSED | EMBEDDED | Curso; trilhas TDAH, Macro, Anthropic Stack, Claude Power User. Sem arquivo proprio. |
| PRD-BUSINESS-SUITE | PRODUCT-BUSINESS-SUITE | PRG-SMALL-BUSINESS | DRAFT | PROPOSED | PARTIAL | Suite para PMEs; modulos M1, M2, M5. Maturidade a validar. |

**Cobertura documental calculada a partir da matriz 07_PRODUCT_DOCUMENTS**

| Produto | PRESENT | PARTIAL | EMBEDDED | MISSING |
| --- | --- | --- | --- | --- |
| PRD-ASA | 4 | 6 | 2 | 0 |
| PRD-TDAH-OS | 0 | 4 | 8 | 0 |
| PRD-COPILOTO-TDAH | 5 | 0 | 6 | 1 |
| PRD-DESK-OS | 10 | 2 | 0 | 0 |
| PRD-LEONARDO-OS | 1 | 5 | 6 | 0 |
| PRD-COURSE-EXPRESS | 0 | 0 | 1 | 11 |
| PRD-BUSINESS-SUITE | 1 | 5 | 1 | 5 |

**Conclusão:** DESK-OS é o produto documentalmente mais completo. Course Express e Business Suite concentram os maiores déficits e não devem avançar para build de produção antes de Charter + Vision + BRD/MRD/PRD mínimos.


# 6. Skills Catalog

O stack canônico contém **10 skills proprietárias**. Fonte: `FILE-025`, autoridade `SSOT`.

| Skill ID | Nome canônico | Prioridade | Camada | Status | Função | Triggers principais | Outputs | Boundary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SKILL-SETUP-OS | setup-os | P0 | onboarding_and_system_configuration | core | FAQ, intake, diagnóstico 3PN, clusterização de perfil, construção de stack, criação de especialista e Prisma operacional. | /3E; /status; /prisma; /stack; onboarding; configurar meu sistema; criar meu perfil; personalizar Claude; IA para meu negócio | intake record; diagnóstico 3PN; cluster de perfil; stack recomendada; spec de agente especialista; Prisma operacional | Não gerar perfil genérico, não expor complexidade desnecessária e não ativar todas as skills por padrão. |
| SKILL-OS-PARTNER-ADMIN | OS-PARTNER-ADMIN | P0 | account_and_project_administration | core | Administra conta/projeto Claude.ai, onboarding, macro-personalização, IDs verbais, agentes, workflows, documentação, DESK-OS, validação e release. | /iniciar; /bom-dia; /status; /proximas-3; /fechar-dia; /bmc-wide-search; /package-release | estrutura de projeto; suíte de agentes; suíte de workflows; BRD/MRD/PRD; GTM pack; runbook; print pack; release validada | Plano de controle administrativo; não substitui o controle canônico de estado do Leonardo-OS. |
| SKILL-LEONARDO-ORCHESTRATOR | leonardo-os-orchestrator | P0 | project_state_and_execution_orchestration | core | Carrega corpus canônico, roteia intenção, controla fases, gates, decisões, documentos, trackers e ciclo das próximas três tarefas. | /day-zero; /gate-zero; /next-3-tasks; /build-doc; /decision-check; /update-tracker; /claims-check; /editorial-week; /export-package | fase atual; gate atual; decisões; próximas três tarefas; documento gerado; tracker atualizado; pacote exportável | Controla estado do projeto; OS Partner Admin controla conta, documentação, arquitetura e negócio. |
| SKILL-STANDALONE-ORCHESTRATOR-TEMPLATE | standalone-orchestrator-template | P2 | reusable_orchestrator_blueprint | factory_reference | Blueprint reutilizável para transformar corpus canônico em orquestrador standalone com fases, gates, decisões, trackers e loop de tarefas. | /day-zero; /gate-zero; /next-3-tasks; /build-doc; /decision-check; /score-portfolio; /export-package | skill orquestradora standalone | Usar para criar novo orquestrador; não invocar na execução ordinária do Leonardo-OS. |
| SKILL-COGNITIVE-TRIGGER | cognitive-framework-router | P0 | reasoning_and_information_structure | core_cross_cutting | Seleciona a combinação mínima de frameworks cognitivos, negócio, produto, estratégia, operações, educação e comunicação. | pesquisa; decisão; planejamento; diagnóstico; priorização; resumo executivo; MECE; Cynefin; JTBD; 5W2H; SCQA; working backwards; causa e efeito | frameworks selecionados; plano de raciocínio; blueprint de resposta; briefing working backwards | Roda antes de fluxos analíticos complexos; não substitui a skill de domínio. |
| SKILL-AGENTIC-PROBLEM-SOLVING | agentic-problem-solving | P0 | complex_problem_resolution | core | Enquadra, cria estratégia, organiza conhecimento, aloca recursos, executa, monitora e avalia problemas ambíguos ou complexos. | /problema intake; definir; classificar; estratégia; conhecimento; recursos; executar; monitorar; avaliar; status; escalar | problem statement; mapa de evidências; estratégia; plano de execução; estado de progresso; relatório de avaliação | Definir o problema antes da solução, separar fato/hipótese/inferência/lacuna e exigir aprovação humana em alto risco. |
| SKILL-META-TEMPLATE-SPECIALIST | meta-template-specialist | P1 | capability_and_artifact_factory | core_factory | Converte conceitos proprietários em agentes especialistas, comandos, schemas, workflows, scripts, skills e módulos Admin-OS. | /router-intention; /widesearch-primary; /forge-specialist; /template-system; /gap-capability-map; /cmd-goldstandard; /schema-forge; /workflow-forge; /script-spec; /skill-package; /admin-os-productize | agente especialista; comando; schema; workflow; spec de script; skill empacotada; módulo Admin-OS | Usar somente quando houver gap confirmado, ausência de equivalente nativo suficiente e necessidade reutilizável. |
| SKILL-EDITORIAL-OS | editorial-os-template | P1 | content_and_editorial_operations | domain_skill | Opera setup editorial, sprint, pesquisa, produção, revisão, analytics, evolução e handoffs Design/Code. | /editorial-setup; /sprint; /derive; /produce; /review; /analytics; /evolve; /vgen; /handoff-design; /handoff-code | stack editorial; sprint; ativo de conteúdo; bloco de evidência; revisão; analytics; handoffs | Ativar somente para estratégia e operação editorial. |
| SKILL-DESK-OS | DESK-OS-Full-Stack-Skill | P0 | physical_digital_execution_interface | core_runtime | Constrói schema semanal, renderiza DESK-OS físico, roteia QR, suporta start/status/close-day e interpreta Recycle. | /preflight; /generate-week; /render; /route-qr; /start-day; /status; /close-day; /recycle; /health | schema semanal; DESK-OS imprimível; rotas QR; estado de execução; resultado Recycle; entrada da próxima semana | Consome workflows validados; não inventa workflows. |
| SKILL-CMD-01-PPS | CMD-01-PPS | P1 | project_packaging_and_release | operational_utility | Escaneia, normaliza, classifica, estrutura, rastreia e empacota arquivos em repositórios e ZIPs versionados. | CMD-01-PPS; Cmd01PPS; action_ID; trigger_ID; workflow_ID; empacota projeto; estrutura repo; normaliza arquivos | projeto normalizado; grafo de dependências; metadados; audit log; release ZIP; repositório GitHub-ready | Usar em empacotamento, exportação e release; não na ideação inicial. |

**Hierarquia funcional**

- **Control plane:** OS Partner Admin + Leonardo Orchestrator.
- **Onboarding/configuração:** Setup OS.
- **Raciocínio transversal:** Cognitive Trigger.
- **Resolução de problemas:** Agentic Problem Solving.
- **Fábrica de capacidades:** Meta Template Specialist + Standalone Orchestrator Template.
- **Domínios:** Editorial OS e DESK-OS.
- **Packaging/release:** CMD-01-PPS.

**Regra de seleção:** usar o menor conjunto suficiente; cada skill precisa ter função distinta, sem ativação duplicada, e capacidades nativas devem ser verificadas antes da criação de novo artefato.


# 7. Plugins, Connectors e Tools

| ID | Tipo | Papel | Status | Uso | Limites | Runtime gate |
| --- | --- | --- | --- | --- | --- | --- |
| PLUGIN-SMALL-BUSINESS | plugin | business_context_and_execution_support | declared_dependency_requires_runtime_verification | Estratégia, operações, clientes, oferta, receita, custos, GTM, processos ou documentação empresarial. | Não substitui orquestrador, skills proprietárias ou SSOT pessoal; não presume capacidades. | Verificar disponibilidade, ações suportadas e permissões; fallback = SKILL-OS-PARTNER-ADMIN. |

**Resultado da auditoria de plugins**

- Há **um único plugin explicitamente declarado**: `PLUGIN-SMALL-BUSINESS`.
- Não foi encontrada duplicação de plugin no workbook.
- As duas variantes de Design System são documentos, não plugins.
- Conectores específicos não estão inventariados como instalados; devem ser tratados como dependências de runtime.
- Fallback sem plugin: `SKILL-OS-PARTNER-ADMIN`, mantendo a resposta sem alegar capacidades externas não verificadas.


# 8. Agents Catalog

| Agent ID | Role | Powered by | Responsabilidades |
| --- | --- | --- | --- |
| AGENT-LEONARDO-ORCHESTRATOR | master_router | SKILL-LEONARDO-ORCHESTRATOR; SKILL-OS-PARTNER-ADMIN | Normalizar intenção; carregar estado; selecionar workflow/skill/plugin; impor gates; atualizar decisões; devolver próxima ação. |
| AGENT-PERSONAL-OPERATOR | personal_execution | SKILL-SETUP-OS; SKILL-COGNITIVE-TRIGGER; SKILL-DESK-OS | Planejamento semanal; prioridade; próxima ação; redução de carga cognitiva; progresso pessoal. |
| AGENT-BUSINESS-PARTNER | small_business_execution | SKILL-OS-PARTNER-ADMIN; PLUGIN-SMALL-BUSINESS; SKILL-AGENTIC-PROBLEM-SOLVING | Produto; operações; GTM; documentos empresariais; decisão; risco. |
| AGENT-CAPABILITY-BUILDER | specialist_and_skill_factory | SKILL-META-TEMPLATE-SPECIALIST; SKILL-STANDALONE-ORCHESTRATOR-TEMPLATE; SKILL-CMD-01-PPS | Detectar gap; construir especialista/workflow/comando/skill; empacotar e liberar. |
| AGENT-EDITORIAL-OPERATOR | content_operations | SKILL-EDITORIAL-OS; SKILL-COGNITIVE-TRIGGER | Planejamento editorial; produção; validação de evidência; revisão; analytics. |

**Boundary canônico**

```text
OS PARTNER ADMIN
├── conta e projetos
├── documentação e arquitetura
├── administração de negócio
├── validação e packaging
└── release

LEONARDO ORCHESTRATOR
├── estado canônico do projeto
├── fase e gate
├── decisões e tracker
├── roteamento de intenção
└── próximas ações
```

A sobreposição parcial foi resolvida por separação de plano de controle administrativo e plano de estado do projeto.


# 9. Commands Catalog

**Router canônico**

| Comando | Owner | Resultado |
| --- | --- | --- |
| /3E | SKILL-SETUP-OS | onboarding_and_initial_system |
| /day-zero | SKILL-LEONARDO-ORCHESTRATOR | current_state_and_next_three_tasks |
| /bom-dia | SKILL-OS-PARTNER-ADMIN | daily_operating_brief |
| /proximas-3 | SKILL-OS-PARTNER-ADMIN | three_prioritized_actions |
| /problema | SKILL-AGENTIC-PROBLEM-SOLVING | controlled_problem_solving_state |
| /router-intention | SKILL-META-TEMPLATE-SPECIALIST | artifact_build_route |
| /workflow-forge | SKILL-META-TEMPLATE-SPECIALIST | executable_workflow |
| /editorial-setup | SKILL-EDITORIAL-OS | editorial_operating_stack |
| /generate-week | SKILL-DESK-OS | weekly_DESK_OS |
| /recycle | SKILL-DESK-OS | reconciled_week_and_next_cycle |
| CMD-01-PPS | SKILL-CMD-01-PPS | packaged_release |

**Biblioteca ampliada por skill**

- Setup OS: `/3E`, `/status`, `/prisma`, `/stack`.
- Leonardo Orchestrator: `/day-zero`, `/gate-zero`, `/next-3-tasks`, `/build-doc`, `/decision-check`, `/update-tracker`, `/claims-check`, `/editorial-week`, `/export-package`.
- OS Partner Admin: `/iniciar`, `/bom-dia`, `/status`, `/proximas-3`, `/fechar-dia`, `/bmc-wide-search`, `/package-release`.
- Agentic Problem Solving: família `/problema`.
- Meta Template Specialist: `/router-intention`, `/widesearch-primary`, `/forge-specialist`, `/template-system`, `/gap-capability-map`, `/cmd-goldstandard`, `/schema-forge`, `/workflow-forge`, `/script-spec`, `/skill-package`, `/admin-os-productize`.
- Editorial OS: `/editorial-setup`, `/sprint`, `/derive`, `/produce`, `/review`, `/analytics`, `/evolve`, `/vgen`, `/handoff-design`, `/handoff-code`.
- DESK-OS: `/preflight`, `/generate-week`, `/render`, `/route-qr`, `/start-day`, `/status`, `/close-day`, `/recycle`, `/health`.


# 10. Workflow Library

| Workflow ID | Prioridade | Finalidade | Sequência | Definition of Done |
| --- | --- | --- | --- | --- |
| WF-ONBOARD-LEONARDO-OS | P0 | Construir/atualizar macro-personalização | SETUP-OS → COGNITIVE-TRIGGER → OS-PARTNER-ADMIN | Contexto operacional validado, agentes/skills/ferramentas/workflows/comandos/exclusões e requisitos DESK-OS definidos. |
| WF-START-WEEK | P0 | Gerar superfície operacional semanal | LEONARDO-ORCHESTRATOR → COGNITIVE-TRIGGER → DESK-OS | Até 3 workflows ativos, 3 etapas cada, 1 entregável por workflow e QR ligado a ação real. |
| WF-SOLVE-COMPLEX-PROBLEM | P0 | Resolver problema ambíguo de alto valor | COGNITIVE-TRIGGER → AGENTIC-PROBLEM-SOLVING → LEONARDO-ORCHESTRATOR | Problema definido, estratégia justificada, stop condition e avaliação contra critérios. |
| WF-VALIDATE-PRODUCT-HYPOTHESIS | P0 | Validar hipótese de produto/mercado/arquitetura | AGENTIC-PROBLEM-SOLVING → PLUGIN-SMALL-BUSINESS → OS-PARTNER-ADMIN | Hipótese falsificável, experimento mínimo, métricas/thresholds e decisão de gate. |
| WF-BUILD-MISSING-CAPABILITY | P1 | Criar especialista/skill/comando/workflow ausente | META-TEMPLATE-SPECIALIST → AGENTIC-PROBLEM-SOLVING → CMD-01-PPS | Capacidade distinta, contratos, progressive disclosure, evals e pacote versionado. |
| WF-CREATE-PROJECT-ORCHESTRATOR | P2 | Converter corpus em orquestrador standalone | STANDALONE-ORCHESTRATOR-TEMPLATE → META-TEMPLATE-SPECIALIST → CMD-01-PPS | Fonte canônica, mapa MECE, fases, gates, decisões, comandos, tracker e skill standalone. |
| WF-OPERATE-EDITORIAL-SPRINT | P1 | Planejar, produzir, revisar e medir conteúdo | EDITORIAL-OS → COGNITIVE-TRIGGER → EDITORIAL-OS | Sprint, ativo, relatório de qualidade, analytics e próxima ação editorial. |
| WF-PACKAGE-RELEASE | P1 | Criar release rastreável e pronta para produção | OS-PARTNER-ADMIN → CMD-01-PPS → LEONARDO-ORCHESTRATOR | Repo normalizado, metadados, audit log, ZIP e decisão de release. |
| WF-CLOSE-AND-RECYCLE-WEEK | P0 | Reconciliar execução e preparar próximo ciclo | DESK-OS → LEONARDO-ORCHESTRATOR → DESK-OS | Concluídos, não resolvidos, carry-over, decisões, tracker atualizado e seed da próxima semana. |

**Contrato obrigatório de workflow**

1. ID verbal.
2. Trigger.
3. Input contract.
4. Exatamente três etapas visíveis ao usuário.
5. Output contract.
6. Definition of Done.
7. Owner skill.
8. Failure mode.
9. Evidência de gate.

Os arquivos `WF1.md` a `WF6.md` permanecem ativos como ativos transversais; `WF5.md` é referência em revisão. O `Workflowagentico` é o master workflow confirmado.


# 11. Templates e Assets

| Item | Nome | Tipo | Status | Autoridade | Fonte |
| --- | --- | --- | --- | --- | --- |
| FILE-004 | 99-TEMPLATE_CDM_OURO | TEMPLATE | CONFIRMED | WORKING | 99-TEMPLATE_CDM_OURO |
| FILE-040 | Template_Minimo_Padronizacao_Processo.xlsx | WORKBOOK | CONFIRMED | WORKING | Template_Minimo_Padronizacao_Processo.xlsx |
| ITEM-040-S023 | Fluxo Completo | WORKBOOK | PROPOSED | WORKING | Template_Minimo_Padronizacao_Processo.xlsx |
| ITEM-040-S024 | Diagnóstico AS IS | WORKBOOK | PROPOSED | WORKING | Template_Minimo_Padronizacao_Processo.xlsx |
| ITEM-040-S025 | TO BE e Piloto | WORKBOOK | PROPOSED | WORKING | Template_Minimo_Padronizacao_Processo.xlsx |
| ITEM-040-S026 | SOP | WORKBOOK | PROPOSED | WORKING | Template_Minimo_Padronizacao_Processo.xlsx |
| ITEM-040-S027 | Implantação e Controle | WORKBOOK | PROPOSED | WORKING | Template_Minimo_Padronizacao_Processo.xlsx |
| ITEM-002-S057 | Briefing_Codificado | CODED_BRIEFING | PROPOSED | WORKING | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx |

**Templates canônicos identificados**

- `99-TEMPLATE_CDM_OURO`: contrato padrão-ouro de prompt/agente.
- `Template_Minimo_Padronizacao_Processo.xlsx`: fluxo completo, AS-IS, TO-BE/piloto, SOP e implantação/controle.
- `Briefing_Codificado`: briefing estruturado.
- YAML Cards: DESK-OS, Leonardo-OS e Card 2 DESK-OS.
- Output Requirements V3: versão de trabalho; V1/V2 preservadas como superseded.


# 12. Directory e Architecture Catalog

| Item | Nome | Tipo | Status | Autoridade | Fonte |
| --- | --- | --- | --- | --- | --- |
| FILE-026 | MASTER-INDEX-AGENTIC-SYSTEMS-ARCHITECT.md | MASTER_INDEX | CONFIRMED | WORKING | MASTER-INDEX-AGENTIC-SYSTEMS-ARCHITECT.md |
| FILE-027 | MATER-FULL-PRINT | UNIFIED_CATALOG | CONFIRMED | WORKING | MATER-FULL-PRINT |
| FILE-034 | README | MASTER_INDEX | CONFIRMED | WORKING | README |
| FILE-035 | README-ASA-TREEFILE.md | TREEFILE | CONFIRMED | WORKING | README-ASA-TREEFILE.md |
| FILE-043 | VARIÁVEIS_PERSONALIZADAS | MECE_TRANSCRIPT | CONFIRMED | WORKING | VARIÁVEIS_PERSONALIZADAS |
| ITM-MEM-005 | TRACK-CLAUDE-POWER-USER | TRACK | PROPOSED | DRAFT |  |

**Arquitetura das 23 abas**

- Executivo: 00–04.
- Produtos e inventário: 05–07 e 20.
- Ativos: 08–10, 12–13.
- Governança: 11, 14–19.
- Técnico: 21–22.

O diretório cataloga, mas não se torna owner dos ativos. A fonte canônica de IDs e tags é `01_ID_TAG_DICTIONARY`; o registro único de entidades é `02_ENTITY_REGISTRY`.


# 13. Design System e UX

| Item | Nome | Tipo | Status | Autoridade | Hash/Fonte |
| --- | --- | --- | --- | --- | --- |
| FILE-016 | Desing_System_.txt | DESIGN_SYSTEM | REVIEW_REQUIRED | REFERENCE | Desing_System_.txt |
| FILE-032 | Propostas_de_wirfremes_.txt | WIREFRAME | CONFIRMED | WORKING | Propostas_de_wirfremes_.txt |
| FILE-039 | SOT_DESING_SYSTEM | DESIGN_SYSTEM | REVIEW_REQUIRED | WORKING | SOT_DESING_SYSTEM |
| FILE-050 | Wireframe | WIREFRAME | CONFIRMED | WORKING | Wireframe |
| FILE-051 | Wireframe_2 | WIREFRAME | CONFIRMED | WORKING | Wireframe_2 |

**Decisão proposta de SSOT**

- `SOT_DESING_SYSTEM` passa a **SSOT provisória V1**, por ser a variante nomeada SOT e estar com autoridade WORKING.
- `Desing_System_.txt` permanece **REFERENCE**.
- A decisão só se torna definitiva após diff semântico dos 552 registros de cada variante.
- Wireframes permanecem WORKING e subordinados aos tokens/regras canônicas.

**Princípios preservados:** neuroinclusivo, iPad-first, A4, fonte ≥9 pt, baixa densidade, rolagem vertical, texto + cor nos status e ausência de macros.


# 14. Macro Personalization e Variable Profile

| Item | Nome | Tipo | Status | Autoridade | Fonte |
| --- | --- | --- | --- | --- | --- |
| FILE-019 | ESPECIALISTA_AGENTE | SPECIALIST | PROPOSED | WORKING | ESPECIALISTA_AGENTE |
| FILE-020 | ESPECIALISTA_RATIONALE | SPECIALIST | PROPOSED | WORKING | ESPECIALISTA_RATIONALE |
| FILE-024 | LEONARDO-OS.md | MACRO | CONFIRMED | WORKING | LEONARDO-OS.md |
| FILE-025 | LEONARDO_MACRO_PERSONALIZATION___PROPRIETARY_SKILL_STACK.md | SKILL_STACK | CONFIRMED | SSOT | LEONARDO_MACRO_PERSONALIZATION___PROPRIETARY_SKILL_STACK.md |
| FILE-028 | OUTPUT-REQUIREMNETS_ | OUTPUT_REQUIREMENTS | CONFIRMED | SUPERSEDED | OUTPUT-REQUIREMNETS_ |
| FILE-029 | OUTPUT_REQUIREMENTS_V2.md | OUTPUT_REQUIREMENTS | CONFIRMED | SUPERSEDED | OUTPUT_REQUIREMENTS_V2.md |
| FILE-030 | OUTPUT_REQUIREMENTS_V3.md | OUTPUT_REQUIREMENTS | CONFIRMED | WORKING | OUTPUT_REQUIREMENTS_V3.md |
| FILE-041 | UNIVERSAL_ICP_OPERATING_SYSTEM_SCHEMA.md | ICP_SCHEMA | CONFIRMED | WORKING | UNIVERSAL_ICP_OPERATING_SYSTEM_SCHEMA.md |
| FILE-042 | VARIÁVEIS_DO_AMBIENTE_ | ENV_VARS | CONFIRMED | WORKING | VARIÁVEIS_DO_AMBIENTE_ |
| ITEM-002-S052 | Macro_Personalizacao | MACRO | PROPOSED | WORKING | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx |
| ITM-MEM-003 | TRACK-MACRO-PERSONALIZATION | TRACK | PROPOSED | DRAFT |  |

**Fixed core**

- Governança e segurança.
- IDs, gates, decisões, rastreabilidade e quality gates.
- Stack proprietário.
- Boundaries dos agentes.
- Contratos de workflow e output.

**Variable profile**

- ICP e contexto.
- Objetivos, dores, ferramentas e restrições.
- Preferências cognitivas.
- Skills/plugin selecionados.
- Workflows e DESK-OS de cada ciclo.

**Regra:** o fixed core não é reescrito por um perfil; o perfil variável só configura parâmetros e seleção de capacidades.


# 15. Business e GTM

| Item | Nome | Programa | Produto | Tipo | Status | Autoridade | Fonte |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FILE-006 | BUSINESS_GMT_RATIONAL_ | PRG-SMALL-BUSINESS |  | DECISION | CONFIRMED | DUPLICATE_COPY | BUSINESS_GMT_RATIONAL_ |
| FILE-008 | cluster_2_mercado_negocio_gtm_unificado.xlsx | PRG-SMALL-BUSINESS |  | WORKBOOK | PROPOSED | WORKING | cluster_2_mercado_negocio_gtm_unificado.xlsx |
| FILE-022 | GTM_RATIONALE.txt | PRG-SMALL-BUSINESS |  | DECISION | CONFIRMED | APPROVED | GTM_RATIONALE.txt |
| ITEM-008-S020 | 00_RESUMO | PRG-SMALL-BUSINESS |  | WORKBOOK | PROPOSED | WORKING | cluster_2_mercado_negocio_gtm_unificado.xlsx |
| ITEM-008-S021 | 01_CLUSTER_2_UNIFICADO | PRG-SMALL-BUSINESS |  | WORKBOOK | PROPOSED | WORKING | cluster_2_mercado_negocio_gtm_unificado.xlsx |
| ITEM-008-S022 | 02_CRITERIOS | PRG-SMALL-BUSINESS |  | WORKBOOK | PROPOSED | WORKING | cluster_2_mercado_negocio_gtm_unificado.xlsx |
| ITM-MEM-006 | INIT-GTM-SHOWROOM |  |  | INITIATIVE | PROPOSED | DRAFT |  |
| ITM-MEM-007 | INIT-AGENCY-KIT |  |  | INITIATIVE | PROPOSED | DRAFT |  |
| ITM-MEM-008 | MODULE-M1 |  |  | MODULE | REVIEW_REQUIRED | DRAFT |  |
| ITM-MEM-009 | MODULE-M2 |  |  | MODULE | REVIEW_REQUIRED | DRAFT |  |
| ITM-MEM-010 | MODULE-M5 |  |  | MODULE | REVIEW_REQUIRED | DRAFT |  |

**Estado**

- `GTM_RATIONALE.txt` é a cópia primária aprovada.
- `BUSINESS_GMT_RATIONAL_` é duplicata idêntica preservada.
- GTM Showroom e Agency Kit são iniciativas propostas.
- M1, M2 e M5 são módulos em revisão, sem BRD/MRD/PRD dedicados.
- O plugin Small Business deve ser usado somente após gate de disponibilidade e sem substituir as skills proprietárias.


# 16. Research e Evidence

| Item | Nome | Programa | Produto | Tipo | Status | Autoridade | Fonte |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FILE-033 | RATIONAL_ADPT_txt.rtf | PRG-ASA | PRD-ASA | DERIVATION | REVIEW_REQUIRED | REFERENCE | RATIONAL_ADPT_txt.rtf |
| FILE-037 | SAKANA-BLUEPRINT_txt.rtf | PRG-ASA | PRD-ASA | EXTERNAL_REFERENCE | CONFIRMED | REFERENCE | SAKANA-BLUEPRINT_txt.rtf |
| FILE-038 | SAKANA_TXT.rtf | PRG-ASA | PRD-ASA | EXTERNAL_REFERENCE | CONFIRMED | REFERENCE | SAKANA_TXT.rtf |
| FILE-048 | WF5.md | PRG-ASA | PRD-ASA | WF | REVIEW_REQUIRED | REFERENCE | WF5.md |
| ITEM-002-S063 | Palantir_Codificado |  |  | EXTERNAL_REFERENCE | REVIEW_REQUIRED | WORKING | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx |

Referências Sakana/Fugu e Palantir são evidência externa ou derivação; não viram requisito automaticamente. Cada referência precisa ser ligada a uma decisão, hipótese ou critério de arquitetura antes de entrar no fixed core.


# 17. Relationships e Dependency Graph

| From | Relação | To | Nota |
| --- | --- | --- | --- |
| PRD-LEONARDO-OS | INTEGRATES_WITH | PRD-DESK-OS | Integra DESK-OS na operacao pessoal. |
| PRD-LEONARDO-OS | USES | PRD-ASA | Utiliza recursos do ASA. |
| PRD-LEONARDO-OS | USES | CAP-MACRO-PERSONALIZATION | Implementacao concreta da macro-personalizacao. |
| PRD-LEONARDO-OS | INTEGRATES_WITH | PRG-TDAH | Pode incorporar modulos do programa TDAH. |
| PLT-PADRAO-OS | PROVIDES_TO | PRJ-LEONARDO-001 | Governanca e arquitetura-base para todos os programas. |
| CAP-MACRO-PERSONALIZATION | PROVIDES_TO | PRD-LEONARDO-OS | Configura ICPs e produtos. |
| PRD-ASA | PROVIDES_TO | PRJ-LEONARDO-001 | Arquitetura, metodos e ativos agenticos. |
| PLT-DIRECTORY | REFERENCES | PRJ-LEONARDO-001 | Cataloga ativos sem ser proprietario. |

```text
PROJECT-LEONARDO-ECOSYSTEM
├── PROGRAM-ASA ─────────────── provides architecture/methods
├── PROGRAM-TDAH ────────────── cognitive modules
├── PROGRAM-DESK-OS ─────────── physical-digital execution
├── PROGRAM-LEONARDO-OS ─────── personal/business operation
├── PROGRAM-EDUCATION ───────── proposed
└── PROGRAM-SMALL-BUSINESS ──── proposed

TRANSVERSAL
├── PLATFORM-PADRAO-OS ─────── governance
├── PLATFORM-DIRECTORY ─────── catalog
└── CAP-MACRO-PERSONALIZATION ─ configuration
```


# 18. Decision Log e ADRs

| Decision ID | Título | Status | Resolução | Origem |
| --- | --- | --- | --- | --- |
| DR-001 | Slot da aba 01 e README | APROVADO | 00_WORKSPACE absorve dashboard+navegacao+legenda; 01=ID_TAG_DICTIONARY; README executivo no workspace e README completo em README_ARCHITECTURE.md. | Leonardo (aprovacao) |
| DEC-G0-1 | WF1-WF6 e Workflowagentico | APLICADA | Ativos transversais de workflow/comando (C06 SHARED), nao exclusivos do ASA. Inspecao item a item; secoes especificas de arquitetura agentica -> ASA; 4D AI Fluency -> ASA EXTERNAL_REFERENCE. | 0.txt |
| DEC-G0-2 | Context vs Contextos_adicionais vs Design System | APLICADA | Context=PROJECT_CONTEXT C09 SHARED; Contextos_adicionais=DESK-OS PRIMARY REVIEW_REQUIRED; Design System=C08 SHARED, primario DESK-OS, versoes preservadas. | 0.txt |
| DEC-G0-3 | Duplicata GTM | APLICADA | DUP-001: GTM_RATIONALE.txt=PRIMARY/preferred; BUSINESS_GMT_RATIONAL_=DUPLICATE_COPY. Hash identico. Nenhuma copia apagada. | 0.txt |
| DEC-G0-4 | Leonardo OS vs ASA/TDAH/DESK-OS | APLICADA | Programas irmaos; Leonardo OS nao e raiz hierarquica. Relacoes por USES/INTEGRATES_WITH/PROVIDES_TO; parent_item_id so para hierarquia real. | 0.txt |
| ADJ-1 | Nao fixar 54/56 antes de reconciliar | APLICADA | physical=56; source=54; generated/system=2 (master_index.json, MASTER_INDEX.md); excluded=2 com motivo; in_scope=54. V1 = discovered=indexed+excluded. | README aprovacao |
| ADJ-2 | Reconciliar 38 vs 41 abas do V3 | APLICADA | inventory_reported=38; runtime_detected=41; delta=+3; todas visiveis, nenhuma vazia/oculta. DoD usa 41 (hash d463c87ca843). | README aprovacao |
| ADJ-3 | Granularidade de item | APLICADA | 1 aba -> >=1 ITEM-ROOT; dividir por SECTION/TABLE quando multi-produto. item_granularity registrado. | README aprovacao |
| ADJ-4 | Separar autoridade de classificacao | APLICADA | authority_status, classification_status e documentation_status em campos distintos. | README aprovacao |
| ADJ-5 | source_basis = PROVIDED_PROJECT_CONTEXT | APLICADA | Entidades informadas no README usam PROVIDED_PROJECT_CONTEXT, nao MEMORY_CONFIRMED. | README aprovacao |
| ADJ-6 | Regras de parada granulares | APLICADA | Arquivo individual ilegivel -> FILE_READ_ERROR e continua. BLOCKED apenas global. | README aprovacao |
| ADJ-7 | Navegacao iPad-first agrupada | APLICADA | 00_WORKSPACE agrupa links por Executivo/Produtos/Ativos/Governanca/Tecnico; abas tecnicas com tag TECHNICAL. | README aprovacao |
| ADJ-8 | A4 como area de impressao | APLICADA | A4 nas abas marcadas; paisagem permitida; fonte nunca <9pt; cabecalho repetido. | README aprovacao |

**Novas decisões de follow-up propostas**

- `FUP-DEC-01`: `SOT_DESING_SYSTEM` = SSOT provisória; `Desing_System_.txt` = referência.
- `FUP-DEC-02`: `Contextos_adicionais_` = cluster primário C04 Architecture/System; C08 apenas quando a seção for visual.
- `FUP-DEC-03`: Setup Suite e AI OS Reset = ofertas candidatas, não produtos confirmados.
- `FUP-DEC-04`: Agent Factory = capability implementada conceitualmente por AGENT-CAPABILITY-BUILDER + WF-BUILD-MISSING-CAPABILITY; documento dedicado ainda obrigatório.
- `FUP-DEC-05`: writable fields e autonomy policy passam a contrato de governança deste follow-up.


# 19. Gap Register, OQs e Resolução

| ID | Lacuna | Estado no follow-up | Tratamento |
| --- | --- | --- | --- |
| GAP-001 | Course Express sem arquivo próprio | PARTIAL | Criar Charter + Vision + BRD + MRD + PRD mínimo. Produto permanece PROPOSED. |
| GAP-002 | Education sem documentação dedicada | PARTIAL | Criar Program Charter; não promover para CONFIRMED antes do owner aprovar escopo e ofertas. |
| GAP-003 | Small Business / maturidade | PARTIAL | Separar Business Suite, GTM Showroom e Agency Kit; aplicar stage gate por evidência. |
| GAP-004 | Agent Factory | PARTIALLY_RESOLVED | Conceito mapeado para AGENT-CAPABILITY-BUILDER e WF-BUILD-MISSING-CAPABILITY; falta documento dedicado. |
| GAP-005 | Neuro-Agent | OPEN_CONTROLLED | Manter módulo candidato. Exigir problema, boundary clínico zero, inputs/outputs, evals e decisão de owner. |
| GAP-006 | Setup Suite | RESOLVED_AS_CANDIDATE | Classificar como OFFER-CANDIDATE apoiada por Setup OS + OS Partner Admin; validar WTP antes de produto. |
| GAP-007 | AI OS Reset | RESOLVED_AS_CANDIDATE | Classificar como OFFER-CANDIDATE; definir JTBD, ICP, DoD, preço e experimento. |
| GAP-008 | Design System variants | PROVISIONAL_RESOLUTION | SOT_DESING_SYSTEM = SSOT provisória; outra variante = REFERENCE; diff semântico obrigatório. |
| GAP-009 | Contextos_adicionais_ | RESOLVED | Cluster primário C04, coerente com ITEMS_MASTER; seções visuais podem receber tag secundária C08. |

**Open Questions do BUILD_REPORT**

| OQ | Tema | Status | Resolução |
| --- | --- | --- | --- |
| OQ-01 | commands_01_03_function | CLOSED | Router canônico com 11 rotas e owners; catálogo ampliado por skill. |
| OQ-02 | leonardo_s_alias | CLOSED | Separação canônica: AGENT-LEONARDO-ORCHESTRATOR e SKILL-OS-PARTNER-ADMIN. |
| OQ-03 | interview_name | PROVISIONAL | Nome operacional: etapa COLLECT-OPERATING-CONTEXT do WF-ONBOARD-LEONARDO-OS. |
| OQ-04 | design_plugins_duplication | CLOSED | Apenas um plugin declarado; variantes de Design System são documentos. |
| OQ-05 | master_spreadsheet_writable_fields | CLOSED_BY_POLICY | Aplicar write policy abaixo. |
| OQ-06 | admin_boundaries | CLOSED | ADR/decision boundary consolidado. |
| OQ-07 | deskos_qr | DOCUMENTED_RUNTIME_OPEN | Contrato abstrato definido; implementação e round-trip dependem de runtime. |
| OQ-08 | autonomy_threshold | CLOSED_BY_POLICY | AUTO / CONFIRM / BLOCK formalizados. |

**Write Policy**

- **EDITABLE:** `classification_status/status`, `documentation_status`, `next_action`, `review_required`, owner, due date e notas de validação.
- **CONTROLLED:** `authority_status`, parent/relation e SSOT; somente owner/governança altera.
- **COMPUTED:** contagens, KPIs, cobertura, fórmulas e indicadores.
- **LOCKED/IMMUTABLE:** `source_file`, `source_hash`, `source_locator`, conteúdo bruto, IDs já publicados, decisões aprovadas e evidências de validação.

**Autonomy Policy**

- **AUTO:** leitura, classificação reversível, geração local, testes estáticos, documentação e propostas.
- **CONFIRM:** ação externa, publicação, envio, alteração de SSOT, exclusão, credenciais, dados privados e decisão que muda produto.
- **BLOCK:** exposição de segredo, alegação de execução não verificada, ação destrutiva sem backup ou violação de guardrail.


**Runtime gaps — permanecem abertos por natureza**

| Gap | Tema | Critério de fechamento |
| --- | --- | --- |
| GR-01 | Environment capabilities | Executar Environment Resolver e registrar capacidades reais. |
| GR-02 | Installed skills | Confirmar importação, versão e disponibilidade de cada skill. |
| GR-03 | Connectors/permissions | Testar autorização mínima e round-trip sem credenciais no pacote. |
| GR-04 | End-to-end real case | Executar TEST-LEONARDO-WORKFLOW-001 com evidências. |
| GR-05 | Intent accuracy | Criar benchmark com intents, expected route e threshold. |
| GR-06 | QR/DESK-OS physical sync | Testar geração, leitura, ação e Recycle em dispositivo real. |
| GR-07 | Frontmatter acceptance | Importar no Claude.ai e validar campos aceitos. |

# 20. Strategic Entities e Offers

| Entity ID | Tipo | Programa/Parent | Classificação | Documentação | Papel | Documentos ausentes |
| --- | --- | --- | --- | --- | --- | --- |
| PLT-PADRAO-OS | PLATFORM | PRJ-LEONARDO-001 | CONFIRMED | EMBEDDED | Governanca, seguranca, memoria, qualidade, nomenclatura, gates, arquitetura-base. | '- |
| PLT-DIRECTORY | PLATFORM | PRJ-LEONARDO-001 | CONFIRMED | EMBEDDED | Cataloga skills, agentes, comandos, workflows, plugins, conectores, templates. | '- |
| CAP-MACRO-PERSONALIZATION | CAPABILITY | PLT-PADRAO-OS | CONFIRMED | EMBEDDED | Configura produtos e ICPs: contexto, variaveis, memoria, skills, agentes, execucao. | '- |
| CAP-AGENT-FACTORY | CAPABILITY | PRG-ASA | REVIEW_REQUIRED | EMBEDDED | Fabrica de agentes. A avaliar; sem documentacao dedicada confirmada. | '- |
| TRACK-TDAH | TRACK | PRD-COURSE-EXPRESS | PROPOSED | MISSING | Trilha TDAH do Course Express. | BRD,MRD,PRD |
| TRACK-MACRO-PERSONALIZATION | TRACK | PRD-COURSE-EXPRESS | PROPOSED | MISSING | Trilha de macro-personalizacao. | BRD,MRD,PRD |
| TRACK-ANTHROPIC-STACK | TRACK | PRD-COURSE-EXPRESS | PROPOSED | MISSING | Trilha Anthropic Stack. | BRD,MRD,PRD |
| TRACK-CLAUDE-POWER-USER | TRACK | PRD-COURSE-EXPRESS | PROPOSED | MISSING | Trilha Claude Power User. | BRD,MRD,PRD |
| INIT-GTM-SHOWROOM | INITIATIVE | PRG-SMALL-BUSINESS | PROPOSED | MISSING | Iniciativa de demonstracao e aquisicao. | BRD,MRD,PRD |
| INIT-AGENCY-KIT | INITIATIVE | PRG-SMALL-BUSINESS | PROPOSED | MISSING | Iniciativa/oferta sem documentacao suficiente. | BRD,MRD,PRD |
| MODULE-M1 | MODULE | PRD-BUSINESS-SUITE | REVIEW_REQUIRED | EMBEDDED | Modulo M1 da Business Suite. | BRD,MRD,PRD |
| MODULE-M2 | MODULE | PRD-BUSINESS-SUITE | REVIEW_REQUIRED | EMBEDDED | Modulo M2 da Business Suite. | BRD,MRD,PRD |
| MODULE-M5 | MODULE | PRD-BUSINESS-SUITE | REVIEW_REQUIRED | EMBEDDED | Modulo M5 da Business Suite. | BRD,MRD,PRD |
| OFFER-DESKOS-KIT | OFFER | PRD-DESK-OS | PROPOSED | MISSING | Oferta kit DESK-OS. | BRD,MRD,PRD |
| OFFER-DESK-AND-GO | OFFER | PRD-DESK-OS | PROPOSED | MISSING | Oferta Desk and Go. | BRD,MRD,PRD |
| MODULE-QR-ORCHESTRATOR | MODULE | PRD-DESK-OS | PROPOSED | MISSING | Modulo orquestrador de QR. | BRD,MRD,PRD |
| MODULE-RECYCLE | MODULE | PRD-DESK-OS | PROPOSED | MISSING | Modulo Recycle. | BRD,MRD,PRD |
| MODULE-PRISMA-DESK-GENERATOR | MODULE | PRD-DESK-OS | PROPOSED | MISSING | Gerador do Prisma Desk. | BRD,MRD,PRD |
| MODULE-ONE-PRINT-HTML | MODULE | PRD-DESK-OS | PROPOSED | MISSING | One Print HTML. | BRD,MRD,PRD |
| MODULE-NEURO-AGENT | MODULE | PRD-TDAH-OS | REVIEW_REQUIRED | EMBEDDED | Neuro-Agent; a avaliar. | BRD,MRD,PRD |
| PRODUCT-SETUP-SUITE | OFFER | PRD-LEONARDO-OS | REVIEW_REQUIRED | EMBEDDED | Setup Suite; candidato a avaliar. | BRD,MRD,PRD |
| PRODUCT-AI-OS-RESET | OFFER | PRD-LEONARDO-OS | REVIEW_REQUIRED | EMBEDDED | AI OS Reset; candidato a avaliar. | BRD,MRD,PRD |

**Regra de promoção**

`PROPOSED → REVIEW_REQUIRED → CONFIRMED` exige: owner, problema, ICP, escopo, boundary, BRD/MRD/PRD adequado, dependências, riscos, experimento e Definition of Done.


# 21. Validation, Audit e Tests

| Gate | Critério | Resultado | Fundamentação |
| --- | --- | --- | --- |
| V1 | Cobertura de arquivos (discovered=indexed+excluded) | PASS | 56 = 54 in_scope + 2 excluidos (artefatos de indice, com motivo). Nenhum elegivel orfao. |
| V2 | Cobertura das abas (1 item por aba) | PASS | 97 abas detectadas -> 97 ITEM-ROOTs em 05_ITEMS_MASTER. V3 reconciliado em 41. |
| V3 | Cobertura conceitual | PASS | 6 programas, 7 produtos, plataformas/capacidades e 9 lacunas registrados. |
| V4 | Proveniencia | PASS | Todo item de arquivo tem source_file, source_locator, source_sheet e source_hash. |
| V5 | Isolamento | PASS | Itens multi-produto marcados REVIEW_REQUIRED; sem fusao silenciosa. Relacoes explicitas em 15. |
| V6 | Seguranca | PASS | Injecao =+-@ neutralizada; chunking >30000 chars; sem macros; reaberto programaticamente. |
| V7 | Autoridade | PASS | authority_status e classification_status separados em todos os itens. |
| V8 | Integridade relacional | PASS | Todos os IDs de 15_RELATIONSHIPS existem em 02_ENTITY_REGISTRY. |
| V9 | Manipulacao | PASS | Filtros, congelamento de paineis e validacoes de dados ativos nas abas operacionais. |
| V10 | DoD | PASS | Quatro entregaveis gerados; workbook reabre sem erro; inferencias marcadas. |

**Build gates**

| Gate | Estado | Interpretação |
|---|---|---|
| BUILD-G1 | PASS | Fontes, source map, OQs e conflitos registrados. |
| BUILD-G2 | PASS | Arquitetura, boundaries, fixed core e variable profile definidos. |
| BUILD-G3 | PASS | Estrutura, YAML, frontmatter e links locais validados no build pai. |
| BUILD-G4 | PARTIAL | Testes estáticos passam; runtime não executado. |
| BUILD-G5 | PASS | Packaging, checksum e scan de secrets do build pai. |

**Nota de consistência:** o `VALIDATION_REPORT.md` registra 39 fórmulas e zero erros após recálculo no LibreOffice. O valor `#NAME?` visível em algumas leituras por biblioteca não deve ser tratado como falha do arquivo final sem reabrir no motor de cálculo usado na validação.


# 22. Traceability e Coverage


**Cadeia de rastreabilidade**

```text
SOURCE FILE
  ↓ file_id + hash
ITEM MASTER
  ↓ item_id + source_locator + source_sheet
ENTITY REGISTRY
  ↓ program/product/platform/capability
RELATIONSHIPS
  ↓ USES / INTEGRATES_WITH / PROVIDES_TO / REFERENCES
DECISIONS + GAPS
  ↓ status + owner + next action
VALIDATION
  ↓ gate + evidence
BUILD / RELEASE
```

**Cobertura garantida**

- Todo file item possui arquivo, locator, sheet e hash.
- 54 file roots + 97 sheet roots + 12 context records = 163 itens.
- 97 abas possuem ITEM-ROOT.
- Todos os IDs usados em relacionamentos existem no registry.
- Nenhum arquivo elegível ficou órfão.
- Duplicatas foram preservadas e classificadas, não apagadas.


**Grupos de duplicatas e versões**

| Grupo | Papel | Item | Hash | Nota |
| --- | --- | --- | --- | --- |
| DUP-001 | PRIMARY | GTM_RATIONALE.txt | 9f7be64c9de1 | preferred_copy=true; conteudo identico por hash. |
| DUP-001 | DUPLICATE_COPY | BUSINESS_GMT_RATIONAL_ | 9f7be64c9de1 | preferred_copy=false; nao apagar do inventario. |
| VG-DESIGN-SYSTEM | VARIANT | SOT_DESING_SYSTEM | 41b66bfa0c08 | Mesmo resumo, hash diferente -> variante/versao. |
| VG-DESIGN-SYSTEM | VARIANT | Desing_System_.txt | 741df5e56b63 | Mesmo resumo, hash diferente -> variante/versao. comparison_status=REVIEW_REQUIRED. |
| VG-DESKOS-MASTER | PREFERRED | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | d463c87ca843 | 41 abas; versao mais completa (V3). |
| VG-DESKOS-MASTER | SUPERSEDED | 03DESKOSPLANILHAMESTRA.xlsx | 90a3b94d359d | 8 abas; versao anterior (v1). supersedes pelo V3. |

# 23. Roadmap e Release Plan

| Ciclo | Objetivo | Saída/Gate |
| --- | --- | --- |
| Ciclo 0 — Governance Closure | Aplicar FUP-DEC-01..05, write policy e autonomy policy | Decision register atualizado; gaps reclassificados |
| Ciclo 1 — Runtime Import | Importar agente e skills no Claude.ai Project | Skills visíveis; frontmatter aceito/rejeitado com log |
| Ciclo 2 — Environment Resolver | Detectar tools, plugin, conectores e permissões | environment-capabilities.yaml real |
| Ciclo 3 — End-to-End | Rodar /day-zero em um caso real | Workflow roteado, três etapas, output, DoD e evidência |
| Ciclo 4 — Intent Benchmark | Executar suíte de intents | Acurácia por rota e falhas classificadas |
| Ciclo 5 — DESK-OS/QR | Gerar semana, QR, ação e Recycle | Round-trip físico-digital comprovado |
| Ciclo 6 — RC2 | Corrigir gaps e empacotar | ZIP, checksum, audit, release decision |

**Stop conditions**

- Não avançar para RC2 se houver segredo, frontmatter rejeitado sem fallback, rota de intenção crítica abaixo do threshold, workflow sem três etapas/DoD ou QR apontando para ação inexistente.
- Não promover produto proposto sem corpus mínimo e aprovação do owner.


# 24. Next Actions e Acceptance Gates

| # | Ação | Owner | Aceite |
| --- | --- | --- | --- |
| 1 | Registrar FUP-DEC-01..05 no decision log | Leonardo | Decisões aprovadas, rejeitadas ou ajustadas. |
| 2 | Aplicar write policy ao workbook | Admin | Campos editáveis/controlados/locked documentados. |
| 3 | Gerar Program Charter de Education e Small Business | Product Admin | Escopo, owner, produtos e gates. |
| 4 | Gerar minimum doc pack de Course Express e Business Suite | Product/Business | Vision, BRD, MRD e PRD mínimos. |
| 5 | Executar diff semântico das variantes de Design System | Design | SSOT definitiva e changelog. |
| 6 | Importar stack no Claude.ai e rodar Environment Resolver | Runtime owner | GR-01, GR-02 e GR-07 evidenciados. |
| 7 | Executar TEST-LEONARDO-WORKFLOW-001 | Leonardo | GR-04 fechado com log e output. |
| 8 | Construir benchmark de intents | Evaluator | GR-05 medido. |
| 9 | Testar conector/plugin e QR round-trip | Runtime/DeskOS | GR-03 e GR-06 fechados. |
| 10 | Empacotar RC2 | CMD-01-PPS | Release report, ZIP, checksum e decisão. |

**Próxima ação única:** aprovar ou ajustar as cinco decisões de follow-up e, em seguida, executar `/day-zero` no Project real do Claude.ai.

**Estado final deste relatório**

```yaml
final_state:
  documentary_inventory: COMPLETE
  governance_model: COMPLETE
  proprietary_stack_extracted: COMPLETE
  plugin_catalog: COMPLETE
  agent_catalog: COMPLETE
  workflow_catalog: COMPLETE
  command_router: COMPLETE
  gap_treatment: CONTROLLED
  local_validation: PASS
  runtime_validation: PENDING
  release_state: RC1_READY_FOR_CONTROLLED_RUNTIME_VALIDATION
```


# APÊNDICE A — Full File Index

| file_id | Arquivo | Tipo | hash12 | Linhas | Papel | scope | cobertura |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FILE-001 | 03DESKOSPLANILHAMESTRA.xlsx | XLSX | 90a3b94d359d | 150 | WORKBOOK | IN_SCOPE | SHEETS->ITEMS |
| FILE-002 | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | XLSX | d463c87ca843 | 1683 | WORKBOOK | IN_SCOPE | SHEETS->ITEMS |
| FILE-003 | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | XLSX | 068eecdaa550 | 167 | WORKBOOK | IN_SCOPE | SHEETS->ITEMS |
| FILE-004 | 99-TEMPLATE_CDM_OURO | TEXT | 62f85e8e3bc7 | 474 | TEMPLATE | IN_SCOPE | FULL |
| FILE-005 | ASA_-_RATIONALE_.txt | TXT | 4028780f2f6d | 1338 | CMD | IN_SCOPE | FULL |
| FILE-006 | BUSINESS_GMT_RATIONAL_ | TEXT | 9f7be64c9de1 | 268 | DECISION | IN_SCOPE | FULL |
| FILE-007 | BUSINESS_PACK_.txt | TXT | 10994f01cc64 | 824 | BRD_MRD_PRD | IN_SCOPE | FULL |
| FILE-008 | cluster_2_mercado_negocio_gtm_unificado.xlsx | XLSX | 757a2ce87dbd | 523 | WORKBOOK | IN_SCOPE | SHEETS->ITEMS |
| FILE-009 | clusters_1_6_7_10_teses_hipoteses_validacao.xlsx | XLSX | fd1a95bef0d3 | 1126 | WORKBOOK | IN_SCOPE | SHEETS->ITEMS |
| FILE-010 | CMD-OUTPUT-REQUIREMENTS-V2-EVOLVER.md | MD | 9b97a116b686 | 534 | CMD | IN_SCOPE | FULL |
| FILE-011 | Context | TEXT | a25b9ae8ca7e | 220 | PROJECT_CONTEXT | IN_SCOPE | FULL |
| FILE-012 | Contextos_adicionais_ | TEXT | 697f42450574 | 601 | PROJECT_CONTEXT | IN_SCOPE | FULL |
| FILE-013 | Continua_FAQ | TEXT | 9cb4a1004dcd | 59 | FAQ | IN_SCOPE | FULL |
| FILE-014 | copilottdahosworkbook.xlsx | XLSX | e2e4e135b69a | 135 | WORKBOOK | IN_SCOPE | SHEETS->ITEMS |
| FILE-015 | Customer_jorney_.txt | TXT | 05804441092d | 672 | CUSTOMER_JOURNEY | IN_SCOPE | FULL |
| FILE-016 | Desing_System_.txt | TXT | 741df5e56b63 | 552 | DESIGN_SYSTEM | IN_SCOPE | FULL |
| FILE-017 | DESK-OS-YAML-CARD | TEXT | dffef0cead38 | 79 | YAML_CARD | IN_SCOPE | FULL |
| FILE-018 | DESKOSMastering.xlsx | XLSX | 31a5860c053f | 5014 | WORKBOOK | IN_SCOPE | SHEETS->ITEMS |
| FILE-019 | ESPECIALISTA_AGENTE | TEXT | b954aee1223b | 313 | SPECIALIST | IN_SCOPE | FULL |
| FILE-020 | ESPECIALISTA_RATIONALE | TEXT | 89460569ff4e | 630 | SPECIALIST | IN_SCOPE | FULL |
| FILE-021 | FAQ | TEXT | ec31f8d48bca | 62 | FAQ | IN_SCOPE | FULL |
| FILE-022 | GTM_RATIONALE.txt | TXT | 9f7be64c9de1 | 268 | DECISION | IN_SCOPE | FULL |
| FILE-023 | ICPS-WORKFLOWS | TEXT | d31420e6fc1f | 1103 | ICP_WORKFLOWS | IN_SCOPE | FULL |
| FILE-024 | LEONARDO-OS.md | MD | d65195c6fb7a | 436 | MACRO | IN_SCOPE | FULL |
| FILE-025 | LEONARDO_MACRO_PERSONALIZATION___PROPRIETARY_SKILL_STACK.md | MD | 9079d7b5168f | 2629 | SKILL_STACK | IN_SCOPE | FULL |
| FILE-026 | MASTER-INDEX-AGENTIC-SYSTEMS-ARCHITECT.md | MD | a2e3537b6767 | 253 | MASTER_INDEX | IN_SCOPE | FULL |
| FILE-027 | MATER-FULL-PRINT | TEXT | 67668885806e | 1050 | UNIFIED_CATALOG | IN_SCOPE | FULL |
| FILE-028 | OUTPUT-REQUIREMNETS_ | TEXT | 34f9bd2c4681 | 1064 | OUTPUT_REQUIREMENTS | IN_SCOPE | FULL |
| FILE-029 | OUTPUT_REQUIREMENTS_V2.md | MD | e5772818bec1 | 740 | OUTPUT_REQUIREMENTS | IN_SCOPE | FULL |
| FILE-030 | OUTPUT_REQUIREMENTS_V3.md | MD | 0153c241ce43 | 640 | OUTPUT_REQUIREMENTS | IN_SCOPE | FULL |
| FILE-031 | PHARMACY_-_CMD | TEXT | fbbee4a348a5 | 415 | CMD | IN_SCOPE | FULL |
| FILE-032 | Propostas_de_wirfremes_.txt | TXT | 86d2f0d046de | 967 | WIREFRAME | IN_SCOPE | FULL |
| FILE-033 | RATIONAL_ADPT_txt.rtf | RTF | c5e4bb03f232 | 49 | DERIVATION | IN_SCOPE | FULL |
| FILE-034 | README | TEXT | e827b6944975 | 808 | MASTER_INDEX | IN_SCOPE | FULL |
| FILE-035 | README-ASA-TREEFILE.md | MD | 3ecf2043a280 | 170 | TREEFILE | IN_SCOPE | FULL |
| FILE-036 | RESUMO_EXECUTIVO_DO_PROJETO_ | TEXT | e7c0fa9b68b9 | 532 | EXECUTIVE_SUMMARY | IN_SCOPE | FULL |
| FILE-037 | SAKANA-BLUEPRINT_txt.rtf | RTF | f5016e9f5f72 | 65 | EXTERNAL_REFERENCE | IN_SCOPE | FULL |
| FILE-038 | SAKANA_TXT.rtf | RTF | 5b5c0c7bc4bd | 1 | EXTERNAL_REFERENCE | IN_SCOPE | FULL |
| FILE-039 | SOT_DESING_SYSTEM | TEXT | 41b66bfa0c08 | 552 | DESIGN_SYSTEM | IN_SCOPE | FULL |
| FILE-040 | Template_Minimo_Padronizacao_Processo.xlsx | XLSX | 36561891aa48 | 200 | WORKBOOK | IN_SCOPE | SHEETS->ITEMS |
| FILE-041 | UNIVERSAL_ICP_OPERATING_SYSTEM_SCHEMA.md | MD | 461c91e8eb5d | 1856 | ICP_SCHEMA | IN_SCOPE | FULL |
| FILE-042 | VARIÁVEIS_DO_AMBIENTE_ | TEXT | 8d6839fa05c8 | 38 | ENV_VARS | IN_SCOPE | FULL |
| FILE-043 | VARIÁVEIS_PERSONALIZADAS | TEXT | 00b681d7aeec | 520 | MECE_TRANSCRIPT | IN_SCOPE | FULL |
| FILE-044 | WF1.md | MD | f6db0a9a574c | 25 | WF | IN_SCOPE | FULL |
| FILE-045 | WF2.md | MD | 453329015e56 | 839 | WF | IN_SCOPE | FULL |
| FILE-046 | WF3.md | MD | 7622ac78c116 | 792 | WF | IN_SCOPE | FULL |
| FILE-047 | WF4.md | MD | 9a0c83032820 | 811 | WF | IN_SCOPE | FULL |
| FILE-048 | WF5.md | MD | 03b2d4ac820d | 964 | WF | IN_SCOPE | FULL |
| FILE-049 | WF6.md | MD | 0669e07cfef5 | 1249 | WF | IN_SCOPE | FULL |
| FILE-050 | Wireframe | TEXT | a9b30cdc79b1 | 267 | WIREFRAME | IN_SCOPE | FULL |
| FILE-051 | Wireframe_2 | TEXT | 2a5278e0a980 | 921 | WIREFRAME | IN_SCOPE | FULL |
| FILE-052 | Workflowagentico | TEXT | 969038a83333 | 1133 | WF_MASTER | IN_SCOPE | FULL |
| FILE-053 | YAML_Card_Leonard_os_ | TEXT | 6cac1a65ff55 | 896 | YAML_CARD | IN_SCOPE | FULL |
| FILE-054 | Yamls_card_2_deskos_ | TEXT | 50419b1237b1 | 945 | YAML_CARD | IN_SCOPE | FULL |
| SYS-001 | master_index.json | JSON | 708da6d7656a | '- | INDEX_ARTIFACT | EXCLUDED | N/A |
| SYS-002 | MASTER_INDEX.md | MD | 51aff3e952d2 | '- | INDEX_ARTIFACT | EXCLUDED | N/A |

# APÊNDICE B — Full Items Master (163 itens)

| item_id | item_name | entity_type | program_id | product_id | cluster_id | item_type | status | authority | documentation | source_basis | source_file | source_sheet | parent_item_id | review_required | next_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FILE-001 | 03DESKOSPLANILHAMESTRA.xlsx | FILE_WORKBOOK | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | CONFIRMED | SUPERSEDED | PRESENT | FILE | 03DESKOSPLANILHAMESTRA.xlsx | 03DESKOSPLANILHAMESTRA.xlsx |  |  |  |
| FILE-002 | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | FILE_WORKBOOK | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | CONFIRMED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx |  |  |  |
| FILE-003 | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | FILE_WORKBOOK | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx |  | SIM | Validar classificacao |
| FILE-004 | 99-TEMPLATE_CDM_OURO | TEMPLATE |  |  | C07 | TEMPLATE | CONFIRMED | WORKING | PRESENT | FILE | 99-TEMPLATE_CDM_OURO | 99-TEMPLATE_CDM_OURO |  |  |  |
| FILE-005 | ASA_-_RATIONALE_.txt | RATIONALE | PRG-ASA | PRD-ASA | C04 | CMD | CONFIRMED | WORKING | PRESENT | FILE | ASA_-_RATIONALE_.txt | ASA_-_RATIONALE_.txt |  |  |  |
| FILE-006 | BUSINESS_GMT_RATIONAL_ | RATIONALE | PRG-SMALL-BUSINESS |  | C02 | DECISION | CONFIRMED | DUPLICATE_COPY | PRESENT | FILE | BUSINESS_GMT_RATIONAL_ | BUSINESS_GMT_RATIONAL_ |  |  |  |
| FILE-007 | BUSINESS_PACK_.txt | PRODUCT_DOC | PRG-DESK-OS | PRD-DESK-OS | C01 | BRD_MRD_PRD | CONFIRMED | WORKING | PRESENT | FILE | BUSINESS_PACK_.txt | BUSINESS_PACK_.txt |  |  |  |
| FILE-008 | cluster_2_mercado_negocio_gtm_unificado.xlsx | FILE_WORKBOOK | PRG-SMALL-BUSINESS |  | C02 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | cluster_2_mercado_negocio_gtm_unificado.xlsx | cluster_2_mercado_negocio_gtm_unificado.xlsx |  | SIM | Validar classificacao |
| FILE-009 | clusters_1_6_7_10_teses_hipoteses_validacao.xlsx | FILE_WORKBOOK |  |  | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | clusters_1_6_7_10_teses_hipoteses_validacao.xlsx | clusters_1_6_7_10_teses_hipoteses_validacao.xlsx |  | SIM | Validar classificacao |
| FILE-010 | CMD-OUTPUT-REQUIREMENTS-V2-EVOLVER.md | COMMAND |  |  | C06 | CMD | CONFIRMED | WORKING | PRESENT | FILE | CMD-OUTPUT-REQUIREMENTS-V2-EVOLVER.md | CMD-OUTPUT-REQUIREMENTS-V2-EVOLVER.md |  |  |  |
| FILE-011 | Context | PROJECT_CONTEXT |  |  | C09 | PROJECT_CONTEXT | CONFIRMED | WORKING | PRESENT | FILE | Context | Context |  |  |  |
| FILE-012 | Contextos_adicionais_ | PROJECT_CONTEXT | PRG-DESK-OS | PRD-DESK-OS | C04 | PROJECT_CONTEXT | REVIEW_REQUIRED | WORKING | PRESENT | FILE | Contextos_adicionais_ | Contextos_adicionais_ |  | SIM | Validar classificacao |
| FILE-013 | Continua_FAQ | FAQ |  |  | C06 | FAQ | PROPOSED | DRAFT | PARTIAL | FILE | Continua_FAQ | Continua_FAQ |  | SIM | Validar classificacao |
| FILE-014 | copilottdahosworkbook.xlsx | FILE_WORKBOOK | PRG-TDAH | PRD-COPILOTO-TDAH | C11 | WORKBOOK | CONFIRMED | WORKING | PRESENT | FILE | copilottdahosworkbook.xlsx | copilottdahosworkbook.xlsx |  |  |  |
| FILE-015 | Customer_jorney_.txt | PRODUCT_DOC | PRG-DESK-OS | PRD-DESK-OS | C01 | CUSTOMER_JOURNEY | CONFIRMED | WORKING | PRESENT | FILE | Customer_jorney_.txt | Customer_jorney_.txt |  |  |  |
| FILE-016 | Desing_System_.txt | DESIGN | PRG-DESK-OS | PRD-DESK-OS | C08 | DESIGN_SYSTEM | REVIEW_REQUIRED | REFERENCE | PRESENT | FILE | Desing_System_.txt | Desing_System_.txt |  | SIM | Validar classificacao |
| FILE-017 | DESK-OS-YAML-CARD | YAML_CARD | PRG-DESK-OS | PRD-DESK-OS | C04 | YAML_CARD | CONFIRMED | WORKING | PRESENT | FILE | DESK-OS-YAML-CARD | DESK-OS-YAML-CARD |  |  |  |
| FILE-018 | DESKOSMastering.xlsx | FILE_WORKBOOK | PRG-DESK-OS | PRD-DESK-OS | C09 | WORKBOOK | CONFIRMED | WORKING | PRESENT | FILE | DESKOSMastering.xlsx | DESKOSMastering.xlsx |  |  |  |
| FILE-019 | ESPECIALISTA_AGENTE | RATIONALE | PRG-LEONARDO-OS | PRD-LEONARDO-OS | C05 | SPECIALIST | PROPOSED | WORKING | PRESENT | FILE | ESPECIALISTA_AGENTE | ESPECIALISTA_AGENTE |  | SIM | Validar classificacao |
| FILE-020 | ESPECIALISTA_RATIONALE | RATIONALE | PRG-LEONARDO-OS | PRD-LEONARDO-OS | C05 | SPECIALIST | PROPOSED | WORKING | PRESENT | FILE | ESPECIALISTA_RATIONALE | ESPECIALISTA_RATIONALE |  | SIM | Validar classificacao |
| FILE-021 | FAQ | FAQ |  |  | C09 | FAQ | PROPOSED | DRAFT | PARTIAL | FILE | FAQ | FAQ |  | SIM | Validar classificacao |
| FILE-022 | GTM_RATIONALE.txt | RATIONALE | PRG-SMALL-BUSINESS |  | C02 | DECISION | CONFIRMED | APPROVED | PRESENT | FILE | GTM_RATIONALE.txt | GTM_RATIONALE.txt |  |  |  |
| FILE-023 | ICPS-WORKFLOWS | WORKFLOW |  |  | C06 | ICP_WORKFLOWS | CONFIRMED | WORKING | PRESENT | FILE | ICPS-WORKFLOWS | ICPS-WORKFLOWS |  |  |  |
| FILE-024 | LEONARDO-OS.md | MACRO_PERSONALIZATION | PRG-LEONARDO-OS | PRD-LEONARDO-OS | C05 | MACRO | CONFIRMED | WORKING | PRESENT | FILE | LEONARDO-OS.md | LEONARDO-OS.md |  |  |  |
| FILE-025 | LEONARDO_MACRO_PERSONALIZATION___PROPRIETARY_SKILL_STACK.md | MACRO_PERSONALIZATION | PRG-LEONARDO-OS | PRD-LEONARDO-OS | C05 | SKILL_STACK | CONFIRMED | SSOT | PRESENT | FILE | LEONARDO_MACRO_PERSONALIZATION___PROPRIETARY_SKILL_STACK.md | LEONARDO_MACRO_PERSONALIZATION___PROPRIETARY_SKILL_STACK.md |  |  |  |
| FILE-026 | MASTER-INDEX-AGENTIC-SYSTEMS-ARCHITECT.md | INDEX | PRG-ASA | PRD-ASA | C10 | MASTER_INDEX | CONFIRMED | WORKING | PRESENT | FILE | MASTER-INDEX-AGENTIC-SYSTEMS-ARCHITECT.md | MASTER-INDEX-AGENTIC-SYSTEMS-ARCHITECT.md |  |  |  |
| FILE-027 | MATER-FULL-PRINT | CATALOG |  |  | C10 | UNIFIED_CATALOG | CONFIRMED | WORKING | PRESENT | FILE | MATER-FULL-PRINT | MATER-FULL-PRINT |  |  |  |
| FILE-028 | OUTPUT-REQUIREMNETS_ | REQUIREMENTS |  |  | C05 | OUTPUT_REQUIREMENTS | CONFIRMED | SUPERSEDED | PRESENT | FILE | OUTPUT-REQUIREMNETS_ | OUTPUT-REQUIREMNETS_ |  |  |  |
| FILE-029 | OUTPUT_REQUIREMENTS_V2.md | REQUIREMENTS |  |  | C05 | OUTPUT_REQUIREMENTS | CONFIRMED | SUPERSEDED | PRESENT | FILE | OUTPUT_REQUIREMENTS_V2.md | OUTPUT_REQUIREMENTS_V2.md |  |  |  |
| FILE-030 | OUTPUT_REQUIREMENTS_V3.md | REQUIREMENTS |  |  | C05 | OUTPUT_REQUIREMENTS | CONFIRMED | WORKING | PRESENT | FILE | OUTPUT_REQUIREMENTS_V3.md | OUTPUT_REQUIREMENTS_V3.md |  |  |  |
| FILE-031 | PHARMACY_-_CMD | COMMAND |  |  | C06 | CMD | CONFIRMED | WORKING | PRESENT | FILE | PHARMACY_-_CMD | PHARMACY_-_CMD |  |  |  |
| FILE-032 | Propostas_de_wirfremes_.txt | DESIGN | PRG-DESK-OS | PRD-DESK-OS | C08 | WIREFRAME | CONFIRMED | WORKING | PRESENT | FILE | Propostas_de_wirfremes_.txt | Propostas_de_wirfremes_.txt |  |  |  |
| FILE-033 | RATIONAL_ADPT_txt.rtf | REFERENCE | PRG-ASA | PRD-ASA | C03 | DERIVATION | REVIEW_REQUIRED | REFERENCE | PRESENT | FILE | RATIONAL_ADPT_txt.rtf | RATIONAL_ADPT_txt.rtf |  | SIM | Validar classificacao |
| FILE-034 | README | INDEX |  |  | C10 | MASTER_INDEX | CONFIRMED | WORKING | PRESENT | FILE | README | README |  |  |  |
| FILE-035 | README-ASA-TREEFILE.md | INDEX | PRG-ASA | PRD-ASA | C10 | TREEFILE | CONFIRMED | WORKING | PRESENT | FILE | README-ASA-TREEFILE.md | README-ASA-TREEFILE.md |  |  |  |
| FILE-036 | RESUMO_EXECUTIVO_DO_PROJETO_ | PROJECT_CONTEXT |  |  | C01 | EXECUTIVE_SUMMARY | CONFIRMED | WORKING | PRESENT | FILE | RESUMO_EXECUTIVO_DO_PROJETO_ | RESUMO_EXECUTIVO_DO_PROJETO_ |  |  |  |
| FILE-037 | SAKANA-BLUEPRINT_txt.rtf | REFERENCE | PRG-ASA | PRD-ASA | C03 | EXTERNAL_REFERENCE | CONFIRMED | REFERENCE | PRESENT | FILE | SAKANA-BLUEPRINT_txt.rtf | SAKANA-BLUEPRINT_txt.rtf |  |  |  |
| FILE-038 | SAKANA_TXT.rtf | REFERENCE | PRG-ASA | PRD-ASA | C03 | EXTERNAL_REFERENCE | CONFIRMED | REFERENCE | PARTIAL | FILE | SAKANA_TXT.rtf | SAKANA_TXT.rtf |  |  |  |
| FILE-039 | SOT_DESING_SYSTEM | DESIGN | PRG-DESK-OS | PRD-DESK-OS | C08 | DESIGN_SYSTEM | REVIEW_REQUIRED | WORKING | PRESENT | FILE | SOT_DESING_SYSTEM | SOT_DESING_SYSTEM |  | SIM | Validar classificacao |
| FILE-040 | Template_Minimo_Padronizacao_Processo.xlsx | FILE_WORKBOOK |  |  | C07 | WORKBOOK | CONFIRMED | WORKING | PRESENT | FILE | Template_Minimo_Padronizacao_Processo.xlsx | Template_Minimo_Padronizacao_Processo.xlsx |  |  |  |
| FILE-041 | UNIVERSAL_ICP_OPERATING_SYSTEM_SCHEMA.md | SCHEMA |  |  | C05 | ICP_SCHEMA | CONFIRMED | WORKING | PRESENT | FILE | UNIVERSAL_ICP_OPERATING_SYSTEM_SCHEMA.md | UNIVERSAL_ICP_OPERATING_SYSTEM_SCHEMA.md |  |  |  |
| FILE-042 | VARIÁVEIS_DO_AMBIENTE_ | MACRO_PERSONALIZATION | PRG-LEONARDO-OS | PRD-LEONARDO-OS | C05 | ENV_VARS | CONFIRMED | WORKING | PARTIAL | FILE | VARIÁVEIS_DO_AMBIENTE_ | VARIÁVEIS_DO_AMBIENTE_ |  |  |  |
| FILE-043 | VARIÁVEIS_PERSONALIZADAS | DIRECTORY |  |  | C10 | MECE_TRANSCRIPT | CONFIRMED | WORKING | PRESENT | FILE | VARIÁVEIS_PERSONALIZADAS | VARIÁVEIS_PERSONALIZADAS |  |  |  |
| FILE-044 | WF1.md | WORKFLOW |  |  | C06 | WF | PROPOSED | WORKING | PRESENT | FILE | WF1.md | WF1.md |  | SIM | Validar classificacao |
| FILE-045 | WF2.md | WORKFLOW |  |  | C06 | WF | PROPOSED | WORKING | PRESENT | FILE | WF2.md | WF2.md |  | SIM | Validar classificacao |
| FILE-046 | WF3.md | WORKFLOW | PRG-ASA | PRD-ASA | C06 | WF | PROPOSED | WORKING | PRESENT | FILE | WF3.md | WF3.md |  | SIM | Validar classificacao |
| FILE-047 | WF4.md | WORKFLOW | PRG-ASA | PRD-ASA | C06 | WF | PROPOSED | WORKING | PRESENT | FILE | WF4.md | WF4.md |  | SIM | Validar classificacao |
| FILE-048 | WF5.md | WORKFLOW | PRG-ASA | PRD-ASA | C03 | WF | REVIEW_REQUIRED | REFERENCE | PRESENT | FILE | WF5.md | WF5.md |  | SIM | Validar classificacao |
| FILE-049 | WF6.md | WORKFLOW | PRG-ASA | PRD-ASA | C06 | WF | PROPOSED | WORKING | PRESENT | FILE | WF6.md | WF6.md |  | SIM | Validar classificacao |
| FILE-050 | Wireframe | DESIGN | PRG-DESK-OS | PRD-DESK-OS | C08 | WIREFRAME | CONFIRMED | WORKING | PRESENT | FILE | Wireframe | Wireframe |  |  |  |
| FILE-051 | Wireframe_2 | DESIGN | PRG-DESK-OS | PRD-DESK-OS | C08 | WIREFRAME | CONFIRMED | WORKING | PRESENT | FILE | Wireframe_2 | Wireframe_2 |  |  |  |
| FILE-052 | Workflowagentico | WORKFLOW |  |  | C06 | WF_MASTER | CONFIRMED | WORKING | PRESENT | FILE | Workflowagentico | Workflowagentico |  |  |  |
| FILE-053 | YAML_Card_Leonard_os_ | YAML_CARD | PRG-LEONARDO-OS | PRD-LEONARDO-OS | C04 | YAML_CARD | CONFIRMED | WORKING | PRESENT | FILE | YAML_Card_Leonard_os_ | YAML_Card_Leonard_os_ |  |  |  |
| FILE-054 | Yamls_card_2_deskos_ | YAML_CARD | PRG-DESK-OS | PRD-DESK-OS | C04 | YAML_CARD | CONFIRMED | WORKING | PRESENT | FILE | Yamls_card_2_deskos_ | Yamls_card_2_deskos_ |  |  |  |
| ITEM-018-S001 | 00_Dashboard | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | DESKOSMastering.xlsx | 00_Dashboard | FILE-018 | SIM |  |
| ITEM-018-S002 | 01_Timeline | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | DESKOSMastering.xlsx | 01_Timeline | FILE-018 | SIM |  |
| ITEM-018-S003 | 02_Fases | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | DESKOSMastering.xlsx | 02_Fases | FILE-018 | SIM |  |
| ITEM-018-S004 | 03_Artefatos | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | DESKOSMastering.xlsx | 03_Artefatos | FILE-018 | SIM |  |
| ITEM-018-S005 | 04_Schema_3x3 | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | DESKOSMastering.xlsx | 04_Schema_3x3 | FILE-018 | SIM |  |
| ITEM-018-S006 | 05_Mapa_Faces | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | DESKOSMastering.xlsx | 05_Mapa_Faces | FILE-018 | SIM |  |
| ITEM-018-S007 | 06_Subagentes | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | DESKOSMastering.xlsx | 06_Subagentes | FILE-018 | SIM |  |
| ITEM-018-S008 | 07_Decisoes | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | DESKOSMastering.xlsx | 07_Decisoes | FILE-018 | SIM |  |
| ITEM-018-S009 | 08_Gaps_Roadmap | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | DESKOSMastering.xlsx | 08_Gaps_Roadmap | FILE-018 | SIM |  |
| ITEM-018-S010 | 09_Indice_Arquivos | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | DESKOSMastering.xlsx | 09_Indice_Arquivos | FILE-018 | SIM |  |
| ITEM-018-S011 | 10_Releases | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | DESKOSMastering.xlsx | 10_Releases | FILE-018 | SIM |  |
| ITEM-009-S012 | 00_DASHBOARD | SHEET_ITEM |  |  | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | clusters_1_6_7_10_teses_hipoteses_validacao.xlsx | 00_DASHBOARD | FILE-009 | SIM |  |
| ITEM-009-S013 | 01_MASTER_VALIDACAO | SHEET_ITEM |  |  | C09 | WORKBOOK | REVIEW_REQUIRED | WORKING | PRESENT | FILE | clusters_1_6_7_10_teses_hipoteses_validacao.xlsx | 01_MASTER_VALIDACAO | FILE-009 | SIM | Inspecionar secoes |
| ITEM-009-S014 | 02_METODOLOGIA | SHEET_ITEM |  |  | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | clusters_1_6_7_10_teses_hipoteses_validacao.xlsx | 02_METODOLOGIA | FILE-009 | SIM |  |
| ITEM-009-S015 | C1_ESTRATEGIA | SHEET_ITEM |  |  | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | clusters_1_6_7_10_teses_hipoteses_validacao.xlsx | C1_ESTRATEGIA | FILE-009 | SIM |  |
| ITEM-009-S016 | C6_CONTEUDO | SHEET_ITEM |  |  | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | clusters_1_6_7_10_teses_hipoteses_validacao.xlsx | C6_CONTEUDO | FILE-009 | SIM |  |
| ITEM-009-S017 | C7_DESIGN_UX | SHEET_ITEM |  |  | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | clusters_1_6_7_10_teses_hipoteses_validacao.xlsx | C7_DESIGN_UX | FILE-009 | SIM |  |
| ITEM-009-S018 | C10_TECNOLOGIA | SHEET_ITEM |  |  | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | clusters_1_6_7_10_teses_hipoteses_validacao.xlsx | C10_TECNOLOGIA | FILE-009 | SIM |  |
| ITEM-009-S019 | 99_LISTAS | SHEET_ITEM |  |  | C09 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | clusters_1_6_7_10_teses_hipoteses_validacao.xlsx | 99_LISTAS | FILE-009 | SIM |  |
| ITEM-008-S020 | 00_RESUMO | SHEET_ITEM | PRG-SMALL-BUSINESS |  | C02 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | cluster_2_mercado_negocio_gtm_unificado.xlsx | 00_RESUMO | FILE-008 | SIM |  |
| ITEM-008-S021 | 01_CLUSTER_2_UNIFICADO | SHEET_ITEM | PRG-SMALL-BUSINESS |  | C02 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | cluster_2_mercado_negocio_gtm_unificado.xlsx | 01_CLUSTER_2_UNIFICADO | FILE-008 | SIM |  |
| ITEM-008-S022 | 02_CRITERIOS | SHEET_ITEM | PRG-SMALL-BUSINESS |  | C02 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | cluster_2_mercado_negocio_gtm_unificado.xlsx | 02_CRITERIOS | FILE-008 | SIM |  |
| ITEM-040-S023 | Fluxo Completo | SHEET_ITEM |  |  | C07 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | Template_Minimo_Padronizacao_Processo.xlsx | Fluxo Completo | FILE-040 | SIM |  |
| ITEM-040-S024 | Diagnóstico AS IS | SHEET_ITEM |  |  | C07 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | Template_Minimo_Padronizacao_Processo.xlsx | Diagnóstico AS IS | FILE-040 | SIM |  |
| ITEM-040-S025 | TO BE e Piloto | SHEET_ITEM |  |  | C07 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | Template_Minimo_Padronizacao_Processo.xlsx | TO BE e Piloto | FILE-040 | SIM |  |
| ITEM-040-S026 | SOP | SHEET_ITEM |  |  | C07 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | Template_Minimo_Padronizacao_Processo.xlsx | SOP | FILE-040 | SIM |  |
| ITEM-040-S027 | Implantação e Controle | SHEET_ITEM |  |  | C07 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | Template_Minimo_Padronizacao_Processo.xlsx | Implantação e Controle | FILE-040 | SIM |  |
| ITEM-002-S028 | Dashboard | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Dashboard | FILE-002 | SIM |  |
| ITEM-002-S029 | Requisitos | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Requisitos | FILE-002 | SIM |  |
| ITEM-002-S030 | Geometria | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Geometria | FILE-002 | SIM |  |
| ITEM-002-S031 | Storyboard | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Storyboard | FILE-002 | SIM |  |
| ITEM-002-S032 | Fluxos_QR | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Fluxos_QR | FILE-002 | SIM |  |
| ITEM-002-S033 | Decisoes_Riscos | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Decisoes_Riscos | FILE-002 | SIM |  |
| ITEM-002-S034 | Fontes | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Fontes | FILE-002 | SIM |  |
| ITEM-002-S035 | Board_PreDev | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Board_PreDev | FILE-002 | SIM |  |
| ITEM-002-S036 | Insumos_V2 | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | REVIEW_REQUIRED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Insumos_V2 | FILE-002 | SIM | Inspecionar secoes |
| ITEM-002-S037 | Arquitetura_Atual | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | REVIEW_REQUIRED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Arquitetura_Atual | FILE-002 | SIM | Inspecionar secoes |
| ITEM-002-S038 | Curso_Orchestrator | SHEET_ITEM | PRG-EDUCATION | PRD-COURSE-EXPRESS | C04 | SKILL | REVIEW_REQUIRED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Curso_Orchestrator | FILE-002 | SIM |  |
| ITEM-002-S039 | GTM_Launch | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | REVIEW_REQUIRED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | GTM_Launch | FILE-002 | SIM | Inspecionar secoes |
| ITEM-002-S040 | Backlog_Update | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Backlog_Update | FILE-002 | SIM |  |
| ITEM-002-S041 | Sessoes_Update | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Sessoes_Update | FILE-002 | SIM |  |
| ITEM-002-S042 | Outputs_V3 | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Outputs_V3 | FILE-002 | SIM |  |
| ITEM-002-S043 | Skill_AI_Gov | SHEET_ITEM | PRG-ASA | PRD-ASA | C06 | SKILL | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Skill_AI_Gov | FILE-002 | SIM |  |
| ITEM-002-S044 | Skill_Project_Standalone | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Skill_Project_Standalone | FILE-002 | SIM |  |
| ITEM-002-S045 | Skill_Anthropic_Handoff | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Skill_Anthropic_Handoff | FILE-002 | SIM |  |
| ITEM-002-S046 | Skill_Leonardo_Orch | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Skill_Leonardo_Orch | FILE-002 | SIM |  |
| ITEM-002-S047 | Skill_Meta_Template | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Skill_Meta_Template | FILE-002 | SIM |  |
| ITEM-002-S048 | Skill_Padrao_OS | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Skill_Padrao_OS | FILE-002 | SIM |  |
| ITEM-002-S049 | Skill_Project_Cleaner | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Skill_Project_Cleaner | FILE-002 | SIM |  |
| ITEM-002-S050 | Skill_Standalone_Orch | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Skill_Standalone_Orch | FILE-002 | SIM |  |
| ITEM-002-S051 | Evil_Tests_V3 | SHEET_ITEM |  |  | C09 | EVALUATION_TEST | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Evil_Tests_V3 | FILE-002 | SIM |  |
| ITEM-002-S052 | Macro_Personalizacao | SHEET_ITEM |  |  | C05 | MACRO | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Macro_Personalizacao | FILE-002 | SIM |  |
| ITEM-002-S053 | ICP_Cascata_Lego | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | ICP_Cascata_Lego | FILE-002 | SIM |  |
| ITEM-002-S054 | TDHA_Superpowers | SHEET_ITEM | PRG-TDAH | PRD-TDAH-OS | C11 | CONTENT | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | TDHA_Superpowers | FILE-002 | SIM |  |
| ITEM-002-S055 | GTM_Semana1_Template | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | GTM_Semana1_Template | FILE-002 | SIM |  |
| ITEM-002-S056 | Product_Mkt_Feed | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Product_Mkt_Feed | FILE-002 | SIM |  |
| ITEM-002-S057 | Briefing_Codificado | SHEET_ITEM |  |  | C07 | CODED_BRIEFING | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Briefing_Codificado | FILE-002 | SIM |  |
| ITEM-002-S058 | Trigger_README | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Trigger_README | FILE-002 | SIM |  |
| ITEM-002-S059 | Trigger_LONG | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Trigger_LONG | FILE-002 | SIM |  |
| ITEM-002-S060 | Trigger_TOP | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Trigger_TOP | FILE-002 | SIM |  |
| ITEM-002-S061 | Trigger_MECE | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Trigger_MECE | FILE-002 | SIM |  |
| ITEM-002-S062 | Trigger_Prop_Map | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Trigger_Prop_Map | FILE-002 | SIM |  |
| ITEM-002-S063 | Palantir_Codificado | SHEET_ITEM |  |  | C03 | EXTERNAL_REFERENCE | REVIEW_REQUIRED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Palantir_Codificado | FILE-002 | SIM |  |
| ITEM-002-S064 | Benchmark_Verificado | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Benchmark_Verificado | FILE-002 | SIM |  |
| ITEM-002-S065 | IDX_Praxis_SSOT | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | IDX_Praxis_SSOT | FILE-002 | SIM |  |
| ITEM-002-S066 | Backlog_V3 | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Backlog_V3 | FILE-002 | SIM |  |
| ITEM-002-S067 | Sessoes_V3 | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Sessoes_V3 | FILE-002 | SIM |  |
| ITEM-002-S068 | Fontes_V3 | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 03DESKOSPLANILHAMESTRAV3OUTPUTSBENCHMARK.xlsx | Fontes_V3 | FILE-002 | SIM |  |
| ITEM-001-S069 | Dashboard | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | SUPERSEDED | PRESENT | FILE | 03DESKOSPLANILHAMESTRA.xlsx | Dashboard | FILE-001 | SIM |  |
| ITEM-001-S070 | Requisitos | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | SUPERSEDED | PRESENT | FILE | 03DESKOSPLANILHAMESTRA.xlsx | Requisitos | FILE-001 | SIM |  |
| ITEM-001-S071 | Geometria | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | SUPERSEDED | PRESENT | FILE | 03DESKOSPLANILHAMESTRA.xlsx | Geometria | FILE-001 | SIM |  |
| ITEM-001-S072 | Storyboard | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | SUPERSEDED | PRESENT | FILE | 03DESKOSPLANILHAMESTRA.xlsx | Storyboard | FILE-001 | SIM |  |
| ITEM-001-S073 | Fluxos_QR | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | SUPERSEDED | PRESENT | FILE | 03DESKOSPLANILHAMESTRA.xlsx | Fluxos_QR | FILE-001 | SIM |  |
| ITEM-001-S074 | Decisoes_Riscos | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | SUPERSEDED | PRESENT | FILE | 03DESKOSPLANILHAMESTRA.xlsx | Decisoes_Riscos | FILE-001 | SIM |  |
| ITEM-001-S075 | Fontes | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | SUPERSEDED | PRESENT | FILE | 03DESKOSPLANILHAMESTRA.xlsx | Fontes | FILE-001 | SIM |  |
| ITEM-001-S076 | Board_PreDev | SHEET_ITEM | PRG-DESK-OS | PRD-DESK-OS | C04 | WORKBOOK | PROPOSED | SUPERSEDED | PRESENT | FILE | 03DESKOSPLANILHAMESTRA.xlsx | Board_PreDev | FILE-001 | SIM |  |
| ITEM-003-S077 | README | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | README | FILE-003 | SIM |  |
| ITEM-003-S078 | PAGINAS | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | PAGINAS | FILE-003 | SIM |  |
| ITEM-003-S079 | CLAIMS_E_DADOS | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | CLAIMS_E_DADOS | FILE-003 | SIM |  |
| ITEM-003-S080 | PALAVRAS_CHAVE | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | PALAVRAS_CHAVE | FILE-003 | SIM |  |
| ITEM-003-S081 | PUBLICO | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | PUBLICO | FILE-003 | SIM |  |
| ITEM-003-S082 | CONCORRENTES | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | CONCORRENTES | FILE-003 | SIM |  |
| ITEM-003-S083 | TECNICAS | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | TECNICAS | FILE-003 | SIM |  |
| ITEM-003-S084 | SISTEMA_EDITORIAL | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | SISTEMA_EDITORIAL | FILE-003 | SIM |  |
| ITEM-003-S085 | CALENDARIO | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | CALENDARIO | FILE-003 | SIM |  |
| ITEM-003-S086 | ROTINA_SEMANAL | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | ROTINA_SEMANAL | FILE-003 | SIM |  |
| ITEM-003-S087 | TEMPLATE_CARROSSEL | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | TEMPLATE_CARROSSEL | FILE-003 | SIM |  |
| ITEM-003-S088 | GAPS | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | GAPS | FILE-003 | SIM |  |
| ITEM-003-S089 | OCR_BRUTO | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | OCR_BRUTO | FILE-003 | SIM |  |
| ITEM-003-S090 | RESUMO | SHEET_ITEM | PRG-TDAH |  | C12 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | 2306_DADOS_ESTRUTURADOS_COMPLETO.xlsx | RESUMO | FILE-003 | SIM |  |
| ITEM-014-S091 | 01_Project_State | SHEET_ITEM | PRG-TDAH | PRD-COPILOTO-TDAH | C11 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | copilottdahosworkbook.xlsx | 01_Project_State | FILE-014 | SIM |  |
| ITEM-014-S092 | 02_GTM_Calendar_D0-D90 | SHEET_ITEM | PRG-TDAH | PRD-COPILOTO-TDAH | C11 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | copilottdahosworkbook.xlsx | 02_GTM_Calendar_D0-D90 | FILE-014 | SIM |  |
| ITEM-014-S093 | 03_Evidence_Ledger | SHEET_ITEM | PRG-TDAH | PRD-COPILOTO-TDAH | C11 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | copilottdahosworkbook.xlsx | 03_Evidence_Ledger | FILE-014 | SIM |  |
| ITEM-014-S094 | 04_Skills_Registry | SHEET_ITEM | PRG-TDAH | PRD-COPILOTO-TDAH | C11 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | copilottdahosworkbook.xlsx | 04_Skills_Registry | FILE-014 | SIM |  |
| ITEM-014-S095 | 05_72H_Master_Plan | SHEET_ITEM | PRG-TDAH | PRD-COPILOTO-TDAH | C11 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | copilottdahosworkbook.xlsx | 05_72H_Master_Plan | FILE-014 | SIM |  |
| ITEM-014-S096 | 06_ICP_Competitors | SHEET_ITEM | PRG-TDAH | PRD-COPILOTO-TDAH | C11 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | copilottdahosworkbook.xlsx | 06_ICP_Competitors | FILE-014 | SIM |  |
| ITEM-014-S097 | 07_Decisions_Log | SHEET_ITEM | PRG-TDAH | PRD-COPILOTO-TDAH | C11 | WORKBOOK | PROPOSED | WORKING | PRESENT | FILE | copilottdahosworkbook.xlsx | 07_Decisions_Log | FILE-014 | SIM |  |
| ITM-MEM-001 | CAP-AGENT-FACTORY | CAPABILITY |  |  | C04 | CAPABILITY | REVIEW_REQUIRED | DRAFT | MISSING | PROVIDED_PROJECT_CONTEXT |  |  | PRG-ASA | SIM | Validar com evidencia |
| ITM-MEM-002 | TRACK-TDAH | TRACK |  |  | C11 | TRACK | PROPOSED | DRAFT | MISSING | PROVIDED_PROJECT_CONTEXT |  |  | PRD-COURSE-EXPRESS | SIM | Validar com evidencia |
| ITM-MEM-003 | TRACK-MACRO-PERSONALIZATION | TRACK |  |  | C05 | TRACK | PROPOSED | DRAFT | MISSING | PROVIDED_PROJECT_CONTEXT |  |  | PRD-COURSE-EXPRESS | SIM | Validar com evidencia |
| ITM-MEM-004 | TRACK-ANTHROPIC-STACK | TRACK |  |  | C04 | TRACK | PROPOSED | DRAFT | MISSING | PROVIDED_PROJECT_CONTEXT |  |  | PRD-COURSE-EXPRESS | SIM | Validar com evidencia |
| ITM-MEM-005 | TRACK-CLAUDE-POWER-USER | TRACK |  |  | C10 | TRACK | PROPOSED | DRAFT | MISSING | PROVIDED_PROJECT_CONTEXT |  |  | PRD-COURSE-EXPRESS | SIM | Validar com evidencia |
| ITM-MEM-006 | INIT-GTM-SHOWROOM | INITIATIVE |  |  | C02 | INITIATIVE | PROPOSED | DRAFT | MISSING | PROVIDED_PROJECT_CONTEXT |  |  | PRG-SMALL-BUSINESS | SIM | Validar com evidencia |
| ITM-MEM-007 | INIT-AGENCY-KIT | INITIATIVE |  |  | C02 | INITIATIVE | PROPOSED | DRAFT | MISSING | PROVIDED_PROJECT_CONTEXT |  |  | PRG-SMALL-BUSINESS | SIM | Validar com evidencia |
| ITM-MEM-008 | MODULE-M1 | MODULE |  |  | C02 | MODULE | REVIEW_REQUIRED | DRAFT | MISSING | PROVIDED_PROJECT_CONTEXT |  |  | PRD-BUSINESS-SUITE | SIM | Validar com evidencia |
| ITM-MEM-009 | MODULE-M2 | MODULE |  |  | C02 | MODULE | REVIEW_REQUIRED | DRAFT | MISSING | PROVIDED_PROJECT_CONTEXT |  |  | PRD-BUSINESS-SUITE | SIM | Validar com evidencia |
| ITM-MEM-010 | MODULE-M5 | MODULE |  |  | C02 | MODULE | REVIEW_REQUIRED | DRAFT | MISSING | PROVIDED_PROJECT_CONTEXT |  |  | PRD-BUSINESS-SUITE | SIM | Validar com evidencia |
| ITM-MEM-011 | PRODUCT-SETUP-SUITE | OFFER |  |  | C04 | OFFER | REVIEW_REQUIRED | DRAFT | MISSING | PROVIDED_PROJECT_CONTEXT |  |  | PRD-LEONARDO-OS | SIM | Validar com evidencia |
| ITM-MEM-012 | PRODUCT-AI-OS-RESET | OFFER |  |  | C04 | OFFER | REVIEW_REQUIRED | DRAFT | MISSING | PROVIDED_PROJECT_CONTEXT |  |  | PRD-LEONARDO-OS | SIM | Validar com evidencia |

# APÊNDICE C — Full Entity Registry

| entity_id | entity_name | type | parent | cluster | authority | classification | source_basis | strategic_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRJ-LEONARDO-001 | PROJECT-LEONARDO-ECOSYSTEM | PROJECT | '- | '- | SSOT | CONFIRMED | FILE | Raiz do ecossistema. |
| PRG-ASA | PROGRAM-ASA | PROGRAM | PRJ-LEONARDO-001 | '- | CONFIRMED | CONFIRMED | FILE | Arquitetura de sistemas agenticos, orquestracao, agentes, avaliacao, first principles. |
| PRG-TDAH | PROGRAM-TDAH | PROGRAM | PRJ-LEONARDO-001 | '- | CONFIRMED | CONFIRMED | FILE | Sistemas operacionais cognitivos neuroinclusivos para ICP TDAH. |
| PRG-DESK-OS | PROGRAM-DESK-OS | PROGRAM | PRJ-LEONARDO-001 | '- | CONFIRMED | CONFIRMED | FILE | Sistema fisico-digital A4, workflows, QR contextual, produto comercial. |
| PRG-LEONARDO-OS | PROGRAM-LEONARDO-OS | PROGRAM | PRJ-LEONARDO-001 | '- | CONFIRMED | CONFIRMED | FILE | Sistema operacional pessoal e empresarial; stack proprietario de skills; orquestrador. |
| PRG-EDUCATION | PROGRAM-EDUCATION | PROGRAM | PRJ-LEONARDO-001 | '- | DRAFT | PROPOSED | PROVIDED_PROJECT_CONTEXT | Programa de educacao; Course Express e trilhas. Inserido como proposto. |
| PRG-SMALL-BUSINESS | PROGRAM-SMALL-BUSINESS | PROGRAM | PRJ-LEONARDO-001 | '- | DRAFT | PROPOSED | PROVIDED_PROJECT_CONTEXT | Programa Small Business; Business Suite, GTM Showroom, Agency Kit. Inserido como proposto. |
| PRD-ASA | PRODUCT-ASA | PRODUCT | PRG-ASA | '- | WORKING | CONFIRMED | FILE | Arquitetura, metodos e ativos agenticos. |
| PRD-TDAH-OS | PRODUCT-TDAH-OS | PRODUCT | PRG-TDAH | '- | WORKING | CONFIRMED | FILE | Sistema operacional cognitivo, 1 workflow/dia, 3 etapas, ICP TDAH. |
| PRD-COPILOTO-TDAH | PRODUCT-COPILOTO-TDAH | PRODUCT | PRG-TDAH | '- | WORKING | CONFIRMED | FILE | Copiloto operacional, ciclos de 72h, proxima acao, evidencias. |
| PRD-DESK-OS | PRODUCT-DESK-OS | PRODUCT | PRG-DESK-OS | '- | WORKING | CONFIRMED | FILE | Produto autonomo comercializavel fisico-digital. |
| PRD-LEONARDO-OS | PRODUCT-LEONARDO-OS | PRODUCT | PRG-LEONARDO-OS | '- | WORKING | CONFIRMED | FILE | Operacao pessoal de Leonardo; integra DESK-OS, ASA e macro-personalizacao. |
| PRD-COURSE-EXPRESS | PRODUCT-COURSE-EXPRESS | PRODUCT | PRG-EDUCATION | '- | DRAFT | PROPOSED | PROVIDED_PROJECT_CONTEXT | Curso; trilhas TDAH, Macro, Anthropic Stack, Claude Power User. Sem arquivo proprio. |
| PRD-BUSINESS-SUITE | PRODUCT-BUSINESS-SUITE | PRODUCT | PRG-SMALL-BUSINESS | '- | DRAFT | PROPOSED | PROVIDED_PROJECT_CONTEXT | Suite para PMEs; modulos M1, M2, M5. Maturidade a validar. |
| PLT-PADRAO-OS | PLATFORM-PADRAO-OS | PLATFORM | PRJ-LEONARDO-001 | C09 | WORKING | CONFIRMED | FILE | Governanca, seguranca, memoria, qualidade, nomenclatura, gates, arquitetura-base. |
| PLT-DIRECTORY | PLATFORM-DIRECTORY | PLATFORM | PRJ-LEONARDO-001 | C10 | WORKING | CONFIRMED | FILE | Cataloga skills, agentes, comandos, workflows, plugins, conectores, templates. |
| CAP-MACRO-PERSONALIZATION | CAP-MACRO-PERSONALIZATION | CAPABILITY | PLT-PADRAO-OS | C05 | WORKING | CONFIRMED | FILE | Configura produtos e ICPs: contexto, variaveis, memoria, skills, agentes, execucao. |
| CAP-AGENT-FACTORY | CAP-AGENT-FACTORY | CAPABILITY | PRG-ASA | C04 | DRAFT | REVIEW_REQUIRED | PROVIDED_PROJECT_CONTEXT | Fabrica de agentes. A avaliar; sem documentacao dedicada confirmada. |
| TRACK-TDAH | TRACK-TDAH | TRACK | PRD-COURSE-EXPRESS | C11 | DRAFT | PROPOSED | PROVIDED_PROJECT_CONTEXT | Trilha TDAH do Course Express. |
| TRACK-MACRO-PERSONALIZATION | TRACK-MACRO-PERSONALIZATION | TRACK | PRD-COURSE-EXPRESS | C05 | DRAFT | PROPOSED | PROVIDED_PROJECT_CONTEXT | Trilha de macro-personalizacao. |
| TRACK-ANTHROPIC-STACK | TRACK-ANTHROPIC-STACK | TRACK | PRD-COURSE-EXPRESS | C04 | DRAFT | PROPOSED | PROVIDED_PROJECT_CONTEXT | Trilha Anthropic Stack. |
| TRACK-CLAUDE-POWER-USER | TRACK-CLAUDE-POWER-USER | TRACK | PRD-COURSE-EXPRESS | C10 | DRAFT | PROPOSED | PROVIDED_PROJECT_CONTEXT | Trilha Claude Power User. |
| INIT-GTM-SHOWROOM | INIT-GTM-SHOWROOM | INITIATIVE | PRG-SMALL-BUSINESS | C02 | DRAFT | PROPOSED | PROVIDED_PROJECT_CONTEXT | Iniciativa de demonstracao e aquisicao. |
| INIT-AGENCY-KIT | INIT-AGENCY-KIT | INITIATIVE | PRG-SMALL-BUSINESS | C02 | DRAFT | PROPOSED | PROVIDED_PROJECT_CONTEXT | Iniciativa/oferta sem documentacao suficiente. |
| MODULE-M1 | MODULE-M1 | MODULE | PRD-BUSINESS-SUITE | C02 | DRAFT | REVIEW_REQUIRED | PROVIDED_PROJECT_CONTEXT | Modulo M1 da Business Suite. |
| MODULE-M2 | MODULE-M2 | MODULE | PRD-BUSINESS-SUITE | C02 | DRAFT | REVIEW_REQUIRED | PROVIDED_PROJECT_CONTEXT | Modulo M2 da Business Suite. |
| MODULE-M5 | MODULE-M5 | MODULE | PRD-BUSINESS-SUITE | C02 | DRAFT | REVIEW_REQUIRED | PROVIDED_PROJECT_CONTEXT | Modulo M5 da Business Suite. |
| OFFER-DESKOS-KIT | OFFER-DESKOS-KIT | OFFER | PRD-DESK-OS | C01 | DRAFT | PROPOSED | EMBEDDED | Oferta kit DESK-OS. |
| OFFER-DESK-AND-GO | OFFER-DESK-AND-GO | OFFER | PRD-DESK-OS | C01 | DRAFT | PROPOSED | EMBEDDED | Oferta Desk and Go. |
| MODULE-QR-ORCHESTRATOR | MODULE-QR-ORCHESTRATOR | MODULE | PRD-DESK-OS | C06 | DRAFT | PROPOSED | EMBEDDED | Modulo orquestrador de QR. |
| MODULE-RECYCLE | MODULE-RECYCLE | MODULE | PRD-DESK-OS | C06 | DRAFT | PROPOSED | EMBEDDED | Modulo Recycle. |
| MODULE-PRISMA-DESK-GENERATOR | MODULE-PRISMA-DESK-GENERATOR | MODULE | PRD-DESK-OS | C07 | DRAFT | PROPOSED | EMBEDDED | Gerador do Prisma Desk. |
| MODULE-ONE-PRINT-HTML | MODULE-ONE-PRINT-HTML | MODULE | PRD-DESK-OS | C07 | DRAFT | PROPOSED | EMBEDDED | One Print HTML. |
| MODULE-NEURO-AGENT | MODULE-NEURO-AGENT | MODULE | PRD-TDAH-OS | C11 | DRAFT | REVIEW_REQUIRED | EMBEDDED | Neuro-Agent; a avaliar. |
| PRODUCT-SETUP-SUITE | PRODUCT-SETUP-SUITE | OFFER | PRD-LEONARDO-OS | C04 | DRAFT | REVIEW_REQUIRED | PROVIDED_PROJECT_CONTEXT | Setup Suite; candidato a avaliar. |
| PRODUCT-AI-OS-RESET | PRODUCT-AI-OS-RESET | OFFER | PRD-LEONARDO-OS | C04 | DRAFT | REVIEW_REQUIRED | PROVIDED_PROJECT_CONTEXT | AI OS Reset; candidato a avaliar. |

# APÊNDICE D — Document Coverage Matrix

| product_id | EXECUTIVE_SUMMARY | VISION | BRD | MRD | PRD | TECHNICAL_SPECS | ROADMAP | BACKLOG | RISKS | DECISIONS | EVIDENCE | GTM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRD-ASA | PRESENT | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PRESENT | PARTIAL | EMBEDDED | PARTIAL | PRESENT | PRESENT | EMBEDDED |
| PRD-TDAH-OS | PARTIAL | PARTIAL | EMBEDDED | EMBEDDED | EMBEDDED | EMBEDDED | EMBEDDED | EMBEDDED | EMBEDDED | EMBEDDED | PARTIAL | PARTIAL |
| PRD-COPILOTO-TDAH | EMBEDDED | MISSING | EMBEDDED | EMBEDDED | EMBEDDED | EMBEDDED | PRESENT | PRESENT | EMBEDDED | PRESENT | PRESENT | PRESENT |
| PRD-DESK-OS | PRESENT | PARTIAL | PRESENT | PRESENT | PRESENT | PRESENT | PRESENT | PRESENT | PRESENT | PRESENT | PARTIAL | PRESENT |
| PRD-LEONARDO-OS | PRESENT | PARTIAL | PARTIAL | EMBEDDED | PARTIAL | PARTIAL | EMBEDDED | EMBEDDED | EMBEDDED | EMBEDDED | PARTIAL | EMBEDDED |
| PRD-COURSE-EXPRESS | EMBEDDED | MISSING | MISSING | MISSING | MISSING | MISSING | MISSING | MISSING | MISSING | MISSING | MISSING | MISSING |
| PRD-BUSINESS-SUITE | PARTIAL | PARTIAL | PARTIAL | PARTIAL | MISSING | MISSING | MISSING | MISSING | MISSING | EMBEDDED | PARTIAL | PRESENT |

# APÊNDICE E — Source Content Manifest

| content_group_id | source_file | chunk_index | chunk_total | source_locator | chars |
| --- | --- | --- | --- | --- | --- |
| CG-004 | 99-TEMPLATE_CDM_OURO | 1 | 1 | file:99-TEMPLATE_CDM_OURO#chunk1 | 12352 |
| CG-005 | ASA_-_RATIONALE_.txt | 1 | 2 | file:ASA_-_RATIONALE_.txt#chunk1 | 30001 |
| CG-005 | ASA_-_RATIONALE_.txt | 2 | 2 | file:ASA_-_RATIONALE_.txt#chunk2 | 1997 |
| CG-006 | BUSINESS_GMT_RATIONAL_ | 1 | 1 | file:BUSINESS_GMT_RATIONAL_#chunk1 | 6085 |
| CG-007 | BUSINESS_PACK_.txt | 1 | 1 | file:BUSINESS_PACK_.txt#chunk1 | 26069 |
| CG-010 | CMD-OUTPUT-REQUIREMENTS-V2-EVOLVER.md | 1 | 1 | file:CMD-OUTPUT-REQUIREMENTS-V2-EVOLVER.md#chunk1 | 21164 |
| CG-011 | Context | 1 | 1 | file:Context#chunk1 | 5639 |
| CG-012 | Contextos_adicionais_ | 1 | 1 | file:Contextos_adicionais_#chunk1 | 25810 |
| CG-013 | Continua_FAQ | 1 | 1 | file:Continua_FAQ#chunk1 | 4890 |
| CG-015 | Customer_jorney_.txt | 1 | 1 | file:Customer_jorney_.txt#chunk1 | 14274 |
| CG-016 | Desing_System_.txt | 1 | 1 | file:Desing_System_.txt#chunk1 | 14307 |
| CG-017 | DESK-OS-YAML-CARD | 1 | 1 | file:DESK-OS-YAML-CARD#chunk1 | 1614 |
| CG-019 | ESPECIALISTA_AGENTE | 1 | 1 | file:ESPECIALISTA_AGENTE#chunk1 | 9317 |
| CG-020 | ESPECIALISTA_RATIONALE | 1 | 1 | file:ESPECIALISTA_RATIONALE#chunk1 | 13850 |
| CG-021 | FAQ | 1 | 1 | file:FAQ#chunk1 | 5623 |
| CG-022 | GTM_RATIONALE.txt | 1 | 1 | file:GTM_RATIONALE.txt#chunk1 | 6085 |
| CG-023 | ICPS-WORKFLOWS | 1 | 1 | file:ICPS-WORKFLOWS#chunk1 | 16509 |
| CG-024 | LEONARDO-OS.md | 1 | 1 | file:LEONARDO-OS.md#chunk1 | 4625 |
| CG-025 | LEONARDO_MACRO_PERSONALIZATION___PROPRIETARY_SKILL_STACK.md | 1 | 2 | file:LEONARDO_MACRO_PERSONALIZATION___PROPRIETARY_SKILL_STACK.md#chunk1 | 30001 |
| CG-025 | LEONARDO_MACRO_PERSONALIZATION___PROPRIETARY_SKILL_STACK.md | 2 | 2 | file:LEONARDO_MACRO_PERSONALIZATION___PROPRIETARY_SKILL_STACK.md#chunk2 | 5372 |
| CG-026 | MASTER-INDEX-AGENTIC-SYSTEMS-ARCHITECT.md | 1 | 1 | file:MASTER-INDEX-AGENTIC-SYSTEMS-ARCHITECT.md#chunk1 | 11508 |
| CG-027 | MATER-FULL-PRINT | 1 | 2 | file:MATER-FULL-PRINT#chunk1 | 30001 |
| CG-027 | MATER-FULL-PRINT | 2 | 2 | file:MATER-FULL-PRINT#chunk2 | 20462 |
| CG-028 | OUTPUT-REQUIREMNETS_ | 1 | 1 | file:OUTPUT-REQUIREMNETS_#chunk1 | 18588 |
| CG-029 | OUTPUT_REQUIREMENTS_V2.md | 1 | 1 | file:OUTPUT_REQUIREMENTS_V2.md#chunk1 | 20377 |
| CG-030 | OUTPUT_REQUIREMENTS_V3.md | 1 | 1 | file:OUTPUT_REQUIREMENTS_V3.md#chunk1 | 17220 |
| CG-031 | PHARMACY_-_CMD | 1 | 1 | file:PHARMACY_-_CMD#chunk1 | 15013 |
| CG-032 | Propostas_de_wirfremes_.txt | 1 | 1 | file:Propostas_de_wirfremes_.txt#chunk1 | 29989 |
| CG-033 | RATIONAL_ADPT_txt.rtf | 1 | 1 | file:RATIONAL_ADPT_txt.rtf#chunk1 | 15104 |
| CG-034 | README | 1 | 1 | file:README#chunk1 | 24260 |
| CG-035 | README-ASA-TREEFILE.md | 1 | 1 | file:README-ASA-TREEFILE.md#chunk1 | 3899 |
| CG-036 | RESUMO_EXECUTIVO_DO_PROJETO_ | 1 | 1 | file:RESUMO_EXECUTIVO_DO_PROJETO_#chunk1 | 15963 |
| CG-037 | SAKANA-BLUEPRINT_txt.rtf | 1 | 1 | file:SAKANA-BLUEPRINT_txt.rtf#chunk1 | 15842 |
| CG-038 | SAKANA_TXT.rtf | 1 | 1 | file:SAKANA_TXT.rtf#chunk1 | 1245 |
| CG-039 | SOT_DESING_SYSTEM | 1 | 1 | file:SOT_DESING_SYSTEM#chunk1 | 14051 |
| CG-041 | UNIVERSAL_ICP_OPERATING_SYSTEM_SCHEMA.md | 1 | 1 | file:UNIVERSAL_ICP_OPERATING_SYSTEM_SCHEMA.md#chunk1 | 23937 |
| CG-042 | VARIÁVEIS_DO_AMBIENTE_ | 1 | 1 | file:VARIÁVEIS_DO_AMBIENTE_#chunk1 | 602 |
| CG-043 | VARIÁVEIS_PERSONALIZADAS | 1 | 1 | file:VARIÁVEIS_PERSONALIZADAS#chunk1 | 8871 |
| CG-044 | WF1.md | 1 | 1 | file:WF1.md#chunk1 | 1821 |
| CG-045 | WF2.md | 1 | 1 | file:WF2.md#chunk1 | 13570 |
| CG-046 | WF3.md | 1 | 1 | file:WF3.md#chunk1 | 15281 |
| CG-047 | WF4.md | 1 | 1 | file:WF4.md#chunk1 | 13728 |
| CG-048 | WF5.md | 1 | 1 | file:WF5.md#chunk1 | 13150 |
| CG-049 | WF6.md | 1 | 1 | file:WF6.md#chunk1 | 15994 |
| CG-050 | Wireframe | 1 | 1 | file:Wireframe#chunk1 | 15190 |
| CG-051 | Wireframe_2 | 1 | 1 | file:Wireframe_2#chunk1 | 25023 |
| CG-052 | Workflowagentico | 1 | 2 | file:Workflowagentico#chunk1 | 30001 |
| CG-052 | Workflowagentico | 2 | 2 | file:Workflowagentico#chunk2 | 5909 |
| CG-053 | YAML_Card_Leonard_os_ | 1 | 1 | file:YAML_Card_Leonard_os_#chunk1 | 26473 |
| CG-054 | Yamls_card_2_deskos_ | 1 | 2 | file:Yamls_card_2_deskos_#chunk1 | 30001 |
| CG-054 | Yamls_card_2_deskos_ | 2 | 2 | file:Yamls_card_2_deskos_#chunk2 | 334 |

O conteúdo integral extraído de 46 documentos textuais permanece na aba `21_FILE_CONTENT` e no arquivo `MASTER_PROJECT_ADMIN_EXTRACT.json` deste evidence pack. O report não replica todo o texto bruto para evitar duplicação, mas preserva a localização de cada chunk.
