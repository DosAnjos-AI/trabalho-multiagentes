---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_132.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9309
tokens_saida: 617
custo_usd: 0.012394
tempo_segundos: 8.16
timestamp: 2026-11-14T19:52:32-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem seus clientes conforme a seguinte prioridade: primeiro, não agendamos os inadimplentes. Depois, atendemos a cada 7 dias os clientes que ainda não compraram com o próprio vendedor e os que fizeram uma única compra com ele.

Entre os que sobrarem, atendemos a cada 14 dias quem tem frequência histórica de compra menor que 11 dias. Em seguida, atendemos a cada 10 dias quem comprou com o próprio vendedor pela última vez entre 11 e 59 dias atrás, e a cada 7 dias quem comprou com ele pela última vez entre 60 e 89 dias atrás. Todos os demais são atendidos a cada 10 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-08-frequencia-e-parametros.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md"
  ],
  "sem_chave": []
}
