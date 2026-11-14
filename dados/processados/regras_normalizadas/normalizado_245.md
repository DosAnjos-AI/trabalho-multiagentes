---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_245.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 10472
tokens_saida: 1634
custo_usd: 0.018642
tempo_segundos: 20.58
timestamp: 2026-11-14T20:05:46-03:00
---

## explicacao_normalizada
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

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-03-financeiros.md
03-secoes/06-05-localizacao-classificacao.md
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limites mínimo e máximo da frequência histórica
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/07-02-preferencia-dia-semana.md
