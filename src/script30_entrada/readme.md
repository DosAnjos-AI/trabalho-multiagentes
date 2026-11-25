# script30_entrada

No do agente que converte a entrada da pessoa em texto e decide se ela traz o minimo para seguir. Nao limpa o texto,
nao escreve regra e nao fala com a pessoa: devolve um objeto, e quem pergunta o que falta e o `agente.py`, a partir
dos tokens. Nao escreve em disco nem no BigQuery.

## O que recebe

`classificar_entrada(tipo_entrada, turno, conteudo, ctx)`

- `tipo_entrada`: `texto`, `audio`, `imagem`, `documento` ou `misto`. O chamador informa o tipo; o no nao adivinha.
  Implementados (`TIPOS_ENTRADA_IMPLEMENTADOS`): `texto`, `imagem` e `documento`. `audio` e `misto` levantam erro
  dizendo que o tipo nao foi provado possivel e que implementa-lo depende de decisao do Mestre.
- `turno`: `primeiro` ou `mudanca`.
- `conteudo`: para `texto`, o que a pessoa disse (quando ela completa um pedido, o chamador soma o pedido original e o
  complemento). Para `imagem` e `documento`, o caminho do arquivo; o modelo le o arquivo e o no devolve o texto.

## Midia aceita

| Tipo | Extensao | Limite | Prova (modelo `gpt-6.1-terra`, 2026-11-24) |
|---|---|---|---|
| imagem | `.png` | 5 000 000 bytes | aceitou; `image_url` com data URL base64 |
| documento | `.pdf` | 10 000 000 bytes | aceitou; bloco `file` com `file_data` base64 |
| audio | (nenhuma) | - | recusado: `Content blocks are expected to be either text or image_url type` |
| misto | (nenhuma) | - | nao implementado: o `agente.py` entrega um arquivo por turno |

Extensoes, limites e a projecao de tokens de midia estao em `config.py` (`EXTENSOES_ENTRADA`, `LIMITE_BYTES_ENTRADA`,
`TOKENS_PROJECAO_MIDIA`). Arquivo inexistente, extensao diferente do tipo ou acima do limite levanta `ErroEntrada` com o
valor recebido e o limite. Jpeg, gif, webp e `.txt` nao foram provados e ficam fora da lista.
- `ctx`: o `Contexto`, criado uma vez por `construir_contexto(config)`.

## O que devolve

Um `Entrada` com quatro campos do prompt: `tipo`, `texto`, `status` (`aprovado`, `incompleto`, `fora_de_escopo`) e
`faltantes` (tokens `quem_atende`, `desfecho`, `conflito`), mais `custo_usd`.
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
