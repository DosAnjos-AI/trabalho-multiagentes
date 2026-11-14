---
regra_id: 135
arquivo_regra: regra_135.gobr
hash_regra_sha256: 5b4753c1c7efa169497b46538fdbc5d3f9edb51bca6ec3467eff1322ec60c642
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 5342
tokens_saida: 1717
custo_usd: 0.013927
tempo_segundos: 21.79
timestamp: 2026-11-14T20:55:41-03:00
---

No televendas, separamos o vendedor 0000002 dos demais vendedores habilitados. Para o 0000002, consideramos seus clientes fixos e os dividimos pelas cidades do cadastro.

Na rota de segunda estão AGUAS DE SAO PEDRO, AMERICANA, ARARAS, CHARQUEADA, CORDEIROPOLIS, Cordeirópolis, IPEUNA, IRACEMAPOLIS, Iracemápolis, PIRACICABA, RIO CLARO, RIO DAS PEDRAS, SANTA BARBARA D OESTE, SANTA BÁRBARA D'OESTE, SANTA GERTRUDES e SAO PEDRO.

Na rota de terça estão AMERICO BRASILIENSE, ARARAQUARA, BARRINHA, CRAVINHOS, DESCALVADO, GUARIBA, IBATE, JABOTICABAL, LEME, MATAO, MONTE ALTO, PIRASSUNUNGA, PONTAL, PORTO FERREIRA, RIBEIRAO PRETO, SANTA CRUZ DAS PALMEIRAS, SANTA RITA DO PASSA QUATRO, SAO CARLOS, SERRANA, SERTAOZINHO e TAQUARITINGA.

Na rota de quarta estão AGUAI, AGUAS DE LINDOIA, AMPARO, ANDRADAS, ARTUR NOGUEIRA, ENGENHEIRO COELHO, ESPIRITO SANTO DO PINHAL, HOLAMBRA, ITAPIRA, JACUTINGA, JAGUARIUNA, LINDOIA, MOGI GUACU, MOGI MIRIM, MONTE ALEGRE DO SUL, MONTE SIAO, OURO FINO, PEDREIRA, PINHALZINHO, POCOS DE CALDAS, SAO JOAO DA BOA VISTA, SERRA NEGRA e SOCORRO.

Na rota de quinta estão ALUMINIO, ARACOIABA DA SERRA, BOITUVA, CERQUILHO, COTIA, IBIUNA, INDAIATUBA, IPERO, ITAPETININGA, ITAPEVI, ITU, MAIRINQUE, MONTE MOR, PORTO FELIZ, SALTO, SAO ROQUE, SOROCABA, TATUI, TIETE, VARGEM GRANDE PAULISTA e VOTORANTIM.

Na rota de sexta estão ATIBAIA, BRAGANCA PAULISTA, CAMPINAS, CAMPO LIMPO PAULISTA, COSMOPOLIS, HORTOLANDIA, ITATIBA, JUNDIAI, LOUVEIRA, NOVA ODESSA, PAULINIA, SUMARE, VALINHOS, VARZEA PAULISTA e VINHEDO.

Também temos o grupo sem preferência de dia, com ARUJA, BARUERI, CAIEIRAS, CAJAMAR, CARAPICUIBA, DIADEMA, EMBU DAS ARTES, FERRAZ DE VASCONCELOS, FRANCISCO MORATO, FRANCO DA ROCHA, GUARULHOS, ITAQUAQUECETUBA, JANDIRA, MAIRIPORA, MAUA, MOGI DAS CRUZES, OSASCO, POA, RIBEIRAO PIRES, SANTANA DE PARNAIBA, SANTO ANDRE, SAO BERNARDO DO CAMPO, SAO CAETANO DO SUL, SAO PAULO e SUZANO.

Nas cinco rotas com dia definido, atendemos semanalmente: os prospects que ainda não compraram com o vendedor, os que compraram com ele nos últimos 30 dias, os que compraram com ele nos últimos 45 dias, os que não compraram com nenhum vendedor da empresa nos últimos 120 dias, os que não compraram com o vendedor nos últimos 180 dias e todos os demais. A preferência de atendimento é sexta-feira para a rota de segunda, segunda-feira para a de terça, terça-feira para a de quarta, quarta-feira para a de quinta e quinta-feira para a de sexta.

Para o grupo sem preferência de dia, seguimos esta prioridade: prospects que ainda não compraram com o vendedor são atendidos semanalmente; quem comprou com ele nos últimos 7 dias, a cada 7 dias; e quem comprou com ele nos últimos 45 dias, a cada 14 dias. Depois, para quem não comprou com nenhum vendedor da empresa nos últimos 120 dias, atendemos a cada 14 dias se for curva A e a cada 30 dias se for curva B ou C, considerando a curva da empresa toda. Quem não comprou com o vendedor nos últimos 180 dias é atendido a cada 21 dias.

Para os clientes do 0000002 em SAO JOSE DO RIO PRETO, o atendimento é a cada 30 dias. Todos os demais clientes dele que não tenham recebido um dos tratamentos anteriores também são atendidos a cada 30 dias.

Para os outros vendedores habilitados do televendas, atendemos primeiro quem nunca comprou com a empresa, a cada 14 dias. Depois, conforme a compra com o próprio vendedor, atendemos quem comprou nos últimos 7 dias a cada 21 dias; nos últimos 30 dias, a cada 30 dias; nos últimos 60 dias, a cada 45 dias; nos últimos 90 dias, a cada 70 dias; e nos últimos 180 dias, a cada 15 dias. Quem se encaixar em mais de uma dessas situações fica com o primeiro tratamento, e todo o resto é atendido a cada 21 dias.
