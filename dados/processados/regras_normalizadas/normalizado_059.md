---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_059.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9462
tokens_saida: 587
custo_usd: 0.012397
tempo_segundos: 7.88
timestamp: 2026-11-14T19:47:34-03:00
---

## explicacao_normalizada
Para os vendedores do televendas, primeiro não agendamos clientes cujo ramo de atividade seja diferente de 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15, 17, 18 e 19.

Depois, atendemos a cada 30 dias os clientes que nunca compraram com a empresa e são dos ramos 2, 7, 11, 12, 14 ou 19.

Entre os que ainda não receberam um tratamento, para os clientes ativos em relação ao vendedor que cuida deles, atendemos a cada 30 dias os dos ramos 3, 4, 6, 8, 15 ou 18; a cada 15 dias os dos ramos 7 ou 17; a cada 7 dias os dos ramos 10, 11, 14 ou 19; e a cada 5 dias os dos ramos 2 ou 12.

Para os demais, sem exigir que sejam inativos, atendemos a cada 30 dias os dos ramos 3, 4, 6, 8, 15 ou 18; a cada 20 dias os do ramo 17; a cada 15 dias os do ramo 10; e a cada 10 dias os dos ramos 11 ou 19. Todo o resto é atendido a cada 5 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-06-classificacao-por-id.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md"
  ],
  "sem_chave": []
}
