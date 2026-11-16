---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_212.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9406
tokens_saida: 590
custo_usd: 0.012356
tempo_segundos: 7.92
timestamp: 2026-11-14T20:02:10-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados no sistema cuidam desses atendimentos. Seguimos a ordem abaixo: quando um cliente se encaixa em mais de uma situação, vale a primeira.

Primeiro, não agendamos clientes que tenham rota prevista para os próximos 7 dias, nem os que compraram com qualquer vendedor da empresa nos últimos 14 dias.

Para clientes cuja rota foi há 7 dias e que receberam visita da empresa na semana anterior, atendemos a cada 7 dias se a última compra com qualquer vendedor da empresa foi entre 14 e 30 dias atrás; se foi entre 31 e 60 dias atrás, atendemos a cada 20 dias.

Clientes que ainda não têm vendas são atendidos a cada 14 dias. Também atendemos a cada 14 dias os que compraram com qualquer vendedor da empresa no ano passado e cuja última compra foi entre 180 e 360 dias atrás.

Quem fez a última compra com qualquer vendedor da empresa entre 61 e 90 dias atrás é atendido a cada 7 dias. O mesmo vale para quem fez a última compra entre 91 e 180 dias atrás. Todos os demais clientes são atendidos a cada 7 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-11-outros-filtros.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md"
  ],
  "sem_chave": [
    "clientes que ainda não têm vendas"
  ]
}
