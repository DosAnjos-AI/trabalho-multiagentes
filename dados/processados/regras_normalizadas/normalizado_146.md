---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_146.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9379
tokens_saida: 562
custo_usd: 0.012189
tempo_segundos: 8.82
timestamp: 2026-11-14T19:54:02-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados no sistema atendem seus clientes seguindo esta ordem de prioridade: primeiro, não agendamos os inadimplentes. Depois, atendemos a cada 7 dias os clientes dos ramos 37, 43 e 15. Também atendemos a cada 7 dias os clientes dos ramos 41, 4 e 25 cujo histórico de compras indica frequência de 7 dias.

Quem ainda não comprou com seu vendedor é atendido a cada 30 dias. Também atendemos a cada 30 dias quem fez uma única compra com seu vendedor e comprou nos últimos 30 dias.

Para os demais, quem tem frequência histórica de compra menor que 21 dias é atendido a cada 21 dias. Quem comprou com seu vendedor entre 30 e 45 dias atrás também é atendido a cada 21 dias. Quem não comprou com seu vendedor nos últimos 46 dias é atendido a cada 45 dias. Se o cliente se encaixar em mais de uma dessas situações, vale a primeira na ordem apresentada.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-03-financeiros.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-06-classificacao-por-id.md
03-secoes/06-08-frequencia-e-parametros.md
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
