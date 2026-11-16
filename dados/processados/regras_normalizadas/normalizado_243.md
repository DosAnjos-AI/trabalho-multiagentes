---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_243.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9300
tokens_saida: 565
custo_usd: 0.012125
tempo_segundos: 7.72
timestamp: 2026-11-14T16:26:29-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade: pessoas jurídicas que ainda não compraram com o próprio vendedor são atendidas a cada 21 dias. As que compraram com ele nos últimos 20 dias são atendidas a cada 3 dias.

Para as pessoas jurídicas cuja última compra com o próprio vendedor foi entre 20 e 33 dias atrás, usamos o intervalo do histórico do cliente acrescido de 2 dias, respeitando o mínimo de 20 dias e o máximo de 33 dias. Nesses atendimentos, preferimos dias úteis e sábado.

As demais pessoas jurídicas não são agendadas, assim como todos os outros clientes.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/07-02-preferencia-dia-semana.md"
  ],
  "sem_chave": [
    "mínimo e máximo na frequência do histórico"
  ]
}
