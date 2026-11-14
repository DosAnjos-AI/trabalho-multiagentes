---
regra_id: 231
arquivo_regra: regra_231.gobr
hash_regra_sha256: 1454c013ecb2fde2f937d1fb7523471e4109616020eab171c4dfe524cd612ef2
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2617
tokens_saida: 391
custo_usd: 0.004572
tempo_segundos: 6.42
timestamp: 2026-11-13T19:40:33-03:00
---

Dividimos o atendimento entre os vendedores 200, 382, 677, 631, 686, 731 e 789 na regional; 706 e 763 na reativação; e 708, 736, 737 e 755 na direta.

Para todos esses vendedores, a primeira prioridade é não agendar clientes com situação baixada na Receita Federal.

Na regional, depois dessa verificação, não agendamos quem comprou com qualquer vendedor da empresa nos últimos 30 dias. Em seguida, atendemos a cada 7 dias quem comprou com qualquer vendedor da empresa entre 30 e 150 dias atrás.

Na reativação, depois da verificação na Receita, não agendamos quem comprou com qualquer vendedor da empresa nos últimos 150 dias. Em seguida, atendemos a cada 14 dias quem nunca comprou com a empresa e também quem está há mais de 149 dias sem comprar com qualquer vendedor da empresa.

Na direta, atendemos todos os demais clientes a cada 7 dias.
