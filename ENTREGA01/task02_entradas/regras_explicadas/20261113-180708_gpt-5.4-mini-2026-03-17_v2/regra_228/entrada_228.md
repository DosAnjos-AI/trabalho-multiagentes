---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: f9de548ddf01743b402eceb1dbf15bf969118a38f07bd83e87cb674bdfe69406
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-5.4-mini-2026-03-17
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 2508
tokens_saida: 263
custo_usd: 0.003064
tempo_segundos: 2.49
timestamp: 2026-11-13T18:10:40-03:00
---

No televendas, atendemos todos os vendedores do time que estão ativados, e cada um cuida dos seus próprios clientes. Primeiro pegamos os clientes que ainda estão no ciclo de vida prospect com o vendedor e fazemos um atendimento a cada 28 dias, para “Ative este novo cliente!”. Depois vêm os clientes que já fizeram uma única compra com o vendedor, com atendimento a cada 21 dias, para “Cliente ativado!”.

Na sequência, quem comprou recentemente entra em faixas diferentes. Os clientes com recencia de positivacao em 90 dias e curva c com a empresa ficam com atendimento a cada 7 dias, no grupo “Compra com regularidade! (Curva C)”. Os demais clientes com recencia de positivacao em 90 dias, sem essa distinção de curva, ficam com atendimento a cada 14 dias, no grupo “Compra com regularidade! (Curva A e B)”. Depois disso, os clientes com recencia de positivacao entre 91 dias e 180 dias entram em “Cliente caminhando para inatividade!” e passam a ser atendidos a cada 28 dias. E, por fim, para “Resgatar cliente inativo!”, o restante dos clientes do televendas fica com atendimento a cada 45 dias.
