---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_101.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9387
tokens_saida: 444
custo_usd: 0.011607
tempo_segundos: 6.22
timestamp: 2026-11-14T19:50:27-03:00
---

## explicacao_normalizada
Dividimos o atendimento entre todos os vendedores de televendas, os vendedores de campo da capital e os do interior. Na capital ficam todos os vendedores de campo, exceto os de códigos 17, 18 e 13; no interior ficam os vendedores 17, 18 e 13.

No televendas, atendemos a cada 7 dias os clientes ativos para o próprio vendedor e os clientes sem venda. Os clientes inativos para o próprio vendedor são atendidos a cada 30 dias.

Na capital, atendemos a cada 7 dias os clientes ativos para o próprio vendedor. Os inativos para esse vendedor que estão em dia são atendidos a cada 14 dias, e os inadimplentes não são agendados. Os clientes sem venda são atendidos a cada 14 dias.

No interior, atendemos a cada 14 dias os clientes ativos para o próprio vendedor. Os inativos para esse vendedor que estão em dia são atendidos a cada 30 dias, e os inadimplentes não são agendados. Os clientes sem venda são atendidos a cada 30 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md"
  ],
  "sem_chave": [
    "clientes sem venda"
  ]
}
