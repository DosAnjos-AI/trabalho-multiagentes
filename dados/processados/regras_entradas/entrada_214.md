---
regra_id: 214
arquivo_regra: regra_214.gobr
hash_regra_sha256: c02ebe049568c3042b55218116976b8ac3da30b331f9498c7bd6a2470ab89843
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2966
tokens_saida: 642
custo_usd: 0.006176
tempo_segundos: 8.70
timestamp: 2026-11-13T19:45:40-03:00
---

Os vendedores do televendas atendem seus clientes, com preferência pelos dias úteis e pelo sábado. Primeiro, não agendamos clientes inadimplentes. Para os demais, seguimos a ordem abaixo: quem se encaixar em mais de uma situação recebe o tratamento da primeira.

Quem fez uma única compra com seu próprio vendedor é atendido a cada 14 dias. Depois, para quem fez uma única compra com esse vendedor e comprou com qualquer vendedor da empresa nos últimos 30 dias, prevemos atendimento a cada 21 dias se o ramo de atividade for 29 e a cada 14 dias se for diferente de 29.

Para os clientes ativos com seu vendedor e com intervalo histórico de compras menor que 14 dias, o atendimento é a cada 10 dias. Para quem comprou com seu vendedor entre 21 e 59 dias atrás, é a cada 30 dias no ramo 29 e a cada 14 dias nos demais ramos. Para quem comprou com seu vendedor entre 60 e 89 dias atrás, é a cada 14 dias, tanto no ramo 29 quanto nos demais. Por fim, para quem não comprou com seu vendedor nos últimos 90 dias, o atendimento é a cada 10 dias.
