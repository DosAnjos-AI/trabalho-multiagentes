---
regra_id: 168
arquivo_regra: regra_168.gobr
hash_regra_sha256: 588f2199f9fde1bae53b09c41254597cb8fa8372455de57c4d31bb599f1abb95
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3506
tokens_saida: 1184
custo_usd: 0.009426
tempo_segundos: 14.07
timestamp: 2026-11-13T19:42:29-03:00
---

Trabalhamos com os vendedores de televendas habilitados e os clientes fixos de cada um. Primeiro, não agendamos clientes com situação baixada na Receita Federal nem clientes bloqueados.

Para os demais, separamos as cidades por rota. Uma cidade pode estar em mais de um grupo; quando um cliente se encaixar em mais de uma situação no mesmo dia, vale a primeira na ordem abaixo. Os atendimentos desses grupos são diários, fixos e podem ser roteirizados.

Para BALNEARIO CAMBORIU, BOMBINHAS, CAMBORIU, ITAJAI, ITAPEMA e PORTO BELO, damos maior preferência à segunda, terça, quarta, quinta e sexta.

Na rota de terça, atendemos na segunda, com maior preferência nesse dia. As cidades são CASCAVEL, LAGES, BOM RETIRO, SAO JOAQUIM, BIGUACU, BLUMENAU, BRUSQUE, FLORIANOPOLIS, GOVERNADOR CELSO RAMOS, GUABIRUBA, IBIRAMA, PALHOCA, POMERODE, RIO DO SUL, SAO JOSE, TIJUCAS, LUIZ ALVES, GASPAR, INDAIAL, BOTUVERA, ILHOTA e RIO DOS CEDROS.

Na rota de quarta, atendemos na terça, com maior preferência nesse dia. As cidades são IRATI, PONTA GROSSA, FERNANDES PINHEIRO, TEIXEIRA SOARES, ARAUCARIA, CURITIBA, SAO JOSE DOS PINHAIS, PIRAQUARA, COLOMBO, PINHAIS, CAMPO LARGO, JARAGUA DO SUL, BALNEARIO BARRA DO SUL, BALNEARIO PICARRAS, CAMPO ALEGRE, JOINVILLE, NAVEGANTES, PENHA, POUSO REDONDO, CORUPA, GUARAMIRIM, SAO BENTO DO SUL, BARRA VELHA, SCHROEDER, REBOUÇAS e RIO AZUL.

Na rota de quinta, atendemos na quarta, com maior preferência nesse dia. As cidades são BENTO GONCALVES, CACHOEIRINHA, CAMPO BOM, CANOAS, CAPAO DA CANOA, CAXIAS DO SUL, GRAMADO, NOVO HAMBURGO, PORTO ALEGRE, TORRES, TRES COROAS, XANGRI LA, BIGUACU, BLUMENAU, COCAL DO SUL, CRICIUMA, BRUSQUE, FORQUILHINHAS, GAROPABA, FLORIANOPOLIS, GOVERNADOR CELSO RAMOS, GUABIRUBA, IMBITUBA, IBIRAMA, PALHOCA, JAGUARUNA, LAGUNA, POMERODE, RIO DO SUL, SAO JOSE, PRAIA GRANDE, TIJUCAS, LUIZ ALVES, GASPAR, TUBARAO, INDAIAL, BOTUVERA, ILHOTA e RIO DOS CEDROS.

Na rota de sexta, atendemos na quinta, com maior preferência nesse dia. As cidades são GUARATUBA, MATINHOS, ITAPOA, MORRETES, PARANAGUA, ARAUCARIA, CURITIBA, SAO JOSE DOS PINHAIS, PIRAQUARA, COLOMBO, PINHAIS, CAMPO LARGO, BALNEARIO BARRA DO SUL, BALNEARIO PICARRAS, CAMPO ALEGRE, JOINVILLE, SAO FRANCISCO DO SUL, NAVEGANTES, PENHA, POUSO REDONDO, CORUPA, GUARAMIRIM, SAO BENTO DO SUL, BARRA VELHA, SCHROEDER, BIGUACU, FLORIANOPOLIS, GOVERNADOR CELSO RAMOS, PALHOCA, SAO JOSE e TIJUCAS.

Os demais clientes que não se encaixarem nessas situações no dia não são agendados.
