---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_191.md
id_prompt: prompt_normalizador_v1.md
hash_prompt: e1c5021908631c73fd33e2d6135a03bd6a33b9a58db7908bcab13d4c72dab3da
id_auxiliar_manual: regras_para_normalizador_v1.md
hash_auxiliar_manual: 26f9f0a6a7c4bf0e55c789b0168c199e25971b21c627d4f22abc749247f9e86f
versao_normalizador: v1
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 7985
tokens_saida: 915
custo_usd: 0.012560
tempo_segundos: 12.19
timestamp: 2026-11-14T12:02:07-03:00
---

## explicacao_normalizada
O atendimento é feito pelos vendedores de televendas habilitados. Primeiro, não agendamos clientes com situação baixada na Receita Federal nem clientes inadimplentes. Para os demais, seguimos esta ordem: clientes que nunca compraram com a empresa são atendidos a cada 21 dias. Depois, quem comprou com o próprio vendedor nos últimos 7 dias também é atendido a cada 21 dias. Quem comprou com esse vendedor nos últimos 30 dias é atendido conforme o intervalo habitual entre suas compras, acrescido de 3 dias, respeitando o mínimo de 14 e o máximo de 30 dias. Em seguida, quem comprou com o próprio vendedor nos últimos 45 dias é atendido a cada 7 dias, assim como quem comprou com ele nos últimos 60 dias. Todos os demais clientes também são atendidos a cada 7 dias. Se o cliente se encaixar em mais de uma dessas situações, vale a primeira.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-03-financeiros.md
sem_chave: prioridade entre situações de atendimento
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Fluxo de uma regra
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limites para frequência histórica
