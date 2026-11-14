---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 6b0557f409f750508f8787e409d6a85b77b0726d8f8abafaded3a15c34fa752f
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 8550
tokens_saida: 1075
custo_usd: 0.013925
tempo_segundos: 14.32
timestamp: 2026-11-14T20:56:12-03:00
---

Trabalhamos com os vendedores de televendas habilitados no sistema, cada um com seus clientes fixos. Dividimos esses clientes em dois grupos: um para PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF; outro para AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE. Pela UF, o cliente não fica nos dois grupos ao mesmo tempo.

Primeiro, não agendamos os clientes da equipe que estejam com situação baixada na Receita Federal. Depois, nos dois grupos de estados, atendemos a cada 14 dias os clientes que nunca compraram com a empresa. Para os demais, seguimos as situações abaixo na ordem apresentada: se o cliente se encaixar em mais de uma, vale o primeiro atendimento previsto para ele.

Em cada ramo, olhamos primeiro quem comprou com qualquer vendedor da empresa nos últimos 120 dias no primeiro grupo de estados ou nos últimos 150 dias no segundo. Depois, olhamos quem comprou com qualquer vendedor nos últimos 150 dias no primeiro grupo ou nos últimos 180 dias no segundo. Por fim, olhamos os clientes do ramo sem exigir prazo de compra. Em cada uma dessas etapas, verificamos primeiro o maior limite de faturamento, depois o menor e, por último, atendemos os demais sem exigir faturamento mínimo. O faturamento considerado é a média por ano com a empresa.

Para MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, assim como para EPI e LICITACAO, na primeira etapa atendemos a cada 14 dias quem tem média acima de R$ 25000, a cada 21 dias quem tem média acima de R$ 10000 e a cada 28 dias os demais, sem exigir faturamento mínimo. Na segunda etapa, essas mesmas três situações são atendidas a cada 14 dias. Nessa segunda etapa há uma diferença para MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER no primeiro grupo de estados: para os que entram sem exigência de faturamento mínimo, a compra nos últimos 150 dias é contada somente com o próprio vendedor do cliente. Para EPI e LICITACAO nesse grupo, e para todos esses ramos no segundo grupo de estados, ela é contada com qualquer vendedor da empresa. Na etapa sem prazo de compra, atendemos a cada 14 dias primeiro quem tem média acima de R$ 25000, depois quem tem média acima de R$ 10000 e, por fim, os demais, sem exigir faturamento mínimo.

Para ATACADO, na primeira etapa atendemos a cada 10 dias quem tem média acima de R$ 50000, a cada 14 dias quem tem média acima de R$ 25000 e a cada 21 dias os demais, sem exigir faturamento mínimo. Na segunda etapa, os mesmos limites e a situação sem mínimo recebem atendimento, respectivamente, a cada 7, 10 e 14 dias. Sem exigir prazo de compra, atendemos a cada 10 dias quem tem média acima de R$ 50000, a cada 10 dias quem tem média acima de R$ 25000 e a cada 21 dias os demais, sem exigir faturamento mínimo.

Para CONS. FINAL, na primeira etapa atendemos a cada 28 dias quem tem média acima de R$ 15000, também a cada 28 dias quem tem média acima de R$ 10000 e a cada 28 dias os demais, sem exigir faturamento mínimo. Na segunda etapa, essas três situações são atendidas a cada 14 dias. Sem exigir prazo de compra, atendemos a cada 28 dias primeiro quem tem média acima de R$ 15000, depois quem tem média acima de R$ 10000 e, por fim, os demais, sem exigir faturamento mínimo.

Os demais clientes da equipe que não se enquadrarem nessas situações não são agendados.
