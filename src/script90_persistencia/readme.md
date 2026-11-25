# Passo 90 - Persistencia da regra aprovada

`script90_persistencia.py` grava na tabela `exemplos` (BigQuery) a regra que a pessoa aprovou no chat. E a unica
operacao de escrita do projeto no BigQuery: um `INSERT` por parametro de consulta, uma linha por aprovacao.

## O que entra na linha

| Coluna | Valor |
|---|---|
| `origem`, `status_revisao` | `ORIGEM_GRAVACAO` (`usuario`) e `STATUS_GRAVACAO` (`pendente`), de `config.py` |
| `exemplo_id`, `regra_id`, `id_sessao_turno` | `usuario:<conversa>-turnoN`, `<conversa>-turnoN`, `<conversa>-turnoN` (N = turno da ultima geracao) |
| `entrada` | a descricao da pessoa mais os pedidos de mudanca ate esta regra |
| `explicacao_normalizada`, `regras_extraidas`, `sem_chave` | saida do no 50 |
| `gobr`, `hash_gobr` | arquivo aprovado e SHA-256 do texto, sem corte de espaco |
| `embedding`, `embedding_modelo`, `hash_texto_embedding` | vetor cru de `PREFIXO_EMBEDDING` + descricao (mesmo caminho do corpus) e SHA-256 desse texto |
| `metadados_normalizado`, `metadados_geracao` | o que os nos 50 e 80 devolveram na execucao |

`metadados_geracao.fornecedor` e `.temperatura` ficam NULL: o no 80 nao devolve esses dois valores e o no nao os
fabrica. `metadados_normalizado.id_explicacao` e NULL para origem `usuario` (so o corpus tem arquivo de explicacao).

## Regras

- Aprovar o mesmo turno duas vezes nao grava duas linhas: o `exemplo_id` e conferido antes, sem chamar o embedding.
- Falha do BigQuery sobe com a mensagem dele; o `INSERT` e um comando so, entao nada fica gravado pela metade.
- A linha entra `pendente`: a recuperacao filtra `status_revisao = 'aprovado'` (`STATUS_BUSCA`), logo a regra so vira
  exemplo depois da revisao do Mestre.
- Custo: so o embedding (`TETO_GASTO_NO90_USD` em `config.py`, com projecao antes da chamada).
