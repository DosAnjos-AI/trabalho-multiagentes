# task04_carga_manual

Cria a tabela `manual` no BigQuery (`multiagentes-514823.govendas_gobr.manual`, dataset em US) e carrega 30 linhas do
manual parseado. Nao altera `exemplos` nem `prompts`.

## Entrada e saida

- Entrada (so leitura): `manual/03-secoes/*.md` (27 arquivos), `manual/01-conceitos.md`, `manual/02-invariantes.md` e
  `manual/03-mapa.md`. `manual/CORRECOES_MANUAL.md` fica de fora (historico humano).
- Saida (nunca apagada): `saida/<carimbo>/manual.ndjson`, o arquivo carregado no BigQuery.

## Schema

| Coluna | Tipo | Nulo? | Observacao |
|---|---|---|---|
| `caminho` | STRING | nao | Chave. Relativo a `manual/`, igual ao valor de `exemplos.regras_extraidas` (ex.: `03-secoes/03-01-times.md`); os 3 de raiz ficam sem pasta |
| `tipo` | STRING | nao | `secao` (`03-secoes/*.md`, inclui `10-gramatica.md`), `conceitos`, `invariantes` ou `mapa` |
| `texto` | STRING | nao | Conteudo fiel do arquivo (bytes decodificados em UTF-8, sem conversao de quebra de linha) |
| `hash` | STRING | nao | SHA-256 hex (64 caracteres) dos bytes do arquivo |

Ligacao com `exemplos`: `manual.caminho IN UNNEST(exemplos.regras_extraidas)`.

## Uso (da raiz do projeto)

```
.venv/bin/python -B ENTREGA02/task04_carga_manual/script_carga_manual.py --verificar   # le, calcula hash, confere caminhos; nao grava
.venv/bin/python -B ENTREGA02/task04_carga_manual/script_carga_manual.py --executar    # cria a tabela, carrega e valida
```

Ordem do `--executar`: leitura e hash, conferencia dos caminhos (de `exemplos` e do auxiliar), NDJSON,
`CREATE TABLE IF NOT EXISTS`, trava (`COUNT(*)` deve ser 0), `bq load` sem autodetect e sem tabela de passagem,
validacoes.

## Avisos

- **`hash` e palavra reservada do BigQuery:** escreva `` `hash` `` entre crases em qualquer SQL.
- **Atualizacao do manual nao esta coberta.** Editar um arquivo do manual muda o `hash` da mesma linha (a chave e o
  `caminho`), e esta carga so roda com a tabela vazia. Atualizar exige `MERGE` ou `UPDATE`, fora deste escopo.
- A carga so roda com a tabela vazia. Tabela com linhas: o script para e nada e carregado.
- O script nunca apaga tabela nem dados. Desfazer e decisao manual (`DROP TABLE` ou `DELETE`).
- Falha em qualquer validacao: o script para e reporta.
