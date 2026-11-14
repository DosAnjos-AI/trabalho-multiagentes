---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_208.md
id_prompt: prompt_normalizador_v1.md
hash_prompt: e1c5021908631c73fd33e2d6135a03bd6a33b9a58db7908bcab13d4c72dab3da
id_auxiliar_manual: regras_para_normalizador_v1.md
hash_auxiliar_manual: 26f9f0a6a7c4bf0e55c789b0168c199e25971b21c627d4f22abc749247f9e86f
versao_normalizador: v1
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 7981
tokens_saida: 692
custo_usd: 0.011441
tempo_segundos: 8.78
timestamp: 2026-11-14T12:02:16-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados no sistema seguem esta ordem de atendimento: primeiro, não agendamos clientes com situação baixada na Receita Federal, inadimplentes, bloqueados ou que sejam filiais. Entre os demais, atendemos a cada 7 dias quem ainda não comprou com o próprio vendedor e, a cada 14 dias, quem fez uma única compra com ele. Depois, atendemos a cada 14 dias quem comprou com seu vendedor neste mês e tem frequência histórica de compra entre 90 e 120 dias; também a cada 14 dias quem comprou com esse vendedor nos últimos 30 dias. Quem comprou com ele nos últimos 89 dias é atendido a cada 7 dias e quem comprou nos últimos 120 dias, a cada 3 dias. Quando o cliente se encaixar em mais de uma dessas situações, vale a primeira dessa sequência. Todos os demais não são agendados.

## regras_extraidas
03-secoes/03-01-times.md
sem_chave: prioridade entre situações de atendimento
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-03-financeiros.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Fluxo de uma regra
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-08-frequencia-e-parametros.md
