---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_237.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9341
tokens_saida: 433
custo_usd: 0.011506
tempo_segundos: 6.14
timestamp: 2026-11-14T20:04:47-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade: quem se encaixar em uma situação fica com aquele atendimento e não passa para as seguintes.

Clientes que ainda não compraram com seu vendedor são atendidos a cada 14 dias. Para quem comprou com seu vendedor nos últimos 30 dias e tem intervalo histórico entre compras menor que 30 dias, usamos esse intervalo histórico para o atendimento, com mínimo de 0 dias e máximo de 30 dias.

Quem comprou com seu vendedor entre 30 e 60 dias atrás é atendido a cada 14 dias. Depois, atendemos a cada 14 dias quem não comprou com seu vendedor nos últimos 60 dias e tem intervalo histórico entre compras maior que 30 dias. Os demais que não compraram com seu vendedor nos últimos 60 dias também são atendidos a cada 14 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/06-08-frequencia-e-parametros.md"
  ],
  "sem_chave": [
    "mínimo e máximo para frequência do histórico"
  ]
}
