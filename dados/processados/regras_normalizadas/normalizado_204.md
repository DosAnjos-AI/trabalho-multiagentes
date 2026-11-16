---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_204.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9268
tokens_saida: 383
custo_usd: 0.011183
tempo_segundos: 5.54
timestamp: 2026-11-14T20:01:13-03:00
---

## explicacao_normalizada
Os vendedores habilitados do televendas atendem seus clientes considerando as compras feitas com o próprio vendedor de cada cliente. Primeiro, quem comprou nos últimos 7 dias não deve ser agendado.

Entre os demais, quem comprou nos últimos 30 dias ou entre 31 e 60 dias deve ser atendido a cada 14 dias. Quem comprou entre 61 e 90 dias deve ser atendido a cada 7 dias. Para todos os outros clientes, o atendimento será a cada 21 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/07-03-frequencia.md"
  ],
  "sem_chave": []
}
