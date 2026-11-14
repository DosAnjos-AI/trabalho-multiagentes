---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_157.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9258
tokens_saida: 375
custo_usd: 0.011133
tempo_segundos: 5.29
timestamp: 2026-11-14T19:55:13-03:00
---

## explicacao_normalizada
Todos os vendedores habilitados no sistema atendem com preferência por dias úteis. Primeiro, para os clientes que estão há mais de 120 dias sem comprar, o atendimento deve ser a cada 14 dias. Depois, para os demais que estão há mais de 30 dias sem comprar, deve ser a cada 7 dias.

Para todos os outros clientes, usamos o intervalo do histórico de atendimento, respeitando o mínimo de 5 dias e o máximo de 30 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limites mínimo e máximo da frequência histórica
