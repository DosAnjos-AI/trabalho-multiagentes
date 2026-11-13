---
regra_id: 208
arquivo_regra: regra_208.gobr
hash_regra_sha256: d587537a36cdb4fc528780862edb0f166eed3b064cfd4dc387d76c9554e597eb
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2670
tokens_saida: 319
custo_usd: 0.004265
tempo_segundos: 5.13
timestamp: 2026-11-13T19:46:34-03:00
---

Os vendedores de televendas habilitados no sistema seguem esta ordem de atendimento: primeiro, não agendamos clientes com situação baixada na Receita Federal, inadimplentes, bloqueados ou que sejam filiais.

Entre os demais, atendemos a cada 7 dias quem ainda não comprou com o próprio vendedor e, a cada 14 dias, quem fez uma única compra com ele. Depois, atendemos a cada 14 dias quem comprou com seu vendedor neste mês e tem frequência histórica de compra entre 90 e 120 dias; também a cada 14 dias quem comprou com esse vendedor nos últimos 30 dias. Quem comprou com ele nos últimos 89 dias é atendido a cada 7 dias e quem comprou nos últimos 120 dias, a cada 3 dias.

Quando o cliente se encaixar em mais de uma dessas situações, vale a primeira dessa sequência. Todos os demais não são agendados.
