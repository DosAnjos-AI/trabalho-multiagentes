---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_081.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9271
tokens_saida: 321
custo_usd: 0.010876
tempo_segundos: 4.91
timestamp: 2026-11-14T19:49:26-03:00
---

## explicacao_normalizada
Todos os vendedores cuidam dos seus clientes fixos. Para os clientes ativos em relação ao próprio vendedor, prevemos atendimento semanal; para os ativos que também estão inadimplentes, prevemos atendimento a cada 21 dias.

Para os clientes inativos em relação ao próprio vendedor, prevemos atendimento a cada 30 dias; se também estiverem inadimplentes, não devem ser agendados. Os clientes sem vendas devem ser atendidos a cada 30 dias. Para todos os atendimentos previstos, a preferência é por dias úteis.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-03-financeiros.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
sem_chave: clientes sem vendas
03-secoes/07-02-preferencia-dia-semana.md
