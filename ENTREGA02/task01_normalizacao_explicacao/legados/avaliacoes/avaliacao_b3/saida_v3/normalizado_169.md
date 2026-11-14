---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_169.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9409
tokens_saida: 781
custo_usd: 0.013314
tempo_segundos: 10.28
timestamp: 2026-11-14T16:26:06-03:00
---

## explicacao_normalizada
Trabalhamos com o vendedor 341 e com duas equipes de televendas: uma formada pelos vendedores 203, 466, 314 e 291, e outra pelos vendedores 132, 232 e 145.

Para a primeira equipe, separamos os clientes em dia com os pagamentos que passam do vendedor 341 para ela por ruptura de compra em 7 dias, além dos prospects. Em outro grupo ficam os clientes fixos dessa equipe que estão em dia com os pagamentos e não tiveram venda em 7 dias. Quem já está no primeiro grupo não entra no segundo.

Para os clientes desses dois grupos, damos prioridade ao atendimento a cada 14 dias quando nunca compraram da empresa; quando compraram com qualquer vendedor da empresa nos últimos 30, 60 ou 90 dias; ou quando a última compra com qualquer vendedor da empresa foi entre 90 e 180 dias atrás.

Depois disso, para as duas equipes, não agendamos os clientes que compraram com qualquer vendedor da empresa nos últimos 7 dias nem os inadimplentes. Entre os que ainda não receberam um tratamento, não agendamos os clientes da primeira equipe; os demais clientes da segunda equipe atendemos a cada 14 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/06-03-financeiros.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-01-atividade-inatividade.md
03-secoes/04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
