---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_190.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9414
tokens_saida: 581
custo_usd: 0.012319
tempo_segundos: 7.86
timestamp: 2026-11-14T19:59:38-03:00
---

## explicacao_normalizada
O atendimento é feito pelos vendedores habilitados do Televendas. Seguimos esta ordem: se um cliente se encaixar em mais de uma situação, vale a primeira.

Atendemos a cada 21 dias quem nunca comprou da empresa. Depois, quem fez uma única compra com a empresa e está cadastrado há 30 dias é atendido a cada 10 dias. Para os clientes em dia com os pagamentos cuja última compra com o próprio vendedor foi entre 61 e 90 dias atrás, o atendimento é a cada 7 dias. Os demais clientes em dia com os pagamentos e inativos para a empresa são atendidos a cada 14 dias.

Para quem tem curva A considerando a empresa toda e teve venda no mês, seguimos o intervalo do histórico, limitado a 30 dias. Os demais de curva A são atendidos a cada 7 dias. Para quem tem curva B considerando a empresa toda e teve venda no mês, também seguimos o histórico, limitado a 30 dias; os demais de curva B são atendidos a cada 14 dias.

Entre os clientes que sobrarem, quem teve venda no mês é atendido conforme o histórico, limitado a 30 dias. Todo o resto é atendido a cada 21 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-11-outros-filtros.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-07-curva-abc-ciclo-de-vida.md"
  ],
  "sem_chave": [
    "limite da frequência do histórico"
  ]
}
