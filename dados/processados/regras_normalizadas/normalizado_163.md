---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_163.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9529
tokens_saida: 748
custo_usd: 0.013269
tempo_segundos: 9.62
timestamp: 2026-11-14T19:55:50-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem os clientes fixos de cada um. Separamos esses clientes em dois grupos: um para os ramos de atividade 3, 6, 15 e 16 e outro para os demais ramos. Em cada grupo, seguimos a ordem abaixo: quem se encaixa em uma situação recebe aquele atendimento e não passa para as seguintes.

Para os clientes dos ramos 3, 6, 15 e 16, primeiro não agendamos quem comprou com qualquer vendedor da empresa nos últimos 30 dias. Depois, atendemos a cada 30 dias quem ainda não comprou com seu próprio vendedor. Quem fez uma única compra com seu vendedor e não comprou com nenhum vendedor da empresa nos últimos 60 dias é atendido a cada 21 dias. Quem fez a última compra com seu vendedor entre 31 e 60 dias atrás é atendido a cada 28 dias; se foi entre 61 e 90 dias atrás, a cada 14 dias. Todos os demais são atendidos a cada 21 dias.

Para os clientes dos outros ramos, atendemos a cada 7 dias quem ainda não comprou com seu próprio vendedor. Quem fez uma única compra com seu vendedor e não comprou com nenhum vendedor da empresa nos últimos 30 dias é atendido a cada 14 dias. Para quem fez a última compra com qualquer vendedor da empresa entre 7 e 30 dias atrás, seguimos o histórico, com intervalo mínimo de 7 e máximo de 30 dias. Quem fez a última compra com seu próprio vendedor entre 31 e 60 dias atrás é atendido a cada 14 dias; se foi entre 61 e 90 dias atrás, a cada 7 dias. Todos os demais são atendidos a cada 7 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/06-06-classificacao-por-id.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limites mínimo e máximo na frequência histórica
