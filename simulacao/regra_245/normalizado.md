---
id: regra_245
origem: simulacao/regra_245/entrada.md
gobr: simulacao/regra_245/regra_245.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 18
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente com cadastro baixado na Receita Federal não é agendado
cliente sem crédito não é agendado
cliente com compra nos últimos 60 dias não é agendado
cliente da rota de todo dia com atendimento ou venda na semana é agendado para a semana seguinte pelo histórico, entre 7 e 14 dias
cliente da rota de todo dia sem atendimento na semana é agendado na semana corrente pelo histórico acrescido de 2 dias, entre 3 e 7 dias
cliente da rota de terça com atendimento na semana é agendado semanalmente, a cada 7 dias, com preferência máxima na segunda
cliente da rota de terça sem atendimento na semana é agendado semanalmente, a cada 7 dias, com preferência máxima na segunda
cliente da rota de quarta com atendimento na semana é agendado semanalmente, a cada 7 dias, com preferência máxima na terça
cliente da rota de quarta sem atendimento na semana é agendado semanalmente, a cada 7 dias, com preferência máxima na terça
cliente da rota de quinta com atendimento na semana é agendado semanalmente, a cada 7 dias, com preferência máxima na quarta
cliente da rota de quinta sem atendimento na semana é agendado semanalmente, a cada 7 dias, com preferência máxima na quarta
cliente da rota de sexta com atendimento na semana é agendado semanalmente, a cada 7 dias, com preferência máxima na quinta
cliente da rota de sexta sem atendimento na semana é agendado semanalmente, a cada 7 dias, com preferência máxima na quinta
cliente da rota de segunda com atendimento na semana é agendado semanalmente, a cada 7 dias, com preferência máxima na sexta
cliente da rota de segunda sem atendimento na semana é agendado semanalmente, a cada 7 dias, com preferência máxima na sexta
cliente de cidade fora das rotas com atendimento na semana é agendado para a semana seguinte pelo histórico, entre 7 e 14 dias
cliente de cidade fora das rotas sem atendimento na semana é agendado na semana corrente pelo histórico menos 1 dia, entre 1 e 7 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar sem crédito
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: sem crédito}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar compra nos últimos 60 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Rota todo dia, com atendimento na semana
    publico: vendedores de televendas ativos, rota de todo dia
    se:
      - {tipo: localizacao, op: igual_a, valor: [Americana, Atibaia, Bom Jesus dos Perdões, Campinas, Hortolândia, Indaiatuba, Itatiba, Itu, Jarinu, Jundiaí, Louveira, Nova Odessa, Paulínia, Salto, Sumaré, Valinhos, Vinhedo, Porangaba, Taquarituba]}
      - {tipo: tempo_sem_visita, op: igual_a, valor: semana atual, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Rota todo dia, sem atendimento na semana
    publico: vendedores de televendas ativos, rota de todo dia
    se:
      - {tipo: localizacao, op: igual_a, valor: [Americana, Atibaia, Bom Jesus dos Perdões, Campinas, Hortolândia, Indaiatuba, Itatiba, Itu, Jarinu, Jundiaí, Louveira, Nova Odessa, Paulínia, Salto, Sumaré, Valinhos, Vinhedo, Porangaba, Taquarituba]}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Rota de terça, com atendimento na semana, agenda na segunda
    publico: vendedores de televendas ativos, rota de terça
    se:
      - {tipo: localizacao, op: igual_a, valor: [Artur Nogueira, Cabreúva, Capivari, Conchal, Cosmópolis, Elias Fausto, Engenheiro Coelho, Estiva Gerbi, Francisco Morato, Holambra, Itupeva, Jaguariúna, Mogi Guaçu, Mogi Mirim, Monte Mor, Santo Antônio de Posse, Conchas, Ibiúna, Itapetininga, Leme, Mairinque, Monte Alegre do Sul, Piraju, Sorocaba, Votorantim, Mairiporã, Nazaré Paulista, Salto de Pirapora, Paranapanema, Bragança Paulista, Piracaia, Limeira, Piracicaba, Rio Claro, Rio das Pedras, Santa Bárbara d'Oeste, Santa Gertrudes, Cordeirópolis, Iracemápolis]}
      - {tipo: tempo_sem_visita, op: igual_a, valor: semana atual, unidade: periodo_nomeado}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de terça, sem atendimento na semana, agenda na segunda
    publico: vendedores de televendas ativos, rota de terça
    se:
      - {tipo: localizacao, op: igual_a, valor: [Artur Nogueira, Cabreúva, Capivari, Conchal, Cosmópolis, Elias Fausto, Engenheiro Coelho, Estiva Gerbi, Francisco Morato, Holambra, Itupeva, Jaguariúna, Mogi Guaçu, Mogi Mirim, Monte Mor, Santo Antônio de Posse, Conchas, Ibiúna, Itapetininga, Leme, Mairinque, Monte Alegre do Sul, Piraju, Sorocaba, Votorantim, Mairiporã, Nazaré Paulista, Salto de Pirapora, Paranapanema, Bragança Paulista, Piracaia, Limeira, Piracicaba, Rio Claro, Rio das Pedras, Santa Bárbara d'Oeste, Santa Gertrudes, Cordeirópolis, Iracemápolis]}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de quarta, com atendimento na semana, agenda na terça
    publico: vendedores de televendas ativos, rota de quarta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Sorocaba, Votorantim, Campo Limpo Paulista, Araçoiaba da Serra, São Pedro, Joanópolis, Pinhalzinho, Vargem, Águas de Lindóia, Amparo, Itapira, Lindóia, Pedreira, Serra Negra, Socorro, Boituva, Cerquilho, Cesário Lange, Iperó, Laranjal Paulista, Porto Feliz, Tatuí, Tietê, Várzea Paulista, Aguaí, Águas de São Pedro, Araras, Capela do Alto, Cerqueira César, Itaí, Manduri, Piedade, Pilar do Sul, Bragança Paulista, Piracaia]}
      - {tipo: tempo_sem_visita, op: igual_a, valor: semana atual, unidade: periodo_nomeado}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de quarta, sem atendimento na semana, agenda na terça
    publico: vendedores de televendas ativos, rota de quarta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Sorocaba, Votorantim, Campo Limpo Paulista, Araçoiaba da Serra, São Pedro, Joanópolis, Pinhalzinho, Vargem, Águas de Lindóia, Amparo, Itapira, Lindóia, Pedreira, Serra Negra, Socorro, Boituva, Cerquilho, Cesário Lange, Iperó, Laranjal Paulista, Porto Feliz, Tatuí, Tietê, Várzea Paulista, Aguaí, Águas de São Pedro, Araras, Capela do Alto, Cerqueira César, Itaí, Manduri, Piedade, Pilar do Sul, Bragança Paulista, Piracaia]}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de quinta, com atendimento na semana, agenda na quarta
    publico: vendedores de televendas ativos, rota de quinta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Artur Nogueira, Cabreúva, Capivari, Conchal, Cosmópolis, Elias Fausto, Engenheiro Coelho, Estiva Gerbi, Francisco Morato, Holambra, Itupeva, Jaguariúna, Mogi Guaçu, Mogi Mirim, Monte Mor, Santo Antônio de Posse, Conchas, Ibiúna, Itapetininga, Leme, Mairinque, Monte Alegre do Sul, Piraju, Bragança Paulista, Piracaia, Arandu, Avaré, Botucatu, Pereiras, Águas de Santa Bárbara, Itatinga]}
      - {tipo: tempo_sem_visita, op: igual_a, valor: semana atual, unidade: periodo_nomeado}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de quinta, sem atendimento na semana, agenda na quarta
    publico: vendedores de televendas ativos, rota de quinta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Artur Nogueira, Cabreúva, Capivari, Conchal, Cosmópolis, Elias Fausto, Engenheiro Coelho, Estiva Gerbi, Francisco Morato, Holambra, Itupeva, Jaguariúna, Mogi Guaçu, Mogi Mirim, Monte Mor, Santo Antônio de Posse, Conchas, Ibiúna, Itapetininga, Leme, Mairinque, Monte Alegre do Sul, Piraju, Bragança Paulista, Piracaia, Arandu, Avaré, Botucatu, Pereiras, Águas de Santa Bárbara, Itatinga]}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de sexta, com atendimento na semana, agenda na quinta
    publico: vendedores de televendas ativos, rota de sexta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Sorocaba, Votorantim, Mairiporã, Nazaré Paulista, Salto de Pirapora, Paranapanema, Campo Limpo Paulista, Araçoiaba da Serra, São Pedro, Boituva, Cerquilho, Cesário Lange, Iperó, Laranjal Paulista, Porto Feliz, Tatuí, Tietê, Várzea Paulista, Aguaí, Águas de São Pedro, Araras, Capela do Alto, Cerqueira César, Itaí, Manduri, Piedade, Pilar do Sul, Limeira, Piracicaba, Rio Claro, Rio das Pedras, Santa Bárbara d'Oeste, Santa Gertrudes, Cordeirópolis, Iracemápolis]}
      - {tipo: tempo_sem_visita, op: igual_a, valor: semana atual, unidade: periodo_nomeado}
      - {tipo: periodo_vigencia, op: igual_a, valor: quinta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de sexta, sem atendimento na semana, agenda na quinta
    publico: vendedores de televendas ativos, rota de sexta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Sorocaba, Votorantim, Mairiporã, Nazaré Paulista, Salto de Pirapora, Paranapanema, Campo Limpo Paulista, Araçoiaba da Serra, São Pedro, Boituva, Cerquilho, Cesário Lange, Iperó, Laranjal Paulista, Porto Feliz, Tatuí, Tietê, Várzea Paulista, Aguaí, Águas de São Pedro, Araras, Capela do Alto, Cerqueira César, Itaí, Manduri, Piedade, Pilar do Sul, Limeira, Piracicaba, Rio Claro, Rio das Pedras, Santa Bárbara d'Oeste, Santa Gertrudes, Cordeirópolis, Iracemápolis]}
      - {tipo: periodo_vigencia, op: igual_a, valor: quinta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de segunda, com atendimento na semana, agenda na sexta
    publico: vendedores de televendas ativos, rota de segunda
    se:
      - {tipo: localizacao, op: igual_a, valor: [Campo Limpo Paulista, Araçoiaba da Serra, São Pedro, Joanópolis, Pinhalzinho, Vargem, Águas de Lindóia, Amparo, Itapira, Lindóia, Pedreira, Serra Negra, Socorro, Morungaba, Bragança Paulista, Piracaia, Águas de Santa Bárbara, Itatinga]}
      - {tipo: tempo_sem_visita, op: igual_a, valor: semana atual, unidade: periodo_nomeado}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de segunda, sem atendimento na semana, agenda na sexta
    publico: vendedores de televendas ativos, rota de segunda
    se:
      - {tipo: localizacao, op: igual_a, valor: [Campo Limpo Paulista, Araçoiaba da Serra, São Pedro, Joanópolis, Pinhalzinho, Vargem, Águas de Lindóia, Amparo, Itapira, Lindóia, Pedreira, Serra Negra, Socorro, Morungaba, Bragança Paulista, Piracaia, Águas de Santa Bárbara, Itatinga]}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Cidades fora das rotas, com atendimento na semana
    se:
      - {tipo: tempo_sem_visita, op: igual_a, valor: semana atual, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Cidades fora das rotas, sem atendimento na semana
    se: []
    entao: {acao: agendar, frequencia: calculada}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - carteira livre
  - frequência pelo histórico com acréscimo
  - frequência pelo histórico com redução
  - preferência máxima de dia
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| carteira livre | jargao | agrupamento de clientes por filtro, sem vínculo fixo |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| rota | jargao | roteiro de visitas programado |

## Lacunas

- A entrada não informa se as compras e os atendimentos consideram o vendedor ou a empresa.

## Ambiguidades

- A regra é declarada como em teste; não fica claro se é provisória.
- A descrição canônica resume as listas de cidades, que estão completas na representação estruturada.
- Algumas cidades, como Bragança Paulista, Piracaia, Sorocaba e Votorantim, aparecem em mais de uma rota.
- "Atendimento ou venda na semana" foi registrado como tempo_sem_visita na semana atual.
- Os limites e ajustes (mais 2 dias, menos 1 dia) da frequência pelo histórico foram registrados apenas na descrição.
- A preferência por dia da semana foi registrada como critério de período de vigência.
- O bloqueio de compra nos últimos 60 dias precede as regras de atendimento na semana, o que pode esvaziar as regras com atendimento ou venda recente.
