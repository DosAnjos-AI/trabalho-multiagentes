# script80_geracao

No do agente que escreve o `.gobr` a partir da descricao normalizada, dos exemplos e do recorte do manual.
Nao confere, nao corrige e nao escreve em disco nem no BigQuery: devolve um objeto; conferir e o no 90.

## O que recebe

`gerar_gobr(descricao, exemplos, secoes_manual, apoio, ctx)`: os tres ultimos vem da `Recuperacao` do no 60.
`ctx` e o `Contexto`, criado uma vez por `construir_contexto(config)`.

## O que devolve

Um `Resultado`: `ok`, `texto_gobr` (a resposta do modelo, sem tratamento; `None` se cortada ou se a API falhou),
`metadados` (modelo, tokens, custo, tempo, `id_prompt`, `hash_prompt`, timestamp), `erros` e `resposta_crua`.

## Config usada (`config.py`, secao do no 80)

| Parametro | Papel |
|---|---|
| `MODELO_NO80` | Modelo da geracao. **Padrao: `gpt-6-luna`** (US$ 0,10 entrada e US$ 0,50 saida por 1M) |
| `MODELOS_NO80` | Lista fechada aceita: `gpt-6-luna`, `gpt-6.1-terra`, `gpt-6.1-sol`. Precos vem de `MODELOS` |
| `TIPO_PROMPT_NO80` | Tipo do prompt na tabela `prompts` (`geracao_gobr`) |
| `TETO_GASTO_NO80_USD` | Teto de gasto da execucao, com projecao antes de cada chamada |
| `MAX_TOKENS_SAIDA` | Limite de saida por chamada (16.000) |

## De onde vem o prompt

Da tabela `prompts` do BigQuery, linha unica com `tipo = geracao_gobr` e `ativo`. O hash gravado precisa regerar do
texto, senao o no interrompe. O prompt ativo e o **v2c**; o v3 e a v1 estao gravados e inativos. Trocar o prompt e
trocar a linha ativa no banco, nao editar arquivo.

## Observacoes

- Os modelos da geracao 6 so aceitam a temperatura padrao (1); o no nao envia o parametro.
- A chave vem da variavel de ambiente `VARIAVEL_CHAVE` (`.env`, ignorado pelo git).
- Modelos de raciocinio gastam parte do limite de saida pensando; uma resposta cortada vem em `erros` e `texto_gobr=None`.
