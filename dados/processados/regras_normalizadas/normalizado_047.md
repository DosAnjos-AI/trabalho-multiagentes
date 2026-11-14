---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_047.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9299
tokens_saida: 349
custo_usd: 0.011044
tempo_segundos: 5.43
timestamp: 2026-11-14T19:46:35-03:00
---

## explicacao_normalizada
Todos os vendedores habilitados no sistema atendem seus próprios clientes fixos. Se um cliente se encaixar em mais de uma situação, vale a primeira na ordem abaixo.

Primeiro, não agendamos pessoas físicas. Depois, atendemos a cada 7 dias os clientes ativos para o vendedor e adimplentes. Os ativos para o vendedor e inadimplentes são atendidos a cada 14 dias, assim como os inativos para o vendedor e adimplentes. Não agendamos os inativos para o vendedor que estejam inadimplentes. Por fim, atendemos a cada 14 dias os clientes sem vendas que não tenham sido enquadrados nas situações anteriores.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-05-localizacao-classificacao.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-03-financeiros.md
sem_chave: clientes sem vendas
