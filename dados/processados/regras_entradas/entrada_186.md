---
regra_id: 186
arquivo_regra: regra_186.gobr
hash_regra_sha256: 30580e8c4285a3ddab77a5428cb2f559f9711350ce6de899ae534d6134c51324
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2856
tokens_saida: 570
custo_usd: 0.005706
tempo_segundos: 8.69
timestamp: 2026-11-13T19:45:22-03:00
---

Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade: quem se encaixar numa situação recebe aquele tratamento e não passa para as seguintes.

Primeiro, não agendamos clientes que compraram com o próprio vendedor nos últimos 7 dias nem os que têm rota prevista para os próximos 7 dias.

Depois, atendemos a cada 14 dias os clientes que nunca compraram com a empresa. Também atendemos nesse intervalo os que compraram com o próprio vendedor no ano passado e cuja última compra com ele foi entre 180 e 360 dias atrás. O mesmo intervalo vale para quem comprou com qualquer vendedor da empresa nos últimos 14 dias e também entre 181 e 360 dias atrás, mas não comprou com a empresa entre 15 e 180 dias atrás.

Atendemos a cada 7 dias os clientes cuja rota foi há 7 dias, que receberam visita da empresa na semana anterior e que compraram com qualquer vendedor da empresa entre 7 e 30 dias atrás ou entre 31 e 60 dias atrás. Também atendemos a cada 7 dias quem teve a última compra com qualquer vendedor da empresa entre 61 e 90 dias atrás ou entre 91 e 180 dias atrás.

Os demais clientes são atendidos a cada 28 dias.
