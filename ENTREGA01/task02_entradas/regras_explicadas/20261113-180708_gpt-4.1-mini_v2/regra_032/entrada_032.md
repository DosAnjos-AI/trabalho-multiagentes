---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-4.1-mini
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 8543
tokens_saida: 1231
custo_usd: 0.005387
tempo_segundos: 13.13
timestamp: 2026-11-13T18:12:42-03:00
---

Os vendedores que fazem o atendimento são todos os ativados do televendas, e eles cuidam das carteiras fixas de clientes atribuídas a eles. A carteira dos clientes do televendas está dividida em duas grandes regiões: Sul, Sudeste e Centro-Oeste, que inclui os estados PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF; e Norte e Nordeste, que inclui AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE. Cada cliente do televendas pertence a uma dessas carteiras fixas conforme seu estado.

A gente não agenda visita para clientes que estejam com status baixado na Receita Federal, ou seja, que a Receita marcou como baixados. Eles são mantidos no cadastro, mas não são visitados nem agendados.

Para os clientes que ainda estão no ciclo de vida prospect com a empresa, ou seja, que ainda não compraram ou estão iniciando relacionamento, independentemente da região, eles são atendidos a cada 14 dias.

Para os clientes que pertencem às regiões Sul, Sudeste e Centro-Oeste, o atendimento varia conforme o ramo de atividade e algumas métricas de compra da empresa toda (não apenas com o vendedor do cliente). A gente separa os clientes nesses ramos: MATCON, FERRAGISTA, AGROPECUARIA, HOME CENTER; EPI, LICITACAO; ATACADO; e CONS. FINAL (corporativo/consumidor). Dentro de cada ramo, a frequência com que visitamos depende do ciclo de vida do cliente (ativo, pré-inativo ou inativo), da curva do cliente (A, B ou C, classificada pela média faturada anual em toda a empresa), e do tempo desde a última compra (recência de positivação) considerando toda a empresa.

Por exemplo, para os clientes ativos desses ramos na região Sul, que compraram com qualquer vendedor da empresa nos últimos 120 dias, a gente define a frequência como segue. Clientes curva A, que têm média faturada no último ano superior a R$ 25.000, são visitados a cada 14 dias; curva B (mais de R$ 10.000) é a cada 21 dias; curva C (qualquer faturamento, desde que tenha comprado nos últimos 120 dias) é a cada 28 dias. Para os clientes pré-inativos (última compra entre 121 e 150 dias atrás), o atendimento passa a ser mais frequente para os que têm maior faturamento (14 dias para curvas A, B e até para C). Para os inativos, que não compraram nos últimos 150 dias, a frequência fica em 14 dias para todas as curvas A e B; para curva C também 14 dias, exceto nos segmentos corporativo/consumidor onde fica 28 dias.

Detalhando os critérios mais específicos: a curva é definida pela média faturada no ano com a empresa toda, por exemplo, para o ramo MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, os clientes A faturam acima de R$ 25.000 por ano, os B faturam acima de R$ 10.000, e o resto é curva C; para o ramo ATACADO os limites são maiores: A é acima de R$ 50.000, B acima de R$ 25.000 e C o restante.

No segmento ATACADO da região Sul, os clientes ativos com curva A e compra nos últimos 120 dias são visitados a cada 10 dias, os curva B a cada 14 dias e os curva C a cada 21 dias. Entre os pré-inativos, o atendimento é mais intenso: curva A a cada 7 dias, curva B a cada 10 dias, e curva C a cada 14 dias. Os inativos têm frequências similares aos pré-inativos, mas um pouco mais espaçadas.

No segmento corporativo/consumidor da região Sul, as frequências para ativos são uniformes em 28 dias, não muito dependentes da curva; para pré-inativos são 14 dias para todos; para inativos também 28 dias, exceto para curva C que mantém 28 dias.

Para a região Norte e Nordeste, as regras são parecidas, só que o tempo considerado para recência de positivação é maior: 150 dias para clientes ativos e 180 dias para pré-inativos, contra 120 e 150 dias da região Sul, respectivamente. As frequências e os limites de faturamento são os mesmos, apenas ajustamos esse prazo maior para determinar o ciclo de vida e qual atendimento realizar.

Os ramos de atividade considerados e suas classificações são as mesmas para as duas regiões, com as mesmas faixas de média faturada anual para definição das curvas A, B e C.

Por fim, para todos os clientes do televendas que não forem enquadrados em nenhuma dessas regras que eu acabei de descrever, ou seja, que não são prospect, não estão em nenhum dos grupos por região, ramo, ciclo de vida e curva mencionados, a orientação é de não agendar atendimento, não agendamos visita para eles.

Resumindo, os clientes são divididos pela carteira fixa dos vendedores do televendas, que se separa em Norte/Nordeste e Sul/Sudeste/Centro-Oeste, cada segmento de ramo tem regras de frequência de atendimento que dependem do status de compra recente da empresa toda, média faturada no ano em toda a empresa, e ciclo de vida do cliente (ativo, pré-inativo e inativo) usando janelas de 120, 150, 180 dias para definir esses ciclos, com visitas que variam de 7 a 28 dias conforme esses critérios. Clientes prospect são atendidos a cada 14 dias, e clientes baixados na Receita não são visitados. O que sobrar não é agendado.
