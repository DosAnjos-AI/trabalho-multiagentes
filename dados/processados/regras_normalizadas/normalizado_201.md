---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_201.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9409
tokens_saida: 633
custo_usd: 0.012574
tempo_segundos: 11.87
timestamp: 2026-11-14T20:00:52-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade: primeiro, não agendamos clientes com situação baixada na Receita Federal, inadimplentes, bloqueados ou que sejam filiais.

Entre os demais, atendemos a cada 7 dias os clientes que ainda não compraram com seu vendedor. Os que não compraram com ele nos últimos 90 dias são atendidos a cada 28 dias. Quem está cadastrado há 60 dias e fez uma única compra com seu vendedor é atendido a cada 30 dias.

Para os demais, considerando as compras com o próprio vendedor, quem comprou nos últimos 30 dias e tem intervalo histórico entre compras menor que 30 dias é atendido a cada 30 dias. Quem comprou nos últimos 30 dias e tem intervalo histórico entre compras menor que 90 dias também é atendido a cada 30 dias. Quem comprou entre 30 e 60 dias atrás é atendido a cada 10 dias, e quem comprou entre 61 e 90 dias atrás, a cada 14 dias.

Quando um cliente se encaixa em mais de uma dessas situações, vale a primeira. Todos os demais não são agendados.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-03-financeiros.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-11-outros-filtros.md
03-secoes/06-08-frequencia-e-parametros.md
