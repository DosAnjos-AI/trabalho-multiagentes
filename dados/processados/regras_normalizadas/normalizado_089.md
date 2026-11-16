---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_089.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9282
tokens_saida: 460
custo_usd: 0.011582
tempo_segundos: 6.33
timestamp: 2026-11-14T19:49:51-03:00
---

## explicacao_normalizada
Para os vendedores de televendas habilitados no sistema, atendemos primeiro os clientes que nunca compraram com a empresa a cada 7 dias. Em seguida, os clientes ativos para o próprio vendedor e adimplentes também são atendidos a cada 7 dias. Os demais clientes ativos para esse vendedor são atendidos a cada 14 dias.

Depois, os demais clientes adimplentes são atendidos a cada 7 dias, e todo o resto, a cada 14 dias. Quem já se encaixou em uma dessas situações segue o prazo indicado nela, sem passar para as seguintes.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md"
  ],
  "sem_chave": []
}
