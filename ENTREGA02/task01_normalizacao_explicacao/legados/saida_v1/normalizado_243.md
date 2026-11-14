---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_243.md
id_prompt: prompt_normalizador_v1.md
hash_prompt: e1c5021908631c73fd33e2d6135a03bd6a33b9a58db7908bcab13d4c72dab3da
id_auxiliar_manual: regras_para_normalizador_v1.md
hash_auxiliar_manual: 26f9f0a6a7c4bf0e55c789b0168c199e25971b21c627d4f22abc749247f9e86f
versao_normalizador: v1
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 7929
tokens_saida: 846
custo_usd: 0.012159
tempo_segundos: 11.12
timestamp: 2026-11-14T12:02:27-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade: pessoas jurídicas que ainda não compraram com o próprio vendedor são atendidas a cada 21 dias. As que compraram com ele nos últimos 20 dias são atendidas a cada 3 dias. Para as pessoas jurídicas cuja última compra com o próprio vendedor foi entre 20 e 33 dias atrás, usamos o intervalo do histórico do cliente acrescido de 2 dias, respeitando o mínimo de 20 dias e o máximo de 33 dias. Nesses atendimentos, preferimos dias úteis e sábado. As demais pessoas jurídicas não são agendadas, assim como todos os outros clientes.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Fluxo de uma regra
03-secoes/04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: mínimo e máximo da frequência do histórico
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
