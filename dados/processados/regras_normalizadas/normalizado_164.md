---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_164.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9722
tokens_saida: 941
custo_usd: 0.014427
tempo_segundos: 11.77
timestamp: 2026-11-14T19:56:02-03:00
---

## explicacao_normalizada
Trabalhamos com todos os vendedores habilitados no sistema e também com a vendedora de código 10bruna. Seguimos a ordem abaixo: quando um cliente se encaixa em mais de uma situação, fica com o primeiro atendimento previsto para ele.

Para a 10bruna, olhamos primeiro os clientes cujo rótulo contém condominio. Os cadastrados a partir de 03/10/2024 são atendidos a cada 14 dias. Depois, os que compraram com qualquer vendedor da empresa nos últimos 30 dias são atendidos a cada 7 dias. Os que não compraram com nenhum vendedor da empresa nos últimos 90 dias são atendidos a cada 30 dias.

Para todos os vendedores habilitados, começamos pelos clientes que ainda não compraram com o próprio vendedor e foram cadastrados a partir de 01/08/2024: atendimento a cada 7 dias, independentemente do rótulo.

Em seguida, para os clientes cujo rótulo contém construtora, atendemos a cada 14 dias os que fizeram uma única compra com a empresa e não compraram com o próprio vendedor nos últimos 60 dias. Para quem tem intervalo histórico entre compras com esse vendedor menor que 30 dias e não comprou com ele nos últimos 14 dias, atendemos em RJ a cada 7 dias se for curva A, a cada 10 dias se for curva B e a cada 14 dias se for curva C, considerando a curva na empresa toda. Os demais que cumprirem essas mesmas condições de intervalo e tempo sem compra com o vendedor são atendidos a cada 14 dias.

Ainda entre os clientes com construtora no rótulo, os ativos na empresa que não compraram com nenhum vendedor nos últimos 45 dias são atendidos a cada 10 dias. Depois, os que não compraram com o próprio vendedor nos últimos 60 dias são atendidos a cada 14 dias; os cadastrados a partir de 03/10/2024, a cada 7 dias; e os demais, a cada 45 dias.

Para os clientes cujo rótulo contém shopping, supermercado, industria, estaleiro, clube, escolas, universidade, igreja, hotel, hospital, clinica, restaurantes ou condominio, atendemos os cadastrados a partir de 03/10/2024 a cada 14 dias. Depois, os que compraram com qualquer vendedor da empresa nos últimos 30 dias são atendidos a cada 7 dias. Também está previsto atendimento a cada 30 dias para quem comprou com qualquer vendedor da empresa nos últimos 30 dias, mas essa mesma condição já é atendida antes, a cada 7 dias.

Os demais clientes dos vendedores habilitados não são agendados.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-11-outros-filtros.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-08-frequencia-e-parametros.md",
    "03-secoes/06-07-curva-abc-ciclo-de-vida.md"
  ],
  "sem_chave": []
}
