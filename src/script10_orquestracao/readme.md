# Passo 10 - Orquestracao

`script10_orquestracao.py` constroi o grafo LangGraph a partir do mapa declarativo `orquestracao.py` (raiz) e traz as
funcoes dos nos, que adaptam os nos 30, 50, 60, 80 e 90 ao estado do grafo. O mapa (estado, agentes, tools, nos, arestas) nao
vive aqui: para mudar uma ligacao, edite `orquestracao.py`.

- `construir_grafo(config, orquestracao)` valida o mapa, le o contexto de cada no uma vez no BigQuery e compila o grafo
  com memoria em processo.
- O `START` e condicional pelo campo `aprovacao`: vazio segue para `entrada` (fluxo normal); preenchido vai para
  `persistencia -> END` (no 90), porque aprovar nao e pedir regra. A persistencia grava a regra vigente em `exemplos`
  com status `pendente`, devolve `exemplo_gravado`, esvazia `aprovacao` e zera `custo_turno` para o custo do embedding.
- Os campos `metadados_normalizado` e `metadados_geracao` guardam o que os nos 50 e 80 devolveram, para a persistencia.
- Todo turno sem aprovacao comeca no no `entrada` (no 30). Aprovado, primeira geracao: `normalizacao -> recuperacao -> geracao`.
  Aprovado com `pedido_mudanca` preenchido: `normalizacao_pedido -> recuperacao -> geracao_reexecucao`.
  `incompleto` ou `fora_de_escopo`: o turno termina na entrada e o `agente.py` volta ao chat. Sete nos no total.
- Entrega ao no 50: o texto que o no 30 devolve entra em `descricao_usuario` (primeiro turno) ou `pedido_mudanca`
  (mudanca), e o `tipo_entrada` que ele devolve vai ao no 50. `entrada_bruta` fica no estado so como registro.
- Rota por `exceto` em `orquestracao.py`: a aresta condicional da entrada olha `status_entrada` antes de olhar
  `pedido_mudanca`.
- Campo `sem_chave` do estado: itens que a descricao pede e que o no 50 nao encontrou no manual.
  O `agente.py` os imprime como ressalva na conversa, depois do arquivo gerado; a ressalva nunca entra no `.gobr`.
- Nada e escrito em disco. No BigQuery so o no 90 escreve, uma linha por aprovacao.

## Ponto de entrada

`agente.py`, na raiz: `.venv/bin/python -B agente.py [id_da_conversa]` (padrao `conversa1`). A primeira linha digitada
e a descricao da regra; depois de cada regra gerada o programa pergunta `Aprovar a regra? (sim/nao)`. Sim chama o grafo
com `aprovacao` preenchida e imprime o `exemplo_id` gravado e o status `pendente`. Nao pede o que mudar, e a linha
seguinte e um pedido de mudanca, no mesmo `thread_id`. Linha vazia encerra.
Entrada `incompleto`: o programa pergunta uma frase por token faltante (texto fixo no `agente.py`), soma a resposta
ao texto anterior e chama o grafo de novo, sem limite de voltas. Entrada `fora_de_escopo`: mensagem padrao, a entrada
alheia e descartada e a conversa continua. A chave da API vem do `.env`, carregado
pelo `config.py`.
