---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_108.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9406
tokens_saida: 814
custo_usd: 0.013476
tempo_segundos: 10.41
timestamp: 2026-11-14T19:50:57-03:00
---

## explicacao_normalizada
No televendas, trabalhamos com todos os vendedores habilitados no sistema. Para os clientes deles, seguimos a ordem abaixo: quando um cliente se encaixa em mais de uma situação, vale a primeira.

Primeiro, não agendamos os clientes inadimplentes. Depois, atendemos a cada 7 dias quem nunca comprou com o próprio vendedor. Quem fez uma única compra com esse vendedor e é do ramo 37 é atendido a cada 21 dias; os demais que fizeram uma única compra com ele são atendidos a cada 7 dias.

Para quem tem frequência histórica de compra menor que 11 dias, o atendimento é a cada 7 dias. Depois, para os clientes do ramo 37 cuja última compra com o próprio vendedor foi entre 60 e 89 dias atrás, atendemos a cada 14 dias; se foi entre 11 e 59 dias atrás, atendemos a cada 21 dias.

Os clientes inativos em relação ao próprio vendedor são atendidos a cada 21 dias. Os que não compraram com esse vendedor nos últimos 90 dias são atendidos a cada 7 dias. Para todos os demais, o atendimento também é a cada 7 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-06-classificacao-por-id.md",
    "03-secoes/06-08-frequencia-e-parametros.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md"
  ],
  "sem_chave": []
}
