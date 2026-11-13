---
regra_id: 126
arquivo_regra: regra_126.gobr
hash_regra_sha256: 3d3ddbfdc778f28c9c2e9868fd8cd6fdc2340e40b1394e422d50bfde13a715b1
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2833
tokens_saida: 481
custo_usd: 0.005238
tempo_segundos: 8.19
timestamp: 2026-11-13T19:43:48-03:00
---

Os vendedores 73, 196, 254 e 313 atendem os clientes sob sua responsabilidade. No televendas, os demais vendedores habilitados cuidam cada um dos seus clientes fixos; no atendimento de campo, todos os vendedores habilitados cuidam também dos seus respectivos clientes fixos.

Para os vendedores 73, 196, 254 e 313, atendemos a cada 14 dias os clientes que estão há mais de 31 dias sem comprar com qualquer vendedor da empresa, dando preferência aos dias úteis. Os demais clientes desses vendedores não devem ser agendados.

No televendas, olhamos primeiro os clientes ativos para o próprio vendedor: os que estão em dia são atendidos a cada 14 dias e os inadimplentes, a cada 21 dias. Depois, entre os inativos para o vendedor, os que estão em dia são atendidos a cada 30 dias e os inadimplentes não são agendados. Por fim, os clientes sem venda que ainda não tenham recebido um desses tratamentos são atendidos a cada 30 dias. Em todos esses atendimentos, damos preferência aos dias úteis.

No campo, os clientes ativos para o próprio vendedor são atendidos a cada 7 dias, em intervalo fixo. Todos os demais são atendidos a cada 15 dias, também em intervalo fixo.
