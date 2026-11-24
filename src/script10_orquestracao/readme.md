# Passo 10 - Orquestracao

`script10_orquestracao.py` constroi o grafo LangGraph a partir do mapa declarativo `orquestracao.py` (raiz) e traz as
funcoes dos nos, que adaptam os nos 50, 60 e 80 ao estado do grafo. O mapa (estado, agentes, tools, nos, arestas) nao
vive aqui: para mudar uma ligacao, edite `orquestracao.py`.

- `construir_grafo(config, orquestracao)` valida o mapa, le o contexto de cada no uma vez no BigQuery e compila o grafo
  com memoria em processo.
- Primeira geracao: `normalizacao -> recuperacao -> geracao`. Com `pedido_mudanca` preenchido:
  `normalizacao_pedido -> recuperacao -> geracao_reexecucao`.
- Nada e escrito em disco nem no BigQuery.

## Ponto de entrada

`agente.py`, na raiz: `.venv/bin/python -B agente.py`. A primeira linha digitada e a descricao da regra; cada linha
seguinte e um pedido de mudanca, no mesmo `thread_id`. Linha vazia encerra. A chave da API vem do `.env`, carregado
pelo `config.py`.
