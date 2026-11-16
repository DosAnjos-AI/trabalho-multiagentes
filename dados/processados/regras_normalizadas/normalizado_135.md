---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_135.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 10359
tokens_saida: 1481
custo_usd: 0.017764
tempo_segundos: 18.17
timestamp: 2026-11-14T21:03:06-03:00
---

## explicacao_normalizada
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

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/07-02-preferencia-dia-semana.md",
    "03-secoes/06-07-curva-abc-ciclo-de-vida.md"
  ],
  "sem_chave": []
}
