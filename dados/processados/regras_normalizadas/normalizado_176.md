---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_176.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9278
tokens_saida: 369
custo_usd: 0.011123
tempo_segundos: 5.63
timestamp: 2026-11-14T19:57:36-03:00
---

## explicacao_normalizada
Os vendedores do televendas atendem seus próprios clientes fixos. Primeiro, não agendamos os clientes com cobrança DH que não têm crédito, os de cobrança BK com menos de R$ 199 de crédito disponível e os inadimplentes.

Para os demais, seguimos esta ordem: clientes ativos para o próprio vendedor são atendidos a cada 7 dias; clientes inativos para o próprio vendedor, a cada 14 dias; e clientes sem venda, também a cada 14 dias. Se um cliente se encaixar em mais de uma dessas situações, vale a primeira.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-06-classificacao-por-id.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-03-frequencia.md"
  ],
  "sem_chave": [
    "clientes sem venda"
  ]
}
