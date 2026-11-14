---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_143.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9382
tokens_saida: 795
custo_usd: 0.013357
tempo_segundos: 10.22
timestamp: 2026-11-14T19:53:36-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados no sistema cuidam dos clientes atendidos pela equipe. Seguimos esta ordem: primeiro, não agendamos clientes que sejam filiais nem clientes que tenham comprado com qualquer vendedor da empresa nos últimos 30 dias.

Entre os que restarem, atendemos a cada 28 dias os que nunca compraram com a empresa. Para os clientes ativos na empresa cuja última compra com qualquer vendedor esteja fora do intervalo entre 30 e 45 dias atrás, atendemos a cada 7 dias os de curva A e a cada 14 dias os de curva B, considerando a curva na empresa toda. Os demais clientes ativos cuja última compra esteja fora desse mesmo intervalo são atendidos a cada 21 dias.

Depois, entre os que ainda não receberam atendimento, os clientes ativos cuja última compra com qualquer vendedor da empresa esteja fora do intervalo entre 45 e 60 dias atrás são atendidos a cada 14 dias. Os demais clientes ativos são atendidos a cada 7 dias e, por fim, todo o resto também é atendido a cada 7 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-07-curva-abc-ciclo-de-vida.md
