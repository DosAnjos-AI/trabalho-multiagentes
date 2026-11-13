---
regra_id: 207
arquivo_regra: regra_207.gobr
hash_regra_sha256: a1dd357ecf0f1ca4c073f811801c66d86d0a2a80039d61b6b62a307e24d202f3
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2547
tokens_saida: 587
custo_usd: 0.005482
tempo_segundos: 9.93
timestamp: 2026-11-13T19:40:08-03:00
---

Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade: clientes pessoa física não devem ser agendados. Para os demais, quem ainda não comprou com seu vendedor deve ser atendido a cada 14 dias.

Para quem já comprou com seu vendedor, olhamos o tempo desde a última compra com ele. Se comprou nos últimos 14 dias, usamos o intervalo do histórico de compras acrescido de 7 dias, com limite de 14 dias. Se a última compra foi entre 14 e 30 dias atrás, atendemos a cada 14 dias; entre 30 e 45 dias, a cada 21 dias; entre 45 e 90 dias, a cada 14 dias. Quem está há mais de 90 dias sem comprar com seu vendedor é atendido a cada 28 dias. Quando o cliente se encaixar em mais de uma dessas situações, vale a primeira nessa ordem.
