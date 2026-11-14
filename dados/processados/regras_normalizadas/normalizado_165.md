---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_165.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9479
tokens_saida: 865
custo_usd: 0.013804
tempo_segundos: 11.16
timestamp: 2026-11-14T19:56:13-03:00
---

## explicacao_normalizada
No televendas, trabalhamos com os vendedores habilitados, e no atendimento de campo com todos os vendedores. Entre os clientes fixos dos vendedores de campo, separamos os que têm histórico de pedidos em intervalos de 1 a 7 dias, de 16 a 30 dias, de 31 a 45 dias e de 61 a 90 dias.

Para os clientes atendidos pelo televendas, seguimos esta ordem: primeiro, não agendamos os que estão inativos na empresa e inadimplentes. Depois, atendemos a cada 7 dias os que estão há mais de 90 dias sem comprar com o próprio vendedor de televendas.

Em seguida, entre os clientes fixos de campo separados pelo histórico de pedidos, atendemos a cada 14 dias os que têm intervalos históricos de 1 a 7 dias e estão entre 8 e 15 dias sem comprar com seu vendedor de televendas; a cada 28 dias os que têm intervalos de 16 a 30 dias e estão entre 31 e 45 dias sem comprar com esse vendedor; e a cada 21 dias os que têm intervalos de 31 a 45 dias e estão entre 46 e 60 dias sem comprar com esse vendedor. Para os que têm intervalos históricos de 61 a 90 dias e estão há mais de 90 dias sem comprar com seu vendedor de televendas, o atendimento seria a cada 15 dias.

Cada cliente fica com o primeiro tratamento em que se encaixar nessa ordem. Os demais não são agendados.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/04-01-carteiras-e-segmentacoes.md#Segmentação como fonte
03-secoes/06-08-frequencia-e-parametros.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-03-financeiros.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-09-segmentacao-contido.md
