---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_076.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9350
tokens_saida: 538
custo_usd: 0.012040
tempo_segundos: 7.33
timestamp: 2026-11-14T19:49:02-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados no sistema atendem os clientes seguindo esta ordem de prioridade: primeiro, não agendamos os inadimplentes, os bloqueados, os inativos para a empresa nem os que compraram com qualquer vendedor da empresa nos últimos 20 dias.

Entre os demais, atendemos diariamente quem tem data de rota hoje. Depois, atendemos a cada 7 dias os clientes que nunca compraram com a empresa e, a cada 15 dias, os que fizeram uma única compra com a empresa.

Para quem comprou com qualquer vendedor da empresa nos últimos 30 dias e tem frequência histórica de compra menor que 30 dias, seguimos o intervalo histórico, respeitando o mínimo de 5 dias e o máximo de 30 dias. Quem comprou com qualquer vendedor da empresa entre 31 e 90 dias atrás é atendido a cada 15 dias. Todo o resto não é agendado.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-11-outros-filtros.md",
    "03-secoes/06-08-frequencia-e-parametros.md"
  ],
  "sem_chave": [
    "mínimo e máximo da frequência histórica"
  ]
}
