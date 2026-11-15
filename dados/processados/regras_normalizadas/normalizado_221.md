---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_221.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9335
tokens_saida: 527
custo_usd: 0.011970
tempo_segundos: 6.91
timestamp: 2026-11-14T21:03:23-03:00
---

## explicacao_normalizada
Os vendedores habilitados do televendas atendem seus clientes com preferência por dias úteis e sábado. Seguimos a ordem abaixo quando um cliente se encaixa em mais de uma situação.

Quem ainda não comprou com o próprio vendedor deve ser atendido a cada 21 dias. Quem fez uma única compra com esse vendedor e não comprou com ele nos últimos 30 dias deve ser atendido a cada 14 dias.

Para os demais, quem comprou com o próprio vendedor nos últimos 30 dias, mas não nos últimos 21 dias, deve ser atendido a cada 14 dias. Quem está entre 31 e 60 dias sem comprar com ele também deve ser atendido a cada 14 dias; entre 61 e 90 dias, a cada 7 dias; e entre 91 e 360 dias, a cada 28 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
