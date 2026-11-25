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

Tabela `exemplos` (descricao, regras, gobr e vetor gravado) e os tres arquivos de apoio da tabela `manual`, lidos
uma vez em `construir_contexto`. As secoes do manual sao lidas sob demanda: em cada turno o no pede ao BigQuery so as
secoes do recorte que ainda nao leu (uma consulta no maximo, nenhuma se todas ja estao em memoria) e guarda o resultado
em memoria do processo; nada vai a disco. A escolha do recorte nao mudou, so o momento da leitura. A credencial do
embedding vem do `google.auth.default`. Secao citada que nao existe no manual interrompe o no, com o nome dela; a
conferencia agora acontece depois do embedding da consulta (custo desprezivel), numa leitura so.
