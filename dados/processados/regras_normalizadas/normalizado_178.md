---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_178.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9376
tokens_saida: 590
custo_usd: 0.012326
tempo_segundos: 7.87
timestamp: 2026-11-14T19:57:49-03:00
---

## explicacao_normalizada
Os vendedores habilitados do televendas atendem seus clientes, e o vendedor 48 segue um atendimento separado para os dele.

Para o televendas, primeiro não agendamos clientes com situação baixada na Receita Federal nem os que compraram com o próprio vendedor nos últimos 39 dias. Depois, atendemos a cada 15 dias quem comprou com esse vendedor entre 40 e 89 dias atrás. Quem comprou entre 90 e 119 dias atrás, entre 120 e 359 dias atrás ou não comprou com ele nos últimos 359 dias é atendido a cada 7 dias.

Para o vendedor 48, primeiro não agendamos os clientes cadastrados há 7 dias. Depois, nessa ordem, atendemos os cadastrados há 60 dias a cada 30 dias; os cadastrados há 30 dias, a cada 20 dias; e os cadastrados há 15 dias ou há 8 dias, a cada 15 dias. Se um cliente se encaixar em mais de uma dessas situações, vale a primeira.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-11-outros-filtros.md
