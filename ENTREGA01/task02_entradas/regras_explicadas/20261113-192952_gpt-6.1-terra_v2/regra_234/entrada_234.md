---
regra_id: 234
arquivo_regra: regra_234.gobr
hash_regra_sha256: 3d6de492f5c711c8ee6b4f54959c30edb979a09a59f078eacb2bd6d30705eea6
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2633
tokens_saida: 305
custo_usd: 0.004158
tempo_segundos: 5.52
timestamp: 2026-11-13T19:40:46-03:00
---

Todos os vendedores atendem seus respectivos clientes fixos. Seguimos esta ordem de prioridade: os clientes com queda de faturamento maior que 5% são atendidos a cada 3 dias. Depois, não agendamos os que fizeram a última compra entre 1138 e 9999 dias atrás.

Entre os demais, os clientes da cidade GOIANIA são atendidos no intervalo que a empresa usa para clientes inativos. Depois, os clientes ativos para o próprio vendedor são atendidos no intervalo que a empresa usa para clientes ativos; os inativos para o próprio vendedor e os clientes sem vendas, no intervalo usado para clientes inativos. Nesses atendimentos, damos preferência a dias úteis, sábado e domingo.

Todos os demais clientes são atendidos a cada 7 dias, com preferência por dias úteis.
