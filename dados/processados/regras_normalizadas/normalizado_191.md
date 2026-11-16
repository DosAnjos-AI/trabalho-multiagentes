---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_191.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9356
tokens_saida: 524
custo_usd: 0.011976
tempo_segundos: 7.17
timestamp: 2026-11-14T16:26:13-03:00
---

## explicacao_normalizada
O atendimento é feito pelos vendedores de televendas habilitados. Primeiro, não agendamos clientes com situação baixada na Receita Federal nem clientes inadimplentes.

Para os demais, seguimos esta ordem: clientes que nunca compraram com a empresa são atendidos a cada 21 dias. Depois, quem comprou com o próprio vendedor nos últimos 7 dias também é atendido a cada 21 dias. Quem comprou com esse vendedor nos últimos 30 dias é atendido conforme o intervalo habitual entre suas compras, acrescido de 3 dias, respeitando o mínimo de 14 e o máximo de 30 dias.

Em seguida, quem comprou com o próprio vendedor nos últimos 45 dias é atendido a cada 7 dias, assim como quem comprou com ele nos últimos 60 dias. Todos os demais clientes também são atendidos a cada 7 dias. Se o cliente se encaixar em mais de uma dessas situações, vale a primeira.

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
