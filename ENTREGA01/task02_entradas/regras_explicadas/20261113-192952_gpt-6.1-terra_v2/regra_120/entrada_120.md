---
regra_id: 120
arquivo_regra: regra_120.gobr
hash_regra_sha256: 6b336dbe98c6838b7963d7f9fed49fe66d907712795f441c3b6e95bc0684468d
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3151
tokens_saida: 559
custo_usd: 0.005946
tempo_segundos: 7.45
timestamp: 2026-11-13T19:48:21-03:00
---

Os vendedores de televendas atendem seus próprios clientes fixos, com exceção do vendedor 12. No interior, trabalham os vendedores 2, 3 e 12; na capital, os vendedores 5, 17 e 18, cada um com seus clientes fixos. Para o vendedor 12, não agendamos atendimentos, mesmo ele fazendo parte da equipe do interior.

Para os demais atendimentos, seguimos a ordem abaixo quando um cliente se encaixa em mais de uma situação. Preferimos marcar em dias úteis.

No televendas, atendemos a cada 14 dias os clientes ativos para o próprio vendedor, a cada 30 dias os inativos para ele e, depois, a cada 7 dias os clientes sem venda.

Na capital, atendemos a cada 20 dias os clientes ativos para o próprio vendedor, tanto os adimplentes quanto os inadimplentes. Os inativos para o vendedor e adimplentes são atendidos a cada 30 dias; depois, os clientes sem venda também são atendidos a cada 30 dias. Para os inativos para o vendedor e inadimplentes, não agendamos atendimento.

No interior, atendemos a cada 21 dias os clientes ativos para o próprio vendedor e também os inativos para ele que estejam adimplentes. Os inativos para o vendedor e inadimplentes são atendidos a cada 42 dias; depois, os clientes sem venda são atendidos a cada 38 dias. Há também a orientação de não agendar os inativos para o vendedor e inadimplentes, mas ela vem depois da de 42 dias, que tem prioridade.
