---
regra_id: 135
arquivo_regra: regra_135.gobr
hash_regra_sha256: 99816a5a2a4d02eece749e28c749c846ec7b335304972ef0a83911065393212e
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 5342
tokens_saida: 1485
custo_usd: 0.012767
tempo_segundos: 17.50
timestamp: 2026-11-13T19:50:31-03:00
---

No televendas, separamos o vendedor 0000002 dos demais vendedores habilitados. Para o 0000002, dividimos os clientes fixos dele pelos grupos de cidades abaixo. Em cada grupo de segunda a sexta, atendemos semanalmente, com preferência pelo dia indicado. Seguimos esta ordem: primeiro os clientes que ainda não compraram com esse vendedor, depois os que compraram com ele nos últimos 30 dias, os que compraram com ele nos últimos 45 dias, os que não compraram com nenhum vendedor da empresa nos últimos 120 dias, os que não compraram com o próprio vendedor nos últimos 180 dias e, por fim, todos os demais do grupo.

O grupo de segunda tem preferência de atendimento na sexta e reúne AGUAS DE SAO PEDRO, AMERICANA, ARARAS, CHARQUEADA, CORDEIROPOLIS, Cordeirópolis, IPEUNA, IRACEMAPOLIS, Iracemápolis, PIRACICABA, RIO CLARO, RIO DAS PEDRAS, SANTA BARBARA D OESTE, SANTA BÁRBARA D'OESTE, SANTA GERTRUDES e SAO PEDRO.

O grupo de terça tem preferência na segunda e reúne AMERICO BRASILIENSE, ARARAQUARA, BARRINHA, CRAVINHOS, DESCALVADO, GUARIBA, IBATE, JABOTICABAL, LEME, MATAO, MONTE ALTO, PIRASSUNUNGA, PONTAL, PORTO FERREIRA, RIBEIRAO PRETO, SANTA CRUZ DAS PALMEIRAS, SANTA RITA DO PASSA QUATRO, SAO CARLOS, SERRANA, SERTAOZINHO e TAQUARITINGA.

O grupo de quarta tem preferência na terça e reúne AGUAI, AGUAS DE LINDOIA, AMPARO, ANDRADAS, ARTUR NOGUEIRA, ENGENHEIRO COELHO, ESPIRITO SANTO DO PINHAL, HOLAMBRA, ITAPIRA, JACUTINGA, JAGUARIUNA, LINDOIA, MOGI GUACU, MOGI MIRIM, MONTE ALEGRE DO SUL, MONTE SIAO, OURO FINO, PEDREIRA, PINHALZINHO, POCOS DE CALDAS, SAO JOAO DA BOA VISTA, SERRA NEGRA e SOCORRO.

O grupo de quinta tem preferência na quarta e reúne ALUMINIO, ARACOIABA DA SERRA, BOITUVA, CERQUILHO, COTIA, IBIUNA, INDAIATUBA, IPERO, ITAPETININGA, ITAPEVI, ITU, MAIRINQUE, MONTE MOR, PORTO FELIZ, SALTO, SAO ROQUE, SOROCABA, TATUI, TIETE, VARGEM GRANDE PAULISTA e VOTORANTIM.

O grupo de sexta tem preferência na quinta e reúne ATIBAIA, BRAGANCA PAULISTA, CAMPINAS, CAMPO LIMPO PAULISTA, COSMOPOLIS, HORTOLANDIA, ITATIBA, JUNDIAI, LOUVEIRA, NOVA ODESSA, PAULINIA, SUMARE, VALINHOS, VARZEA PAULISTA e VINHEDO.

Há outro grupo de clientes fixos do 0000002, nas cidades ARUJA, BARUERI, CAIEIRAS, CAJAMAR, CARAPICUIBA, DIADEMA, EMBU DAS ARTES, FERRAZ DE VASCONCELOS, FRANCISCO MORATO, FRANCO DA ROCHA, GUARULHOS, ITAQUAQUECETUBA, JANDIRA, MAIRIPORA, MAUA, MOGI DAS CRUZES, OSASCO, POA, RIBEIRAO PIRES, SANTANA DE PARNAIBA, SANTO ANDRE, SAO BERNARDO DO CAMPO, SAO CAETANO DO SUL, SAO PAULO e SUZANO. Nesse grupo, atendemos semanalmente quem ainda não comprou com o próprio vendedor; quem comprou com ele nos últimos 7 dias, a cada 7 dias; e quem comprou com ele nos últimos 45 dias, a cada 14 dias. Depois, para quem não comprou com nenhum vendedor da empresa nos últimos 120 dias, atendemos a cada 14 dias se estiver na curva A da empresa e a cada 30 dias se estiver na curva B ou C da empresa. Quem não comprou com o próprio vendedor nos últimos 180 dias é atendido a cada 21 dias. Essa é a ordem de prioridade quando o cliente se encaixa em mais de uma situação.

Para os clientes do 0000002 em SAO JOSE DO RIO PRETO, atendemos a cada 30 dias. Todos os demais clientes dele que não tiverem sido atendidos pelas situações anteriores também ficam com atendimento a cada 30 dias.

Para os demais vendedores habilitados do televendas, seguimos esta ordem: clientes que nunca compraram com a empresa são atendidos a cada 14 dias; os que compraram com o próprio vendedor nos últimos 7 dias, a cada 21 dias; nos últimos 30 dias, a cada 30 dias; nos últimos 60 dias, a cada 45 dias; nos últimos 90 dias, a cada 70 dias; e nos últimos 180 dias, a cada 15 dias. Todos os demais são atendidos a cada 21 dias.
