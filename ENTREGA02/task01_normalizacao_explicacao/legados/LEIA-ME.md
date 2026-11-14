# legados

Tudo aqui saiu de uso, mas nada e apagado: saida paga nunca se exclui, e prompts antigos servem de comparacao.
Nenhum arquivo ativo (`config.py`, `script_normalizacao.py`, `verificar_chaves.py`) le esta pasta.

| Caminho | O que e | Por que fica |
|---|---|---|
| `saida_v1/` | 10 normalizados gerados com o prompt v1 e o auxiliar v1 (ids 037, 057, 116, 128, 148, 158, 169, 191, 208, 243) | Saida paga de versao antiga; substituida pelos 10 do v3 em `dados/processados/regras_normalizadas/` |
| `avaliacoes/avaliacao_b2/saida_v2/` | 10 normalizados do prompt v2 | Saida paga da avaliacao |
| `avaliacoes/avaliacao_b3/saida_v3/` | 10 normalizados do prompt v3 (originais) | Saida paga da avaliacao; copias identicas (mesmo SHA-256) estao em `regras_normalizadas/` |
| `avaliacoes/avaliacao_b3/critico/` | Gabarito, regua, medicao cega, tabela avaliativa e mapa selado | Registro da escolha do v3 |
| `avaliacoes/avaliacao_b3/manual_antes/` | Copia do `manual/` no estado anterior as correcoes | Mostra contra qual manual a avaliacao rodou |
| `avaliacoes/avaliacao_b3/mudancas_manual.md` | Mudancas feitas no manual na rodada | Registro |
| `prompts/` | Prompts v1, rascunho do v1 e v2 | Versoes antigas, para comparacao |
| `prompts/duplicatas_raiz/` | Copias identicas (mesmo SHA-256) dos prompts v1 e v2 que estavam na raiz da tarefa | Preservadas ao mover |
| `regras_para_normalizador_v1.md` | Auxiliar v1 | Versao antiga; o ativo e o v2 |

Os scripts do critico e as copias anonimizadas da avaliacao (`anonimo/`) foram excluidos com aprovacao do Mestre:
eram derivados dos arquivos acima.
