---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v1.md
hash_prompt_sha256: 40b5974705636c81d4d57c25c412ca473605bb769027303c4200113603a52462
modelo: gemini-3.5-flash-lite
fornecedor: gemini
temperatura: 0.3
tokens_entrada: 8350
tokens_saida: 1896
custo_usd: 0.007245
tempo_segundos: 5.37
timestamp: 2026-11-13T16:49:50-03:00
---

Para organizar os nossos atendimentos pelo televendas, primeiro separamos os que não devem ser agendados: qualquer cliente que esteja com o cadastro baixado na Receita Federal não recebe visitas ou contatos agendados. Além disso, temos uma regra geral para fechar a nossa rotina onde o que sobrar de cliente que não se enquadrou nas demais regras do televendas simplesmente não deve ser agendado. 

Dividimos os nossos clientes atendidos pelo televendas em duas grandes regiões geográficas. Na região Sul, Sudeste e Centro-Oeste, que abrange os estados do Paraná, Santa Catarina, Rio Grande do Sul, São Paulo, Rio de Janeiro, Minas Gerais, Espírito Santo, Goiás, Mato Grosso, Mato Grosso do Sul e Distrito Federal, aplicamos regras específicas baseadas no ramo de atividade, no tempo desde a última compra, na média faturada no ano e na curva do cliente. Já na região Norte e Nordeste, que inclui Acre, Amapá, Amazonas, Pará, Rondônia, Roraima, Tocantins, Alagoas, Bahia, Ceará, Maranhão, Paraíba, Pernambuco, Piauí, Rio Grande do Norte e Sergipe, usamos a mesma lógica de segmentação por ramo, curva e faturamento, mas ajustamos os prazos de dias sem comprar devido à distância e logística. Os prospects, que são aqueles que estão no ciclo de vida de prospect com a empresa em qualquer uma dessas regiões, entram em uma frequência fixa de 14 dias.

Para os clientes da região Sul, Sudeste e Centro-Oeste dos ramos de Material de Construção, Ferragista, Agropecuária e Home Center, tratamos os ativos, que são os que compraram nos últimos 120 dias, com frequências de 14 dias para a Curva A com faturamento médio anual acima de R$ 25000, 21 dias para a Curva B acima de R$ 10000, e 28 dias para a Curva C. Os pré-inativos, que são os que estão sem comprar há 150 dias, são atendidos a cada 14 dias para todas as curvas, sendo a Curva A acima de R$ 25000, a Curva B acima de R$ 10000 e a Curva C os demais. Os inativos, que são os clientes sem limite recente de compra, também vão a cada 14 dias para todas as curvas, mantendo o corte de faturamento médio anual maior que R$ 25000 para a Curva A, maior que R$ 10000 para a Curva B e o restante na Curva C.

Ainda na região Sul, Sudeste e Centro-Oeste, para os ramos de EPI e Licitação, a lógica de dias é exatamente a mesma dos materiais de construção: ativos com compra nos últimos 120 dias têm frequência de 14 dias para a Curva A acima de R$ 25000, 21 dias para a Curva B acima de R$ 10000 e 28 dias para a Curva C. Os pré-inativos com 150 dias sem compra e os inativos sem restrição de tempo são agendados a cada 14 dias para todas as curvas, respeitando os mesmos patamares de faturamento médio anual de R$ 25000 para a Curva A e R$ 10000 para a Curva B.

Para o segmento de Atacado e Distribuidores na região Sul, Sudeste e Centro-Oeste, os ativos com 120 dias de prazo são atendidos a cada 10 dias na Curva A com faturamento médio anual acima de R$ 50000, a cada 14 dias na Curva B acima de R$ 25000, e a cada 21 dias na Curva C. Os pré-inativos, com 150 dias sem comprar, têm frequências mais apertadas: 7 dias para a Curva A acima de R$ 50000, 10 dias para a Curva B acima de R$ 25000, e 14 dias para a Curva C. Já os inativos desse mesmo atacado vão a cada 10 dias para a Curva A acima de R$ 50000, a cada 10 dias para a Curva B acima de R$ 25000, e a cada 21 dias para a Curva C.

Para o segmento Corporativo e Consumidor Final na região Sul, Sudeste e Centro-Oeste, os ativos com 120 dias e os inativos sem restrição de tempo seguem a mesma frequência de 28 dias para todas as curvas, com a Curva A exigindo faturamento médio anual acima de R$ 15000, a Curva B acima de R$ 10000, e a Curva C para o restante. Os pré-inativos desse grupo, que acumulam 150 dias sem compra, são visitados a cada 14 dias em todas as curvas, mantendo os mesmos cortes de faturamento de R$ 15000 para a Curva A e R$ 10000 para a Curva B.

Passando para as regiões Norte e Nordeste, os prazos de dias sem comprar aumentam um pouco para dar conta da operação. Para os segmentos de Material de Construção, Ferragista, Agropecuária e Home Center, os ativos são os que compraram nos últimos 150 dias, com frequência de 14 dias para a Curva A acima de R$ 25000, 21 dias para a Curva B acima de R$ 10000, e 28 dias para a Curva C. Os pré-inativos daqui são os que estão há 180 dias sem comprar, e vão a cada 14 dias para todas as curvas, assim como os inativos, que também ficam em 14 dias para todas as curvas, sempre divididos entre Curva A acima de R$ 25000, Curva B acima de R$ 10000 e Curva C para os demais.

Para os ramos de EPI e Licitação no Norte e Nordeste, seguimos o mesmo padrão dos materiais de construção locais: ativos com 150 dias a cada 14 dias para Curva A acima de R$ 25000, 21 dias para Curva B acima de R$ 10000 e 28 dias para Curva C. Os pré-inativos com 180 dias e os inativos de qualquer período são atendidos a cada 14 dias em todas as três curvas, respeitando os mesmos limites de faturamento de R$ 25000 e R$ 10000.

Para o Atacado e Distribuidores no Norte e Nordeste, os ativos com 150 dias sem compra são atendidos a cada 10 dias na Curva A acima de R$ 50000, a cada 14 dias na Curva B acima de R$ 25000, e a cada 21 dias na Curva C. Os pré-inativos, com 180 dias sem comprar, têm frequências de 7 dias para a Curva A acima de R$ 50000, 10 dias para a Curva B acima de R$ 25000, e 14 dias para a Curva C. Nos inativos do atacado nordestino e nortista, a frequência é de 10 dias para a Curva A acima de R$ 50000, 10 dias para a Curva B acima de R$ 25000, e 21 dias para a Curva C.

Finalmente, para o segmento Corporativo e Consumidor Final no Norte e Nordeste, os ativos com 150 dias e os inativos sem restrição de tempo são atendidos a cada 28 dias em todas as curvas, sendo a Curva A com faturamento médio anual acima de R$ 15000, a Curva B acima de R$ 10000, e a Curva C para os demais. Os pré-inativos desse grupo, que completam 180 dias sem comprar, têm o atendimento intensificado para a cada 14 dias em todas as curvas, mantendo os cortes financeiros de R$ 15000 para a Curva A e R$ 10000 para a Curva B.
