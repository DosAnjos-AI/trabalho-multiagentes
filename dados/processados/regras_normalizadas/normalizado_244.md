---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_244.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9365
tokens_saida: 568
custo_usd: 0.012205
tempo_segundos: 7.66
timestamp: 2026-11-14T20:05:25-03:00
---

## explicacao_normalizada
No televendas, trabalhamos com todos os vendedores habilitados. Para cada cliente, seguimos esta ordem: primeiro, não agendamos clientes que são filiais nem clientes inadimplentes. Se o cliente se encaixar em mais de uma situação, vale a primeira.

Os clientes que ainda não compraram com o próprio vendedor são atendidos a cada 14 dias. Quem fez uma única compra com esse vendedor é atendido a cada 7 dias. Para os clientes ativos em relação ao próprio vendedor, cuja frequência histórica de compra seja menor que 8 dias, seguimos essa frequência, respeitando o mínimo de 5 e o máximo de 7 dias.

Depois, para os demais clientes, consideramos o tempo desde a última compra com o próprio vendedor: entre 8 e 30 dias, atendemos a cada 14 dias; entre 31 e 60 dias, a cada 7 dias; e, se não compraram com ele nos últimos 60 dias, a cada 14 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-08-frequencia-e-parametros.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md"
  ],
  "sem_chave": [
    "mínimo e máximo na frequência do histórico"
  ]
}
