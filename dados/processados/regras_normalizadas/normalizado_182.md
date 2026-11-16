---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_182.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9535
tokens_saida: 1023
custo_usd: 0.014650
tempo_segundos: 12.71
timestamp: 2026-11-14T19:58:27-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem os clientes da equipe. Primeiro, não agendamos pessoas físicas, clientes inadimplentes, clientes com situação baixada na Receita Federal ou clientes que compraram com o próprio vendedor nos últimos 7 dias.

Depois, atendemos a cada 7 dias os clientes que nunca compraram com a empresa e são dos ramos 089, 090, 091, 092, 093, 094, 095, 096, 097, 098, 099, 100, 101, 102 ou 103.

Para os demais clientes desses ramos, consideramos as compras feitas com o próprio vendedor. Quem comprou no prazo indicado recebe a primeira frequência; os demais daquele ramo recebem a segunda:

Nos ramos 089, 091, 093, 099 e 102, quem comprou nos últimos 45 dias é atendido a cada 14 dias; os demais, a cada 7 dias. Nos ramos 090, 097 e 098, quem comprou nos últimos 60 dias é atendido a cada 21 dias; os demais, a cada 10 dias. Nos ramos 092, 094, 101 e 103, quem comprou nos últimos 90 dias é atendido a cada 28 dias; os demais, a cada 14 dias.

No ramo 095, quem comprou nos últimos 75 dias é atendido a cada 21 dias; os demais, a cada 14 dias. No ramo 096, quem comprou nos últimos 75 dias é atendido a cada 28 dias; os demais, a cada 14 dias. No ramo 100, quem comprou nos últimos 75 dias é atendido a cada 28 dias; os demais, a cada 7 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-06-classificacao-por-id.md"
  ],
  "sem_chave": []
}
