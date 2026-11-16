# task03_carga_prompts

Cria a tabela `prompts` no BigQuery (`multiagentes-514823.govendas_gobr.prompts`, dataset em US) e carrega os 3 prompts
em uso e os legados, uma linha por hash. Nao altera `exemplos` e nao cria a tabela `manual`.

## Entrada e saida

- Entrada (so leitura): os arquivos listados em `PROMPTS` no `config.py` (3 em uso e 5 legados).
- Saida (nunca apagada): `saida/<carimbo>/prompts.ndjson`, o arquivo carregado no BigQuery.

## Schema

| Coluna | Tipo | Nulo? | Observacao |
|---|---|---|---|
| `hash` | STRING | nao | Chave. SHA-256 hex (64 caracteres) dos bytes do arquivo |
| `arquivo` | STRING | nao | Nome do arquivo, so para leitura humana |
| `tipo` | STRING | nao | `geracao_explicacao`, `normalizador` ou `auxiliar_manual` |
| `versao` | STRING | nao | Do nome do arquivo (`v1`, `v2`, `v3`, `v1_rascunho`) |
| `texto` | STRING | nao | Conteudo fiel do arquivo (bytes decodificados em UTF-8, sem conversao de quebra de linha) |
| `ativo` | BOOL | nao | `true` so nos 3 em uso; legados `false` |

Ligacao com `exemplos`: `metadados_normalizado.hash_prompt` com `normalizador`;
`metadados_normalizado.hash_auxiliar_manual` com `auxiliar_manual`; `metadados_geracao.hash_prompt` com
`geracao_explicacao`.

## Uso (da raiz do projeto)

```
.venv/bin/python -B ENTREGA02/task03_carga_prompts/script_carga_prompts.py --verificar   # le, calcula hash, confere com exemplos; nao grava
.venv/bin/python -B ENTREGA02/task03_carga_prompts/script_carga_prompts.py --executar    # cria a tabela, carrega e valida
```

Ordem do `--executar`: leitura e hash, conferencia com `exemplos`, NDJSON, `CREATE TABLE IF NOT EXISTS`, trava
(`COUNT(*)` deve ser 0), `bq load` sem autodetect e sem tabela de passagem, validacoes.

## Avisos

- **Editar um prompt muda o hash e cria uma linha nova.** As linhas antigas permanecem, porque os exemplos antigos
  apontam para elas pelo hash. Ao trocar um prompt em uso, marque o anterior como `ativo = false` e o novo como `true`.
- O BigQuery nao impede duas linhas ativas no mesmo `tipo`; a validacao de 1 ativo por tipo so roda na carga.
- A carga so roda com a tabela vazia. Tabela com linhas: o script para e nada e carregado.
- O script nunca apaga tabela nem dados. Desfazer e decisao manual (`DROP TABLE` ou `DELETE`).
- Falha em qualquer validacao: o script para e reporta.
- As copias de `legados/prompts/duplicatas_raiz/` ficam de fora (mesmo hash dos arquivos de `legados/prompts/`).
