---
regra_id: 199
arquivo_regra: regra_199.gobr
hash_regra_sha256: fbcaa3d9366f80a3ab156360734d515569aaac0797a852559b0d9e140dbd4017
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2654
tokens_saida: 424
custo_usd: 0.004774
tempo_segundos: 10.25
timestamp: 2026-11-13T19:43:01-03:00
---

Os vendedores do televendas atendem seus clientes seguindo esta ordem de prioridade: primeiro, não agendamos os inadimplentes nem os bloqueados. Para os demais, quando um cliente se encaixar em mais de uma situação, vale a primeira.

Clientes que nunca compraram com a empresa são atendidos a cada 30 dias. Também atendemos a cada 30 dias quem fez uma única compra com a empresa e comprou com seu próprio vendedor nos últimos 40 dias.

Depois vêm os clientes ativos para o próprio vendedor cuja frequência histórica de compra é menor que 21 dias: esses são atendidos a cada 90 dias. Em seguida, quem comprou com qualquer vendedor da empresa entre 31 e 59 dias atrás é atendido a cada 30 dias; quem comprou entre 60 e 89 dias atrás, a cada 21 dias; e quem não comprou com nenhum vendedor da empresa nos últimos 90 dias, a cada 45 dias.
