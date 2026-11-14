---
regra_id: 164
arquivo_regra: regra_164.gobr
hash_regra_sha256: e036078569b2d5a98776ce2f03c0da5a11d95fb084554c9e69458b9b625c292d
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3677
tokens_saida: 930
custo_usd: 0.008327
tempo_segundos: 11.84
timestamp: 2026-11-13T19:49:21-03:00
---

Trabalhamos com todos os vendedores habilitados no sistema e também com a vendedora de código 10bruna. Seguimos a ordem abaixo: quando um cliente se encaixa em mais de uma situação, fica com o primeiro atendimento previsto para ele.

Para a 10bruna, olhamos primeiro os clientes cujo rótulo contém condominio. Os cadastrados a partir de 03/10/2024 são atendidos a cada 14 dias. Depois, os que compraram com qualquer vendedor da empresa nos últimos 30 dias são atendidos a cada 7 dias. Os que não compraram com nenhum vendedor da empresa nos últimos 90 dias são atendidos a cada 30 dias.

Para todos os vendedores habilitados, começamos pelos clientes que ainda não compraram com o próprio vendedor e foram cadastrados a partir de 01/08/2024: atendimento a cada 7 dias, independentemente do rótulo.

Em seguida, para os clientes cujo rótulo contém construtora, atendemos a cada 14 dias os que fizeram uma única compra com a empresa e não compraram com o próprio vendedor nos últimos 60 dias. Para quem tem intervalo histórico entre compras com esse vendedor menor que 30 dias e não comprou com ele nos últimos 14 dias, atendemos em RJ a cada 7 dias se for curva A, a cada 10 dias se for curva B e a cada 14 dias se for curva C, considerando a curva na empresa toda. Os demais que cumprirem essas mesmas condições de intervalo e tempo sem compra com o vendedor são atendidos a cada 14 dias.

Ainda entre os clientes com construtora no rótulo, os ativos na empresa que não compraram com nenhum vendedor nos últimos 45 dias são atendidos a cada 10 dias. Depois, os que não compraram com o próprio vendedor nos últimos 60 dias são atendidos a cada 14 dias; os cadastrados a partir de 03/10/2024, a cada 7 dias; e os demais, a cada 45 dias.

Para os clientes cujo rótulo contém shopping, supermercado, industria, estaleiro, clube, escolas, universidade, igreja, hotel, hospital, clinica, restaurantes ou condominio, atendemos os cadastrados a partir de 03/10/2024 a cada 14 dias. Depois, os que compraram com qualquer vendedor da empresa nos últimos 30 dias são atendidos a cada 7 dias. Também está previsto atendimento a cada 30 dias para quem comprou com qualquer vendedor da empresa nos últimos 30 dias, mas essa mesma condição já é atendida antes, a cada 7 dias.

Os demais clientes dos vendedores habilitados não são agendados.
