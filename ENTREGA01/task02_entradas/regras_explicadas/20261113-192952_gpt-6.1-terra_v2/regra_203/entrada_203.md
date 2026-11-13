---
regra_id: 203
arquivo_regra: regra_203.gobr
hash_regra_sha256: db773506ad40a4ad4bf33da50020b3ac776f1b1b25d7080f9064fdc758d7b5c4
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2839
tokens_saida: 345
custo_usd: 0.004564
tempo_segundos: 6.58
timestamp: 2026-11-13T19:48:13-03:00
---

Para os vendedores de televendas habilitados no sistema, não agendamos clientes com situação baixada na Receita Federal, filiais cujo cliente principal tem código diferente de 36979, inadimplentes, clientes sem venda e clientes que não compraram nos últimos 95 dias.

Entre os demais, damos prioridade aos clientes que fizeram uma única compra com a empresa, atendendo-os a cada 28 dias. Depois, conforme o intervalo histórico médio entre pedidos, atendemos a cada 6 dias quem tem intervalo de 0 a 7 dias; a cada 9 dias, de 8 a 14 dias; a cada 16 dias, de 15 a 21 dias; a cada 23 dias, de 22 a 28 dias; a cada 29 dias, de 29 a 38 dias; e a cada 35 dias, de 39 a 60 dias. Todo o restante é atendido a cada 55 dias.
