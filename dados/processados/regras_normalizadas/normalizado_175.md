---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_175.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9372
tokens_saida: 720
custo_usd: 0.012972
tempo_segundos: 9.32
timestamp: 2026-11-14T19:57:30-03:00
---

## explicacao_normalizada
Os vendedores habilitados do televendas cuidam dos seus clientes fixos. Para os clientes dos ramos de atividade 1, 2, 3, 4, 8, 18 e 23, seguimos a ordem abaixo: se um cliente se encaixar em mais de uma situação, vale a primeira.

Primeiro, não agendamos clientes que sejam filiais, que estejam inadimplentes ou que tenham comprado com seu próprio vendedor nos últimos 30 dias. Depois, atendemos a cada 14 dias os clientes ativos na empresa e, a cada 21 dias, os inativos na empresa.

Para quem ainda não tiver sido contemplado, atendemos a cada 21 dias os clientes que tiveram venda com a empresa no ano anterior e não tiveram venda no ano atual. Atendemos a cada 30 dias aqueles cuja última compra com o próprio vendedor ocorreu entre 2023-01-01 e 2023-12-31.

Todos os demais clientes dos vendedores do televendas não são agendados.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/06-06-classificacao-por-id.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-03-financeiros.md
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
