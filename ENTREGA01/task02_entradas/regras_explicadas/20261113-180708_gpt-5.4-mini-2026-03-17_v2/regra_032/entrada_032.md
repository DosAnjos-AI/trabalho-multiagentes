---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-5.4-mini-2026-03-17
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 8542
tokens_saida: 1317
custo_usd: 0.012333
tempo_segundos: 9.37
timestamp: 2026-11-13T18:15:35-03:00
---

Nós trabalhamos com os vendedores do televendas que estão ativados. Os clientes desse time são separados em duas carteiras por estado: a carteira sul_sudeste_centrooeste pega PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF; a carteira norte_nordeste pega AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE. A partir daí, o mesmo cliente pode entrar nas regras de curva e de prazo conforme o ramo, o tempo sem comprar e o faturamento, e primeiro tiramos da agenda os que estão baixados na Receita Federal: se o status na receita federal estiver definido como baixada, não agendamos.

Para quem ainda é prospect, a gente atende a cada 14 dias, tanto na carteira sul_sudeste_centrooeste quanto na carteira norte_nordeste. Depois disso, a prioridade segue pelo estágio do cliente e pela curva. Nas regiões Sul, Sudeste e Centro-Oeste, para MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, quem comprou em até 120 dias e fatura mais de R$ 25000 por ano vai a cada 14 dias; se fatura mais de R$ 10000, vai a cada 21 dias; e os demais desses ativos vão a cada 28 dias. Se o cliente desse grupo já está com 150 dias sem positivação, então ele entra como pré-inativo: com faturamento acima de R$ 25000, atendimento a cada 14 dias; com faturamento acima de R$ 10000, também a cada 14 dias; e os que só se enquadram pelo ramo e pela falta de positivação, também a cada 14 dias. Quando o cliente desse mesmo conjunto já está inativo, sem considerar o tempo de positivação, a frequência continua sendo 14 dias em todos os três cortes de faturamento e também para os demais.

Ainda nas regiões Sul, Sudeste e Centro-Oeste, para EPI e LICITACAO a lógica é a mesma, mas com os mesmos prazos de 120 dias para ativo e 150 dias para pré-inativo. Nos ativos, com faturamento acima de R$ 25000 por ano atendemos a cada 14 dias, com faturamento acima de R$ 10000 a cada 21 dias, e os demais a cada 28 dias. Nos pré-inativos, todas as faixas ficam a cada 14 dias. Nos inativos, o atendimento também fica a cada 14 dias para todos os cortes.

Para ATACADO nas regiões Sul, Sudeste e Centro-Oeste, os ativos com faturamento acima de R$ 50000 vão a cada 10 dias, acima de R$ 25000 a cada 14 dias e os demais a cada 21 dias. Se já estão pré-inativos, com 150 dias sem positivação, o cliente acima de R$ 50000 vai a cada 7 dias, acima de R$ 25000 a cada 10 dias e os demais a cada 14 dias. Nos inativos, acima de R$ 50000 e acima de R$ 25000 vão a cada 10 dias, e os demais a cada 21 dias.

Para CONS. FINAL nas regiões Sul, Sudeste e Centro-Oeste, os ativos com mais de R$ 15000 por ano e os que passam de R$ 10000, além dos demais, ficam todos a cada 28 dias quando a compra recente é de até 120 dias. Se estiverem pré-inativos, com 150 dias sem positivação, todos ficam a cada 14 dias. Se estiverem inativos, todos ficam a cada 28 dias.

Nas regiões Norte e Nordeste, a divisão é parecida, mas os prazos mudam em alguns pontos. Para MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, os ativos com faturamento acima de R$ 25000 vão a cada 14 dias, acima de R$ 10000 a cada 21 dias e os demais a cada 28 dias, considerando 150 dias para ativo. Os pré-inativos entram com 180 dias sem positivação: acima de R$ 25000 fica a cada 14 dias, acima de R$ 10000 a cada 14 dias e os demais também a cada 14 dias. Nos inativos, todos ficam a cada 14 dias.

Para EPI e LICITACAO no Norte e Nordeste, os ativos com faturamento acima de R$ 25000 vão a cada 14 dias, acima de R$ 10000 a cada 21 dias e os demais a cada 28 dias, com 150 dias para ativo. Os pré-inativos usam 180 dias sem positivação e ficam todos a cada 14 dias. Nos inativos, todos também ficam a cada 14 dias.

Para ATACADO no Norte e Nordeste, os ativos com faturamento acima de R$ 50000 vão a cada 10 dias, acima de R$ 25000 a cada 14 dias e os demais a cada 21 dias, com 150 dias para ativo. Os pré-inativos usam 180 dias sem positivação: acima de R$ 50000 vai a cada 7 dias, acima de R$ 25000 a cada 10 dias e os demais a cada 14 dias. Nos inativos, acima de R$ 50000 e acima de R$ 25000 vão a cada 10 dias, e os demais a cada 21 dias.

Para CONS. FINAL no Norte e Nordeste, os ativos com mais de R$ 15000 por ano ficam a cada 28 dias, os que passam de R$ 10000 também ficam a cada 28 dias, e os demais ficam a cada 28 dias, com 150 dias para ativo. Os pré-inativos, com 180 dias sem positivação, ficam todos a cada 14 dias. Nos inativos, os de mais de R$ 15000 ficam a cada 28 dias, os de mais de R$ 10000 a cada 28 dias e os demais também a cada 28 dias.

E, se algum cliente do televendas não entrar em nenhuma dessas situações, ele não deve ser agendado.
