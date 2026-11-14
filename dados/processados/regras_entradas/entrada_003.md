---
regra_id: 003
arquivo_regra: regra_003.gobr
hash_regra_sha256: b8980d6c8dd09c46cb4c9862a10f043e708775621e03b10dc25a05b7e83d64e8
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2860
tokens_saida: 658
custo_usd: 0.006150
tempo_segundos: 9.98
timestamp: 2026-11-13T19:46:54-03:00
---

Os vendedores de televendas habilitados no sistema atendem os clientes seguindo esta ordem: quando um cliente se encaixar em mais de uma situação, vale a primeira.

Não agendamos filiais, clientes cuja última visita do representante tenha sido na semana anterior, clientes com rota programada para os próximos 7 dias nem clientes que compraram com qualquer vendedor da empresa nos últimos 7 dias.

Depois, atendemos a cada 14 dias os clientes que nunca compraram com a empresa e os que foram cadastrados há 60 dias e fizeram uma única compra com o vendedor responsável. Para os demais, considerando a última compra com qualquer vendedor da empresa, atendemos a cada 14 dias se ela ocorreu entre 7 e 30 dias atrás; a cada 7 dias se ocorreu entre 31 e 60 dias atrás; e a cada 3 dias se ocorreu entre 61 e 90 dias atrás.

Também atendemos a cada 14 dias quem comprou com qualquer vendedor da empresa nos últimos 14 dias e cuja última compra com qualquer vendedor da empresa não tenha ocorrido entre 15 e 90 dias atrás. Quem não comprou com nenhum vendedor da empresa nos últimos 90 dias também é atendido a cada 14 dias. Todo o resto é atendido a cada 21 dias.
