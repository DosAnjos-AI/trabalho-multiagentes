---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_144.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9460
tokens_saida: 776
custo_usd: 0.013340
tempo_segundos: 10.31
timestamp: 2026-11-14T19:53:46-03:00
---

## explicacao_normalizada
Trabalhamos com todos os vendedores habilitados no sistema. Também temos as equipes de fabricantes, com os vendedores F, L e A; de segmentos de revendas/manutenção, com J; de consumidor final recorrente e de compra exporadica, ambas com LC; e de consumidor final de grande porte, com A. Assim, LC participa de duas equipes e A também.

Para os vendedores habilitados, seguimos a ordem abaixo quando um cliente se encaixa em mais de uma situação: vale o primeiro atendimento indicado. Quem ainda não comprou com a empresa é atendido a cada 14 dias. Depois, atendemos a cada 21 dias os clientes inadimplentes. Quem fez uma única compra com a empresa e está cadastrado há 30 dias é atendido a cada 28 dias.

Em seguida, quem comprou com seu próprio vendedor entre 31 e 60 dias atrás é atendido a cada 30 dias; quem comprou com ele entre 61 e 90 dias atrás, a cada 10 dias. Os clientes inativos considerando a empresa são atendidos a cada 21 dias.

Para os vendedores F, L, A e J, os clientes que compraram com seu próprio vendedor nos últimos 30 dias são atendidos a cada 21 dias. Para LC e A, esses clientes são atendidos a cada 28 dias. Como A participa dos dois conjuntos, para ele prevalece o atendimento a cada 21 dias nessa situação.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-03-financeiros.md
03-secoes/06-11-outros-filtros.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-02-recencia-visita-positivacao.md
