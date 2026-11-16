---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_140.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9442
tokens_saida: 810
custo_usd: 0.013492
tempo_segundos: 10.25
timestamp: 2026-11-14T21:03:16-03:00
---

## explicacao_normalizada
Os vendedores do televendas cuidam dos seus clientes fixos, separados pelas rotas de código 8, 9, 10 e 11; 3 e 4; 5; 6; e 7.

Primeiro, não agendamos clientes que sejam pessoas físicas, filiais ou inadimplentes, em toda a equipe. Também não agendamos, em nenhum desses grupos de rotas, quem recebeu visita de qualquer vendedor da empresa nos últimos 3 dias.

Para cada um desses grupos, atendemos semanalmente os clientes que ainda não compraram com seu próprio vendedor, os que compraram com ele nos últimos 21 dias, os que compraram com qualquer vendedor da empresa entre 21 e 41 dias atrás ou entre 41 e 90 dias atrás, e os que não compraram com nenhum vendedor da empresa nos últimos 90 dias.

Nas rotas 8, 9, 10 e 11, o atendimento é em dias variáveis, de segunda a sexta. Nas rotas 3 e 4, é fixo na segunda; na rota 5, na terça; na rota 6, na quarta; e na rota 7, na sexta.

Os demais clientes da equipe, inclusive os que não têm rota associada, também são atendidos semanalmente, desde que não estejam nas situações de não agendamento.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/06-06-classificacao-por-id.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-02-preferencia-dia-semana.md",
    "03-secoes/07-04-conflito-pivot-rota.md"
  ],
  "sem_chave": []
}
