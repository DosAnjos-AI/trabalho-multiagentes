---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_055.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9368
tokens_saida: 579
custo_usd: 0.012263
tempo_segundos: 7.59
timestamp: 2026-11-14T19:47:15-03:00
---

## explicacao_normalizada
Atendemos os clientes fixos de cada vendedor. No televendas, participam todos os vendedores de televendas. No interior, atendem os vendedores 27, 35 e 34; na capital, todos os vendedores de campo, exceto 27, 35 e 34.

Para os clientes do televendas, seguimos esta ordem: os adimplentes são atendidos a cada 14 dias; depois, os inadimplentes ativos para o próprio vendedor, a cada 30 dias; em seguida, os clientes sem venda, a cada 30 dias; e os inadimplentes inativos para o próprio vendedor não são agendados. Se um cliente se encaixar em mais de uma dessas situações, vale a primeira.

Na capital, também seguimos a ordem: clientes sem venda são atendidos a cada 30 dias, depois os inadimplentes a cada 30 dias e todos os demais a cada 14 dias. No interior, todos os clientes são atendidos a cada 30 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/03-01-times.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md"
  ],
  "sem_chave": [
    "sem venda isolado"
  ]
}
