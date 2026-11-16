---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_234.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9327
tokens_saida: 468
custo_usd: 0.011667
tempo_segundos: 6.69
timestamp: 2026-11-14T20:04:14-03:00
---

## explicacao_normalizada
Todos os vendedores atendem seus respectivos clientes fixos. Seguimos esta ordem de prioridade: os clientes com queda de faturamento maior que 5% são atendidos a cada 3 dias. Depois, não agendamos os que fizeram a última compra entre 1138 e 9999 dias atrás.

Entre os demais, os clientes da cidade GOIANIA são atendidos no intervalo que a empresa usa para clientes inativos. Depois, os clientes ativos para o próprio vendedor são atendidos no intervalo que a empresa usa para clientes ativos; os inativos para o próprio vendedor e os clientes sem vendas, no intervalo usado para clientes inativos. Nesses atendimentos, damos preferência a dias úteis, sábado e domingo.

Todos os demais clientes são atendidos a cada 7 dias, com preferência por dias úteis.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-11-outros-filtros.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-02-preferencia-dia-semana.md"
  ],
  "sem_chave": [
    "clientes sem vendas"
  ]
}
