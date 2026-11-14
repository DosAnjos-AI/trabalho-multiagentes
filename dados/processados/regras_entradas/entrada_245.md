---
regra_id: 245
arquivo_regra: regra_245.gobr
hash_regra_sha256: 6f64138b8f5115ef2f1a10bb4ae513fdf043429e5d3f980c5e08d0bb0f11ae97
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 4527
tokens_saida: 1494
custo_usd: 0.011997
tempo_segundos: 18.33
timestamp: 2026-11-13T19:49:39-03:00
---

Trabalhamos com os vendedores de televendas habilitados, cada um cuidando dos seus clientes fixos. Primeiro, não agendamos clientes inadimplentes, com situação baixada na Receita Federal, sem crédito ou que compraram com o próprio vendedor nos últimos 60 dias.

Para os demais, separamos os clientes pelas cidades das rotas abaixo. Um cliente pode estar em mais de uma rota; nesse caso, vale o primeiro atendimento aplicável na ordem em que apresentamos as rotas.

Na rota de todos os dias estão AMERICANA, ATIBAIA, BOM JESUS DOS PERDOES, CAMPINAS, HORTOLANDIA, INDAIATUBA, ITATIBA, ITU, JARINU, JUNDIAI, LOUVEIRA, NOVA ODESSA, PAULINIA, SALTO, SUMARE, VALINHOS, VINHEDO, PORANGABA e TAQUARITUBA. Para quem já recebeu visita do próprio vendedor na semana, usamos o intervalo de atendimento do histórico, com mínimo de 7 e máximo de 14 dias. Para os demais dessa rota, usamos o intervalo do histórico acrescido de 2 dias, com mínimo de 3 e máximo de 7 dias.

Nas outras rotas, o atendimento é a cada 7 dias, tanto para quem já recebeu visita do próprio vendedor na semana quanto para os demais. A preferência de dia depende da rota:

Na rota de terça, preferimos atender na segunda. Ela inclui ARTUR NOGUEIRA, CABREUVA, CAPIVARI, CONCHAL, COSMOPOLIS, ELIAS FAUSTO, ENGENHEIRO COELHO, ESTIVA GERBI, FRANCISCO MORATO, HOLAMBRA, ITUPEVA, JAGUARIUNA, MOGI GUACU, MOGI MIRIM, MONTE MOR, SANTO ANTONIO DE POSSE, CONCHAS, IBIUNA, ITAPETININGA, LEME, MAIRINQUE, MONTE ALEGRE DO SUL, PIRAJU, SOROCABA, VOTORANTIM, MAIRIPORA, NAZARE PAULISTA, SALTO DE PIRAPORA, PARANAPANEMA, BRAGANCA PAULISTA, PIRACAIA, LIMEIRA, PIRACICABA, RIO CLARO, RIO DAS PEDRAS, SANTA BARBARA DO OESTE, SANTA GERTRUDES, CORDEIROPOLIS e IRACEMAPOLIS.

Na rota de quarta, preferimos atender na terça. Ela inclui SOROCABA, VOTORANTIM, CAMPO LIMPO PAULISTA, ARACOIABA DA SERRA, SAO PEDRO, JOANOPOLIS, PINHALZINHO, VARGEM, AGUAS DE LINDOIA, AMPARO, ITAPIRA, LINDOIA, PEDREIRA, SERRA NEGRA, SOCORRO, BOITUVA, CERQUILHO, CESARIO LANGE, IPERO, LARANJAL PAULISTA, PORTO FELIZ, TATUI, TIETE, VARZEA PAULISTA, AGUAI, AGUAS DE SAO PEDRO, ARARAS, CAPELA DO ALTO, CERQUEIRA CESAR, ITAI, MANDURI, PIEDADE, PILAR DO SUL, BRAGANCA PAULISTA e PIRACAIA.

Na rota de quinta, preferimos atender na quarta. Ela inclui ARTUR NOGUEIRA, CABREUVA, CAPIVARI, CONCHAL, COSMOPOLIS, ELIAS FAUSTO, ENGENHEIRO COELHO, ESTIVA GERBI, FRANCISCO MORATO, HOLAMBRA, ITUPEVA, JAGUARIUNA, MOGI GUACU, MOGI MIRIM, MONTE MOR, SANTO ANTONIO DE POSSE, CONCHAS, IBIUNA, ITAPETININGA, LEME, MAIRINQUE, MONTE ALEGRE DO SUL, PIRAJU, BRAGANCA PAULISTA, PIRACAIA, ARANDU, AVARE, BOTUCATU, PEREIRAS, AGUAS DE SANTA BARBARA e ITATINGA.

Na rota de sexta, preferimos atender na quinta. Ela inclui SOROCABA, VOTORANTIM, MAIRIPORA, NAZARE PAULISTA, SALTO DE PIRAPORA, PARANAPANEMA, CAMPO LIMPO PAULISTA, ARACOIABA DA SERRA, SAO PEDRO, BOITUVA, CERQUILHO, CESARIO LANGE, IPERO, LARANJAL PAULISTA, PORTO FELIZ, TATUI, TIETE, VARZEA PAULISTA, AGUAI, AGUAS DE SAO PEDRO, ARARAS, CAPELA DO ALTO, CERQUEIRA CESAR, ITAI, MANDURI, PIEDADE, PILAR DO SUL, LIMEIRA, PIRACICABA, RIO CLARO, RIO DAS PEDRAS, SANTA BARBARA DO OESTE, SANTA GERTRUDES, CORDEIROPOLIS e IRACEMAPOLIS.

Na rota de segunda, preferimos atender na sexta. Ela inclui CAMPO LIMPO PAULISTA, ARACOIABA DA SERRA, SAO PEDRO, JOANOPOLIS, PINHALZINHO, VARGEM, AGUAS DE LINDOIA, AMPARO, ITAPIRA, LINDOIA, PEDREIRA, SERRA NEGRA, SOCORRO, MORUNGABA, BRAGANCA PAULISTA, PIRACAIA, AGUAS DE SANTA BARBARA e ITATINGA.

Para todo o resto dos clientes da equipe, se já receberam visita do próprio vendedor na semana, usamos o intervalo do histórico, com mínimo de 7 e máximo de 14 dias. Para os demais, usamos o intervalo do histórico menos 1 dia, com mínimo de 1 e máximo de 7 dias.
