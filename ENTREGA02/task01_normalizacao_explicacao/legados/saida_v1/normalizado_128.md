---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_128.md
id_prompt: prompt_normalizador_v1.md
hash_prompt: e1c5021908631c73fd33e2d6135a03bd6a33b9a58db7908bcab13d4c72dab3da
id_auxiliar_manual: regras_para_normalizador_v1.md
hash_auxiliar_manual: 26f9f0a6a7c4bf0e55c789b0168c199e25971b21c627d4f22abc749247f9e86f
versao_normalizador: v1
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 8123
tokens_saida: 970
custo_usd: 0.012973
tempo_segundos: 12.50
timestamp: 2026-11-14T12:01:25-03:00
---

## explicacao_normalizada

No televendas, o vendedor 291 atende os clientes fixos dos vendedores externos 283 e 279; o 292, os dos externos 286 e 284; o 294, os dos externos 275 e 277; o 375, os dos externos 278 e 280; o 900, os dos externos 273 e 274; e o 901, os dos externos 282 e 276. Um mesmo cliente pode aparecer em mais de um desses grupos.

Para todos esses vendedores de televendas, primeiro não agendamos clientes com situação baixada na Receita Federal. Depois, para cada grupo de clientes dos externos atendido pelo respectivo vendedor de televendas, seguimos esta ordem: quem nunca comprou com a empresa é atendido a cada 7 dias; quem comprou com qualquer vendedor da empresa nos últimos 60 dias é atendido a cada 5 dias, a partir do dia 16 de cada mês; quem comprou com qualquer vendedor da empresa nos últimos 90 dias é atendido a cada 7 dias; e os demais desse grupo também são atendidos a cada 7 dias.

Em seguida, para os clientes desses vendedores de televendas que ainda não tenham recebido um tratamento, atendemos a cada 7 dias quem nunca comprou com a empresa, depois quem comprou com qualquer vendedor da empresa nos últimos 60 dias e depois quem comprou com qualquer vendedor da empresa nos últimos 90 dias. Também atendemos a cada 7 dias os demais que não pertençam a nenhum dos seis grupos de clientes dos externos. Os clientes que sobrarem depois disso não são agendados.

## regras_extraidas

03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/04-01-carteiras-e-segmentacoes.md#Exclusiva x livre
03-secoes/04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa
03-secoes/06-05-localizacao-classificacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Fluxo de uma regra
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/05-01-filtros-temporais-calendario.md#Dia do mês
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Com restrição temporal
