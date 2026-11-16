---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_230.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9346
tokens_saida: 455
custo_usd: 0.011621
tempo_segundos: 6.59
timestamp: 2026-11-14T20:03:46-03:00
---

## explicacao_normalizada
Os vendedores de televendas cuidam dos seus clientes. Primeiro, não agendamos atendimento para os inadimplentes. Para os demais, seguimos a ordem abaixo: se o cliente se encaixar em mais de uma situação, vale a primeira.

Quem ainda não comprou com seu vendedor é atendido a cada 14 dias. Quem fez uma única compra com esse vendedor é atendido a cada 7 dias. Os clientes ativos para seu vendedor, com frequência histórica de compras inferior a 16 dias, são atendidos a cada 14 dias.

Quem fez a última compra com seu vendedor entre 16 e 45 dias atrás é atendido a cada 14 dias. Quem fez a última compra com ele entre 60 e 89 dias atrás é atendido a cada 7 dias. Por fim, quem não comprou com seu vendedor nos últimos 60 dias é atendido a cada 21 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-08-frequencia-e-parametros.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md"
  ],
  "sem_chave": []
}
