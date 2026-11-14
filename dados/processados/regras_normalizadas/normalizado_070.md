---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_070.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9328
tokens_saida: 413
custo_usd: 0.011393
tempo_segundos: 6.53
timestamp: 2026-11-14T19:48:29-03:00
---

## explicacao_normalizada
Trabalhamos com todos os vendedores de televendas e todos os vendedores de campo. No televendas, cada vendedor cuida dos seus clientes fixos. Seguimos a ordem abaixo caso um cliente se encaixe em mais de uma situação.

No televendas, não agendamos os clientes que estão inativos para o vendedor e inadimplentes. Atendemos a cada 14 dias os clientes ativos para o vendedor e, a cada 30 dias, os inativos para o vendedor que estão em dia e os clientes sem venda. Preferimos fazer esses atendimentos em dias úteis.

Para os vendedores de campo, atendemos a cada 14 dias os clientes ativos para o vendedor e a cada 30 dias os inativos para o vendedor, com preferência por dias úteis. Não agendamos os clientes sem venda.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-03-financeiros.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/07-03-frequencia.md#Fixa por período
sem_chave: clientes sem venda
03-secoes/07-02-preferencia-dia-semana.md
