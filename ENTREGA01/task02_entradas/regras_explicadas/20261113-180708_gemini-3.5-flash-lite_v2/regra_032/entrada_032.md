---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gemini-3.5-flash-lite
fornecedor: gemini
temperatura: 0.3
tokens_entrada: 9380
tokens_saida: 1633
custo_usd: 0.006896
tempo_segundos: 4.81
timestamp: 2026-11-13T18:11:33-03:00
---

Para a nossa equipe de televendas, a gente divide a operação considerando os clientes fixos de cada vendedor habilitado no sistema, separados por região. Nos estados de PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF, a gente atende a carteira dos estados do sul, sudeste e centro-oeste. Já nos estados de AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE, a gente atende a carteira norte e nordeste. 

Primeiro de tudo, a gente olha a situação cadastral de qualquer cliente do televendas: quem estiver com o status na receita federal definido como baixada a gente não agenda de jeito nenhum. Em seguida, para os novos clientes, todo prospect da carteira sul, sudeste e centro-oeste e da carteira norte e nordeste tem atendimento agendado a cada 14 dias.

Para a base das regiões do Sul, Sudeste e Centro-Oeste, a gente separa os clientes por ramo de atividade, considerando o faturamento médio anual com a empresa e a última compra feita com qualquer vendedor da empresa. Nos ramos MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, os ativos que compraram nos últimos 120 dias são visitados a cada 14 dias se faturam mais de R$ 25000, a cada 21 dias se faturam mais de R$ 10000, e a cada 28 dias os demais. Quem comprou nos últimos 150 dias entra como pré-inativo e é atendido a cada 14 dias, tanto para quem fatura mais de R$ 25000 quanto para quem fatura mais de R$ 10000 ou para os demais. Já os inativos desses mesmos ramos, que são os que não entram nas regras anteriores, recebem atendimento a cada 14 dias se a média faturada for maior que R$ 25000, maior que R$ 10000 ou para os demais. 

Ainda no Sul, Sudeste e Centro-Oeste, para os ramos EPI e LICITACAO, a lógica é idêntica: os ativos com compra nos últimos 120 dias são atendidos a cada 14 dias para faturamento acima de R$ 25000, a cada 21 dias acima de R$ 10000, e a cada 28 dias os demais; os pré-inativos com compra nos últimos 150 dias vão a cada 14 dias em qualquer faixa de faturamento; e os inativos também vão a cada 14 dias para faturamento acima de R$ 25000, acima de R$ 10000 ou para o restante.

Para o segmento ATACADO no Sul, Sudeste e Centro-Oeste, os ativos com compra nos últimos 120 dias têm frequência de 10 dias se faturam mais de R$ 50000, de 14 dias se faturam mais de R$ 25000, e de 21 dias para os demais. Nos pré-inativos com compra nos últimos 150 dias, a frequência é de 7 dias para faturamento acima de R$ 50000, de 10 dias acima de R$ 25000, e de 14 dias para os demais. Nos inativos do ATACADO, a frequência é de 10 dias para quem fatura mais de R$ 50000, de 10 dias para quem fatura mais de R$ 25000, e de 21 dias para os demais.

Para o segmento CONS. FINAL no Sul, Sudeste e Centro-Oeste, os ativos com compra nos últimos 120 dias e os inativos são atendidos a cada 28 dias, independentemente de faturarem mais de R$ 15000, mais de R$ 10000 ou nos demais casos. Já os pré-inativos com compra nos últimos 150 dias do mesmo segmento CONS. FINAL são atendidos a cada 14 dias, tanto para faturamento acima de R$ 15000 quanto acima de R$ 10000 ou para os demais.

Passando para as regiões Norte e Nordeste, os prazos de compra mudam um pouco para dar mais fôlego. Nos ramos MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, os ativos são os que compraram nos últimos 150 dias e os pré-inativos são os que compraram nos últimos 180 dias. Nesses grupos e nos inativos, a frequência é de 14 dias para quem fatura mais de R$ 25000, de 21 dias para quem fatura mais de R$ 10000 nos ativos, e de 14 dias nos pré-inativos e inativos acima de R$ 10000, sendo os demais atendidos a cada 28 dias nos ativos e a cada 14 dias nos pré-inativos e inativos. 

Para os ramos EPI e LICITACAO no Norte e Nordeste, seguimos a mesma régua dos materiais de construção: ativos com compra nos últimos 150 dias e pré-inativos com compra nos últimos 180 dias, com atendimento a cada 14 dias para faturamento acima de R$ 25000, a cada 21 dias para faturamento acima de R$ 10000 nos ativos e 14 nos pré-inativos, e os demais a cada 28 dias nos ativos e a cada 14 dias nos pré-inativos; para os inativos, a frequência é de 14 dias para qualquer faixa de faturamento.

Para o ATACADO no Norte e Nordeste, os ativos são os que compraram nos últimos 150 dias e os pré-inativos os que compraram nos últimos 180 dias. Os ativos com faturamento maior que R$ 50000 vão a cada 10 dias, maior que R$ 25000 a cada 14 dias, e os demais a cada 21 dias. Nos pré-inativos, a frequência é de 7 dias para faturamento acima de R$ 50000, de 10 dias acima de R$ 25000, e de 14 dias para os demais. Nos inativos do ATACADO, a frequência é de 10 dias para faturamento acima de R$ 50000, de 10 dias para faturamento acima de R$ 25000, e de 21 dias para os demais.

Por fim, no segmento CONS. FINAL no Norte e Nordeste, os ativos com compra nos últimos 150 dias e os inativos são atendidos a cada 28 dias, seja para faturamento maior que R$ 15000, maior que R$ 10000 ou para os demais. Os pré-inativos, que são os com compra nos últimos 180 dias, são atendidos a cada 14 dias em qualquer dessas faixas de faturamento. Todo o resto de cliente do televendas que não se encaixou em nenhuma dessas situações padrão não deve ser agendado.
