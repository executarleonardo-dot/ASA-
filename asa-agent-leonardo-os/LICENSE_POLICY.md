# LICENSE_POLICY.md — ASA Agent / Leonardo-OS

**Classificação:** internal · **Owner:** Leonardo Batista

## Propriedade

Todo o conteúdo deste pacote — código, contratos, blueprints, Skills, agentes e documentação — é **propriedade de Leonardo Batista** e destina-se a uso interno do Leonardo-OS (ICP 0). Não é software de código aberto e não há concessão de licença pública.

## Fontes incorporadas

As fontes em `references/` e `references/_sources/` são materiais próprios de Leonardo (PRD, System Prompt, Blueprint, briefings, planilha master, referências Sakana/Fugu adaptadas). Devem ser preservadas com atribuição interna e não redistribuídas externamente sem autorização do owner.

## Dependências de terceiros

- **Runtime:** Claude.ai (Anthropic) — sujeito aos termos da Anthropic.
- **Build:** Claude Code (Anthropic).
- **Scripts:** Python 3 (PSF License) usando apenas a biblioteca padrão; nenhuma dependência de terceiros adicionada.

Nenhuma biblioteca com licença restritiva (copyleft viral) foi incluída. Caso uma dependência externa seja adicionada no futuro, registrar licença e compatibilidade aqui antes do empacotamento.

## Uso e redistribuição

- Uso: interno, por Leonardo e agentes autorizados.
- Redistribuição/publicação: requer autorização explícita do owner (alinhado a `SECURITY.md` e à governança de ação externa).
- Marca/atribuição: manter cabeçalhos de schema e `source-map.yaml` ao derivar novos artefatos.

## Revisão

Esta política deve ser revista ao mover o pacote para distribuição (plugin Claude Code / Agent SDK) ou ao adicionar dependências externas.
