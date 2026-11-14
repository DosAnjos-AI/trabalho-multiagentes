---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_213.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9376
tokens_saida: 493
custo_usd: 0.011841
tempo_segundos: 6.61
timestamp: 2026-11-14T20:02:16-03:00
---

## explicacao_normalizada
Trabalhamos com os vendedores de televendas habilitados no sistema e os clientes fixos de cada um. Primeiro, os clientes que são filiais não devem ser agendados.

Separamos os demais clientes pelos códigos de rota: 24, 523, 524, 525 e 526 para segunda; 3, 4, 17, 500, 512, 514 e 515 para terça; 502, 530 e 531 para quarta; 20, 501, 504, 505, 506, 508, 513, 516, 527 e 528 para quinta; e 5, 19, 510, 511 e 521 para sexta.

Em cada um desses grupos, os clientes ativos para o próprio vendedor são atendidos semanalmente. Os demais são atendidos a cada 28 dias. O atendimento é fixo, com preferência pelo dia correspondente ao grupo.

Para os clientes das rotas 10 e 11, o atendimento é semanal, sem dia específico.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/06-05-localizacao-classificacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-06-classificacao-por-id.md
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/07-04-conflito-pivot-rota.md#Roteirização e fixação
