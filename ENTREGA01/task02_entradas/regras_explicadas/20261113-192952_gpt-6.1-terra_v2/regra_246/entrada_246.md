---
regra_id: 246
arquivo_regra: regra_246.gobr
hash_regra_sha256: a2a35299f9f0d41acd35c2589c92ccb5bedfa820a0d40fcea61ca095bf90a4f8
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 4105
tokens_saida: 757
custo_usd: 0.007890
tempo_segundos: 9.54
timestamp: 2026-11-13T19:46:44-03:00
---

Os vendedores de televendas habilitados atendem seus respectivos clientes fixos. Dividimos esses clientes em quatro grupos pelos códigos de ramo de atividade do cadastro. Os grupos são independentes: se um cliente atender aos critérios de mais de um, ele pode aparecer em mais de um grupo.

Primeiro, não agendamos os clientes cuja situação na Receita Federal é baixada. Depois, atendemos a cada 7 dias os clientes que nunca compraram com a empresa. Para os demais, seguimos os grupos abaixo; em cada grupo, verificamos primeiro a compra recente e aplicamos a outra frequência aos que sobrarem.

Para os ramos 101009, 101016, 101025, 101101, 101102, 101103, 101104, 101105, 201008, 201009, 201018 e 201099, quem comprou com qualquer vendedor da empresa nos últimos 45 dias é atendido a cada 14 dias; os demais, a cada 7 dias.

Para os ramos 101001, 101002, 101003, 101004, 101005, 101006, 101007, 101011, 101012, 101014, 101015, 101027, 101028, 101029, 101032, 101035, 101037, 101039, 101106, 101107, 201012, 201016, 301001, 301004, 301007 e 301015, quem comprou com qualquer vendedor da empresa nos últimos 60 dias é atendido a cada 21 dias; os demais, a cada 10 dias.

Para os ramos 101008, 101010, 101017, 101018, 101019, 101020, 101021, 101022, 101023, 101024, 101026, 101031, 101033, 101034, 101036, 101038, 201003, 201004, 201010, 201013, 201014, 201015, 201019, 201022, 201023, 301002, 301005, 301006, 301009, 301010, 301011, 301012, 301013 e 301014, quem comprou com qualquer vendedor da empresa nos últimos 75 dias é atendido a cada 28 dias; os demais, a cada 14 dias.

Para os ramos 101013, 101040, 102001, 102002, 201011, 201021, 201025 e 999999, quem comprou com qualquer vendedor da empresa nos últimos 90 dias é atendido a cada 28 dias; os demais, a cada 14 dias.

Se um cliente se encaixar em mais de uma dessas situações, vale a primeira na ordem apresentada. Todo o resto dos clientes do televendas não deve ser agendado.
