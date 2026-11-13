---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: f9de548ddf01743b402eceb1dbf15bf969118a38f07bd83e87cb674bdfe69406
arquivo_prompt: prompt_v1.md
hash_prompt_sha256: 40b5974705636c81d4d57c25c412ca473605bb769027303c4200113603a52462
modelo: gemini-3.5-flash-lite
fornecedor: gemini
temperatura: 0.3
tokens_entrada: 1606
tokens_saida: 352
custo_usd: 0.001362
tempo_segundos: 1.94
timestamp: 2026-11-13T16:49:30-03:00
---

Para organizar os atendimentos do nosso pessoal do televendas, a gente divide os clientes de acordo com o histórico e o momento de cada um com a empresa, garantindo que todo mundo seja visitado no ritmo certo. Primeiro, olhamos para os novos cadastros e os clientes que estão começando a comprar com a gente. Para os clientes que ainda são prospectos e estão com o vendedor, a gente agenda visitas a cada 28 dias sob o perfil "Ative este novo cliente!". Logo depois, para aqueles que já fizeram a primeira compra com o vendedor, a situação muda para "Cliente ativado!", e a gente passa a atender a cada 21 dias.

Depois, cuidamos dos clientes que já compram com regularidade, separando eles pelo volume. Para os clientes da curva C que compraram nos últimos 90 dias, a gente roda o atendimento "Compra com regularidade! (Curva C!)" a cada 7 dias. Já para os demais clientes que também compraram nos últimos 90 dias, ou seja, as curvas A e B, o atendimento chamado "Compra com regularidade! (Curva A e B)" acontece a cada 14 dias.

Para quem está dando uma sumida, o tratamento é outro. Se o cliente está caminhando para a inatividade, com o último pedido feito entre 91 e 180 dias atrás, a gente programa a situação "Cliente caminhando para inatividade!" a cada 28 dias. Por fim, para todo o resto dos clientes que já são considerados inativos e que a gente precisa trazer de volta, entra a regra "Resgatar cliente inativo!" com uma frequência de 45 dias.
