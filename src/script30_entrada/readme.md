# script30_entrada

No do agente que converte a entrada da pessoa em texto e decide se ela traz o minimo para seguir. Nao limpa o texto,
nao escreve regra e nao fala com a pessoa: devolve um objeto, e quem pergunta o que falta e o `agente.py`, a partir
dos tokens. Nao escreve em disco nem no BigQuery.

## O que recebe

`classificar_entrada(tipo_entrada, turno, conteudo, ctx)`

- `tipo_entrada`: `texto`, `audio`, `imagem`, `documento` ou `misto`. **Nesta etapa so `texto`**: os demais levantam
  erro dizendo que a midia entra em etapa propria.
- `turno`: `primeiro` ou `mudanca`.
- `conteudo`: o que a pessoa disse. Quando ela completa um pedido, o chamador soma o pedido original e o complemento.
- `ctx`: o `Contexto`, criado uma vez por `construir_contexto(config)`.

## O que devolve

Um `Entrada` com quatro campos do prompt: `tipo`, `texto`, `status` (`aprovado`, `incompleto`, `fora_de_escopo`) e
`faltantes` (tokens `quem_atende`, `desfecho`, `conflito`), mais `custo_usd`, `metadados` e `resposta_crua`.
Status ou token fora do conjunto, cabecalho ausente ou fora de ordem, tipo diferente do enviado e resposta cortada
levantam erro (falha alta).

## De onde vem o conteudo

Prompt: tabela `prompts` do BigQuery, linha unica ativa com `tipo = entrada_minimos` (`TIPO_PROMPT_NO30`), hash
regerado do texto na leitura. Modelo: `MODELO_NO30`, igual ao do no 50. Limite de saida, preco e teto vem das chaves
do no 50 em `config.py`. A chave da API vem de `VARIAVEL_CHAVE` (`.env`).

## No grafo

O no `entrada` e o primeiro do grafo. Devolve `tipo_entrada`, `status_entrada`, `faltantes`, `custo_turno` e o texto
em `descricao_usuario` (primeiro turno) ou `pedido_mudanca` (mudanca); o no 50 le esses campos sem transformacao.
Reprovado (`incompleto` ou `fora_de_escopo`) encerra o turno e o `agente.py` volta ao chat.
