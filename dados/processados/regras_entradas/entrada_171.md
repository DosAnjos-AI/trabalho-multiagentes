---
regra_id: 171
arquivo_regra: regra_171.gobr
hash_regra_sha256: d81b243d39826e8db937f53a80412a8137312e6faaac190c15808bea0bd280e6
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2797
tokens_saida: 471
custo_usd: 0.005152
tempo_segundos: 6.63
timestamp: 2026-11-13T19:46:16-03:00
---

Os vendedores do televendas cuidam dos seus clientes seguindo esta ordem de prioridade: primeiro, não agendamos clientes inadimplentes, bloqueados, filiais ou com situação baixada na Receita Federal.

Entre os demais, atendemos a cada 14 dias os clientes que nunca compraram com a empresa. Quem fez uma única compra com a empresa e está cadastrado há 30 dias é atendido a cada 10 dias.

Depois, para quem comprou com qualquer vendedor da empresa nos últimos 30 dias e tem intervalo histórico de compras menor que 14 dias, o atendimento é a cada 14 dias. Se esse intervalo histórico for menor que 30 dias, usamos o próprio intervalo histórico para o atendimento, respeitando o mínimo de 14 e o máximo de 28 dias.

Em seguida, atendemos a cada 14 dias quem fez a última compra com qualquer vendedor da empresa entre 21 e 60 dias atrás, e a cada 7 dias quem fez a última compra entre 61 e 90 dias atrás. Por fim, os clientes cuja última compra com qualquer vendedor da empresa estiver fora do intervalo de 90 a 180 dias são atendidos a cada 21 dias. Quem se encaixar em mais de uma dessas situações fica com o primeiro tratamento da sequência.
