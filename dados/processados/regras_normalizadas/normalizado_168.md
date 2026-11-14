---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_168.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 10036
tokens_saida: 1254
custo_usd: 0.016306
tempo_segundos: 15.97
timestamp: 2026-11-14T19:56:41-03:00
---

## explicacao_normalizada
Trabalhamos com os vendedores de televendas habilitados e os clientes fixos de cada um. Primeiro, não agendamos clientes com situação baixada na Receita Federal nem clientes bloqueados.

Para os demais, separamos as cidades por rota. Uma cidade pode estar em mais de um grupo; quando um cliente se encaixar em mais de uma situação no mesmo dia, vale a primeira na ordem abaixo. Os atendimentos desses grupos são diários, fixos e podem ser roteirizados.

Para BALNEARIO CAMBORIU, BOMBINHAS, CAMBORIU, ITAJAI, ITAPEMA e PORTO BELO, damos maior preferência à segunda, terça, quarta, quinta e sexta.

Na rota de terça, atendemos na segunda, com maior preferência nesse dia. As cidades são CASCAVEL, LAGES, BOM RETIRO, SAO JOAQUIM, BIGUACU, BLUMENAU, BRUSQUE, FLORIANOPOLIS, GOVERNADOR CELSO RAMOS, GUABIRUBA, IBIRAMA, PALHOCA, POMERODE, RIO DO SUL, SAO JOSE, TIJUCAS, LUIZ ALVES, GASPAR, INDAIAL, BOTUVERA, ILHOTA e RIO DOS CEDROS.

Na rota de quarta, atendemos na terça, com maior preferência nesse dia. As cidades são IRATI, PONTA GROSSA, FERNANDES PINHEIRO, TEIXEIRA SOARES, ARAUCARIA, CURITIBA, SAO JOSE DOS PINHAIS, PIRAQUARA, COLOMBO, PINHAIS, CAMPO LARGO, JARAGUA DO SUL, BALNEARIO BARRA DO SUL, BALNEARIO PICARRAS, CAMPO ALEGRE, JOINVILLE, NAVEGANTES, PENHA, POUSO REDONDO, CORUPA, GUARAMIRIM, SAO BENTO DO SUL, BARRA VELHA, SCHROEDER, REBOUÇAS e RIO AZUL.

Na rota de quinta, atendemos na quarta, com maior preferência nesse dia. As cidades são BENTO GONCALVES, CACHOEIRINHA, CAMPO BOM, CANOAS, CAPAO DA CANOA, CAXIAS DO SUL, GRAMADO, NOVO HAMBURGO, PORTO ALEGRE, TORRES, TRES COROAS, XANGRI LA, BIGUACU, BLUMENAU, COCAL DO SUL, CRICIUMA, BRUSQUE, FORQUILHINHAS, GAROPABA, FLORIANOPOLIS, GOVERNADOR CELSO RAMOS, GUABIRUBA, IMBITUBA, IBIRAMA, PALHOCA, JAGUARUNA, LAGUNA, POMERODE, RIO DO SUL, SAO JOSE, PRAIA GRANDE, TIJUCAS, LUIZ ALVES, GASPAR, TUBARAO, INDAIAL, BOTUVERA, ILHOTA e RIO DOS CEDROS.

Na rota de sexta, atendemos na quinta, com maior preferência nesse dia. As cidades são GUARATUBA, MATINHOS, ITAPOA, MORRETES, PARANAGUA, ARAUCARIA, CURITIBA, SAO JOSE DOS PINHAIS, PIRAQUARA, COLOMBO, PINHAIS, CAMPO LARGO, BALNEARIO BARRA DO SUL, BALNEARIO PICARRAS, CAMPO ALEGRE, JOINVILLE, SAO FRANCISCO DO SUL, NAVEGANTES, PENHA, POUSO REDONDO, CORUPA, GUARAMIRIM, SAO BENTO DO SUL, BARRA VELHA, SCHROEDER, BIGUACU, FLORIANOPOLIS, GOVERNADOR CELSO RAMOS, PALHOCA, SAO JOSE e TIJUCAS.

Os demais clientes que não se encaixarem nessas situações no dia não são agendados.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/06-05-localizacao-classificacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/07-04-conflito-pivot-rota.md#Roteirização e fixação
03-secoes/07-02-preferencia-dia-semana.md
