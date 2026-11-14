---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_120.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9494
tokens_saida: 629
custo_usd: 0.012639
tempo_segundos: 8.19
timestamp: 2026-11-14T19:51:25-03:00
---

## explicacao_normalizada
Os vendedores de televendas atendem seus próprios clientes fixos, com exceção do vendedor 12. No interior, trabalham os vendedores 2, 3 e 12; na capital, os vendedores 5, 17 e 18, cada um com seus clientes fixos. Para o vendedor 12, não agendamos atendimentos, mesmo ele fazendo parte da equipe do interior.

Para os demais atendimentos, seguimos a ordem abaixo quando um cliente se encaixa em mais de uma situação. Preferimos marcar em dias úteis.

No televendas, atendemos a cada 14 dias os clientes ativos para o próprio vendedor, a cada 30 dias os inativos para ele e, depois, a cada 7 dias os clientes sem venda.

Na capital, atendemos a cada 20 dias os clientes ativos para o próprio vendedor, tanto os adimplentes quanto os inadimplentes. Os inativos para o vendedor e adimplentes são atendidos a cada 30 dias; depois, os clientes sem venda também são atendidos a cada 30 dias. Para os inativos para o vendedor e inadimplentes, não agendamos atendimento.

No interior, atendemos a cada 21 dias os clientes ativos para o próprio vendedor e também os inativos para ele que estejam adimplentes. Os inativos para o vendedor e inadimplentes são atendidos a cada 42 dias; depois, os clientes sem venda são atendidos a cada 38 dias. Há também a orientação de não agendar os inativos para o vendedor e inadimplentes, mas ela vem depois da de 42 dias, que tem prioridade.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-01-atividade-inatividade.md
sem_chave: clientes sem venda
03-secoes/06-03-financeiros.md
