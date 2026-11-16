---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_154.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9805
tokens_saida: 976
custo_usd: 0.014685
tempo_segundos: 12.56
timestamp: 2026-11-14T19:54:52-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem os clientes conforme a cidade e, para quem não entrar nessas rotas, conforme a situação de compra. Quando um cliente se encaixar em mais de uma situação, vale a primeira: consideramos primeiro as rotas e depois as demais condições.

O atendimento é semanal, em dia fixo, às segundas para BALNEARIO BARRA DO S, BELA VISTA, CAMPO ALEGRE, CANOINHAS, CORUPA, ITAIOPOLIS, MAFRA, MAJOR VIEIRA, MONTE CASTELO, PAPANDUVA, PORTO UNIAO, RIO NEGRINHO, SAO BENTO DO SUL e TRES BARRAS; às terças para APIUNA, ASCURRA, BENEDITO NOVO, BLUMENAU, DOUTOR PEDRINHO, GASPAR, IBIRAMA, INDAIAL, POMERODE, PRESIDENTE GETULIO, RIO DOS CEDROS e TIMBO; às quartas para ARARANGUA, BIGUACU, BRACO DO NORTE, CAPIVARI DE BAIXO, COCAL DO SUL, CRICIUMA, FLORIANOPOLIS, FORQUILHINHA, GRAVATAL, ICARA, IMBITUBA, JAGUARUMA, LAGUNA, LUIZ ALVES, MORRO DA FUMACA, ORLEANS, PALHOCA, PAULO LOPES, PEDRAS GRANDES, PESCARIA BRAVA, PRAIA GRANDE, SANGAO, SANTA ROSA DO SUL, SAO JOAO DO SUL, SAO JOSE, SAO LUDGERO, SOMBRIO, TUBARAO e URUSSANGA; e às quintas para ARAQUARI, MASSARANDUBA, PIRABEIRABA e SAO JOAO DO ITAPERIU.

Também atendemos semanalmente, com preferência por segunda, terça ou sexta em BRUSQUE; terça ou sexta em NOVA TRENTO; segunda ou quinta em GUARAMIRIM, JARAGUA DO SUL, JOINVILLE e SCHROEDER; e terça ou quinta em BARRA VELHA, NAVEGANTES, PENHA e BALNEARIO PICARRAS. Em BALNEARIO CAMBORIU, CAMBORIU, CANELINHA, ITAJAI, ITAPEMA, PORTO BELO, SAO JOAO BATISTA e TIJUCAS, o atendimento é semanal, em dias variados.

Para os clientes que não entraram nas rotas, atendemos a cada 30 dias quem nunca comprou com a empresa. Em seguida, atendemos a cada 14 dias os clientes ativos para seu vendedor que sejam curva A considerando a empresa toda, e a cada 21 dias os ativos para seu vendedor que sejam curva B considerando a empresa toda. Os demais clientes ativos para seu vendedor são atendidos a cada 28 dias. Todo o resto é atendido a cada 30 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/07-04-conflito-pivot-rota.md",
    "03-secoes/07-02-preferencia-dia-semana.md",
    "03-secoes/06-01-atividade-inatividade.md",
    "03-secoes/06-07-curva-abc-ciclo-de-vida.md"
  ],
  "sem_chave": []
}
