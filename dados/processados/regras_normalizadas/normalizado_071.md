---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_071.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9693
tokens_saida: 815
custo_usd: 0.013768
tempo_segundos: 10.37
timestamp: 2026-11-14T19:48:39-03:00
---

## explicacao_normalizada
Na Palmed, temos os vendedores de televendas ligados ao supervisor 2736, os ligados ao supervisor 2731, os vendedores 435, 261, 385, 276, 438, 63 e 164, todos os vendedores de televendas e todos os vendedores de campo. Para os grupos dos supervisores e para os vendedores identificados pelos códigos, consideramos os clientes fixos de cada vendedor. Um vendedor e seus clientes podem aparecer tanto em um desses grupos quanto no grupo geral de televendas; a entrada em um grupo não impede a participação em outro.

Seguimos a ordem das situações abaixo quando um cliente se encaixar em mais de uma. Para os clientes fixos dos grupos dos supervisores 2736 e 2731, se o cliente estiver inativo para o próprio vendedor e inadimplente, atendemos a cada 14 dias, de preferência em dias úteis. Para os demais clientes fixos do grupo do supervisor 2736, seguimos o histórico de atendimento, sem ultrapassar 7 dias entre atendimentos, com preferência por dias úteis e sábado. Para os demais do grupo do supervisor 2731, fazemos o mesmo, mas com preferência por dias úteis. Em todos esses casos, evitamos que o atendimento coincida com a rota da equipe de campo.

Para os clientes fixos dos vendedores 435, 261, 385, 276, 438, 63 e 164, os que estiverem inativos para o próprio vendedor e inadimplentes são atendidos a cada 14 dias, de preferência em dias úteis. Para os demais, seguimos o histórico, sem ultrapassar 7 dias entre atendimentos, de preferência em dias úteis e sábado. Também evitamos coincidência com a rota da equipe de campo.

Para os clientes dos vendedores de televendas em geral, os ativos para o próprio vendedor e adimplentes são atendidos conforme o histórico, sem ultrapassar 7 dias entre atendimentos, de preferência em dias úteis. Os ativos para o próprio vendedor e inadimplentes são atendidos a cada 14 dias, também de preferência em dias úteis. Para os inativos para o próprio vendedor e adimplentes, seguimos o histórico, sem ultrapassar 7 dias, de preferência de segunda a sexta. Para os inativos para o próprio vendedor e inadimplentes, atendemos a cada 30 dias, de preferência de segunda a sexta. Todos os demais clientes do televendas são atendidos conforme o histórico, sem ultrapassar 7 dias, de preferência de segunda a sexta.

Para todos os clientes da equipe de campo, o atendimento é semanal.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/04-01-carteiras-e-segmentacoes.md#Exclusiva x livre
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-03-financeiros.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limite máximo da frequência do histórico
03-secoes/07-04-conflito-pivot-rota.md#Evitar choque entre televendas e campo
