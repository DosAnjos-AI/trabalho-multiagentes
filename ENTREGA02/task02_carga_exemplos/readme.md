# task02_carga_exemplos

Cria a tabela `exemplos` no BigQuery (`multiagentes-514823.govendas_gobr.exemplos`, dataset em US) e carrega os 193
exemplos sinteticos com embeddings. Nao cria as tabelas `prompts` e `manual`.

## Entrada e saida

- Entrada (so leitura): `dados/processados/regras_normalizadas/`, `regras_entradas/` e `regras_gobr/`.
- Vetores: as 193 linhas do formato B de `ENTREGA02/task02_teste_prefixo_embedding/embeddings.jsonl`, copiadas so
  quando o hash do texto bate. O que faltar e gerado na API (ADC).
- Saida (nunca apagada): `saida/<carimbo>_gemini-embedding-2_3072/` com `embeddings.jsonl` (cache dos vetores) e
  `exemplos.ndjson` (arquivo carregado no BigQuery).

## Formato do embedding (regra para consultas futuras)

O texto embutido e `task: sentence similarity | query: ` + `explicacao_normalizada` (formato B). O modelo nao aceita
`task_type`; a instrucao de tarefa vai dentro do texto. `hash_texto_embedding` e o SHA-256 do texto exato enviado,
com prefixo.

**Toda consulta futura deve usar o mesmo prefixo**, com a explicacao normalizada da consulta no lugar. Prefixo
diferente entre consulta e documento distorce a similaridade.

## Configuracao

`config.py`: projeto, dataset, tabela, modelo, endpoint, prefixo, dimensoes, teto de gasto (US$ 2,00) e caminhos.
O preco por milhao de tokens e uma hipotese de referencia; o custo real usa o `usageMetadata` da API.

## Uso (da raiz do projeto)

```
.venv/bin/python -B ENTREGA02/task02_carga_exemplos/script_carga_exemplos.py --estimar     # valida e projeta; nao grava
.venv/bin/python -B ENTREGA02/task02_carga_exemplos/script_carga_exemplos.py --executar    # cria a tabela e carrega
.venv/bin/python -B ENTREGA02/task02_carga_exemplos/script_carga_exemplos.py --executar --retomar <pasta em saida/>
```

Ordem do `--executar`: leitura e validacao local, projecao de custo e teto, embeddings, NDJSON,
`CREATE TABLE IF NOT EXISTS`, trava (`COUNT(*)` deve ser 0), `bq load` sem autodetect, validacoes.

## Avisos

- A carga so roda com a tabela vazia. Tabela com linhas: o script para e nada e carregado.
- O script nunca apaga tabela nem dados. Desfazer e decisao manual (`DROP TABLE` ou `DELETE`).
- Falha em qualquer validacao: o script para e reporta.
- Colunas `NOT NULL`: `exemplo_id`, `origem`, `explicacao_normalizada`, `embedding_modelo`, `hash_texto_embedding` e
  `metadados_normalizado`. Os demais campos aceitam NULL (entradas reais futuras).
