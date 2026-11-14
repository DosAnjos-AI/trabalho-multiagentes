---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_130.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9328
tokens_saida: 615
custo_usd: 0.012403
tempo_segundos: 8.15
timestamp: 2026-11-14T19:52:17-03:00
---

## explicacao_normalizada
Trabalhamos com todos os vendedores de televendas e todos os vendedores de campo, cada um com seus clientes.

No televendas, primeiro não agendamos pessoas físicas, inclusive as que não têm compras. Para os demais, atendemos a cada 7 dias os clientes ativos para o próprio vendedor. Os inativos para esse vendedor que estão em dia com os pagamentos são atendidos a cada 15 dias; os inadimplentes não são agendados. As pessoas jurídicas sem compras são atendidas a cada 20 dias. Quando um cliente se encaixa em mais de uma dessas situações, seguimos essa ordem.

Para os vendedores de campo, atendemos os clientes ativos para o próprio vendedor em intervalos fixos de 7 dias. Todos os demais são atendidos em intervalos fixos de 15 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/06-05-localizacao-classificacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
sem_chave: clientes sem compras
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-03-financeiros.md
