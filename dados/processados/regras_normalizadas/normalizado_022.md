---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_022.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9232
tokens_saida: 282
custo_usd: 0.010642
tempo_segundos: 4.77
timestamp: 2026-11-14T19:46:02-03:00
---

## explicacao_normalizada
Todos os vendedores de televendas atendem seus clientes a cada 14 dias, com preferência pelos dias úteis.

Para todos os vendedores de campo, consideramos os clientes fixos de cada vendedor. Primeiro, os clientes sem venda não devem ser agendados. Os demais são atendidos a cada 14 dias, com preferência pelos dias úteis.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/04-02-selecao-clientes-ruptura.md
sem_chave: clientes sem venda
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
