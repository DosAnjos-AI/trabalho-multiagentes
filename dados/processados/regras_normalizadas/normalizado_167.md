---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_167.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9361
tokens_saida: 525
custo_usd: 0.011986
tempo_segundos: 7.09
timestamp: 2026-11-14T19:56:25-03:00
---

## explicacao_normalizada
Os vendedores habilitados do televendas cuidam dos seus clientes seguindo esta ordem de prioridade: quem estiver com a situação baixada na Receita Federal não deve ser agendado. Em seguida, atendemos a cada 7 dias os clientes que nunca compraram com a empresa e, a cada 15 dias, os que fizeram uma única compra com a empresa.

Para os demais, se a última compra com o próprio vendedor foi nos últimos 30 dias, usamos a frequência do histórico de atendimento, respeitando o mínimo de 7 e o máximo de 21 dias. Se a última compra com esse vendedor foi entre 31 e 90 dias atrás, atendemos a cada 28 dias; se foi entre 91 e 120 dias atrás, a cada 45 dias. Por fim, os que não tiveram venda da empresa nos últimos 120 dias são atendidos a cada 60 dias. Quem se encaixar em mais de uma situação recebe o tratamento da primeira que se aplicar.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md"
  ],
  "sem_chave": [
    "mínimo e máximo da frequência do histórico"
  ]
}
