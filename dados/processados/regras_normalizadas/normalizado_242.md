---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_242.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9407
tokens_saida: 482
custo_usd: 0.011817
tempo_segundos: 6.57
timestamp: 2026-11-14T20:05:18-03:00
---

## explicacao_normalizada
A equipe é formada pelos vendedores de televendas habilitados no sistema. Para os clientes de cada vendedor, consideramos a frequência histórica das compras e o tempo desde a última compra com esse próprio vendedor. Seguimos a ordem abaixo: se o cliente se encaixar em mais de uma situação, vale a primeira.

Com frequência histórica de 0 a 30 dias e última compra entre 20 e 30 dias atrás, atendemos a cada 21 dias. Com frequência histórica de 31 a 60 dias, atendemos a cada 21 dias tanto quem comprou pela última vez entre 29 e 44 dias atrás quanto quem comprou entre 44 e 60 dias atrás.

Com frequência histórica de 61 a 90 dias, atendemos a cada 15 dias quem comprou pela última vez entre 61 e 90 dias atrás; quem comprou entre 90 e 180 dias atrás é atendido a cada 21 dias.

Com frequência histórica de 91 a 180 dias, atendemos a cada 21 dias quem comprou pela última vez entre 44 e 120 dias atrás; quem comprou entre 120 e 180 dias atrás é atendido a cada 15 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/06-08-frequencia-e-parametros.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/07-03-frequencia.md"
  ],
  "sem_chave": []
}
