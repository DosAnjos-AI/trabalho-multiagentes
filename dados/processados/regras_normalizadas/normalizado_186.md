---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_186.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9426
tokens_saida: 1091
custo_usd: 0.014881
tempo_segundos: 13.41
timestamp: 2026-11-14T19:59:04-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade: quem se encaixar numa situação recebe aquele tratamento e não passa para as seguintes.

Primeiro, não agendamos clientes que compraram com o próprio vendedor nos últimos 7 dias nem os que têm rota prevista para os próximos 7 dias.

Depois, atendemos a cada 14 dias os clientes que nunca compraram com a empresa. Também atendemos nesse intervalo os que compraram com o próprio vendedor no ano passado e cuja última compra com ele foi entre 180 e 360 dias atrás. O mesmo intervalo vale para quem comprou com qualquer vendedor da empresa nos últimos 14 dias e também entre 181 e 360 dias atrás, mas não comprou com a empresa entre 15 e 180 dias atrás.

Atendemos a cada 7 dias os clientes cuja rota foi há 7 dias, que receberam visita da empresa na semana anterior e que compraram com qualquer vendedor da empresa entre 7 e 30 dias atrás ou entre 31 e 60 dias atrás. Também atendemos a cada 7 dias quem teve a última compra com qualquer vendedor da empresa entre 61 e 90 dias atrás ou entre 91 e 180 dias atrás.

Os demais clientes são atendidos a cada 28 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/06-11-outros-filtros.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md"
  ],
  "sem_chave": [
    "visita da empresa na semana anterior"
  ]
}
