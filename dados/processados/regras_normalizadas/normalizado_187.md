---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_187.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9349
tokens_saida: 574
custo_usd: 0.012219
tempo_segundos: 7.77
timestamp: 2026-11-14T19:59:12-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados no sistema cuidam desses atendimentos. Primeiro, não agendamos clientes com situação baixada na Receita Federal, filiais, inadimplentes, clientes cadastrados nos últimos 60 dias ou que compraram com qualquer vendedor da empresa nos últimos 60 dias.

Entre os demais, seguimos esta ordem: quem nunca comprou com a empresa é atendido a cada 14 dias; quem comprou com seu próprio vendedor nos últimos 90 dias, a cada 7 dias; quem comprou com esse vendedor nos últimos 120 dias, também a cada 7 dias; quem comprou com ele nos últimos 180 dias, a cada 14 dias; e quem comprou com ele nos últimos 360 dias, a cada 21 dias. Todo o resto é atendido a cada 28 dias. Quando o cliente se encaixa em mais de uma dessas situações, vale a primeira.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-03-financeiros.md
03-secoes/06-11-outros-filtros.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
