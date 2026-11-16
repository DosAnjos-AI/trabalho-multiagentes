---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_205.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9701
tokens_saida: 831
custo_usd: 0.013856
tempo_segundos: 11.53
timestamp: 2026-11-14T20:01:24-03:00
---

## explicacao_normalizada
Trabalhamos com os vendedores de televendas habilitados e com os clientes fixos de cada um. Primeiro, atendemos a cada 28 dias os clientes que ainda não compraram com o próprio vendedor. Depois, entre os demais, atendemos a cada 14 dias aqueles que não compraram com seu vendedor nos últimos 90 dias.

Para os demais clientes, organizamos o atendimento por cidade, uma vez por semana, com preferência pelos dias indicados. Um cliente pode fazer parte de mais de um grupo de cidades; nesse caso, seguimos a primeira preferência indicada abaixo.

Para PONTA GROSSA, a preferência é quinta ou segunda. Para ARAPOTI, GUAMIRANGA, IMBITUVA, IPIRANGA, ITARARe, IVAI, JAGUARIAIVA, PIRAI DO SUL, PRUDENTOPOLIS, SENGES, WENCESLAU BRAZ e SANTO ANTONIO DA PLATINA, a preferência é terça.

Para CACADOR, CANDIDO DE ABREU, CANOINHAS, IMBAU, LAPA, ORTIGUEIRA, PORTO AMAZONAS, PORTO UNIAO, RESERVA, SAO JOAO DO TRIUNFO, SAO MATEUS DO SUL, TELEMACO BORBA, TIBAGI, TRES BARRAS, UNIAO DA VITORIA e VENTANIA, a preferência é quarta.

Para CARAMBEI, CASTRO, CURITIBA, GUARAPUAVA, IMBITUVA, IPIRANGA, IRATI, IVAI, PALMEIRA, PITANGA, PRUDENTOPOLIS, REBOUCAS, RIO AZUL, TEIXEIRA SOARES, TURVO, ADRINOPOLIS, AGUDOS DO SUL, ALMIRANTE TAMANDARE, ARAUCARIA, BALSA NOVA, BOCAIUVA DO SUL, CAMPINA GRANDE DO SUL, CAMPO DO TENENTE, CAMPO LARGO, CAMPO MAGRO, CERRO AZUL, COLOMBO, CONTENDA, DOUTOR ULYSSES, FAZENDA RIO GRANDE, ITAPERUCU, LAPA, MANDIRITUBA, PIEN, PINHAIS, PIRAQUARA, QUATRO BARRAS, RIO BRANCO DO SUL, RIO NEGRO, SAO JOSE DOS PINHAIS, QUITANDINHA, TIJUCAS DO SUL e TUNAS DO PARANA, a preferência é sexta.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/07-02-preferencia-dia-semana.md"
  ],
  "sem_chave": []
}
