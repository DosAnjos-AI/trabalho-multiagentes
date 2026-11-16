---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_174.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9494
tokens_saida: 890
custo_usd: 0.013944
tempo_segundos: 11.22
timestamp: 2026-11-14T19:57:21-03:00
---

## explicacao_normalizada
No televendas, todos os vendedores atendem seus clientes. Primeiro, não agendamos clientes inadimplentes nem os que constam como baixada na Receita Federal. Para os demais, seguimos a ordem abaixo: se um cliente se encaixar em mais de uma situação, vale a primeira.

Clientes que ainda não compraram com o próprio vendedor são atendidos a cada 14 dias. Os que fizeram uma única compra com esse vendedor e estão cadastrados há 60 dias são atendidos a cada 21 dias.

Para quem comprou com seu vendedor nos últimos 30 dias e tem frequência histórica de compra menor que 14 dias, seguimos essa frequência histórica, respeitando o mínimo de 10 e o máximo de 14 dias. Para quem comprou com seu vendedor nos últimos 60 dias e tem frequência histórica de compra menor que 30 dias, atendemos os clientes dos ramos 9 e 18 conforme a frequência histórica, com mínimo de 14 e máximo de 21 dias; os de outros ramos são atendidos a cada 28 dias.

Entre os demais que compraram com seu vendedor entre 21 e 60 dias atrás, os dos ramos 9 e 18 são atendidos a cada 14 dias, e os de outros ramos, a cada 21 dias. Entre os que compraram com seu vendedor entre 61 e 90 dias atrás, tanto os dos ramos 9 e 18 quanto os de outros ramos são atendidos a cada 14 dias. Por fim, os que não compraram com seu vendedor nos últimos 90 dias são atendidos a cada 21 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-11-outros-filtros.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-08-frequencia-e-parametros.md",
    "03-secoes/06-06-classificacao-por-id.md"
  ],
  "sem_chave": [
    "limites mínimo e máximo da frequência histórica"
  ]
}
