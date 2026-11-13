---
regra_id: 059
arquivo_regra: regra_059.gobr
hash_regra_sha256: 6781af05840724fcb632d459a063c15bb1f622534fa63bbe5bee4b8e43da2927
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3004
tokens_saida: 456
custo_usd: 0.005284
tempo_segundos: 6.66
timestamp: 2026-11-13T19:45:46-03:00
---

Para os vendedores do televendas, primeiro não agendamos clientes cujo ramo de atividade seja diferente de 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 17, 18 e 19.

Depois, atendemos a cada 30 dias os clientes que nunca compraram com a empresa e são dos ramos 2, 7, 11, 12, 14 ou 19.

Entre os que ainda não receberam um tratamento, para os clientes ativos em relação ao vendedor que cuida deles, atendemos a cada 30 dias os dos ramos 3, 4, 6, 8, 15 ou 18; a cada 15 dias os dos ramos 7 ou 17; a cada 7 dias os dos ramos 10, 11, 14 ou 19; e a cada 5 dias os dos ramos 2 ou 12.

Para os demais, sem exigir que sejam inativos, atendemos a cada 30 dias os dos ramos 3, 4, 6, 8, 15 ou 18; a cada 20 dias os do ramo 17; a cada 15 dias os do ramo 10; e a cada 10 dias os dos ramos 11 ou 19. Todo o resto é atendido a cada 5 dias.
