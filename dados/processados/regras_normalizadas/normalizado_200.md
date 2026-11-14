---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_200.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9351
tokens_saida: 441
custo_usd: 0.011556
tempo_segundos: 5.97
timestamp: 2026-11-14T20:00:40-03:00
---

## explicacao_normalizada
Os vendedores do televendas atendem seus clientes, com exceção do vendedor de código 1. Quando um cliente se encaixar em mais de uma situação, seguimos a primeira delas nesta ordem.

Os clientes que nunca compraram com a empresa são atendidos a cada 21 dias. Os que fizeram uma única compra com a empresa são atendidos a cada 10 dias. Para quem comprou com qualquer vendedor da empresa nos últimos 30 dias, usamos o intervalo do histórico de compras acrescido de 5 dias, limitado a no máximo 30 dias.

Depois, atendemos a cada 14 dias os clientes que compraram com o próprio vendedor nos últimos 30 dias. Quem comprou com qualquer vendedor da empresa entre 31 e 60 dias atrás é atendido a cada 7 dias, assim como quem comprou entre 61 e 90 dias atrás. Todos os demais clientes são atendidos a cada 21 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limite máximo para frequência do histórico
