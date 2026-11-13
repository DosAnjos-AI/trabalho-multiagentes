---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 8542
tokens_saida: 970
custo_usd: 0.013392
tempo_segundos: 13.12
timestamp: 2026-11-13T18:11:28-03:00
---

Trabalhamos com os vendedores de televendas habilitados e os clientes fixos de cada um. Separamos esses clientes em dois grupos pelo estado: um com PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF; outro com AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE.

Primeiro, não agendamos os clientes de televendas que estejam baixados na Receita Federal. Depois, nos dois grupos de estados, atendemos a cada 14 dias os prospects que nunca compraram com a empresa. Para os demais, seguimos a ordem abaixo: se o cliente se encaixar em mais de uma situação, vale a primeira.

Em cada ramo, olhamos primeiro quem comprou com qualquer vendedor da empresa nos últimos 120 dias no primeiro grupo de estados ou nos últimos 150 dias no segundo. Depois olhamos quem comprou com qualquer vendedor da empresa nos últimos 150 dias no primeiro grupo ou nos últimos 180 dias no segundo. Por fim, olhamos os clientes do ramo sem exigir prazo de compra. Em cada uma dessas etapas, verificamos primeiro quem tem faturamento médio anual com a empresa acima do limite maior, depois quem tem média acima do limite menor e, por último, os demais, sem exigir um valor de faturamento. A exceção na forma de contar a compra está indicada abaixo.

Para MATCON, FERRAGISTA, AGROPECUARIA, HOME CENTER, EPI e LICITACAO, os limites são R$ 25000 e R$ 10000. Na primeira etapa, atendemos respectivamente a cada 14, 21 e 28 dias. Na segunda, as três situações são atendidas a cada 14 dias; na última, também a cada 14 dias. No primeiro grupo de estados, porém, para MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, a terceira situação da segunda etapa olha a compra nos últimos 150 dias só com o próprio vendedor do cliente, não com qualquer vendedor da empresa.

Para ATACADO, os limites são R$ 50000 e R$ 25000. Na primeira etapa, atendemos respectivamente a cada 10, 14 e 21 dias; na segunda, a cada 7, 10 e 14 dias; e, na última, a cada 10, 10 e 21 dias.

Para CONS. FINAL, os limites são R$ 15000 e R$ 10000. Na primeira etapa, as três situações são atendidas a cada 28 dias; na segunda, a cada 14 dias. Na última, atendemos a cada 28 dias quem tem média acima de R$ 15000 e depois quem tem média acima de R$ 10000. Para os demais dessa última etapa, no primeiro grupo de estados o atendimento é a cada 28 dias; no segundo grupo, ainda não definimos de quanto em quanto tempo atender.

Os outros clientes de televendas que não se enquadrarem nessas situações não devem ser agendados.
