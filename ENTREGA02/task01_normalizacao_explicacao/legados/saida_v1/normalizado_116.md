---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_116.md
id_prompt: prompt_normalizador_v1.md
hash_prompt: e1c5021908631c73fd33e2d6135a03bd6a33b9a58db7908bcab13d4c72dab3da
id_auxiliar_manual: regras_para_normalizador_v1.md
hash_auxiliar_manual: 26f9f0a6a7c4bf0e55c789b0168c199e25971b21c627d4f22abc749247f9e86f
versao_normalizador: v1
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 7954
tokens_saida: 584
custo_usd: 0.010874
tempo_segundos: 7.88
timestamp: 2026-11-14T12:01:13-03:00
---

## explicacao_normalizada
Trabalhamos com todos os vendedores de televendas e todos os vendedores de campo. Primeiro, não agendamos atendimento para clientes que são filiais, em nenhuma das duas equipes. Para os demais clientes do televendas, o atendimento é a cada 7 dias, preferencialmente nos dias úteis e no sábado, sem coincidir com o atendimento da equipe de campo. No campo, atendemos a cada 7 dias os clientes ativos para o vendedor e adimplentes, e a cada 14 dias os ativos para o vendedor e inadimplentes. Os inativos para o vendedor e adimplentes são atendidos a cada 30 dias, e os inativos para o vendedor e inadimplentes, a cada 60 dias. Os clientes sem vendas são atendidos a cada 7 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/06-05-localizacao-classificacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Fluxo de uma regra
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/07-04-conflito-pivot-rota.md#Evitar choque entre televendas e campo
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-03-financeiros.md
sem_chave: clientes sem vendas
