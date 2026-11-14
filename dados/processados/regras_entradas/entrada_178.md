---
regra_id: 178
arquivo_regra: regra_178.gobr
hash_regra_sha256: 1a7d314a6e07ad6bfcea5457eb260cfb47e16ae485fda6060a8bb9009a15b900
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2718
tokens_saida: 682
custo_usd: 0.006128
tempo_segundos: 8.94
timestamp: 2026-11-13T19:46:25-03:00
---

Os vendedores habilitados do televendas atendem seus clientes, e o vendedor 48 segue um atendimento separado para os dele.

Para o televendas, primeiro não agendamos clientes com situação baixada na Receita Federal nem os que compraram com o próprio vendedor nos últimos 39 dias. Depois, atendemos a cada 15 dias quem comprou com esse vendedor entre 40 e 89 dias atrás. Quem comprou entre 90 e 119 dias atrás, entre 120 e 359 dias atrás ou não comprou com ele nos últimos 359 dias é atendido a cada 7 dias.

Para o vendedor 48, primeiro não agendamos os clientes cadastrados há 7 dias. Depois, nessa ordem, atendemos os cadastrados há 60 dias a cada 30 dias; os cadastrados há 30 dias, a cada 20 dias; e os cadastrados há 15 dias ou há 8 dias, a cada 15 dias. Se um cliente se encaixar em mais de uma dessas situações, vale a primeira.
