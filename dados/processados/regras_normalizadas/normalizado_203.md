---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_203.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9356
tokens_saida: 551
custo_usd: 0.012111
tempo_segundos: 7.98
timestamp: 2026-11-14T20:01:07-03:00
---

## explicacao_normalizada
Para os vendedores de televendas habilitados no sistema, não agendamos clientes com situação baixada na Receita Federal, filiais cujo cliente principal tem código diferente de 36979, inadimplentes, clientes sem venda e clientes que não compraram nos últimos 95 dias.

Entre os demais, damos prioridade aos clientes que fizeram uma única compra com a empresa, atendendo-os a cada 28 dias. Depois, conforme o intervalo histórico médio entre pedidos, atendemos a cada 6 dias quem tem intervalo de 0 a 7 dias; a cada 9 dias, de 8 a 14 dias; a cada 16 dias, de 15 a 21 dias; a cada 23 dias, de 22 a 28 dias; a cada 29 dias, de 29 a 38 dias; e a cada 35 dias, de 39 a 60 dias. Todo o restante é atendido a cada 55 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-06-classificacao-por-id.md
03-secoes/06-03-financeiros.md
sem_chave: clientes sem venda
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-08-frequencia-e-parametros.md
