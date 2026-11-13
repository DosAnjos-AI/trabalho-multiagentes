---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gemini-2.5-flash-image
fornecedor: gemini
temperatura: 0.3
tokens_entrada: 9380
tokens_saida: 2402
custo_usd: 0.008819
tempo_segundos: 10.16
timestamp: 2026-11-13T18:15:47-03:00
---

A política de atendimento para o nosso time de televendas funciona assim: primeiro, a gente separa os clientes que estão com o status "baixada" na Receita Federal, e esses a gente não agenda de jeito nenhum.

Depois, a gente divide os clientes fixos do televendas em dois grandes grupos por região. O primeiro grupo é o "sul_sudeste_centrooeste", que inclui os estados PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF. O segundo grupo é o "norte_nordeste", com os estados AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE. Um cliente pode estar em apenas um desses grupos.

Para os clientes que são "prospects" com a empresa, independentemente da região, o atendimento é a cada 14 dias.

Agora, vamos para as regras específicas de cada região e segmento, sempre considerando a média faturada no ano com a empresa e a recência de positivação global, que é o tempo desde a última compra com qualquer vendedor da empresa.

Para os clientes da região "sul_sudeste_centrooeste":

Nos segmentos MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER:
* Se o cliente comprou nos últimos 120 dias e fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se comprou nos últimos 120 dias e fatura mais de R$ 10000, atendemos a cada 21 dias.
* Se comprou nos últimos 120 dias, atendemos a cada 28 dias.
* Se comprou nos últimos 150 dias e fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se comprou nos últimos 150 dias e fatura mais de R$ 10000, atendemos a cada 14 dias.
* Se comprou nos últimos 150 dias, atendemos a cada 14 dias.
* Se fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se fatura mais de R$ 10000, atendemos a cada 14 dias.
* Os demais clientes desse segmento são atendidos a cada 14 dias.

Nos segmentos EPI e LICITACAO:
* Se o cliente comprou nos últimos 120 dias e fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se comprou nos últimos 120 dias e fatura mais de R$ 10000, atendemos a cada 21 dias.
* Se comprou nos últimos 120 dias, atendemos a cada 28 dias.
* Se comprou nos últimos 150 dias e fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se comprou nos últimos 150 dias e fatura mais de R$ 10000, atendemos a cada 14 dias.
* Se comprou nos últimos 150 dias, atendemos a cada 14 dias.
* Se fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se fatura mais de R$ 10000, atendemos a cada 14 dias.
* Os demais clientes desse segmento são atendidos a cada 14 dias.

Nos segmentos ATACADO:
* Se o cliente comprou nos últimos 120 dias e fatura mais de R$ 50000, atendemos a cada 10 dias.
* Se comprou nos últimos 120 dias e fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se comprou nos últimos 120 dias, atendemos a cada 21 dias.
* Se comprou nos últimos 150 dias e fatura mais de R$ 50000, atendemos a cada 7 dias.
* Se comprou nos últimos 150 dias e fatura mais de R$ 25000, atendemos a cada 10 dias.
* Se comprou nos últimos 150 dias, atendemos a cada 14 dias.
* Se fatura mais de R$ 50000, atendemos a cada 10 dias.
* Se fatura mais de R$ 25000, atendemos a cada 10 dias.
* Os demais clientes desse segmento são atendidos a cada 21 dias.

Nos segmentos CONS. FINAL:
* Se o cliente comprou nos últimos 120 dias e fatura mais de R$ 15000, atendemos a cada 28 dias.
* Se comprou nos últimos 120 dias e fatura mais de R$ 10000, atendemos a cada 28 dias.
* Se comprou nos últimos 120 dias, atendemos a cada 28 dias.
* Se comprou nos últimos 150 dias e fatura mais de R$ 15000, atendemos a cada 14 dias.
* Se comprou nos últimos 150 dias e fatura mais de R$ 10000, atendemos a cada 14 dias.
* Se comprou nos últimos 150 dias, atendemos a cada 14 dias.
* Se fatura mais de R$ 15000, atendemos a cada 28 dias.
* Se fatura mais de R$ 10000, atendemos a cada 28 dias.
* Os demais clientes desse segmento são atendidos a cada 28 dias.

Para os clientes da região "norte_nordeste":

Nos segmentos MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER:
* Se o cliente comprou nos últimos 150 dias e fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se comprou nos últimos 150 dias e fatura mais de R$ 10000, atendemos a cada 21 dias.
* Se comprou nos últimos 150 dias, atendemos a cada 28 dias.
* Se comprou nos últimos 180 dias e fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se comprou nos últimos 180 dias e fatura mais de R$ 10000, atendemos a cada 14 dias.
* Se comprou nos últimos 180 dias, atendemos a cada 14 dias.
* Se fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se fatura mais de R$ 10000, atendemos a cada 14 dias.
* Os demais clientes desse segmento são atendidos a cada 14 dias.

Nos segmentos EPI e LICITACAO:
* Se o cliente comprou nos últimos 150 dias e fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se comprou nos últimos 150 dias e fatura mais de R$ 10000, atendemos a cada 21 dias.
* Se comprou nos últimos 150 dias, atendemos a cada 28 dias.
* Se comprou nos últimos 180 dias e fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se comprou nos últimos 180 dias e fatura mais de R$ 10000, atendemos a cada 14 dias.
* Se comprou nos últimos 180 dias, atendemos a cada 14 dias.
* Se fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se fatura mais de R$ 10000, atendemos a cada 14 dias.
* Os demais clientes desse segmento são atendidos a cada 14 dias.

Nos segmentos ATACADO:
* Se o cliente comprou nos últimos 150 dias e fatura mais de R$ 50000, atendemos a cada 10 dias.
* Se comprou nos últimos 150 dias e fatura mais de R$ 25000, atendemos a cada 14 dias.
* Se comprou nos últimos 150 dias, atendemos a cada 21 dias.
* Se comprou nos últimos 180 dias e fatura mais de R$ 50000, atendemos a cada 7 dias.
* Se comprou nos últimos 180 dias e fatura mais de R$ 25000, atendemos a cada 10 dias.
* Se comprou nos últimos 180 dias, atendemos a cada 14 dias.
* Se fatura mais de R$ 50000, atendemos a cada 10 dias.
* Se fatura mais de R$ 25000, atendemos a cada 10 dias.
* Os demais clientes desse segmento são atendidos a cada 21 dias.

Nos segmentos CONS. FINAL:
* Se o cliente comprou nos últimos 150 dias e fatura mais de R$ 15000, atendemos a cada 28 dias.
* Se comprou nos últimos 150 dias e fatura mais de R$ 10000, atendemos a cada 28 dias.
* Se comprou nos últimos 150 dias, atendemos a cada 28 dias.
* Se comprou nos últimos 180 dias e fatura mais de R$ 15000, atendemos a cada 14 dias.
* Se comprou nos últimos 180 dias e fatura mais de R$ 10000, atendemos a cada 14 dias.
* Se comprou nos últimos 180 dias, atendemos a cada 14 dias.
* Se fatura mais de R$ 15000, atendemos a cada 28 dias.
* Se fatura mais de R$ 10000, atendemos a cada 28 dias.
* Os demais clientes desse segmento são atendidos a cada 28 dias.

Por fim, os clientes que não se encaixarem em nenhuma dessas regras não serão agendados pelo televendas.
