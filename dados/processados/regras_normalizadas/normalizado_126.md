---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_126.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9433
tokens_saida: 539
custo_usd: 0.012128
tempo_segundos: 7.47
timestamp: 2026-11-14T19:52:02-03:00
---

## explicacao_normalizada
Os vendedores 73, 196, 254 e 313 atendem os clientes sob sua responsabilidade. No televendas, os demais vendedores habilitados cuidam cada um dos seus clientes fixos; no atendimento de campo, todos os vendedores habilitados cuidam também dos seus respectivos clientes fixos.

Para os vendedores 73, 196, 254 e 313, atendemos a cada 14 dias os clientes que estão há mais de 31 dias sem comprar com qualquer vendedor da empresa, dando preferência aos dias úteis. Os demais clientes desses vendedores não devem ser agendados.

No televendas, olhamos primeiro os clientes ativos para o próprio vendedor: os que estão em dia são atendidos a cada 14 dias e os inadimplentes, a cada 21 dias. Depois, entre os inativos para o vendedor, os que estão em dia são atendidos a cada 30 dias e os inadimplentes não são agendados. Por fim, os clientes sem venda que ainda não tenham recebido um desses tratamentos são atendidos a cada 30 dias. Em todos esses atendimentos, damos preferência aos dias úteis.

No campo, os clientes ativos para o próprio vendedor são atendidos a cada 7 dias, em intervalo fixo. Todos os demais são atendidos a cada 15 dias, também em intervalo fixo.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/07-02-preferencia-dia-semana.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-03-financeiros.md"
  ],
  "sem_chave": [
    "clientes sem venda"
  ]
}
