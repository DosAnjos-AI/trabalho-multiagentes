---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_214.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9412
tokens_saida: 584
custo_usd: 0.012332
tempo_segundos: 7.98
timestamp: 2026-11-14T20:02:24-03:00
---

## explicacao_normalizada
Os vendedores do televendas atendem seus clientes, com preferência pelos dias úteis e pelo sábado. Primeiro, não agendamos clientes inadimplentes. Para os demais, seguimos a ordem abaixo: quem se encaixar em mais de uma situação recebe o tratamento da primeira.

Quem fez uma única compra com seu próprio vendedor é atendido a cada 14 dias. Depois, para quem fez uma única compra com esse vendedor e comprou com qualquer vendedor da empresa nos últimos 30 dias, prevemos atendimento a cada 21 dias se o ramo de atividade for 29 e a cada 14 dias se for diferente de 29.

Para os clientes ativos com seu vendedor e com intervalo histórico de compras menor que 14 dias, o atendimento é a cada 10 dias. Para quem comprou com seu vendedor entre 21 e 59 dias atrás, é a cada 30 dias no ramo 29 e a cada 14 dias nos demais ramos. Para quem comprou com seu vendedor entre 60 e 89 dias atrás, é a cada 14 dias, tanto no ramo 29 quanto nos demais. Por fim, para quem não comprou com seu vendedor nos últimos 90 dias, o atendimento é a cada 10 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/06-03-financeiros.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-06-classificacao-por-id.md
03-secoes/06-08-frequencia-e-parametros.md
