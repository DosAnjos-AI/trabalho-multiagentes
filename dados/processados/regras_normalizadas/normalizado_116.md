---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_116.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9325
tokens_saida: 524
custo_usd: 0.011945
tempo_segundos: 7.78
timestamp: 2026-11-14T16:25:29-03:00
---

## explicacao_normalizada
Trabalhamos com todos os vendedores de televendas e todos os vendedores de campo. Primeiro, não agendamos atendimento para clientes que são filiais, em nenhuma das duas equipes.

Para os demais clientes do televendas, o atendimento é a cada 7 dias, preferencialmente nos dias úteis e no sábado, sem coincidir com o atendimento da equipe de campo.

No campo, atendemos a cada 7 dias os clientes ativos para o vendedor e adimplentes, e a cada 14 dias os ativos para o vendedor e inadimplentes. Os inativos para o vendedor e adimplentes são atendidos a cada 30 dias, e os inativos para o vendedor e inadimplentes, a cada 60 dias. Os clientes sem vendas são atendidos a cada 7 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/07-02-preferencia-dia-semana.md",
    "03-secoes/07-04-conflito-pivot-rota.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-03-financeiros.md"
  ],
  "sem_chave": [
    "clientes sem vendas"
  ]
}
