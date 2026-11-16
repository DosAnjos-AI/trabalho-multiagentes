---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_235.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9633
tokens_saida: 740
custo_usd: 0.013333
tempo_segundos: 9.64
timestamp: 2026-11-14T20:04:23-03:00
---

## explicacao_normalizada
Atendemos com os vendedores de televendas habilitados, exceto 503, 518, 519, 521, 623, 624 e 626. Também atendemos com os vendedores 519, 503, 518, 521, 623, 624 e 626; para 521, 623 e 624 há ainda um atendimento temporário específico. As situações abaixo seguem a ordem de prioridade: quando o cliente se encaixar em mais de uma, vale a primeira.

Primeiro, não agendamos clientes cuja situação na Receita Federal esteja baixada. Para os vendedores 519, 503, 518, 521, 623, 624 e 626, também não agendamos clientes com rota prevista para os próximos 7 dias ou que compraram com o próprio vendedor nos últimos 7 dias. Para os demais vendedores de televendas habilitados, não agendamos quem comprou com o próprio vendedor nos últimos 30 dias.

Depois desses impedimentos, para 521, 623 e 624, atendemos a cada 1 dia os clientes com 5% de crédito cuja rota foi há exatamente 14 dias. Para os demais vendedores de televendas habilitados, atendemos a cada 15 dias quem comprou com o próprio vendedor entre 30 e 90 dias atrás; todo o restante é atendido a cada 10 dias.

Para os vendedores 519, 503, 518, 521, 623 e 624 e 626, atendemos a cada 14 dias os clientes com 5% de crédito e rota nos últimos 7 dias. Em seguida, considerando compras com qualquer vendedor da empresa e sempre exigindo 5% de crédito, atendemos a cada 14 dias quem comprou entre 7 e 30 dias atrás ou entre 31 e 60 dias atrás; a cada 7 dias quem comprou entre 61 e 89 dias atrás; e a cada 14 dias quem comprou entre 90 e 179 dias atrás. Os demais clientes desses vendedores que tenham 5% de crédito são atendidos a cada 21 dias.

Em todos os atendimentos com intervalo definido, damos preferência aos dias úteis e ao sábado. Os clientes que não se encaixarem nas situações acima não são agendados.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-11-outros-filtros.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/07-02-preferencia-dia-semana.md"
  ],
  "sem_chave": []
}
