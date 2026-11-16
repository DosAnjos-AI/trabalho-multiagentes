---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_003.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9424
tokens_saida: 537
custo_usd: 0.012109
tempo_segundos: 8.51
timestamp: 2026-11-14T19:45:39-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados no sistema atendem os clientes seguindo esta ordem: quando um cliente se encaixar em mais de uma situação, vale a primeira.

Não agendamos filiais, clientes cuja última visita do representante tenha sido na semana anterior, clientes com rota programada para os próximos 7 dias nem clientes que compraram com qualquer vendedor da empresa nos últimos 7 dias.

Depois, atendemos a cada 14 dias os clientes que nunca compraram com a empresa e os que foram cadastrados há 60 dias e fizeram uma única compra com o vendedor responsável. Para os demais, considerando a última compra com qualquer vendedor da empresa, atendemos a cada 14 dias se ela ocorreu entre 7 e 30 dias atrás; a cada 7 dias se ocorreu entre 31 e 60 dias atrás; e a cada 3 dias se ocorreu entre 61 e 90 dias atrás.

Também atendemos a cada 14 dias quem comprou com qualquer vendedor da empresa nos últimos 14 dias e cuja última compra com qualquer vendedor da empresa não tenha ocorrido entre 15 e 90 dias atrás. Quem não comprou com nenhum vendedor da empresa nos últimos 90 dias também é atendido a cada 14 dias. Todo o resto é atendido a cada 21 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-11-outros-filtros.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md"
  ],
  "sem_chave": []
}
