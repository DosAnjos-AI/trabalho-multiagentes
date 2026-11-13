---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-5.4-mini
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 8542
tokens_saida: 1472
custo_usd: 0.013031
tempo_segundos: 9.74
timestamp: 2026-11-13T18:15:25-03:00
---

Nós atendemos os vendedores do televendas que estão ativados, e os clientes fixos de cada vendedor entram conforme a região do estado. Ficam na carteira sul_sudeste_centrooeste os clientes de PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF. Ficam na carteira norte_nordeste os clientes de AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE. Os clientes do televendas ainda têm um bloqueio geral: quem está com status na receita federal definido como baixada não deve ser agendado.

Para os clientes que ainda são prospect, a gente agenda a cada 14 dias, valendo para as duas carteiras. Depois, para as demais carteiras, a prioridade é sempre primeiro separar os que estão ativos, depois os pré-inativos e por fim os inativos; dentro de cada grupo, a curva muda pela média faturada no ano com a empresa. No sul, sudeste e centro-oeste, nos ramos MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, quem teve recencia de positivacao global em 120 dias vai a cada 14 dias se a média faturada no ano com a empresa for maior que R$ 25000, a cada 21 dias se for maior que R$ 10000, e a cada 28 dias no restante. Se a recencia de positivacao global for em 150 dias, o atendimento fica a cada 14 dias tanto para curva A, curva B quanto para curva C. Se o cliente desse grupo não estiver em recencia de positivacao, então os inativos vão a cada 14 dias, com corte de curva A acima de R$ 25000, curva B acima de R$ 10000 e curva C sem outro filtro.

Ainda no sul, sudeste e centro-oeste, para EPI e LICITACAO a lógica é a mesma de separar ativos, pré-inativos e inativos, mas com frequências diferentes. Nos ativos, com recencia de positivacao global em 120 dias, a curva A atende a cada 14 dias acima de R$ 25000, a curva B a cada 21 dias acima de R$ 10000, e a curva C a cada 28 dias. Nos pré-inativos, com recencia de positivacao global em 150 dias, curva A, B e C ficam todas a cada 14 dias, com os mesmos cortes de faturamento para A e B. Nos inativos, curva A e curva B ficam a cada 14 dias acima de R$ 25000 e acima de R$ 10000, e curva C também fica a cada 14 dias.

Para ATACADO no sul, sudeste e centro-oeste, os ativos com recencia de positivacao global em 120 dias ficam a cada 10 dias se a média faturada no ano com a empresa for maior que R$ 50000, a cada 14 dias acima de R$ 25000, e a cada 21 dias no restante. Os pré-inativos, com recencia de positivacao global em 150 dias, ficam a cada 7 dias acima de R$ 50000, a cada 10 dias acima de R$ 25000, e a cada 14 dias na curva C. Os inativos ficam a cada 10 dias acima de R$ 50000, a cada 10 dias acima de R$ 25000, e a cada 21 dias na curva C.

Para CONS. FINAL no sul, sudeste e centro-oeste, os ativos com recencia de positivacao global em 120 dias ficam a cada 28 dias, sendo curva A acima de R$ 15000, curva B acima de R$ 10000 e curva C sem outro corte. Os pré-inativos, com recencia de positivacao global em 150 dias, também ficam a cada 14 dias, com os mesmos cortes de A e B. Os inativos ficam a cada 28 dias, com curva A acima de R$ 15000, curva B acima de R$ 10000 e curva C no restante.

No norte e nordeste, a separação é parecida, mas com prazos mais longos nos grupos ativos e pré-inativos. Em MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, os ativos com recencia de positivacao global em 150 dias ficam a cada 14 dias se a média faturada no ano com a empresa for maior que R$ 25000, a cada 21 dias acima de R$ 10000, e a cada 28 dias no restante. Os pré-inativos, com recencia de positivacao global em 180 dias, ficam a cada 14 dias em todas as curvas, com os mesmos cortes de A e B. Os inativos ficam a cada 14 dias, com curva A acima de R$ 25000, curva B acima de R$ 10000 e curva C sem corte adicional.

Em EPI e LICITACAO no norte e nordeste, os ativos com recencia de positivacao global em 150 dias ficam a cada 14 dias acima de R$ 25000, a cada 21 dias acima de R$ 10000, e a cada 28 dias no restante. Os pré-inativos, com recencia de positivacao global em 180 dias, ficam a cada 14 dias nas três curvas, com os mesmos cortes de A e B. Os inativos ficam a cada 14 dias em A e B e também na curva C.

Em ATACADO no norte e nordeste, os ativos com recencia de positivacao global em 150 dias ficam a cada 10 dias acima de R$ 50000, a cada 14 dias acima de R$ 25000, e a cada 21 dias no restante. Os pré-inativos, com recencia de positivacao global em 180 dias, ficam a cada 7 dias acima de R$ 50000, a cada 10 dias acima de R$ 25000, e a cada 14 dias na curva C. Os inativos ficam a cada 10 dias acima de R$ 50000, a cada 10 dias acima de R$ 25000, e a cada 21 dias na curva C.

Para CONS. FINAL no norte e nordeste, os ativos com recencia de positivacao global em 150 dias ficam a cada 28 dias, com curva A acima de R$ 15000, curva B acima de R$ 10000 e curva C sem corte. Os pré-inativos, com recencia de positivacao global em 180 dias, ficam a cada 14 dias, com os mesmos cortes de A e B. Os inativos ficam a cada 28 dias, com curva A acima de R$ 15000, curva B acima de R$ 10000 e curva C no restante. E, se mesmo assim o cliente não entrar em nenhuma dessas situações, a gente não agenda.
