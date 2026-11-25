# script60_recuperacao

No do agente que, dada a descricao normalizada, devolve os exemplos `.gobr` mais proximos e o recorte do manual.
So le o BigQuery: nao escreve em disco nem na nuvem.

## O que recebe

`recuperar(texto, regras_consulta, ctx, *, excluir_ids=frozenset(), vetor_consulta=None)`

- `texto`: a descricao normalizada.
- `regras_consulta`: as `regras_extraidas` da consulta (caminhos do manual), vindas do normalizador (no 50).
- `ctx`: o `Contexto`, criado uma vez por `construir_contexto(config)`.
- `excluir_ids`: tira candidatos da busca (leave-one-out do corpus nos testes).
- `vetor_consulta`: reaproveita um embedding ja pago; `None` gera o embedding (cobrado).

## O que devolve

Uma `Recuperacao`: `exemplos`, `secoes_manual` (so o recorte), `apoio` (os tres arquivos, sempre),
`registro` (por que cada exemplo entrou), `caminhos_recorte`, `empate_jaccard`, `tokens_embedding`, `custo_usd`.

## Como escolhe

1. Ramo denso: os `N1_DENSO` exemplos de maior cosseno com a consulta.
2. Ramo Jaccard: os `N2_JACCARD` de maior sobreposicao entre `regras_extraidas` (empate decidido pelo cosseno).
3. Uniao sem duplicata. O recorte do manual e a uniao das `regras_extraidas` da consulta e dos exemplos escolhidos.
   O manual inteiro nunca sai.

## Config usada (`config.py`, secao do no 60)

`TABELA_EXEMPLOS`, `STATUS_BUSCA`, `N1_DENSO` (2), `N2_JACCARD` (2), `MODELO_EMBEDDING`, `DIMENSOES`,
`LOCALIZACAO_EMBEDDING`, `PREFIXO_EMBEDDING`, `TETO_GASTO_NO60_USD`. Tambem usa `PROJETO_GCP`, `DATASET`,
`TABELA_MANUAL` e `CARACTERES_POR_TOKEN_PESSIMISTA`.

Prefixo, modelo, dimensao e endereco do embedding (`PREFIXO_EMBEDDING`, `MODELO_EMBEDDING`, `DIMENSOES`,
`ENDERECO_EMBEDDING`) vem so do `config.py`; o no nao escreve nenhum desses valores. O texto embutido e o prefixo mais a
descricao, sem corte de espaco, igual ao no 90. Mudar prefixo ou modelo invalida os vetores ja gravados.

## De onde vem o conteudo

Tabela `exemplos` e os tres arquivos de apoio da tabela `manual` (lidos uma vez em `construir_contexto`). Os exemplos
NAO sao baixados: nenhum vetor de 3072 posicoes chega a memoria da aplicacao, salvo o da propria consulta. Em cada turno
o no faz duas consultas ao BigQuery, com vetor e chaves como parametro (nunca no texto da consulta):

1. `_pontuar`: para cada exemplo com `status_revisao = STATUS_BUSCA` (e fora de `excluir_ids`), devolve so `exemplo_id`,
   `cosseno` e `jaccard`. Cosseno = `1 - COSINE_DISTANCE(embedding, @vetor)` (funcao nativa do BigQuery; normaliza os
   dois vetores sozinha). Jaccard = chaves em comum / uniao das chaves, sobre conjuntos (`COUNT(DISTINCT ...)`), com
   dois conjuntos vazios valendo 0. A ordenacao, o corte em `N1_DENSO` e `N2_JACCARD`, o desempate e a uniao continuam
   no Python, sobre essas duas colunas numericas, com a mesma regra de antes.
2. `_ler_exemplos`: le so os exemplos escolhidos (ate 4), com explicacao, regras, `sem_chave` e `gobr`, sem `embedding`.

Na partida o BigQuery apenas conta as linhas aprovadas e as de vetor com tamanho errado (nada e baixado). Equivalencia
com a versao anterior (leitura do corpus e numpy) medida em cinco entradas: mesmos exemplos, mesma ordem, diferenca
de cosseno abaixo de 4e-15 e Jaccard identico.

As secoes do manual sao lidas sob demanda: em cada turno o no pede ao BigQuery so as secoes do recorte que ainda nao
leu (uma consulta no maximo, nenhuma se todas ja estao em memoria) e guarda o resultado em memoria do processo; nada
vai a disco. A credencial do embedding vem do `google.auth.default`. Secao citada que nao existe no manual interrompe o
no, com o nome dela.
