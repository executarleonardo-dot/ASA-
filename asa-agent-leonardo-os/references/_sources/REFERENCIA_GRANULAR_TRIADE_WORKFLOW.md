A tríade funciona como interface executiva. Cada bloco visível contém um pipeline interno completo, com tarefas, recursos, gates, evidências e handoffs.

REFERÊNCIA GRANULAR — TRÍADE DE UM WORKFLOW

Caso aplicado

Workflow: Desenvolver uma skill para o Leonardo OSResponsável: Leonardo + Leonardo Admin OSResultado final: skill validada, testada, documentada, salva e pronta para uso ou entrega.

  

1. Visão simplificada da tríade

WF1 — DESENVOLVER UMA SKILL

  

1. DEFINIR

   └── transformar a necessidade em briefing aprovado

  

2. DESENVOLVER

   └── transformar o briefing em skill funcional e testada

  

3. ENTREGAR

   └── transformar a skill validada em pacote utilizável

Essa é a visão que pode aparecer no DeskOS, dashboard ou folha operacional.

  

2. Estrutura completa

NECESSIDADE

│

▼

1. DEFINIR

│

├── descobrir

├── enquadrar

├── especificar

└── aprovar

    │

    ▼

GATE 1 — BRIEFING APROVADO

│

▼

2. DESENVOLVER

│

├── arquitetar

├── pesquisar

├── construir

├── integrar

└── testar

    │

    ▼

GATE 2 — SKILL VALIDADA

│

▼

3. ENTREGAR

│

├── documentar

├── empacotar

├── salvar

├── comunicar

└── registrar

    │

    ▼

GATE 3 — ENTREGA CONCLUÍDA

  

3. ETAPA 1 — DEFINIR

Objetivo

Transformar uma ideia, dor ou solicitação em uma especificação clara e executável.

Entrada

- ideia inicial;
- problema percebido;
- solicitação de cliente;
- necessidade interna;
- documento existente;
- projeto ativo;
- contexto da macro personalização.

Pipeline granular

1.1 Capturar a necessidade

ENTRADA BRUTA

│

├── mensagem

├── documento

├── problema

├── insight

└── pedido do cliente

Perguntas:

- O que precisa ser criado?
- Para quem?
- Qual problema resolve?
- Qual resultado deve produzir?
- Em qual ambiente será utilizada?
- Qual é a urgência?
- O que já existe?

1.2 Recuperar contexto

Consultar:

- Leonardo Mental;
- Macro Personalização;
- Planilha Master;
- UID do projeto;
- documentos relacionados;
- skills existentes;
- histórico de decisões;
- memória autorizada.

1.3 Identificar o tipo de solução

Decidir se a necessidade exige:

NECESSIDADE

│

├── command

├── skill

├── agent

├── plugin

├── workflow

├── template

└── combinação modular

1.4 Definir usuário e caso de uso

Registrar:

- ICP;
- função do usuário;
- nível técnico;
- contexto de uso;
- frequência;
- dor principal;
- resultado esperado;
- restrições cognitivas e operacionais.

1.5 Definir o escopo

Incluir:

- o que a skill fará;
- o que não fará;
- entradas aceitas;
- outputs obrigatórios;
- ferramentas permitidas;
- dependências;
- riscos;
- critérios de qualidade;
- critérios de parada.

1.6 Criar briefing

Estrutura mínima:

ROLE

GOAL

CONTEXT

INPUTS

CONSTRAINTS

WORKFLOW

DECISION RULES

TOOLS

OUTPUT FORMAT

QUALITY CRITERIA

GUARDRAILS

FAILURE HANDLING

STOP CONDITIONS

1.7 Validar briefing

Verificar:

- problema claramente definido;
- usuário identificado;
- output mensurável;
- dependências conhecidas;
- escopo sem sobreposição;
- ausência de contradições;
- critérios de aceite definidos.

Recursos possíveis

- Product Self Knowledge;
- Cognitive Framework Router;
- AI Gov Discovery Orchestrator;
- OS Partner Admin;
- Planilha Master;
- Google Drive;
- Enterprise Search;
- Web Search;
- Comando 01.

Output da etapa

SKILL_BRIEF.md

Evidência

- briefing preenchido;
- decisões registradas;
- lacunas marcadas;
- escopo aprovado.

Gate 1

GATE 1 — BRIEFING APROVADO

  

PASSA SE:

├── problema está claro

├── usuário está definido

├── output está definido

├── escopo está delimitado

├── recursos estão mapeados

└── critérios de aceite existem

  

FALHA SE:

├── objetivo é genérico

├── usuário é desconhecido

├── solução já existe

├── dependências críticas faltam

└── não é possível validar o resultado

  

4. ETAPA 2 — DESENVOLVER

Objetivo

Transformar o briefing aprovado em uma skill funcional, segura e testável.

Entrada

- briefing aprovado;
- referências;
- template de skill;
- stack autorizado;
- decisões arquiteturais.

Pipeline granular

2.1 Projetar a arquitetura

Definir:

SKILL

│

├── SKILL.md

├── commands

├── agents

├── references

├── templates

├── schemas

├── tests

└── README

Decidir:

- standalone ou integrada;
- progressive disclosure;
- comandos necessários;
- referências internas;
- subagentes;
- conectores;
- memória;
- estado;
- logs.

2.2 Mapear dependências

Para cada atividade, identificar:

- documento necessário;
- skill necessária;
- plugin;
- conector;
- permissão;
- ferramenta;
- decisão humana;
- saída anterior obrigatória.

Exemplo:

CRIAR SKILL

│

├── depende de briefing aprovado

├── depende de template validado

├── depende de referências

├── depende de regras de segurança

└── depende de ambiente de teste

2.3 Pesquisar referências

Executar:

- busca na Planilha Master;
- busca no Drive;
- consulta ao repositório;
- Web Search;
- documentação oficial;
- pesquisa de padrões;
- comparação com skills existentes.

Registrar:

- fonte;
- relevância;
- data;
- decisão suportada;
- lacuna encontrada.

2.4 Selecionar recursos

Exemplo de composição:

Comando 01

│

└── inicia o desenvolvimento

  

Meta Template Specialist

│

└── cria a arquitetura-base

  

Standalone Progressive Skill Template

│

└── estrutura diretórios e arquivos

  

Cognitive Framework Router

│

└── seleciona lógica de raciocínio

  

Drive Connector

│

└── recupera referências

  

Web Search

│

└── pesquisa fontes externas

  

Comando de Síntese

│

└── consolida os insumos

  

GitHub

│

└── versiona o resultado

2.5 Construir a skill

Produzir:

- descrição;
- gatilhos;
- instruções;
- workflow;
- regras de decisão;
- outputs;
- guardrails;
- tratamento de falhas;
- exemplos Do/Don’t;
- estrutura de arquivos.

2.6 Criar os comandos

Cada comando deve possuir:

COMMAND

│

├── nome

├── objetivo

├── gatilho

├── inputs

├── ação

├── recursos

├── output

├── validação

└── condição de parada

2.7 Criar templates e schemas

Exemplos:

- briefing;
- YAML Card;
- relatório;
- handoff;
- checklist;
- eval;
- decision record;
- error report.

2.8 Integrar recursos

Validar:

- conectores chamados corretamente;
- plugins utilizados apenas quando necessários;
- commands encadeados;
- arquivos encontrados;
- outputs transferidos entre etapas;
- permissões respeitadas.

2.9 Testar

Tipos de teste:

TESTES

│

├── happy path

├── entrada incompleta

├── entrada ambígua

├── dado conflitante

├── ferramenta indisponível

├── conector sem acesso

├── risco de segurança

├── output genérico

└── condição de parada

2.10 Corrigir

Ciclo:

TESTAR

│

▼

IDENTIFICAR FALHA

│

▼

LOCALIZAR CAUSA

│

▼

CORRIGIR

│

▼

RETESTAR

Recursos possíveis

- Meta Template Specialist;
- Standalone Progressive Skill Template;
- Directory Specialist;
- Padrão OS;
- SOP OS;
- plugin Engineer;
- plugin Product Management;
- Claude Design;
- GitHub;
- Drive;
- Web Search;
- Comando 02.

Outputs da etapa

skill/

├── SKILL.md

├── README.md

├── commands/

├── references/

├── templates/

├── schemas/

└── tests/

Evidências

- arquivos gerados;
- testes executados;
- falhas corrigidas;
- versão registrada;
- critérios de aceite atendidos.

Gate 2

GATE 2 — SKILL VALIDADA

  

PASSA SE:

├── estrutura está completa

├── instruções são executáveis

├── outputs estão padronizados

├── testes críticos passaram

├── guardrails estão ativos

├── dependências estão documentadas

└── skill resolve o problema original

  

FALHA SE:

├── output continua genérico

├── skill depende de contexto oculto

├── testes falham

├── arquivos estão incompletos

├── existem segredos

└── não há rastreabilidade

  

5. ETAPA 3 — ENTREGAR

Objetivo

Transformar a skill validada em um pacote utilizável, rastreável e acessível.

Entrada

- skill validada;
- testes aprovados;
- arquivos finais;
- versão;
- destino da entrega.

Pipeline granular

3.1 Revisar

Verificar:

- nome oficial;
- IDs;
- versão;
- estrutura;
- links internos;
- referências;
- formatação;
- arquivos duplicados;
- dados sensíveis.

3.2 Documentar

Criar:

- README geral;
- instruções de instalação;
- instruções de uso;
- exemplos;
- dependências;
- limitações;
- changelog;
- critérios de manutenção.

3.3 Empacotar

Gerar:

nome-da-skill.skill.zip

Validar:

- diretório correto;
- arquivos obrigatórios;
- ausência de temporários;
- ausência de segredos;
- nomenclatura consistente.

3.4 Salvar

Destinos possíveis:

- GitHub;
- Google Drive;
- diretório Leonardo OS;
- biblioteca de skills;
- workspace do cliente.

3.5 Registrar

Atualizar:

- Planilha Master;
- UID da skill;
- versão;
- owner;
- data;
- status;
- dependências;
- localização;
- testes;
- cliente ou projeto relacionado.

3.6 Comunicar

Produzir:

- mensagem de conclusão;
- resumo executivo;
- link do arquivo;
- instruções;
- limitações;
- próxima ação.

3.7 Executar handoff

Quando existir cliente ou desenvolvedor:

HANDOFF

│

├── o que foi criado

├── por que foi criado

├── como utilizar

├── dependências

├── riscos

├── testes realizados

├── arquivos

└── próximo responsável

3.8 Liberar próximo workflow

Ao concluir a skill:

SKILL ENTREGUE

│

├── pode entrar em operação

├── pode ser publicada

├── pode gerar conteúdo

├── pode virar case

└── pode alimentar novo produto

Recursos possíveis

- Cross Account Handoff Orchestrator;
- DOC Authoring;
- Internal Comms;
- GitHub;
- Drive;
- Gmail;
- Excel;
- Planilha Master;
- Comando 03.

Outputs da etapa

- pacote .skill.zip;
- README;
- changelog;
- registro na Planilha Master;
- link do repositório;
- mensagem de handoff;
- evidência de entrega.

Gate 3

GATE 3 — ENTREGA CONCLUÍDA

  

PASSA SE:

├── pacote final existe

├── pacote abre corretamente

├── versão está registrada

├── documentação está incluída

├── destino está acessível

├── handoff foi produzido

└── próxima ação está definida

  

FALHA SE:

├── arquivo está apenas local

├── não existe documentação

├── versão não foi registrada

├── cliente não recebeu acesso

├── pacote está incompleto

└── não existe evidência de conclusão

  

6. Resumo operacional da tríade

|   |   |   |
|---|---|---|
|Camada|Pergunta central|Resultado|
|Definir|O que deve ser criado e por quê?|Briefing aprovado|
|Desenvolver|Como transformar o briefing em solução funcional?|Skill validada|
|Entregar|Como tornar a solução utilizável e rastreável?|Pacote entregue|

  

7. Interface para uso diário

WF1 — DESENVOLVER SKILL

  

[ ] 1. DEFINIR

    Output: briefing aprovado

  

[ ] 2. DESENVOLVER

    Output: skill testada

  

[ ] 3. ENTREGAR

    Output: pacote salvo e registrado

Próxima ação dinâmica

O DeskOS não precisa mostrar todas as tarefas ao mesmo tempo.

Exemplo:

STATUS: ETAPA 1 — DEFINIR

  

PRÓXIMA AÇÃO:

Preencher o problema, usuário e output esperado.

  

BLOQUEIO:

Ainda não foi escolhido o ICP.

  

EVIDÊNCIA ESPERADA:

SKILL_BRIEF.md aprovado.

  

8. Regra arquitetural

TRÍADE VISÍVEL

│

├── reduz carga cognitiva

├── mostra progresso

└── orienta próxima ação

  

PIPELINE INTERNO

│

├── executa SOP completo

├── aciona o stack necessário

├── controla dependências

├── valida gates

└── registra evidências

A tríade não reduz o workflow. Ela reduz apenas a complexidade apresentada ao usuário.