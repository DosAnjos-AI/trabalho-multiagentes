---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_189.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9396
tokens_saida: 856
custo_usd: 0.013676
tempo_segundos: 10.89
timestamp: 2026-11-14T19:59:30-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade quando alguém se encaixa em mais de uma situação.

Para quem não comprou com nenhum vendedor da empresa neste ano e tem ticket médio acima de R$ 4999, o atendimento é semanal, em dia fixo, com preferência por segunda e sexta. Para quem também não comprou da empresa neste ano e tem ticket médio abaixo de R$ 4999, o atendimento é semanal, em dia fixo, com preferência por terça e sexta. Quem não comprou da empresa neste ano, mas comprou no ano passado, é atendido semanalmente, com preferência por quarta e quinta.

Quem ainda não comprou com o próprio vendedor é atendido a cada 7 dias, assim como quem fez uma única compra com esse vendedor. Para clientes com intervalo histórico de compra entre 0 e 14 dias, seguimos esse histórico, atendendo no mínimo a cada 4 dias e no máximo a cada 6 dias. Por fim, quem está entre 25 e 30 dias além do período habitual de compra com o próprio vendedor é atendido a cada 7 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-03-financeiros.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/07-04-conflito-pivot-rota.md#Roteirização e fixação
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/06-08-frequencia-e-parametros.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limites mínimo e máximo na frequência histórica
sem_chave: faixa de atraso além do período habitual
