---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6-luna
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 8542
tokens_saida: 3445
custo_usd: 0.002577
tempo_segundos: 31.52
timestamp: 2026-11-13T18:11:15-03:00
---

A gente considera os clientes fixos dos vendedores habilitados de televendas. Separamo-los pela UF: PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF ficam em um grupo; AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE ficam no outro. Os clientes não deixam de pertencer ao grupo da sua região por também se encaixarem em alguma condição de atendimento.

Antes das demais situações, cliente com status na Receita Federal como baixada não deve ser agendado. Depois, prospect de qualquer uma das duas regiões deve ser atendido a cada 14 dias. Para os demais casos, a prioridade é seguir as situações regionais abaixo, considerando primeiro as condições mais específicas de faturamento; o que não se enquadrar nas situações padrão fica sem agendamento.

Nas regiões PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF, para MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, quem comprou com qualquer vendedor da empresa nos últimos 120 dias e tem faturamento médio anual com a empresa acima de R$ 25000 deve ser atendido a cada 14 dias; acima de R$ 10000, a cada 21 dias; e, sem exigência de faturamento, a cada 28 dias. Para quem comprou com qualquer vendedor da empresa nos últimos 150 dias, os que têm faturamento médio anual acima de R$ 25000 ou acima de R$ 10000 devem ser atendidos a cada 14 dias. Também há atendimento a cada 14 dias para quem comprou nos últimos 150 dias com o próprio vendedor responsável, sem exigência de faturamento. Para os demais clientes desses ramos, sem exigência de compra recente, os que têm faturamento médio anual acima de R$ 25000, acima de R$ 10000 ou sem exigência de faturamento são atendidos a cada 14 dias.

Para EPI e LICITACAO nessas mesmas UFs, o padrão é igual: compra com qualquer vendedor da empresa nos últimos 120 dias e faturamento médio anual acima de R$ 25000 significa atendimento a cada 14 dias; acima de R$ 10000, a cada 21 dias; e, sem exigência de faturamento, a cada 28 dias. Para compra com qualquer vendedor nos últimos 150 dias, os clientes acima de R$ 25000 ou acima de R$ 10000 de faturamento médio anual são atendidos a cada 14 dias, assim como os que não têm exigência de faturamento. Sem exigência de compra recente, os clientes acima de R$ 25000, acima de R$ 10000 ou sem exigência de faturamento também são atendidos a cada 14 dias.

Para ATACADO nessas UFs, quem comprou com qualquer vendedor da empresa nos últimos 120 dias e tem faturamento médio anual acima de R$ 50000 é atendido a cada 10 dias; acima de R$ 25000, a cada 14 dias; e, sem exigência de faturamento, a cada 21 dias. Para quem comprou com qualquer vendedor nos últimos 150 dias, o atendimento é a cada 7 dias acima de R$ 50000, a cada 10 dias acima de R$ 25000 e a cada 14 dias sem exigência de faturamento. Sem exigência de compra recente, é a cada 10 dias acima de R$ 50000 ou acima de R$ 25000, e a cada 21 dias sem exigência de faturamento.

Para CONS. FINAL nessas UFs, quem comprou com qualquer vendedor da empresa nos últimos 120 dias é atendido a cada 28 dias, tanto acima de R$ 15000 como acima de R$ 10000 de faturamento médio anual, e também sem exigência de faturamento. Para quem comprou com qualquer vendedor nos últimos 150 dias, o atendimento é a cada 14 dias acima de R$ 15000, acima de R$ 10000 ou sem exigência de faturamento. Sem exigência de compra recente, os clientes acima de R$ 15000, acima de R$ 10000 ou sem exigência de faturamento são atendidos a cada 28 dias.

Nas regiões AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE, para MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, quem comprou com qualquer vendedor da empresa nos últimos 150 dias e tem faturamento médio anual acima de R$ 25000 deve ser atendido a cada 14 dias; acima de R$ 10000, a cada 21 dias; e, sem exigência de faturamento, a cada 28 dias. Para quem comprou com qualquer vendedor da empresa nos últimos 180 dias, os que têm faturamento médio anual acima de R$ 25000 ou acima de R$ 10000 são atendidos a cada 14 dias, assim como os que não têm exigência de faturamento. Sem exigência de compra recente, os clientes acima de R$ 25000, acima de R$ 10000 ou sem exigência de faturamento são atendidos a cada 14 dias.

Para EPI e LICITACAO nessas mesmas UFs, quem comprou com qualquer vendedor da empresa nos últimos 150 dias é atendido a cada 14 dias acima de R$ 25000 de faturamento médio anual, a cada 21 dias acima de R$ 10000 e a cada 28 dias sem exigência de faturamento. Para compra com qualquer vendedor nos últimos 180 dias, o atendimento é a cada 14 dias acima de R$ 25000, acima de R$ 10000 ou sem exigência de faturamento. Sem exigência de compra recente, os clientes acima de R$ 25000, acima de R$ 10000 ou sem exigência de faturamento também são atendidos a cada 14 dias.

Para ATACADO nessas UFs, quem comprou com qualquer vendedor da empresa nos últimos 150 dias e tem faturamento médio anual acima de R$ 50000 é atendido a cada 10 dias; acima de R$ 25000, a cada 14 dias; e, sem exigência de faturamento, a cada 21 dias. Para quem comprou com qualquer vendedor nos últimos 180 dias, o atendimento é a cada 7 dias acima de R$ 50000, a cada 10 dias acima de R$ 25000 e a cada 14 dias sem exigência de faturamento. Sem exigência de compra recente, é a cada 10 dias acima de R$ 50000 ou acima de R$ 25000, e a cada 21 dias sem exigência de faturamento.

Para CONS. FINAL nessas UFs, quem comprou com qualquer vendedor da empresa nos últimos 150 dias é atendido a cada 28 dias, tanto acima de R$ 15000 como acima de R$ 10000 de faturamento médio anual, e também sem exigência de faturamento. Para quem comprou com qualquer vendedor nos últimos 180 dias, o atendimento é a cada 14 dias acima de R$ 15000, acima de R$ 10000 ou sem exigência de faturamento. Sem exigência de compra recente, os clientes acima de R$ 15000 ou acima de R$ 10000 são atendidos a cada 28 dias. Para os demais clientes CONS. FINAL dessa região, não está definido de quanto em quanto tempo atender. Todo cliente que não se enquadrar nas situações padrão fica sem agendamento.

Quando um cliente se encaixa em mais de uma faixa de faturamento, vale primeiro a frequência da faixa acima de R$ 25000 ou R$ 50000, conforme o ramo, depois a da faixa acima de R$ 10000 ou R$ 25000 e, por fim, a faixa sem exigência de faturamento. As condições de compra recente com prazos diferentes também podem se sobrepor; nesse caso, vale primeiro a situação de prazo mais curto descrita para o ramo e a região.
