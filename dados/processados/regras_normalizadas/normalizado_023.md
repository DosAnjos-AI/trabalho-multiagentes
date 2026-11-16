---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_023.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9407
tokens_saida: 467
custo_usd: 0.011742
tempo_segundos: 6.75
timestamp: 2026-11-14T19:46:09-03:00
---

## explicacao_normalizada
No televendas de GYN, trabalhamos com todos os vendedores de televendas do supervisor 5178 e com os clientes fixos de cada um. No televendas de DF, trabalhamos com todos os vendedores de televendas e seus respectivos clientes fixos. Os vendedores do supervisor 5178 também estão nesse segundo grupo. Quando um cliente se encaixar em mais de uma situação, seguimos a primeira das situações abaixo.

Para os clientes do televendas de GYN que estão sem vendas, o atendimento é a cada 7 dias; para todos os demais, a cada 14 dias.

Para os clientes do televendas de DF, atendemos os adimplentes a cada 7 dias. Depois, os inadimplentes que estão ativos para seu vendedor são atendidos a cada 14 dias, e os inadimplentes que estão inativos para seu vendedor não devem ser agendados. Os demais clientes que estão sem vendas são atendidos a cada 7 dias.

No atendimento externo de DF, trabalhamos com todos os vendedores de campo. Os clientes ativos para seu vendedor são atendidos em intervalos fixos de 7 dias; todos os demais, em intervalos fixos de 15 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/06-01-atividade-inatividade.md"
  ],
  "sem_chave": [
    "clientes sem vendas"
  ]
}
