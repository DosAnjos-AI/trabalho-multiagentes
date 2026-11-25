# script30_entrada

No do agente que converte a entrada da pessoa em texto e decide se ela traz o minimo para seguir. Nao limpa o texto,
nao escreve regra e nao fala com a pessoa: devolve um objeto, e quem pergunta o que falta e o `agente.py`, a partir
dos tokens. Nao escreve em disco nem no BigQuery.

## O que recebe

`classificar_entrada(tipo_entrada, turno, conteudo, ctx)`

- `tipo_entrada`: `texto`, `audio`, `imagem`, `documento` ou `misto`. O chamador informa o tipo; o no nao adivinha.
  Implementados (`TIPOS_ENTRADA_IMPLEMENTADOS`): `texto`, `imagem`, `documento` e `audio`. `misto` levanta erro: o
  `agente.py` entrega um arquivo por turno, entao nao ha como compor mais de um tipo; depende de decisao do Mestre.
- `turno`: `primeiro` ou `mudanca`.
- `conteudo`: para `texto`, o que a pessoa disse (quando ela completa um pedido, o chamador soma o pedido original e o
  complemento). Para `imagem` e `documento`, o caminho do arquivo; o modelo le o arquivo e o no devolve o texto.
  Para `audio`, o caminho do `.wav`; o reconhecimento de fala transcreve e o modelo recebe so o texto.

## Midia aceita

| Tipo | Extensao | Limite | Prova (modelo `gpt-6.1-terra`, 2026-11-24) |
|---|---|---|---|
| imagem | `.png` | 5 000 000 bytes | aceitou; `image_url` com data URL base64 |
| documento | `.pdf` | 10 000 000 bytes | aceitou; bloco `file` com `file_data` base64 |
| audio | `.wav` | 5 000 000 bytes e 55 s | modelo do no recusa audio (`Content blocks are expected to be either text or image_url type`); por isso a conversao e do reconhecimento de fala |
| misto | (nenhuma) | - | nao implementado: o `agente.py` entrega um arquivo por turno |

Extensoes, limites e a projecao de tokens de midia estao em `config.py` (`EXTENSOES_ENTRADA`, `LIMITE_BYTES_ENTRADA`,
`TOKENS_PROJECAO_MIDIA`). Arquivo inexistente, extensao diferente do tipo ou acima do limite levanta `ErroEntrada` com o
valor recebido e o limite. Jpeg, gif, webp e `.txt` nao foram provados e ficam fora da lista.
- `ctx`: o `Contexto`, criado uma vez por `construir_contexto(config)`.

## Audio: caminho de conversao

```
arquivo .wav -> reconhecimento de fala (Speech-to-Text v2, modelo `long`, pt-BR) -> texto -> modelo do no -> tipo, texto, status, faltantes
```

- Chamada direta por REST (`ENDERECO_FALA`), reconhecedor implicito `_`, autenticacao ADC; nenhum recurso e criado no
  projeto e nenhuma biblioteca foi acrescentada. Modelo, idioma, localizacao e limites: `MODELO_FALA`, `IDIOMA_FALA`,
  `LOCALIZACAO_FALA`, `LIMITE_SEGUNDOS_AUDIO` e `LIMITE_BYTES_ENTRADA` em `config.py`.
- O servico recusa mais de 60 s no reconhecimento direto (erro: `Audio can be of a maximum of 60 seconds.`); o limite do
  no e 55 s e o no confere a duracao pelo cabecalho do `.wav` antes da chamada paga. Acima disso so por lote, que exige
  bucket e fica fora.
- Audio sem fala (silencio) levanta `ErroEntrada` ("nenhuma fala reconhecida") antes de chamar o modelo.
- Custo: `Entrada.custo_fala_usd` e a parte do reconhecimento de fala; `custo_usd` e o total do no. A duracao faturada vem
  da resposta; o preco por minuto (`PRECO_FALA_USD_POR_MINUTO`) e hipotese a confirmar na fatura.
- Prova com voz sintetica (Google TTS, pt-BR): prova o encanamento, nao a qualidade com fala humana.
- Formatos alem de `.wav` nao foram provados e ficam fora da lista.

## O que devolve

Um `Entrada` com quatro campos do prompt: `tipo`, `texto`, `status` (`aprovado`, `incompleto`, `fora_de_escopo`) e
`faltantes` (tokens `quem_atende`, `desfecho`, `conflito`), mais `custo_usd` (total do no) e `custo_fala_usd` (so o reconhecimento de fala; zero fora de audio).
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
