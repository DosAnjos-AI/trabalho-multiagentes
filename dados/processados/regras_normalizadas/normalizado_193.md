---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_193.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9441
tokens_saida: 665
custo_usd: 0.012766
tempo_segundos: 8.73
timestamp: 2026-11-14T19:59:53-03:00
---

## explicacao_normalizada
Trabalhamos com os vendedores de televendas habilitados no sistema e os clientes fixos de cada um. Separamos esses clientes em dois grupos pelo ramo de atividade: no primeiro ficam os de códigos 30, 583, 33, 26, 42, 34, 7, 21, 2, 29, 43, 4, 40, 52, 20, 584, 110, 124, 39, 120, 75, 57, 240, 366, 470, 237, 58, 69, 242, 46, 298 e 56; no segundo ficam os de ramos diferentes desses. Um cliente não fica nos dois grupos.

Antes de definir a frequência, não agendamos clientes que sejam filiais, que estejam com situação baixada na Receita Federal ou que tenham data de rota futura do vendedor nos próximos 21 dias e tenham comprado com qualquer vendedor da empresa nos últimos 60 dias.

Entre os que sobrarem, atendemos a cada 14 dias os clientes do primeiro grupo que compraram com qualquer vendedor da empresa nos últimos 60 dias. Para os do segundo grupo que também compraram com qualquer vendedor da empresa nesse período, o atendimento é a cada 21 dias. Todos os demais clientes são atendidos a cada 7 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/06-06-classificacao-por-id.md
03-secoes/04-01-carteiras-e-segmentacoes.md#Exclusiva x livre
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-11-outros-filtros.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-03-frequencia.md#Fixa por período
