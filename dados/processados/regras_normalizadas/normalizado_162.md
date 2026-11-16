---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_162.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9306
tokens_saida: 546
custo_usd: 0.012036
tempo_segundos: 7.37
timestamp: 2026-11-14T19:55:40-03:00
---

## explicacao_normalizada
No televendas, consideramos todos os vendedores habilitados no sistema. Primeiro, não agendamos clientes que sejam pessoas físicas nem os inadimplentes.

Para os demais, seguimos esta ordem: os clientes prospect são atendidos a cada 14 dias; depois, os clientes inativos para o vendedor que cuida deles também são atendidos a cada 14 dias. Em seguida, os que não compraram nos últimos 45 dias são atendidos a cada 30 dias.

Para todo o resto, usamos o intervalo do histórico, respeitando o mínimo de 14 e o máximo de 45 dias entre atendimentos. Se o cliente se encaixar em mais de uma situação, vale a primeira dessa ordem.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md"
  ],
  "sem_chave": [
    "limites mínimo e máximo da frequência histórica"
  ]
}
