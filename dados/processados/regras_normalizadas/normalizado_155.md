---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_155.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9457
tokens_saida: 683
custo_usd: 0.012872
tempo_segundos: 8.67
timestamp: 2026-11-14T19:55:01-03:00
---

## explicacao_normalizada
Os vendedores habilitados do televendas cuidam dos clientes atendidos pela equipe. Seguimos esta ordem: primeiro não agendamos pessoas físicas, filiais, clientes com situação baixada na Receita Federal, inadimplentes ou clientes que compraram com o próprio vendedor nos últimos 30 dias.

Entre os demais, atendemos a cada 7 dias os clientes que nunca compraram com a empresa e foram cadastrados há 30 dias. Os outros que nunca compraram com a empresa são atendidos a cada 21 dias. Depois, os clientes que fizeram uma única compra com o próprio vendedor são atendidos a cada 7 dias.

Em seguida, para os clientes cuja última compra com qualquer vendedor da empresa não foi entre 30 e 45 dias atrás, atendemos a cada 14 dias os de curva A, considerando a empresa toda, e a cada 28 dias os de curva B, também considerando a empresa toda. Os demais nessa mesma situação são atendidos a cada 45 dias, sem exigência de curva.

Depois disso, atendemos a cada 28 dias quem não teve a última compra com qualquer vendedor da empresa entre 46 e 60 dias atrás e, em seguida, a cada 21 dias quem não teve essa última compra entre 61 e 90 dias atrás. Todo o resto é atendido a cada 14 dias. Quando um cliente se encaixa em mais de uma dessas situações, vale a primeira que aparecer nessa ordem.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-11-outros-filtros.md",
    "03-secoes/06-07-curva-abc-ciclo-de-vida.md"
  ],
  "sem_chave": []
}
