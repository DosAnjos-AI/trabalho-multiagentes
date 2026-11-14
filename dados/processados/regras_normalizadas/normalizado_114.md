---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_114.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9521
tokens_saida: 648
custo_usd: 0.012761
tempo_segundos: 8.41
timestamp: 2026-11-14T19:51:10-03:00
---

## explicacao_normalizada
Trabalhamos com os vendedores 39, 16, 40, 6 e 45 no interior. Na capital, entram todos os vendedores de campo, exceto 39, 16, 40, 6, 45 e 55. No televendas, consideramos todos os vendedores, exceto 4 e 54. Os vendedores 4, 54 e 55 têm atendimento separado. Em cada caso, seguimos a ordem abaixo: quem já recebeu um tratamento não passa para os seguintes.

Para o vendedor 4, atendemos todos os clientes a cada 15 dias, com preferência por dias úteis.

Para o vendedor 55, não agendamos clientes cuja última compra com qualquer vendedor da empresa tenha ocorrido entre 0 e 30 dias atrás. Todos os demais são atendidos a cada 14 dias.

Para o vendedor 54, primeiro não agendamos clientes cuja última compra com qualquer vendedor da empresa tenha ocorrido entre 0 e 30 dias atrás. Também não agendamos os clientes bloqueados. Todos os demais são atendidos a cada 14 dias.

No interior, não agendamos clientes que estejam inativos para o próprio vendedor e inadimplentes. Todos os demais são atendidos a cada 30 dias, com preferência por dias úteis.

Na capital, não agendamos clientes que estejam inativos para o próprio vendedor e inadimplentes. Os ativos para o próprio vendedor que estejam inadimplentes são atendidos a cada 30 dias. Todos os demais são atendidos a cada 14 dias. Nos dois casos, preferimos dias úteis.

No televendas, atendemos os clientes ativos para o próprio vendedor a cada 15 dias e todos os demais a cada 7 dias, com preferência por dias úteis.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-03-financeiros.md
