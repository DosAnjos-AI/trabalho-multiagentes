---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_179.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9754
tokens_saida: 938
custo_usd: 0.014444
tempo_segundos: 11.58
timestamp: 2026-11-14T19:58:00-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem os clientes fixos de cada um. Nós os dividimos pelo ramo de atividade em três grupos, sem sobreposição.

No grupo construtora ficam os ramos 10207004, 10301009, 10101016, 10301016, 10207001, 10301010, 10207002, 10301011, 10207003, 10301015, 10205001, 10205002 e 10204002. No grupo matcon ficam 10103004, 10202002, 10201004, 10201006, 10201009, 10201003, 10201011, 10201005, 10201002, 10201001, 10101013, 10103003, 10102004, 10202005, 10201007, 10205003, 10301001, 10101019, 10301019, 10301002, 10301007, 10301004, 10101006 e 10301006. O terceiro grupo reúne os clientes cujo ramo é diferente de todos esses códigos.

A ordem abaixo é a prioridade: se o cliente se encaixar em mais de uma situação, seguimos a primeira que se aplicar. Nos três grupos, quem nunca comprou com o próprio vendedor é atendido a cada 7 dias. Depois, para quem fez uma única compra com esse vendedor, o atendimento é a cada 14 dias no grupo construtora e a cada 7 dias nos outros dois grupos.

Em seguida, nos grupos matcon e de outros ramos, quem comprou com o próprio vendedor entre 7 e 30 dias atrás é atendido conforme o histórico, com intervalo mínimo de 7 e máximo de 30 dias. No grupo construtora, quem comprou com o próprio vendedor nos últimos 30 dias é atendido a cada 7 dias; quem não comprou com ele nesse período, a cada 14 dias.

Nas situações seguintes, consideramos as compras com qualquer vendedor da empresa. Para quem comprou entre 30 e 60 dias atrás, o atendimento é a cada 7 dias no grupo matcon e a cada 14 dias nos outros dois. Para quem comprou entre 60 e 89 dias atrás, é a cada 7 dias no matcon, 14 dias no construtora e 21 dias no grupo de outros ramos. Para quem comprou entre 90 e 179 dias atrás, é a cada 7 dias no matcon, 21 dias no construtora e 14 dias no grupo de outros ramos. Por fim, quem não comprou com nenhum vendedor da empresa nos últimos 180 dias é atendido a cada 14 dias nos grupos matcon e de outros ramos, e a cada 28 dias no construtora.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/06-06-classificacao-por-id.md
03-secoes/04-01-carteiras-e-segmentacoes.md#Exclusiva x livre
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: mínimo e máximo na frequência do histórico
