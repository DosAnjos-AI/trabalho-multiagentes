---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_173.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9334
tokens_saida: 495
custo_usd: 0.011809
tempo_segundos: 6.79
timestamp: 2026-11-14T19:57:10-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem seus clientes. Primeiro, não agendamos os clientes com situação baixada na Receita Federal, os inadimplentes ou aqueles cuja data da rota cai na semana.

Para os demais, seguimos esta ordem: quem nunca comprou com a empresa é atendido a cada 14 dias. Depois, quem comprou com seu próprio vendedor nos últimos 60 dias é atendido a cada 14 dias; nos últimos 90 dias, a cada 7 dias; nos últimos 120 dias, a cada 14 dias; nos últimos 150 dias, a cada 21 dias; e nos últimos 180 dias, a cada 28 dias. Quando o cliente se encaixa em mais de uma dessas situações, vale a primeira em que ele se encaixar.

Todos os demais clientes não são agendados.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-03-financeiros.md",
    "03-secoes/06-11-outros-filtros.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-02-recencia-visita-positivacao.md"
  ],
  "sem_chave": []
}
