---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_227.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9351
tokens_saida: 479
custo_usd: 0.011746
tempo_segundos: 6.76
timestamp: 2026-11-14T20:03:33-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem seus clientes, com exceção dos vendedores de códigos 518, 519, 521, 626, 503, 624 e 623. Para decidir o atendimento, seguimos a ordem abaixo: quando um cliente se encaixa em mais de uma situação, vale a primeira.

Primeiro, os clientes cuja data da rota foi há 7 dias devem ser atendidos a cada 1 dia, de forma fixa. Depois, não agendamos os clientes que compraram com qualquer vendedor da empresa nos últimos 30 dias. Para quem nunca comprou com a empresa, o atendimento é a cada 60 dias. Para quem comprou com qualquer vendedor da empresa entre 30 e 90 dias atrás, atendemos a cada 15 dias.

Todos os demais clientes são atendidos a cada 10 dias. Quem não for contemplado por essas situações não deve ser agendado.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-11-outros-filtros.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/07-04-conflito-pivot-rota.md#Roteirização e fixação
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-01-atividade-inatividade.md
