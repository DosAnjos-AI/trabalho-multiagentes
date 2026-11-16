---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_106.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9355
tokens_saida: 388
custo_usd: 0.011295
tempo_segundos: 5.81
timestamp: 2026-11-14T19:50:42-03:00
---

## explicacao_normalizada
Trabalhamos com todos os vendedores de televendas e todos os vendedores de campo, cada um atendendo seus clientes fixos. Quando um cliente se encaixar em mais de uma situação, seguimos a ordem abaixo.

No televendas, os clientes ativos para o próprio vendedor e em dia são atendidos a cada 10 dias; os ativos para o vendedor e inadimplentes, a cada 21 dias. Os inativos para o vendedor e em dia são atendidos a cada 14 dias; os inativos para o vendedor e inadimplentes, a cada 60 dias. Por último, atendemos os clientes sem venda a cada 30 dias.

No campo, atendemos os clientes ativos para o próprio vendedor e em dia a cada 30 dias e os inativos para o vendedor e em dia a cada 14 dias. Não agendamos os inadimplentes. Por último, atendemos os clientes sem venda a cada 30 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/07-03-frequencia.md"
  ],
  "sem_chave": [
    "clientes sem venda"
  ]
}
