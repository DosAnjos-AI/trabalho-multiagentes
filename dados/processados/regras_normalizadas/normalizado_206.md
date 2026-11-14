---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_206.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9376
tokens_saida: 672
custo_usd: 0.012736
tempo_segundos: 8.76
timestamp: 2026-11-14T20:01:33-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados, exceto o vendedor 135, cuidam dos seus clientes fixos. Separamos esses clientes pelo tempo desde a última compra com qualquer vendedor da empresa: de um lado, os que compraram nos últimos 90 dias; de outro, os que compraram entre 91 e 180 dias atrás. Um cliente não fica nos dois grupos ao mesmo tempo. O vendedor 135 atende seus próprios clientes.

Antes de definir a frequência, não agendamos filiais nem clientes inadimplentes, tanto para os vendedores de televendas quanto para o vendedor 135. Os vendedores de televendas, exceto o 135, também não agendam clientes que nunca compraram com a empresa.

Para os clientes dos dois grupos e também para os clientes do vendedor 135, depois dessas exclusões, atendemos a cada 7 dias quem tem ramo de atividade com código 1, 2, 4 ou 12; a cada 15 dias quem tem código 3; e a cada 28 dias os demais.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/04-01-carteiras-e-segmentacoes.md#Exclusiva x livre
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-03-financeiros.md
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-06-classificacao-por-id.md
