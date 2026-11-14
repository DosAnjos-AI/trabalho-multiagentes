---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_158.md
id_prompt: prompt_normalizador_v1.md
hash_prompt: e1c5021908631c73fd33e2d6135a03bd6a33b9a58db7908bcab13d4c72dab3da
id_auxiliar_manual: regras_para_normalizador_v1.md
hash_auxiliar_manual: 26f9f0a6a7c4bf0e55c789b0168c199e25971b21c627d4f22abc749247f9e86f
versao_normalizador: v1
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 8048
tokens_saida: 889
custo_usd: 0.012493
tempo_segundos: 10.99
timestamp: 2026-11-14T12:01:45-03:00
---

## explicacao_normalizada
Os vendedores do televendas cuidam dos seus clientes. Primeiro, não agendamos os inadimplentes nem os que estão com situação baixada na Receita Federal. Para os demais, seguimos a ordem abaixo: se o cliente se encaixar em mais de uma situação, vale a primeira.

Quem nunca comprou com a empresa é atendido a cada 30 dias. Quem fez uma única compra com a empresa, comprou com qualquer vendedor nos últimos 45 dias e está cadastrado há 120 dias é atendido a cada 21 dias.

Depois, quem comprou com qualquer vendedor nos últimos 45 dias e tem intervalo histórico entre compras menor que 30 dias é atendido a cada 14 dias. Quem comprou com qualquer vendedor nos últimos 120 dias e tem intervalo histórico entre compras menor que 120 dias é atendido a cada 30 dias.

Para quem ainda não se encaixou nas situações anteriores, atendemos a cada 30 dias os que fizeram a última compra com qualquer vendedor da empresa entre 45 e 70 dias atrás, e a cada 21 dias os que fizeram essa compra entre 71 e 120 dias atrás. Quem não comprou com nenhum vendedor da empresa nos últimos 120 dias é atendido a cada 30 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-03-financeiros.md
03-secoes/06-05-localizacao-classificacao.md
03-secoes/04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Fluxo de uma regra
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-11-outros-filtros.md
03-secoes/06-08-frequencia-e-parametros.md
03-secoes/06-02-recencia-visita-positivacao.md
