---
regra_id: 189
arquivo_regra: regra_189.gobr
hash_regra_sha256: 9edc86ced43a78da5a53afa459fa70bda6fa4a2d5ed664a1eeac7af4ababc26a
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2622
tokens_saida: 730
custo_usd: 0.006272
tempo_segundos: 9.62
timestamp: 2026-11-13T19:39:47-03:00
---

Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade quando alguém se encaixa em mais de uma situação.

Para quem não comprou com nenhum vendedor da empresa neste ano e tem ticket médio acima de R$ 4999, o atendimento é semanal, em dia fixo, com preferência por segunda e sexta. Para quem também não comprou da empresa neste ano e tem ticket médio abaixo de R$ 4999, o atendimento é semanal, em dia fixo, com preferência por terça e sexta. Quem não comprou da empresa neste ano, mas comprou no ano passado, é atendido semanalmente, com preferência por quarta e quinta.

Quem ainda não comprou com o próprio vendedor é atendido a cada 7 dias, assim como quem fez uma única compra com esse vendedor. Para clientes com intervalo histórico de compra entre 0 e 14 dias, seguimos esse histórico, atendendo no mínimo a cada 4 dias e no máximo a cada 6 dias. Por fim, quem está entre 25 e 30 dias além do período habitual de compra com o próprio vendedor é atendido a cada 7 dias.
