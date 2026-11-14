---
regra_id: 190
arquivo_regra: regra_190.gobr
hash_regra_sha256: 806a45d3b2c76b11c45ff213f6ff4368cc8580d01a88c4f557d6e0d9c5445cef
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2879
tokens_saida: 675
custo_usd: 0.006254
tempo_segundos: 8.70
timestamp: 2026-11-13T19:45:31-03:00
---

O atendimento é feito pelos vendedores habilitados do Televendas. Seguimos esta ordem: se um cliente se encaixar em mais de uma situação, vale a primeira.

Atendemos a cada 21 dias quem nunca comprou da empresa. Depois, quem fez uma única compra com a empresa e está cadastrado há 30 dias é atendido a cada 10 dias. Para os clientes em dia com os pagamentos cuja última compra com o próprio vendedor foi entre 61 e 90 dias atrás, o atendimento é a cada 7 dias. Os demais clientes em dia com os pagamentos e inativos para a empresa são atendidos a cada 14 dias.

Para quem tem curva A considerando a empresa toda e teve venda no mês, seguimos o intervalo do histórico, limitado a 30 dias. Os demais de curva A são atendidos a cada 7 dias. Para quem tem curva B considerando a empresa toda e teve venda no mês, também seguimos o histórico, limitado a 30 dias; os demais de curva B são atendidos a cada 14 dias.

Entre os clientes que sobrarem, quem teve venda no mês é atendido conforme o histórico, limitado a 30 dias. Todo o resto é atendido a cada 21 dias.
