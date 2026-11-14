---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_199.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9358
tokens_saida: 615
custo_usd: 0.012433
tempo_segundos: 8.30
timestamp: 2026-11-14T20:00:34-03:00
---

## explicacao_normalizada
Os vendedores do televendas atendem seus clientes seguindo esta ordem de prioridade: primeiro, não agendamos os inadimplentes nem os bloqueados. Para os demais, quando um cliente se encaixar em mais de uma situação, vale a primeira.

Clientes que nunca compraram com a empresa são atendidos a cada 30 dias. Também atendemos a cada 30 dias quem fez uma única compra com a empresa e comprou com seu próprio vendedor nos últimos 40 dias.

Depois vêm os clientes ativos para o próprio vendedor cuja frequência histórica de compra é menor que 21 dias: esses são atendidos a cada 90 dias. Em seguida, quem comprou com qualquer vendedor da empresa entre 31 e 59 dias atrás é atendido a cada 30 dias; quem comprou entre 60 e 89 dias atrás, a cada 21 dias; e quem não comprou com nenhum vendedor da empresa nos últimos 90 dias, a cada 45 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-03-financeiros.md
03-secoes/06-05-localizacao-classificacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-08-frequencia-e-parametros.md
