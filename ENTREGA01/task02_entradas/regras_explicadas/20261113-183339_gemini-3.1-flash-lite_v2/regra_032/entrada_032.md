---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gemini-3.1-flash-lite
fornecedor: gemini
temperatura: 0.3
tokens_entrada: 9380
tokens_saida: 791
custo_usd: 0.003531
tempo_segundos: 3.36
timestamp: 2026-11-13T18:36:15-03:00
---

Para a nossa equipe de televendas, a política de agendamento de visitas segue critérios específicos baseados na localização, no ramo de atividade, no histórico de compras e no faturamento médio anual do cliente.

Primeiro, temos uma regra prioritária: qualquer cliente que esteja com o status na Receita Federal definido como baixada não deve ser agendado, independentemente de qualquer outra condição.

Para os demais, separamos os clientes em dois grandes grupos geográficos. O grupo sul_sudeste_centrooeste abrange os estados PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF. O grupo norte_nordeste abrange AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE.

Para clientes que estão no ciclo de vida prospect com a empresa, a frequência de atendimento é de 14 dias.

Para os clientes ativos, pré-inativos e inativos, a frequência varia conforme o ramo de atividade e a curva de faturamento. Consideramos a recência de positivação global (com qualquer vendedor da empresa) e a média faturada no ano com a empresa.

Nos estados do sul, sudeste e centro-oeste, para os ramos MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, bem como para EPI e LICITACAO, os ativos (positivados nos últimos 120 dias) com faturamento acima de R$ 25000 são atendidos a cada 14 dias, acima de R$ 10000 a cada 21 dias, e os demais a cada 28 dias. Os pré-inativos (positivados nos últimos 150 dias) e os inativos desses mesmos ramos são atendidos a cada 14 dias, independentemente da curva de faturamento.

Para o ramo ATACADO no sul, sudeste e centro-oeste, os ativos (positivados nos últimos 120 dias) com faturamento acima de R$ 50000 são atendidos a cada 10 dias, acima de R$ 25000 a cada 14 dias, e os demais a cada 21 dias. Os pré-inativos (positivados nos últimos 150 dias) com faturamento acima de R$ 50000 são atendidos a cada 7 dias, acima de R$ 25000 a cada 10 dias, e os demais a cada 14 dias. Os inativos do ATACADO com faturamento acima de R$ 50000 ou acima de R$ 25000 são atendidos a cada 10 dias, e os demais a cada 21 dias.

Para o ramo CONS. FINAL no sul, sudeste e centro-oeste, os ativos (positivados nos últimos 120 dias) e inativos são atendidos a cada 28 dias, independentemente do faturamento. Os pré-inativos (positivados nos últimos 150 dias) são atendidos a cada 14 dias.

Nas regiões norte e nordeste, a lógica é a mesma, mas com prazos de recência maiores: os ativos são considerados com positivação nos últimos 150 dias e os pré-inativos nos últimos 180 dias. As frequências de atendimento para cada faixa de faturamento e ramo seguem os mesmos padrões descritos para as regiões sul, sudeste e centro-oeste.

Por fim, qualquer cliente da nossa equipe de televendas que não se enquadrar em nenhuma dessas regras específicas não deve ser agendado.
