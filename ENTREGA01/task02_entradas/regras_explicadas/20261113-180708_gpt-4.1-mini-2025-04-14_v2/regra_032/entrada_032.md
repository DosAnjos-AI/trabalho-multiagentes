---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-4.1-mini-2025-04-14
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 8543
tokens_saida: 1853
custo_usd: 0.006382
tempo_segundos: 16.60
timestamp: 2026-11-13T18:12:58-03:00
---

O time responsável pelo atendimento é o televendas, formado por todos os vendedores ativados nessa equipe, que cuidam dos clientes fixos de cada um deles.

Os clientes do televendas são divididos em duas carteiras livres conforme a região onde estão localizados, considerando o estado de seu cadastro: uma carteira reúne os clientes nos estados do Sul, Sudeste e Centro-Oeste — com unidades federativas PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF — e a outra carteira reúne os clientes dos estados do Norte e Nordeste — AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE. Um cliente só pertence a uma dessas duas carteiras, conforme seu estado.

Temos uma regra geral de que clientes cujo status na Receita Federal está definido como baixada não devem ser agendados para atendimento. Além disso, para clientes prospect com a empresa, ou seja, que ainda não compraram, dos dois grupos juntos (tanto Sul, Sudeste e Centro-Oeste quanto Norte e Nordeste), a frequência de atendimento é a cada 14 dias.

Para o restante dos clientes, as regras variam conforme a carteira de região, o ramo de atividade e o ciclo de vida com a empresa, que é considerado ativo, pré-inativo ou inativo, além da curva e do faturamento médio anual.

Começando pela carteira Sul, Sudeste e Centro-Oeste, os clientes são classificados por ramo de atividade em cinco segmentos: MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER; EPI e LICITACAO; ATACADO; e CONS. FINAL.

Para cada segmento, consideramos clientes ativos aqueles que compraram com qualquer vendedor da empresa nos últimos 120 dias, para os três primeiros segmentos, e para o segmento Corporativo/Consumidor também relativo a 120 dias. Já para Norte e Nordeste, o período de referência para considerar ativo o cliente é de 150 dias para os três primeiros segmentos e para o Corporativo/Consumidor, também de 150 dias.

Entre os ativos, a frequência de atendimento depende da curva e do faturamento médio anual: por exemplo, no Sul, Sudeste e Centro-Oeste, clientes dos segmentos MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER que compraram nos últimos 120 dias e faturam em média mais de R$ 25.000 por ano são atendidos a cada 14 dias; os que faturam acima de R$ 10.000 têm visitação a cada 21 dias; e o restante, que comprou nos últimos 120 dias mas não se enquadra nesses valores de faturamento, a cada 28 dias. Nas regiões Norte e Nordeste, a referência é a compra nos últimos 150 dias e as mesmas faixas de faturamento e frequência: acima de R$ 25.000 a cada 14 dias, acima de R$ 10.000 a cada 21 dias, e os demais a cada 28 dias.

Clientes pré-inativos são aqueles que compraram pela última vez em um período mais longo: no Sul, Sudeste e Centro-Oeste, clientes do segmento MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER que compraram nos últimos 150 dias, e no Norte e Nordeste, nos últimos 180 dias, são considerados pré-inativos. Para eles, a frequência é de 14 dias, independentemente da curva, mas semelhante à regra dos ativos para faturamento: no Sul, Sudeste e Centro-Oeste, os que faturam mais de R$ 25.000 ou mais de R$ 10.000 são atendidos a cada 14 dias; no Norte e Nordeste, a mesma regra de 14 dias para todos os pré-inativos desses segmentos em qualquer faixa de faturamento. Na curva C pré-inativos, que só considera compra nos últimos 150 ou 180 dias conforme a região, a frequência é igualmente 14 dias.

Para os clientes inativos nesses segmentos, que não compraram dentro desses períodos, a frequência é de 14 dias tanto para Sul, Sudeste e Centro-Oeste quanto para Norte e Nordeste, com diferenciação de valores de faturamento, mas sempre a frequência igual para todas as curvas (A, B ou C). Clientes do segmento MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER que faturam mais de R$ 25.000 e estão inativos recebem visitação a cada 14 dias; os que faturam acima de R$ 10.000 também a cada 14 dias; e demais clientes do segmento a cada 14 dias.

No segmento EPI e LICITACAO, a lógica é parecida, mudando apenas o acúmulo de dias para considerar ativo, pré-inativo ou inativo. No Sul, Sudeste e Centro-Oeste, são 120 dias para ativos e 150 dias para pré-inativos, com a mesma classificação de frequência conforme curva e faturamento: ativos com faturamento acima de R$ 25.000 são atendidos a cada 14 dias, acima de R$ 10.000 a cada 21 dias, e outros a cada 28 dias. Pré-inativos nesses valores todos são atendidos a cada 14 dias. Inativos recebem visitação a cada 14 dias, independente da curva e no mesmo critério de faturamento citado para pré-inativos. No Norte e Nordeste, esses prazos são maiores: 150 dias para ativos, 180 dias para pré-inativos, mantendo frequência idêntica à mencionada para Sul, Sudeste e Centro-Oeste.

Para o segmento ATACADO, que são clientes atacadistas e distribuidores, a regionalização também influencia os prazos. No Sul, Sudeste e Centro-Oeste, clientes ativos compraram nos últimos 120 dias, no Norte e Nordeste nos últimos 150 dias. Para os ativos dessas regiões, os que faturam em média mais de R$ 50.000 por ano recebem visitação a cada 10 dias; os que faturam acima de R$ 25.000, a cada 14 dias; e os que compraram dentro do prazo mas não atingem esses valores, a cada 21 dias. Os pré-inativos no Sul, Sudeste e Centro-Oeste, que compraram pela última vez nos últimos 150 dias, recebem atendimentos com frequência variável segundo faturamento: acima de R$ 50.000 a cada 7 dias, acima de R$ 25.000 a cada 10 dias, e demais a cada 14 dias. No Norte e Nordeste, o prazo para pré-inativos é 180 dias, com a mesma frequência de atendimento para os mesmos níveis de faturamento. Para inativos o atendimento é a cada 10 dias para faturamento acima de R$ 50.000 e acima de R$ 25.000, e a cada 21 dias para os demais, tanto Norte e Nordeste quanto Sul, Sudeste e Centro-Oeste.

No segmento Corporativo/Consumidor, o critério de tempo para considerar ativos é 120 dias de compra na Sul, Sudeste e Centro-Oeste e 150 dias no Norte e Nordeste; para pré-inativos são 150 dias no Sul, Sudeste e Centro-Oeste e 180 dias no Norte e Nordeste. A frequência padrão para os que compraram dentro de 120 ou 150 dias é sempre 28 dias, independentemente da curva e do faturamento, desde que o faturamento anual médio seja superior a R$ 15.000 ou R$ 10.000, com os demais acionados no mesmo ritmo. Clientes pré-inativos desse segmento são atendidos a cada 14 dias, independentemente da curva e do faturamento, dentro dos prazos descritos. Inativos do segmento têm seu atendimento feito a cada 28 dias, independentemente da curva, para quem tem faturamento maior que R$ 15.000 ou 10.000, e os demais também obedecem essa frequência.

Quem não se encaixar em nenhuma dessas regras padrão, mesmo vindo do time de televendas, não deve ser agendado para atendimento.

Em resumo, todo o atendimento é feito pelos vendedores do televendas para seus clientes fixos, que são separados em duas carteiras regionais: uma para os estados do Sul, Sudeste e Centro-Oeste, e outra para o Norte e Nordeste. A prioridade é não agendar clientes baixados na Receita Federal. Prospect são atendidos a cada 14 dias em qualquer região. Clientes ativos, pré-inativos e inativos têm frequência de atendimento que varia conforme o ramo de atividade, a curva e o faturamento médio anual com a empresa. Os prazos considerados para definição de atividade variam pela região, sendo maiores no Norte e Nordeste, com prazos maiores para ativação e pré-inativação. Clientes que não se encaixam em nenhuma regra padrão não devem ser agendados.
