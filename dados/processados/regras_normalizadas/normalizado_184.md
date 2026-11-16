---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_184.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9507
tokens_saida: 698
custo_usd: 0.012997
tempo_segundos: 10.23
timestamp: 2026-11-14T19:58:44-03:00
---

## explicacao_normalizada
Trabalhamos com duas equipes: uma com os vendedores de televendas habilitados, exceto os de códigos 39, 11, 63, 8, 49, 31, 29 e 10; e outra formada pelos vendedores desses mesmos códigos, que chamamos de equipe de São Paulo.

Para o televendas, seguimos a ordem a seguir quando um cliente se encaixa em mais de uma situação. Quem fez uma única compra com a empresa e comprou com seu vendedor neste mês é atendido a cada 5 dias. Para quem comprou com seu vendedor entre 1 e 7 dias atrás, seguimos o intervalo do histórico, respeitando o mínimo de 1 e o máximo de 5 dias, com preferência por segunda e terça. Entre 7 e 14 dias, seguimos o histórico, com intervalo mínimo de 7 e máximo de 12 dias; entre 14 e 30 dias, também seguimos o histórico, com mínimo de 14 e máximo de 28 dias. Quem comprou com seu vendedor entre 31 e 90 dias atrás é atendido a cada 14 dias, assim como quem comprou entre 91 e 180 dias atrás. Quem não comprou com seu vendedor nos últimos 360 dias é atendido a cada 21 dias.

Para a equipe de São Paulo, quem tem histórico de atendimento a cada 7, 14, 28, 56 ou 84 dias continua sendo atendido, respectivamente, a cada 7, 14, 28, 56 ou 84 dias, em dias fixos e com maior preferência pela segunda-feira.

Os demais clientes das duas equipes são atendidos a cada 30 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/07-02-preferencia-dia-semana.md",
    "03-secoes/06-08-frequencia-e-parametros.md",
    "03-secoes/07-04-conflito-pivot-rota.md"
  ],
  "sem_chave": [
    "limites mínimo e máximo da frequência do histórico"
  ]
}
