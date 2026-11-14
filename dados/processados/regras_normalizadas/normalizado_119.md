---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_119.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9269
tokens_saida: 297
custo_usd: 0.010754
tempo_segundos: 4.73
timestamp: 2026-11-14T19:51:17-03:00
---

## explicacao_normalizada
Os vendedores do televendas habilitados no sistema atendem os clientes conforme a situação de cada um. Considerando se o cliente está ativo ou inativo para o próprio vendedor, atendemos os ativos em dia com os pagamentos a cada 15 dias e os ativos inadimplentes a cada 30 dias. Os inativos em dia são atendidos a cada 7 dias; os inativos inadimplentes não devem ser agendados.

Depois desses casos, os demais clientes sem compras são atendidos a cada 15 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-03-financeiros.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
sem_chave: clientes sem compras
