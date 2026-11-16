---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_217.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9240
tokens_saida: 406
custo_usd: 0.011270
tempo_segundos: 6.03
timestamp: 2026-11-14T20:02:36-03:00
---

## explicacao_normalizada
Os vendedores habilitados do televendas atendem seus clientes. Primeiro, quem fez uma única compra com o próprio vendedor deve ser atendido a cada 7 dias.

Entre os demais, para quem fez a última compra com seu vendedor entre 7 e 30 dias atrás, seguimos a frequência do histórico do cliente, com intervalo mínimo de 14 dias e máximo de 28 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md"
  ],
  "sem_chave": [
    "limites mínimo e máximo da frequência histórica"
  ]
}
