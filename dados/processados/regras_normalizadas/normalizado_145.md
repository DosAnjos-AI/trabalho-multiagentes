---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_145.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9374
tokens_saida: 548
custo_usd: 0.012114
tempo_segundos: 7.30
timestamp: 2026-11-14T19:53:53-03:00
---

## explicacao_normalizada
Todos os vendedores habilitados no sistema participam do atendimento. Não agendamos clientes que sejam filiais.

Para os demais clientes, seguimos esta ordem: pessoas jurídicas que são prospects em relação ao próprio vendedor são atendidas a cada 10 dias. Depois, entre as pessoas jurídicas que ainda não compraram com seu vendedor, atendemos as do ramo 2 a cada 14 dias e as do ramo 1 a cada 7 dias.

Em seguida, atendemos a cada 14 dias as pessoas jurídicas adimplentes cuja última compra com o próprio vendedor foi entre 31 e 60 dias atrás. As pessoas jurídicas adimplentes que compraram com seu vendedor nos últimos 30 dias são atendidas a cada 21 dias. Já as adimplentes cuja última compra com esse vendedor foi entre 61 e 90 dias atrás são atendidas a cada 7 dias.

As demais pessoas jurídicas são atendidas a cada 21 dias. Se um cliente se encaixar em mais de uma dessas situações, vale a primeira que aparecer nessa ordem.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-06-classificacao-por-id.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md"
  ],
  "sem_chave": []
}
