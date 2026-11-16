---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_195.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9352
tokens_saida: 435
custo_usd: 0.011527
tempo_segundos: 6.31
timestamp: 2026-11-14T20:00:05-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem os clientes seguindo esta prioridade: primeiro, não agendamos pessoas físicas, clientes com situação baixada na Receita Federal ou clientes que compraram com qualquer vendedor da empresa nos últimos 7 dias.

Entre os demais, quem comprou com qualquer vendedor da empresa entre 7 e 30 dias atrás é atendido a cada 21 dias. Quem nunca comprou com a empresa é atendido a cada 14 dias; quem fez uma única compra com a empresa, a cada 21 dias.

Depois, considerando as compras feitas somente com o vendedor que cuida do cliente, atendemos a cada 21 dias quem comprou entre 31 e 60 dias atrás e a cada 7 dias quem comprou entre 61 e 90 dias atrás. Todo o resto é atendido a cada 14 dias. Se um cliente se encaixar em mais de uma dessas situações, vale a primeira.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md"
  ],
  "sem_chave": []
}
