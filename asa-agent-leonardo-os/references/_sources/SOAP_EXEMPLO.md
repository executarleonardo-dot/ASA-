A lógica é: o agente não explica o workflow; ele instancia, executa, atualiza, valida e registra o workflow. Cada ID representa uma unidade operacional já vinculada a comandos, skills, templates, ferramentas e destinos.

WF1 — DESENVOLVER, VALIDAR E REGISTRAR UMA SKILL

1. Estrutura cartesiana de quatro colunas

|   |   |
|---|---|
|Coluna|Significado|
|ID + condição|Identifica a operação e informa quando ela deve ser executada|
|Entradas + dependências|Define tudo que precisa existir antes da execução|
|Ação do agente + decisão|Determina o que o agente deve fazer, não apenas descrever|
|Recursos + saída + gate|Define comandos, skills, ferramentas, destino, evidência e aprovação|

  

2. Comando de inicialização

/WF1-SKILL-BUILD

Ao receber esse ID, o orquestrador deve:

1. recuperar a macro personalização;

2. identificar o projeto e a skill solicitada;

3. consultar o catálogo de recursos;

4. localizar templates, diretórios e arquivos existentes;

5. montar o plano de execução;

6. selecionar o caminho mais eficiente;

7. criar somente os artefatos necessários;

8. executar cada subworkflow;

9. validar os gates;

10. salvar e registrar o resultado final.

  

11. FASE A — INICIALIZAÇÃO E MISE EN PLACE

|   |   |   |   |
|---|---|---|---|
|ID + condição|Entradas + dependências|Ação do agente + decisão|Recursos + saída + gate|
|WF1-A00 — Iniciar workflowExecutar ao receber /WF1-SKILL-BUILD.|ID do projeto; solicitação; usuário; ambiente; permissões.|Interpretar a solicitação, abrir uma execução e gerar um run_id. Não produzir a skill ainda.|Recurso: Leonardo Orchestrator.Saída: registro de execução.Gate: projeto e solicitante identificados.|
|WF1-A01 — Recuperar personalizaçãoExecutar imediatamente após A00.|UID Leonardo; UID Macro Personalização; memória autorizada.|Recuperar objetivos, funções, preferências, restrições cognitivas, stack permitido e formato de saída.|Recurso: Macro Personalização + memória.Saída: runtime_context.Gate: contexto mínimo disponível.|
|WF1-A02 — Recuperar contexto do projeto|UID do projeto; Planilha Master; relações registradas.|Localizar projeto atual, objetivo macro, meso e micro, entregáveis, documentos e decisões anteriores.|Recurso: Excel/Planilha Master.Saída: project_context.Gate: projeto ativo localizado.|
|WF1-A03 — Classificar solicitação|Solicitação original; runtime_context; catálogo de artefatos.|Decidir se o pedido exige uma skill, command, agent, template, plugin ou atualização de artefato existente.|Recurso: Cognitive Framework Router.Saída: artifact_type.Gate: tipo de artefato definido.|
|WF1-A04 — Verificar existência|Nome proposto; finalidade; Directory Specialist; repositórios.|Pesquisar se já existe skill equivalente, versão anterior, template aplicável ou componente reutilizável.|Recurso: Directory Specialist + Enterprise Search.Saída: relatório de similaridade.Gate: criar, atualizar, compor ou abortar duplicação.|
|WF1-A05 — Definir estratégia|Resultado de A03 e A04.|Escolher entre create_new, extend_existing, compose_modules ou update_version.|Recurso: OS Partner Admin.Saída: build_strategy.Gate: estratégia registrada.|
|WF1-A06 — Localizar diretório-base|Tipo de skill; estratégia; catálogo de templates.|Localizar o ZIP ou diretório padrão mais adequado. Não criar uma estrutura nova quando houver template compatível.|Recurso: Standalone Progressive Skill Template.Saída: caminho do template-base.Gate: template encontrado ou criação justificada.|
|WF1-A07 — Instanciar workspace|Diretório-base; nome; ID; versão inicial.|Copiar ou descompactar o template em workspace temporário, substituir variáveis iniciais e preservar o original.|Recurso: comando de scaffolding.Saída: diretório de trabalho.Gate: estrutura criada sem alterar o template original.|
|WF1-A08 — Inventariar arquivos esperados|Diretório instanciado; schema da skill.|Verificar arquivos obrigatórios, opcionais, ausentes e desnecessários.|Recurso: Directory Specialist.Saída: file_manifest.yaml.Gate: inventário concluído.|
|WF1-A09 — Resolver dependências|Manifesto; estratégia; recursos disponíveis.|Mapear quais arquivos dependem de briefing, pesquisa, templates, comandos, scripts, conectores ou validação humana.|Recurso: SOP OS.Saída: grafo de dependências.Gate: nenhuma dependência crítica desconhecida.|
|WF1-A10 — Gerar plano de execução|Grafo de dependências; catálogo de commands, skills e ferramentas.|Ordenar as operações, identificar paralelismo seguro e impedir execução fora de sequência.|Recurso: ASA Orchestrator.Saída: execution_plan.yaml.Gate: plano executável criado.|

Gate A — Mise en place concluído

PASSA SE

├── contexto foi recuperado;

├── tipo de artefato foi validado;

├── duplicações foram verificadas;

├── estratégia foi escolhida;

├── diretório-base foi instanciado;

├── arquivos foram inventariados;

└── dependências foram ordenadas.

  

4. FASE B — BRIEFING EXECUTÁVEL

|   |   |   |   |
|---|---|---|---|
|ID + condição|Entradas + dependências|Ação do agente + decisão|Recursos + saída + gate|
|WF1-B01 — Abrir briefing-base|Template de briefing; contexto recuperado.|Abrir o template diretamente no ambiente de coautoria. Não gerar cópias intermediárias desnecessárias.|Recurso: DOC Authoring / Co-authoring.Saída: briefing ativo.Gate: documento editável disponível.|
|WF1-B02 — Pré-preencher briefing|Macro personalização; contexto do projeto; solicitação.|Preencher automaticamente nome, usuário, ambiente, objetivo, restrições, stack e outputs conhecidos.|Recurso: STR Replace ou edição estruturada equivalente.Saída: briefing parcialmente preenchido.Gate: campos conhecidos preenchidos sem inventar dados.|
|WF1-B03 — Detectar lacunas|Briefing parcialmente preenchido.|Identificar somente lacunas que alteram arquitetura, segurança, escopo ou aceite.|Recurso: Cognitive Framework Router.Saída: critical_gaps.Gate: lacunas classificadas.|
|WF1-B04 — Inferir campos permitidos|Memória; Planilha Master; documentos existentes.|Preencher campos dedutíveis e registrar a origem. Não perguntar novamente dados já disponíveis.|Recurso: Product Self Knowledge + Enterprise Search.Saída: briefing enriquecido.Gate: inferências rastreáveis.|
|WF1-B05 — Solicitar decisão humana|Lacunas críticas não inferíveis.|Exibir somente decisões bloqueadoras, preferencialmente em opções fechadas.|Recurso: DOC Co-authoring.Saída: decisões do usuário.Gate: bloqueios resolvidos.|
|WF1-B06 — Atualizar inline|Respostas do usuário.|Atualizar o mesmo documento usando substituição localizada. Não reescrever o arquivo integralmente.|Recurso: STR Replace.Saída: briefing atualizado.Gate: nenhuma informação anterior perdida.|
|WF1-B07 — Definir Definition of Done|Problema; usuário; output esperado.|Converter expectativa em critérios verificáveis de conclusão.|Recurso: SOP OS.Saída: DoD da skill.Gate: todos os critérios podem ser testados.|
|WF1-B08 — Definir não escopo|Briefing; riscos de expansão.|Registrar explicitamente o que a skill não deve fazer.|Recurso: Padrão OS.Saída: non_goals.Gate: fronteira definida.|
|WF1-B09 — Validar briefing|Briefing completo; DoD; não escopo.|Executar checklist automático de completude, consistência e testabilidade.|Recurso: Comando de validação de briefing.Saída: relatório PASS/FAIL.Gate: briefing aprovado.|
|WF1-B10 — Persistir briefing|Briefing aprovado; destino configurado.|Atualizar diretamente o arquivo no Drive quando houver documento oficial. Criar upload manual somente quando escrita direta não estiver disponível.|Recurso: Drive Connector.Saída: link permanente.Gate: briefing salvo e acessível.|

Regra AI-first da coautoria

SE existe documento oficial editável

→ editar inline no mesmo arquivo.

  

SE a alteração é localizada

→ utilizar STR Replace.

  

SE o documento não existe

→ criar uma vez no destino oficial.

  

NÃO

→ gerar versões soltas, baixar, editar, reenviar e duplicar.

  

5. FASE C — ARQUITETURA DA SKILL

|   |   |   |   |
|---|---|---|---|
|ID + condição|Entradas + dependências|Ação do agente + decisão|Recursos + saída + gate|
|WF1-C01 — Selecionar arquitetura|Briefing aprovado; estratégia A05.|Escolher skill standalone, integrada, orquestradora, router, template ou composição.|Recurso: Meta Template Specialist.Saída: architecture decision.Gate: arquitetura compatível com o uso.|
|WF1-C02 — Definir disclosure|Complexidade; frequência; tamanho das referências.|Separar instruções de runtime, referências sob demanda e arquivos auxiliares.|Recurso: Progressive Skill Template.Saída: mapa de progressive disclosure.Gate: SKILL.md não ficará monolítico.|
|WF1-C03 — Definir runtime principal|Caso de uso; DoD.|Especificar gatilhos, inputs, workflow, decisões, outputs e stop conditions.|Recurso: Meta Template Specialist.Saída: schema lógico da skill.Gate: runtime completo.|
|WF1-C04 — Definir comandos|Operações recorrentes identificadas.|Transformar operações reutilizáveis em commands com IDs próprios.|Recurso: Command Builder.Saída: command registry.Gate: nenhum comando sem função operacional.|
|WF1-C05 — Definir referências|Conhecimento necessário; regras; SOPs.|Decidir quais informações ficam fora do SKILL.md e são carregadas somente quando necessárias.|Recurso: Directory Specialist.Saída: reference map.Gate: referências têm gatilho de consulta.|
|WF1-C06 — Definir templates|Outputs repetitivos.|Criar templates somente para outputs com estrutura estável.|Recurso: Template Builder.Saída: template registry.Gate: template reduz trabalho futuro.|
|WF1-C07 — Definir ferramentas|Ações da skill; conectores disponíveis.|Vincular cada ação a uma ferramenta concreta e definir fallback.|Recurso: Tool Router.Saída: tool contract.Gate: nenhuma etapa depende de ferramenta abstrata.|
|WF1-C08 — Definir memória|Dados necessários entre execuções.|Classificar dados em runtime, memória persistente, Planilha Master ou documento.|Recurso: Memory Policy.Saída: memory contract.Gate: nenhuma informação é persistida sem regra.|
|WF1-C09 — Definir segurança|Ferramentas; dados; ações externas.|Adicionar confirmações, permissões, limites e ações proibidas.|Recurso: Padrão OS.Saída: guardrails.Gate: riscos críticos tratados.|
|WF1-C10 — Registrar arquitetura|Todas as decisões anteriores.|Gerar e salvar o blueprint arquitetural antes de escrever os arquivos finais.|Recurso: DOC Authoring + Drive.Saída: SKILL_ARCHITECTURE.md.Gate: arquitetura aprovada.|

  

6. FASE D — PESQUISA E CONSOLIDAÇÃO

|   |   |   |   |
|---|---|---|---|
|ID + condição|Entradas + dependências|Ação do agente + decisão|Recursos + saída + gate|
|WF1-D01 — Buscar fontes internas|Termos; UIDs; projeto.|Pesquisar Planilha Master, Drive, diretório de skills e memória.|Recurso: Enterprise Search.Saída: conjunto de fontes internas.Gate: fontes classificadas.|
|WF1-D02 — Buscar documentação oficial|Lacunas técnicas; ferramentas utilizadas.|Pesquisar documentação primária atual somente quando a informação externa for necessária.|Recurso: Web Search.Saída: source register.Gate: fonte oficial identificada.|
|WF1-D03 — Comparar padrões|Skills existentes; template-base; fontes.|Identificar convenções, diferenças, riscos de inconsistência e elementos reutilizáveis.|Recurso: Product Self Knowledge.Saída: comparison matrix.Gate: decisões fundamentadas.|
|WF1-D04 — Remover redundâncias|Fontes internas e externas.|Consolidar informações equivalentes e preservar a fonte de verdade.|Recurso: Comando de síntese.Saída: knowledge pack.Gate: sem duplicações conflitantes.|
|WF1-D05 — Sinalizar conflitos|Knowledge pack.|Identificar regras incompatíveis, versões divergentes ou instruções obsoletas.|Recurso: Padrão OS.Saída: conflict register.Gate: conflitos resolvidos ou marcados.|
|WF1-D06 — Persistir referências|Fontes aprovadas.|Salvar referências diretamente na pasta oficial do projeto ou vincular links; não copiar documentos sem necessidade.|Recurso: Drive/GitHub.Saída: reference index.Gate: rastreabilidade mantida.|

  

7. FASE E — AUTORIA DOS ARQUIVOS

|   |   |   |   |
|---|---|---|---|
|ID + condição|Entradas + dependências|Ação do agente + decisão|Recursos + saída + gate|
|WF1-E01 — Criar README inicial|Briefing; arquitetura; manifesto.|Preencher finalidade, estrutura, instalação, uso, dependências e status.|Recurso: DOC Authoring.Saída: README.md.Gate: estrutura compreensível.|
|WF1-E02 — Criar SKILL.md|Runtime schema; guardrails; tool contract.|Escrever instruções enxutas e executáveis, evitando conteúdo que pertence às referências.|Recurso: Meta Template Specialist.Saída: SKILL.md.Gate: runtime autossuficiente.|
|WF1-E03 — Criar commands|Command registry.|Gerar um arquivo por comando, com gatilho, inputs, ação, saída, falha e stop condition.|Recurso: Command Builder.Saída: /commands/*.Gate: comandos executáveis.|
|WF1-E04 — Criar references|Reference map; knowledge pack.|Criar ou vincular arquivos de referência e explicar quando devem ser consultados.|Recurso: DOC Authoring.Saída: /references/*.Gate: referências carregáveis sob demanda.|
|WF1-E05 — Criar templates|Template registry.|Produzir modelos preenchíveis para outputs repetitivos.|Recurso: Template Builder.Saída: /templates/*.Gate: todos possuem exemplo ou schema.|
|WF1-E06 — Criar schemas|Estruturas de entrada e saída.|Criar YAML/JSON schemas quando validação estrutural for necessária.|Recurso: Schema Builder.Saída: /schemas/*.Gate: schemas válidos.|
|WF1-E07 — Criar exemplos|Casos reais; DoD; não escopo.|Gerar exemplos Do/Don’t, happy path e falhas críticas.|Recurso: Eval Builder.Saída: /examples/*.Gate: exemplos cobrem comportamento esperado.|
|WF1-E08 — Criar testes|DoD; guardrails; outputs.|Converter critérios de aceite em casos de teste reproduzíveis.|Recurso: Eval/Test Builder.Saída: /tests/*.Gate: cada critério possui teste.|
|WF1-E09 — Atualizar README|Arquivos finais produzidos.|Substituir status provisório por instruções reais e inventário final.|Recurso: STR Replace.Saída: README final.Gate: documentação reflete o pacote.|
|WF1-E10 — Validar consistência interna|Todos os arquivos.|Verificar nomes, IDs, links, referências, paths, versões e termos.|Recurso: Directory Specialist.Saída: consistency report.Gate: zero erro estrutural crítico.|

Regra de edição

SE o arquivo já existe

→ editar o arquivo existente.

  

SE apenas um bloco mudou

→ substituir somente esse bloco.

  

SE vários arquivos compartilham uma variável

→ executar atualização em lote controlada.

  

NÃO

→ recriar arquivos inteiros sem necessidade.

  

8. FASE F — SCRIPT CREATOR E EMPACOTAMENTO PRELIMINAR

|   |   |   |   |
|---|---|---|---|
|ID + condição|Entradas + dependências|Ação do agente + decisão|Recursos + saída + gate|
|WF1-F01 — Preparar entrada do script|Diretório completo; manifesto; schemas.|Verificar que o diretório contém todos os arquivos requeridos antes de chamar o empacotador.|Recurso: Preflight Command.Saída: preflight PASS/FAIL.Gate: diretório elegível.|
|WF1-F02 — Normalizar estrutura|Diretório aprovado.|Corrigir nomes, extensões, encoding, paths e arquivos temporários.|Recurso: Directory Normalizer.Saída: diretório normalizado.Gate: estrutura canônica.|
|WF1-F03 — Remover informações proibidas|Todos os arquivos.|Procurar segredos, chaves, dados pessoais não autorizados, caminhos locais e conteúdo residual.|Recurso: Security Scanner.Saída: security report.Gate: zero segredo detectado.|
|WF1-F04 — Acionar Script Creator|Diretório normalizado e seguro.|Executar o script de criação ou build, capturar logs e impedir avanço em caso de erro.|Recurso: Script Creator.Saída: pacote preliminar.Gate: build concluído.|
|WF1-F05 — Validar pacote preliminar|ZIP ou pacote gerado.|Abrir, listar arquivos, comparar com manifesto e verificar integridade.|Recurso: Package Validator.Saída: package report.Gate: pacote íntegro.|

  

9. FASE G — TESTES E CORREÇÕES

|   |   |   |   |
|---|---|---|---|
|ID + condição|Entradas + dependências|Ação do agente + decisão|Recursos + saída + gate|
|WF1-G01 — Criar ambiente de teste|Pacote preliminar; configuração.|Instalar ou carregar a skill em ambiente isolado.|Recurso: Test Runner.Saída: ambiente pronto.Gate: skill carregada.|
|WF1-G02 — Testar ativação|Gatilhos definidos.|Verificar quando a skill é acionada e quando não deve ser acionada.|Recurso: Trigger Eval.Saída: trigger results.Gate: precisão mínima atingida.|
|WF1-G03 — Testar happy path|Inputs válidos.|Executar o fluxo principal do início ao output final.|Recurso: Test Runner.Saída: resultado esperado.Gate: DoD funcional atendido.|
|WF1-G04 — Testar entradas incompletas|Casos com lacunas.|Verificar se a skill recupera contexto, pergunta somente o necessário ou interrompe corretamente.|Recurso: Failure Eval.Saída: failure behavior report.Gate: sem invenção de dados.|
|WF1-G05 — Testar ferramentas indisponíveis|Conectores simulados como indisponíveis.|Executar fallback, explicar limitação ou interromper com estado recuperável.|Recurso: Tool Failure Test.Saída: fallback report.Gate: falha controlada.|
|WF1-G06 — Testar guardrails|Casos proibidos ou sensíveis.|Confirmar bloqueio, confirmação humana ou redução de escopo.|Recurso: Safety Eval.Saída: guardrail report.Gate: regras respeitadas.|
|WF1-G07 — Testar qualidade|Outputs gerados.|Avaliar clareza, completude, personalização, rastreabilidade e não genericidade.|Recurso: Quality Eval.Saída: scorecard.Gate: limiar mínimo atingido.|
|WF1-G08 — Diagnosticar falhas|Relatórios de teste.|Agrupar falhas por causa raiz e identificar arquivos responsáveis.|Recurso: Agentic Problem Solving.Saída: defect register.Gate: causa identificada.|
|WF1-G09 — Corrigir arquivos|Defect register.|Alterar somente os trechos responsáveis pelas falhas.|Recurso: STR Replace + editor estruturado.Saída: versão corrigida.Gate: correção aplicada.|
|WF1-G10 — Reexecutar testes afetados|Versão corrigida.|Rodar testes diretamente relacionados e depois regressão essencial.|Recurso: Test Runner.Saída: retest report.Gate: defeitos resolvidos.|
|WF1-G11 — Aprovar versão candidata|Todos os relatórios.|Consolidar resultados e promover a build para release candidate.|Recurso: Quality Gate Command.Saída: release candidate.Gate: todos os testes críticos PASS.|

  

10. FASE H — RELEASE, SALVAMENTO E REGISTRO

|   |   |   |   |
|---|---|---|---|
|ID + condição|Entradas + dependências|Ação do agente + decisão|Recursos + saída + gate|
|WF1-H01 — Definir versão|Estratégia A05; versão anterior; mudanças.|Aplicar regra de versionamento e gerar changelog.|Recurso: Version Manager.Saída: versão final.Gate: versão única.|
|WF1-H02 — Gerar pacote final|Release candidate; versão.|Executar build final e nomear o pacote conforme padrão.|Recurso: Script Creator.Saída: .skill.zip final.Gate: hash e integridade válidos.|
|WF1-H03 — Escolher destinos|Política do projeto; tipo de skill.|Selecionar GitHub, Drive, diretório Leonardo OS e/ou workspace de cliente.|Recurso: Storage Router.Saída: destination plan.Gate: destino oficial identificado.|
|WF1-H04 — Salvar no GitHub|Repositório autorizado; pacote e fontes.|Criar commit, tag ou release conforme política. Não solicitar upload manual se o conector puder escrever.|Recurso: GitHub Connector.Saída: commit/release URL.Gate: artefato versionado.|
|WF1-H05 — Salvar no Drive|Pasta oficial; pacote; documentação.|Gravar diretamente na pasta correta e obter link compartilhável.|Recurso: Drive Connector.Saída: Drive URL.Gate: arquivo acessível.|
|WF1-H06 — Atualizar Planilha Master|UID; versão; links; status; owner; testes.|Escrever diretamente nas células ou registros correspondentes. Evitar gerar uma nova planilha.|Recurso: Excel Co-Working.Saída: registro atualizado.Gate: linha validada.|
|WF1-H07 — Atualizar relações|Skill; comandos; projetos; documentos; plugins.|Criar ou atualizar relações entre os UIDs envolvidos.|Recurso: Excel/Relations Registry.Saída: relações registradas.Gate: rastreabilidade completa.|
|WF1-H08 — Registrar evidências|Relatórios; links; pacote; hash.|Vincular testes, source register, changelog e locais de armazenamento.|Recurso: Evidence Register.Saída: evidence pack.Gate: auditoria possível.|
|WF1-H09 — Gerar handoff|Artefato final; destinatário; uso previsto.|Criar resumo operacional com acesso, instalação, uso, limitações e próxima ação.|Recurso: Cross Account Handoff Orchestrator.Saída: handoff document.Gate: destinatário consegue usar a skill.|
|WF1-H10 — Fechar workflow|Todos os gates anteriores.|Alterar status para DONE, registrar data, duração, problemas e aprendizados.|Recurso: OS Partner Admin.Saída: workflow encerrado.Gate: DoD integralmente atendido.|
|WF1-H11 — Disparar próximo workflow|Skill pronta; estratégia de conteúdo.|Criar entrada para o WF2 — transformar produto em conteúdo e portfólio.|Recurso: Workflow Router.Saída: WF2 preparado.Gate: handoff entre workflows concluído.|

  

11. Inteligência de seleção do agente

O WorkStructor deve decidir como executar, considerando custo cognitivo, número de transferências, risco de erro, persistência e rastreabilidade.

Matriz de decisão operacional

|   |   |   |   |
|---|---|---|---|
|Situação|Decisão do agente|Não fazer|Critério|
|Documento oficial já existe|Editar inline|Criar cópia paralela|Menor duplicação|
|Alteração é localizada|Usar STR Replace|Reescrever documento inteiro|Preservar conteúdo|
|Arquivo deve ficar no Drive|Escrever diretamente via conector|Gerar localmente e pedir upload|Menos handoffs|
|Registro pertence à Planilha Master|Atualizar via Excel Co-Working|Criar nova planilha|Fonte única|
|Template padrão já existe|Instanciar o template|Criar estrutura do zero|Reutilização|
|Skill semelhante já existe|Estender ou compor|Duplicar capacidade|Menor manutenção|
|Vários arquivos dependem do mesmo dado|Alteração parametrizada|Editar manualmente um a um|Consistência|
|Ação pode causar efeito externo|Solicitar confirmação|Executar silenciosamente|Segurança|
|Pesquisa interna é suficiente|Não realizar busca externa|Pesquisar a web por padrão|Menor custo|
|Informação técnica pode ter mudado|Consultar fonte oficial atual|Usar memória desatualizada|Confiabilidade|
|Dois passos podem rodar em paralelo|Paralelizar sem conflito|Executar sequencialmente sem motivo|Eficiência|
|Output intermediário não terá reutilização|Manter em estado temporário|Salvar cada rascunho|Menor ruído|

  

12. Fórmula de eficiência

Para cada operação, o agente deve comparar alternativas:

EFICIÊNCIA

=

MENOS TRANSFERÊNCIAS

+

MENOS ARQUIVOS INTERMEDIÁRIOS

+

MENOS AÇÕES MANUAIS

+

MAIOR RASTREABILIDADE

+

MAIOR REVERSIBILIDADE

-

RISCO

Exemplo 1 — Autoria documental

OPÇÃO A

Criar arquivo novo

→ baixar

→ editar

→ salvar

→ enviar ao Drive

→ substituir versão anterior

  

OPÇÃO B

Abrir documento oficial

→ editar inline com STR Replace

→ validar

→ salvar automaticamente

  

ESCOLHA

→ OPÇÃO B

Exemplo 2 — Atualização da Planilha Master

OPÇÃO A

Gerar CSV

→ baixar

→ abrir Excel

→ localizar linha

→ copiar dados

→ salvar

  

OPÇÃO B

Localizar UID

→ atualizar células via Excel Co-Working

→ validar registro

→ retornar link/evidência

  

ESCOLHA

→ OPÇÃO B

Exemplo 3 — Diretório inicial

OPÇÃO A

Criar pastas e arquivos manualmente

  

OPÇÃO B

Localizar template homologado

→ instanciar

→ substituir variáveis

→ remover módulos desnecessários

  

ESCOLHA

→ OPÇÃO B

  

13. Contrato mínimo de cada ID

operation:

  id: WF1-E02

  name: create_skill_md

  

  trigger:

    after: WF1-C10

    requires_gate: architecture_approved

  

  inputs:

    - approved_brief

    - runtime_schema

    - tool_contract

    - guardrails

    - progressive_disclosure_map

  

  agent_action:

    mode: execute

    instruction: >

      Criar ou atualizar o SKILL.md no diretório oficial,

      mantendo apenas instruções necessárias durante o runtime.

  

  decision_rules:

    - reuse_existing_file_when_available

    - use_str_replace_for_local_changes

    - move_long_reference_content_outside_skill_md

    - never_invent_missing_business_data

  

  resources:

    primary_skill: meta_template_specialist

    editor: doc_co_authoring

    tool: str_replace

    destination: project_workspace

  

  outputs:

    - path: /SKILL.md

    - evidence: updated_file_diff

  

  acceptance:

    - runtime_instructions_complete

    - no_unnecessary_reference_content

    - tools_have_explicit_conditions

    - stop_conditions_defined

  

  failure:

    action: block_and_register

    output: skill_md_error_report

  

  next:

    on_pass: WF1-E03

    on_fail: WF1-E02-FIX

  

14. Interface apresentada a Leonardo

Leonardo não precisa visualizar todas as operações simultaneamente.

WF1 — DESENVOLVER SKILL

  

ETAPA ATUAL

Desenvolvimento dos arquivos

  

SUBWORKFLOW

WF1-E02 — Criar SKILL.md

  

O SISTEMA ESTÁ

Editando o arquivo existente por substituição localizada.

  

PRECISA DE LEONARDO

Nenhuma ação.

  

PRÓXIMO GATE

SKILL.md executável e consistente com o briefing.

  

STATUS

Em execução

Quando houver intervenção:

DECISÃO NECESSÁRIA

  

O sistema encontrou duas estratégias:

  

A. Atualizar a skill existente.

B. Criar uma nova skill independente.

  

RECOMENDAÇÃO

A — 78% da estrutura já existe e pode ser reutilizada.

  

AÇÃO DE LEONARDO

Aprovar A ou selecionar B.

  

15. Resultado do comando principal

/WF1-SKILL-BUILD

│

├── recupera contexto

├── localiza template

├── instancia diretório

├── prepara briefing

├── edita documento inline

├── define arquitetura

├── pesquisa referências

├── escreve README

├── escreve SKILL.md

├── cria commands

├── cria templates

├── cria schemas

├── cria testes

├── chama Script Creator

├── testa o pacote

├── corrige falhas

├── gera release

├── salva no GitHub

├── salva no Drive

├── atualiza Excel

├── registra evidências

└── libera WF2

Definition of Done do WF1

O WF1 TERMINA SOMENTE QUANDO

├── a skill foi construída;

├── os arquivos foram validados;

├── o pacote foi gerado;

├── os testes críticos passaram;

├── a versão foi registrada;

├── o pacote foi salvo;

├── a Planilha Master foi atualizada;

├── as evidências foram vinculadas;

├── o handoff foi produzido;

└── o próximo workflow foi preparado.

O ponto central é: o catálogo de recursos funciona como uma biblioteca executável; o WorkStructor cruza objetivo, contexto, dependências e capacidades para compor automaticamente o menor pipeline ponta a ponta.