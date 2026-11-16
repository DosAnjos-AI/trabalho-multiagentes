---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_142.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9517
tokens_saida: 711
custo_usd: 0.013072
tempo_segundos: 9.11
timestamp: 2026-11-14T19:53:25-03:00
---

## explicacao_normalizada
Trabalhamos com os vendedores habilitados no sistema, exceto os de código 10, 5 e 3, que têm atendimentos próprios: Yara, Lúcia e Wanderson, respectivamente. Em cada caso, seguimos a ordem abaixo; se um cliente se encaixar em mais de uma situação, vale a primeira.

Para os clientes da Yara, considerando a curva na empresa toda, atendemos os de curva A a cada 3 dias, os de curva B a cada 7 dias e os de curva C a cada 14 dias. Todos os demais são atendidos a cada 14 dias.

Para os clientes da Lúcia, também considerando a curva na empresa toda, atendemos os de curva A a cada 2 dias, os de curva B a cada 7 dias e os de curva C a cada 14 dias. Todos os demais são atendidos a cada 7 dias.

Para os clientes do Wanderson, considerando a curva na empresa toda, atendemos os de curva A a cada 4 dias, os de curva B a cada 7 dias e os de curva C a cada 9 dias. Todos os demais são atendidos a cada 14 dias.

Para os demais vendedores habilitados, primeiro não agendamos os clientes inadimplentes. Entre os que sobrarem, atendemos os dos ramos 001 e 002 a cada 14 dias, os do ramo 003 a cada 7 dias e os do ramo 004 a cada 21 dias. Não agendamos os dos ramos 005, 006 e 100. Depois disso, os clientes ativos para o próprio vendedor são atendidos a cada 7 dias, e todos os demais, a cada 15 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/06-07-curva-abc-ciclo-de-vida.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/06-06-classificacao-por-id.md",
    "03-secoes/06-01-atividade-inatividade.md"
  ],
  "sem_chave": []
}
