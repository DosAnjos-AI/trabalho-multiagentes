---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_246.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9783
tokens_saida: 936
custo_usd: 0.014463
tempo_segundos: 11.66
timestamp: 2026-11-14T20:05:57-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem seus respectivos clientes fixos. Dividimos esses clientes em quatro grupos pelos códigos de ramo de atividade do cadastro. Os grupos são independentes: se um cliente atender aos critérios de mais de um, ele pode aparecer em mais de um grupo.

Primeiro, não agendamos os clientes cuja situação na Receita Federal é baixada. Depois, atendemos a cada 7 dias os clientes que nunca compraram com a empresa. Para os demais, seguimos os grupos abaixo; em cada grupo, verificamos primeiro a compra recente e aplicamos a outra frequência aos que sobrarem.

Para os ramos 101009, 101016, 101025, 101101, 101102, 101103, 101104, 101105, 201008, 201009, 201018 e 201099, quem comprou com qualquer vendedor da empresa nos últimos 45 dias é atendido a cada 14 dias; os demais, a cada 7 dias.

Para os ramos 101001, 101002, 101003, 101004, 101005, 101006, 101007, 101011, 101012, 101014, 101015, 101027, 101028, 101029, 101032, 101035, 101037, 101039, 101106, 101107, 201012, 201016, 301001, 301004, 301007 e 301015, quem comprou com qualquer vendedor da empresa nos últimos 60 dias é atendido a cada 21 dias; os demais, a cada 10 dias.

Para os ramos 101008, 101010, 101017, 101018, 101019, 101020, 101021, 101022, 101023, 101024, 101026, 101031, 101033, 101034, 101036, 101038, 201003, 201004, 201010, 201013, 201014, 201015, 201019, 201022, 201023, 301002, 301005, 301006, 301009, 301010, 301011, 301012, 301013 e 301014, quem comprou com qualquer vendedor da empresa nos últimos 75 dias é atendido a cada 28 dias; os demais, a cada 14 dias.

Para os ramos 101013, 101040, 102001, 102002, 201011, 201021, 201025 e 999999, quem comprou com qualquer vendedor da empresa nos últimos 90 dias é atendido a cada 28 dias; os demais, a cada 14 dias.

Se um cliente se encaixar em mais de uma dessas situações, vale a primeira na ordem apresentada. Todo o resto dos clientes do televendas não deve ser agendado.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/06-06-classificacao-por-id.md",
    "03-secoes/04-01-carteiras-e-segmentacoes.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md"
  ],
  "sem_chave": []
}
