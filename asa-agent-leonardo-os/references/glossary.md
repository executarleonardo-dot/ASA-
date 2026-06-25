# Glossary — ASA Agent / Leonardo-OS

**Schema:** LEO-GLOSSARY-v1.0

| Termo | Definição |
|---|---|
| **ASA** | Agentic Systems Architect — papel oficial do agente orquestrador. |
| **ASA Orchestrator Agent** | Único agente runtime v1; orquestra ponta a ponta com o menor stack suficiente. |
| **Leonardo-OS** | Ecossistema operacional de Leonardo: Skills, conectores, DESK-OS, memória, planilha master, projetos, workflows. |
| **Skill (runtime)** | Procedimento empacotado em `SKILL.md` com boundary único (Leonardo Admin, ASA Admin, DeskOS). |
| **Subagente (build-time)** | Agente Claude Code usado apenas para construir/auditar o pacote; não faz parte do runtime v1. |
| **Especialista temporário** | Composição efêmera (role, goal, skills, tools, método, critérios) que existe apenas durante a execução de uma tarefa. |
| **Environment Resolver** | Componente que verifica capacidades reais do ambiente; nunca presume. |
| **Context cascade** | Recuperação de contexto em 9 camadas (0–8): Constituição → Estado. |
| **Intent Classifier** | Classifica domínio, caso de uso, complexidade e risco. |
| **Specialist Composer** | Compõe o especialista temporário a partir da intenção e do menor stack. |
| **Workflow (WF1/WF2/WF3)** | BUILD / COMMUNICATE / OPERATE, sempre com 3 etapas visíveis e gates. |
| **Gate** | Ponto de verificação com `pass_when`/`fail_when`; pode exigir confirmação humana. |
| **Execution Trace** | Registro estruturado de uma execução (intenção, recursos, decisões, gates, evidências, resultado). |
| **DeskOS Handoff** | Contrato que converte estado digital em representação semanal de baixa carga cognitiva. |
| **Recycle** | Classificação pós-execução do que é descartado, mantido ou carregado para o próximo ciclo. |
| **Fixed core** | Parte universal do ASA (governança, cascata, classifier, composer, planner, gates, trace, etc.). |
| **Variable profile** | Parte específica de um ICP (identidade, projetos, Skills instaladas, connectors, rotinas, UIDs). |
| **Fugu / Sakana** | Referência arquitetural adaptada ao ecossistema Claude (orquestrar recursos Claude, não múltiplos modelos externos). |
| **Progressive disclosure** | Mostrar o mínimo necessário na superfície; manter complexidade interna oculta. |
| **`[FATO]` / `[INFERÊNCIA]` / `[HIPÓTESE]` / `[GAP]` / `[LACUNA]`** | Labels epistemológicas obrigatórias de governança. |
| **`[GAP-RUNTIME]`** | Lacuna que só pode ser resolvida com instalação/inspeção/teste no Claude.ai. |
| **OQ-0x** | Open Question do AGENT_BUILD_SPEC §24 (gaps de decisão). |
| **ICP** | Ideal Customer Profile; Leonardo é o ICP 0. |
| **DESK-OS** | Interface físico-digital de baixa carga cognitiva para o estado semanal. |
| **Planilha Master** | `LEONARDO_ADMIN_OS_MASTER.xlsx`; leitura permitida, escrita requer confirmação (OQ-05). |
