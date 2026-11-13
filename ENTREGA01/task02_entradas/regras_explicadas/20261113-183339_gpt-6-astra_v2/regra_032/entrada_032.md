---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6-astra
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 8542
tokens_saida: 1564
custo_usd: 0.163620
tempo_segundos: 26.69
timestamp: 2026-11-13T18:38:00-03:00
---

A gente trabalha com todos os vendedores do televendas que estão habilitados no sistema, cada um cuidando dos seus clientes fixos. Separamos esses clientes em dois grupos: um com os estados PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF, e outro com AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE. Os grupos são formados de maneira independente, sem tirar do segundo quem entrou no primeiro; pelas siglas de estado, porém, eles não se sobrepõem.

Antes de qualquer atendimento, não agendamos clientes com situação baixada na Receita Federal. Isso vale para todos os clientes atendidos pelo televendas, não só para os dois grupos regionais. Depois, nos dois grupos regionais juntos, atendemos a cada 14 dias quem nunca comprou com a empresa. Para os demais, seguimos os critérios abaixo na ordem apresentada: cada cliente fica com o primeiro atendimento em que se encaixar, sem passar para os seguintes.

O padrão por ramo é parecido nos dois grupos, mas os prazos de compra mudam. No grupo de PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF, olhamos primeiro quem comprou nos últimos 120 dias e, entre os que sobraram, quem comprou nos últimos 150 dias. No grupo de AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE, olhamos primeiro quem comprou nos últimos 150 dias e depois, entre os que sobraram, quem comprou nos últimos 180 dias. Em todos esses casos, contamos compras com qualquer vendedor da empresa, com uma única exceção que explicamos a seguir. Todos os valores de faturamento citados são a média por ano considerando a empresa inteira.

Para os ramos MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, entre os clientes que compraram no primeiro prazo do seu grupo regional, atendemos a cada 14 dias os que têm faturamento médio por ano acima de R$ 25000; depois, a cada 21 dias os que têm essa média acima de R$ 10000; e a cada 28 dias os demais que compraram nesse mesmo prazo. Entre os clientes desses ramos que sobraram, olhamos o segundo prazo regional: primeiro os de média acima de R$ 25000, com atendimento a cada 14 dias; depois os de média acima de R$ 10000, também a cada 14 dias; e depois os demais que compraram nesse segundo prazo, igualmente a cada 14 dias. É nessa última situação que há a exceção: no grupo de PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF, os últimos 150 dias são contados somente pelas compras com o próprio vendedor do cliente, não com qualquer vendedor da empresa. No outro grupo, essa situação continua considerando compras com qualquer vendedor nos últimos 180 dias. Para quem ainda sobrar nesses quatro ramos, sem exigir compra em determinado prazo, atendemos primeiro os de média acima de R$ 25000 a cada 14 dias, depois os de média acima de R$ 10000 a cada 14 dias e, por fim, todos os demais a cada 14 dias.

Para EPI e LICITACAO, seguimos a mesma sequência nos dois grupos regionais, mas sem aquela exceção de contar compras só com o próprio vendedor. Entre os que compraram com qualquer vendedor no primeiro prazo regional, atendemos primeiro os de média acima de R$ 25000 a cada 14 dias, depois os de média acima de R$ 10000 a cada 21 dias e os demais desse prazo a cada 28 dias. Dos que sobraram e compraram com qualquer vendedor no segundo prazo regional, atendemos primeiro os de média acima de R$ 25000, depois os de média acima de R$ 10000 e depois os demais desse prazo, todos a cada 14 dias. Dos que ainda sobraram nesses dois ramos, sem exigir prazo de compra, atendemos primeiro os de média acima de R$ 25000, depois os de média acima de R$ 10000 e depois todo o resto, também a cada 14 dias.

Para ATACADO, nos dois grupos regionais, entre os que compraram com qualquer vendedor no primeiro prazo regional, atendemos primeiro os de faturamento médio por ano acima de R$ 50000 a cada 10 dias, depois os de média acima de R$ 25000 a cada 14 dias e os demais desse prazo a cada 21 dias. Entre os que sobraram e compraram com qualquer vendedor no segundo prazo regional, atendemos primeiro os de média acima de R$ 50000 a cada 7 dias, depois os de média acima de R$ 25000 a cada 10 dias e os demais desse prazo a cada 14 dias. Para os que ainda sobraram em ATACADO, sem exigir prazo de compra, atendemos primeiro os de média acima de R$ 50000 a cada 10 dias, depois os de média acima de R$ 25000 também a cada 10 dias e todos os demais a cada 21 dias.

Para CONS. FINAL, nos dois grupos regionais, entre os que compraram com qualquer vendedor no primeiro prazo regional, atendemos primeiro os de faturamento médio por ano acima de R$ 15000, depois os de média acima de R$ 10000 e depois os demais desse prazo, todos a cada 28 dias. Entre os que sobraram e compraram com qualquer vendedor no segundo prazo regional, atendemos primeiro os de média acima de R$ 15000, depois os de média acima de R$ 10000 e depois os demais desse prazo, todos a cada 14 dias. Entre os que ainda sobraram em CONS. FINAL, sem exigir prazo de compra, atendemos primeiro os de média acima de R$ 15000 a cada 28 dias e depois os de média acima de R$ 10000 também a cada 28 dias. Para todos os demais desse ramo no grupo de PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF, o atendimento é a cada 28 dias. Já para todos os demais desse ramo no grupo de AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE, ainda não definimos de quanto em quanto tempo atender.

Por último, não agendamos os demais clientes do televendas que não se encaixaram nas situações anteriores.
