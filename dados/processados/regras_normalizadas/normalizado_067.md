---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_067.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9444
tokens_saida: 837
custo_usd: 0.013629
tempo_segundos: 10.72
timestamp: 2026-11-14T19:48:16-03:00
---

## explicacao_normalizada
No televendas, trabalhamos com todos os vendedores dessa equipe. Na capital, os vendedores são 2, 4, 5 e 6, e cada um cuida de seus clientes fixos. No interior, os vendedores são 11, 3, 12 e 21. Todos os atendimentos são preferencialmente em dias úteis.

Para o televendas, atendemos a cada 14 dias os clientes ativos para seu vendedor, a cada 30 dias os inativos para seu vendedor e a cada 7 dias os clientes sem venda.

Para os clientes fixos da capital, atendemos a cada 20 dias os ativos para seu vendedor, tanto adimplentes quanto inadimplentes. Os inativos para seu vendedor que estão adimplentes são atendidos a cada 30 dias; os inadimplentes não devem ser agendados. Os clientes sem venda são atendidos a cada 30 dias.

No interior, atendemos a cada 21 dias os clientes ativos para seu vendedor e também os inativos para seu vendedor que estão adimplentes. Os inativos para seu vendedor que estão inadimplentes são atendidos a cada 42 dias. Reforçamos que, para os clientes fixos da capital inativos para seu vendedor e inadimplentes, não se agenda atendimento. No interior, os clientes sem venda são atendidos a cada 14 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/06-05-localizacao-classificacao.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-01-atividade-inatividade.md
sem_chave: clientes sem venda
03-secoes/06-03-financeiros.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
