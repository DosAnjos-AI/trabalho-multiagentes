---
id: regra_135
origem: simulacao/regra_135/entrada.md
gobr: simulacao/regra_135/regra_135.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 46
procedencia: corpus_sintetico
---

## Regras

prospect com o vendedor na rota de segunda é atendido semanalmente, agendado na sexta
cliente com compra do vendedor em 30 dias na rota de segunda é atendido semanalmente, agendado na sexta
cliente com compra do vendedor em 45 dias na rota de segunda é atendido semanalmente, agendado na sexta
cliente sem compra com qualquer vendedor há mais de 120 dias na rota de segunda é atendido semanalmente, agendado na sexta
cliente sem compra há mais de 180 dias na rota de segunda é atendido semanalmente, agendado na sexta
o restante da rota de segunda é atendido semanalmente, agendado na sexta
prospect com o vendedor na rota de terça é atendido semanalmente, agendado na segunda
cliente com compra do vendedor em 30 dias na rota de terça é atendido semanalmente, agendado na segunda
cliente com compra do vendedor em 45 dias na rota de terça é atendido semanalmente, agendado na segunda
cliente sem compra com qualquer vendedor há mais de 120 dias na rota de terça é atendido semanalmente, agendado na segunda
cliente sem compra há mais de 180 dias na rota de terça é atendido semanalmente, agendado na segunda
o restante da rota de terça é atendido semanalmente, agendado na segunda
prospect com o vendedor na rota de quarta é atendido semanalmente, agendado na terça
cliente com compra do vendedor em 30 dias na rota de quarta é atendido semanalmente, agendado na terça
cliente com compra do vendedor em 45 dias na rota de quarta é atendido semanalmente, agendado na terça
cliente sem compra com qualquer vendedor há mais de 120 dias na rota de quarta é atendido semanalmente, agendado na terça
cliente sem compra há mais de 180 dias na rota de quarta é atendido semanalmente, agendado na terça
o restante da rota de quarta é atendido semanalmente, agendado na terça
prospect com o vendedor na rota de quinta é atendido semanalmente, agendado na quarta
cliente com compra do vendedor em 30 dias na rota de quinta é atendido semanalmente, agendado na quarta
cliente com compra do vendedor em 45 dias na rota de quinta é atendido semanalmente, agendado na quarta
cliente sem compra com qualquer vendedor há mais de 120 dias na rota de quinta é atendido semanalmente, agendado na quarta
cliente sem compra há mais de 180 dias na rota de quinta é atendido semanalmente, agendado na quarta
o restante da rota de quinta é atendido semanalmente, agendado na quarta
prospect com o vendedor na rota de sexta é atendido semanalmente, agendado na quinta
cliente com compra do vendedor em 30 dias na rota de sexta é atendido semanalmente, agendado na quinta
cliente com compra do vendedor em 45 dias na rota de sexta é atendido semanalmente, agendado na quinta
cliente sem compra com qualquer vendedor há mais de 120 dias na rota de sexta é atendido semanalmente, agendado na quinta
cliente sem compra há mais de 180 dias na rota de sexta é atendido semanalmente, agendado na quinta
o restante da rota de sexta é atendido semanalmente, agendado na quinta
prospect da carteira irrestrita é atendido semanalmente
cliente com compra nos últimos 7 dias é atendido a cada 7 dias
cliente com compra nos últimos 45 dias é atendido a cada 14 dias
cliente de curva A sem compra com qualquer vendedor há mais de 120 dias é atendido a cada 14 dias
cliente de curva B sem compra com qualquer vendedor há mais de 120 dias é atendido a cada 30 dias
cliente de curva C sem compra com qualquer vendedor há mais de 120 dias é atendido a cada 30 dias
cliente sem compra há mais de 180 dias é atendido a cada 21 dias
cliente da cidade de São José do Rio Preto é atendido a cada 30 dias
o restante sem regra mapeada é atendido a cada 30 dias
prospect é atendido a cada 14 dias
cliente com compra nos últimos 7 dias é atendido a cada 21 dias
cliente com compra entre 8 e 30 dias é atendido a cada 30 dias
cliente com compra entre 31 e 60 dias é atendido a cada 45 dias
cliente com compra entre 61 e 90 dias é atendido a cada 70 dias
cliente com compra entre 91 e 180 dias é atendido a cada 15 dias
cliente sem compra há mais de 180 dias é atendido a cada 21 dias

## Estrutura

```yaml
publico: televendas 1 (todos os televendas ativos exceto VENDEDOR_01) e televendas 2 (VENDEDOR_01)
comuns: []
regras:
  - nome: Prospects da rota de segunda
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de segunda, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Águas de São Pedro, Americana, Araras, Charqueada, Cordeirópolis, Ipeúna, Iracemápolis, Piracicaba, Rio Claro, Rio das Pedras, Santa Bárbara d'Oeste, Santa Gertrudes, São Pedro]}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Alta frequência da rota de segunda
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de segunda, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Águas de São Pedro, Americana, Araras, Charqueada, Cordeirópolis, Ipeúna, Iracemápolis, Piracicaba, Rio Claro, Rio das Pedras, Santa Bárbara d'Oeste, Santa Gertrudes, São Pedro]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Regularidade da rota de segunda
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de segunda, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Águas de São Pedro, Americana, Araras, Charqueada, Cordeirópolis, Ipeúna, Iracemápolis, Piracicaba, Rio Claro, Rio das Pedras, Santa Bárbara d'Oeste, Santa Gertrudes, São Pedro]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Risco de inatividade da rota de segunda
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de segunda, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Águas de São Pedro, Americana, Araras, Charqueada, Cordeirópolis, Ipeúna, Iracemápolis, Piracicaba, Rio Claro, Rio das Pedras, Santa Bárbara d'Oeste, Santa Gertrudes, São Pedro]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 120, unidade: dias, alcance: empresa}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos da rota de segunda
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de segunda, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Águas de São Pedro, Americana, Araras, Charqueada, Cordeirópolis, Ipeúna, Iracemápolis, Piracicaba, Rio Claro, Rio das Pedras, Santa Bárbara d'Oeste, Santa Gertrudes, São Pedro]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 180, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Sem regra da rota de segunda
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de segunda, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Águas de São Pedro, Americana, Araras, Charqueada, Cordeirópolis, Ipeúna, Iracemápolis, Piracicaba, Rio Claro, Rio das Pedras, Santa Bárbara d'Oeste, Santa Gertrudes, São Pedro]}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects da rota de terça
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de terça, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Américo Brasiliense, Araraquara, Barrinha, Cravinhos, Descalvado, Guariba, Ibaté, Jaboticabal, Leme, Matão, Monte Alto, Pirassununga, Pontal, Porto Ferreira, Ribeirão Preto, Santa Cruz das Palmeiras, Santa Rita do Passa Quatro, São Carlos, Serrana, Sertãozinho, Taquaritinga]}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Alta frequência da rota de terça
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de terça, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Américo Brasiliense, Araraquara, Barrinha, Cravinhos, Descalvado, Guariba, Ibaté, Jaboticabal, Leme, Matão, Monte Alto, Pirassununga, Pontal, Porto Ferreira, Ribeirão Preto, Santa Cruz das Palmeiras, Santa Rita do Passa Quatro, São Carlos, Serrana, Sertãozinho, Taquaritinga]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Regularidade da rota de terça
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de terça, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Américo Brasiliense, Araraquara, Barrinha, Cravinhos, Descalvado, Guariba, Ibaté, Jaboticabal, Leme, Matão, Monte Alto, Pirassununga, Pontal, Porto Ferreira, Ribeirão Preto, Santa Cruz das Palmeiras, Santa Rita do Passa Quatro, São Carlos, Serrana, Sertãozinho, Taquaritinga]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Risco de inatividade da rota de terça
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de terça, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Américo Brasiliense, Araraquara, Barrinha, Cravinhos, Descalvado, Guariba, Ibaté, Jaboticabal, Leme, Matão, Monte Alto, Pirassununga, Pontal, Porto Ferreira, Ribeirão Preto, Santa Cruz das Palmeiras, Santa Rita do Passa Quatro, São Carlos, Serrana, Sertãozinho, Taquaritinga]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 120, unidade: dias, alcance: empresa}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos da rota de terça
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de terça, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Américo Brasiliense, Araraquara, Barrinha, Cravinhos, Descalvado, Guariba, Ibaté, Jaboticabal, Leme, Matão, Monte Alto, Pirassununga, Pontal, Porto Ferreira, Ribeirão Preto, Santa Cruz das Palmeiras, Santa Rita do Passa Quatro, São Carlos, Serrana, Sertãozinho, Taquaritinga]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 180, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Sem regra da rota de terça
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de terça, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Américo Brasiliense, Araraquara, Barrinha, Cravinhos, Descalvado, Guariba, Ibaté, Jaboticabal, Leme, Matão, Monte Alto, Pirassununga, Pontal, Porto Ferreira, Ribeirão Preto, Santa Cruz das Palmeiras, Santa Rita do Passa Quatro, São Carlos, Serrana, Sertãozinho, Taquaritinga]}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects da rota de quarta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de quarta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Aguaí, Águas de Lindóia, Amparo, Andradas, Artur Nogueira, Engenheiro Coelho, Espírito Santo do Pinhal, Holambra, Itapira, Jacutinga, Jaguariúna, Lindóia, Mogi Guaçu, Mogi Mirim, Monte Alegre do Sul, Monte Sião, Ouro Fino, Pedreira, Pinhalzinho, Poços de Caldas, São João da Boa Vista, Serra Negra, Socorro]}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Alta frequência da rota de quarta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de quarta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Aguaí, Águas de Lindóia, Amparo, Andradas, Artur Nogueira, Engenheiro Coelho, Espírito Santo do Pinhal, Holambra, Itapira, Jacutinga, Jaguariúna, Lindóia, Mogi Guaçu, Mogi Mirim, Monte Alegre do Sul, Monte Sião, Ouro Fino, Pedreira, Pinhalzinho, Poços de Caldas, São João da Boa Vista, Serra Negra, Socorro]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Regularidade da rota de quarta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de quarta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Aguaí, Águas de Lindóia, Amparo, Andradas, Artur Nogueira, Engenheiro Coelho, Espírito Santo do Pinhal, Holambra, Itapira, Jacutinga, Jaguariúna, Lindóia, Mogi Guaçu, Mogi Mirim, Monte Alegre do Sul, Monte Sião, Ouro Fino, Pedreira, Pinhalzinho, Poços de Caldas, São João da Boa Vista, Serra Negra, Socorro]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Risco de inatividade da rota de quarta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de quarta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Aguaí, Águas de Lindóia, Amparo, Andradas, Artur Nogueira, Engenheiro Coelho, Espírito Santo do Pinhal, Holambra, Itapira, Jacutinga, Jaguariúna, Lindóia, Mogi Guaçu, Mogi Mirim, Monte Alegre do Sul, Monte Sião, Ouro Fino, Pedreira, Pinhalzinho, Poços de Caldas, São João da Boa Vista, Serra Negra, Socorro]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 120, unidade: dias, alcance: empresa}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos da rota de quarta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de quarta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Aguaí, Águas de Lindóia, Amparo, Andradas, Artur Nogueira, Engenheiro Coelho, Espírito Santo do Pinhal, Holambra, Itapira, Jacutinga, Jaguariúna, Lindóia, Mogi Guaçu, Mogi Mirim, Monte Alegre do Sul, Monte Sião, Ouro Fino, Pedreira, Pinhalzinho, Poços de Caldas, São João da Boa Vista, Serra Negra, Socorro]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 180, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Sem regra da rota de quarta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de quarta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Aguaí, Águas de Lindóia, Amparo, Andradas, Artur Nogueira, Engenheiro Coelho, Espírito Santo do Pinhal, Holambra, Itapira, Jacutinga, Jaguariúna, Lindóia, Mogi Guaçu, Mogi Mirim, Monte Alegre do Sul, Monte Sião, Ouro Fino, Pedreira, Pinhalzinho, Poços de Caldas, São João da Boa Vista, Serra Negra, Socorro]}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects da rota de quinta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de quinta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Alumínio, Araçoiaba da Serra, Boituva, Cerquilho, Cotia, Ibiúna, Indaiatuba, Iperó, Itapetininga, Itapevi, Itu, Mairinque, Monte Mor, Porto Feliz, Salto, São Roque, Sorocaba, Tatuí, Tietê, Vargem Grande Paulista, Votorantim]}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Alta frequência da rota de quinta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de quinta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Alumínio, Araçoiaba da Serra, Boituva, Cerquilho, Cotia, Ibiúna, Indaiatuba, Iperó, Itapetininga, Itapevi, Itu, Mairinque, Monte Mor, Porto Feliz, Salto, São Roque, Sorocaba, Tatuí, Tietê, Vargem Grande Paulista, Votorantim]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Regularidade da rota de quinta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de quinta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Alumínio, Araçoiaba da Serra, Boituva, Cerquilho, Cotia, Ibiúna, Indaiatuba, Iperó, Itapetininga, Itapevi, Itu, Mairinque, Monte Mor, Porto Feliz, Salto, São Roque, Sorocaba, Tatuí, Tietê, Vargem Grande Paulista, Votorantim]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Risco de inatividade da rota de quinta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de quinta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Alumínio, Araçoiaba da Serra, Boituva, Cerquilho, Cotia, Ibiúna, Indaiatuba, Iperó, Itapetininga, Itapevi, Itu, Mairinque, Monte Mor, Porto Feliz, Salto, São Roque, Sorocaba, Tatuí, Tietê, Vargem Grande Paulista, Votorantim]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 120, unidade: dias, alcance: empresa}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos da rota de quinta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de quinta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Alumínio, Araçoiaba da Serra, Boituva, Cerquilho, Cotia, Ibiúna, Indaiatuba, Iperó, Itapetininga, Itapevi, Itu, Mairinque, Monte Mor, Porto Feliz, Salto, São Roque, Sorocaba, Tatuí, Tietê, Vargem Grande Paulista, Votorantim]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 180, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Sem regra da rota de quinta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de quinta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Alumínio, Araçoiaba da Serra, Boituva, Cerquilho, Cotia, Ibiúna, Indaiatuba, Iperó, Itapetininga, Itapevi, Itu, Mairinque, Monte Mor, Porto Feliz, Salto, São Roque, Sorocaba, Tatuí, Tietê, Vargem Grande Paulista, Votorantim]}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects da rota de sexta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de sexta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Atibaia, Bragança Paulista, Campinas, Campo Limpo Paulista, Cosmópolis, Hortolândia, Itatiba, Jundiaí, Louveira, Nova Odessa, Paulínia, Sumaré, Valinhos, Várzea Paulista, Vinhedo]}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: quinta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Alta frequência da rota de sexta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de sexta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Atibaia, Bragança Paulista, Campinas, Campo Limpo Paulista, Cosmópolis, Hortolândia, Itatiba, Jundiaí, Louveira, Nova Odessa, Paulínia, Sumaré, Valinhos, Várzea Paulista, Vinhedo]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: quinta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Regularidade da rota de sexta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de sexta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Atibaia, Bragança Paulista, Campinas, Campo Limpo Paulista, Cosmópolis, Hortolândia, Itatiba, Jundiaí, Louveira, Nova Odessa, Paulínia, Sumaré, Valinhos, Várzea Paulista, Vinhedo]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: quinta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Risco de inatividade da rota de sexta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de sexta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Atibaia, Bragança Paulista, Campinas, Campo Limpo Paulista, Cosmópolis, Hortolândia, Itatiba, Jundiaí, Louveira, Nova Odessa, Paulínia, Sumaré, Valinhos, Várzea Paulista, Vinhedo]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 120, unidade: dias, alcance: empresa}
      - {tipo: periodo_vigencia, op: igual_a, valor: quinta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos da rota de sexta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de sexta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Atibaia, Bragança Paulista, Campinas, Campo Limpo Paulista, Cosmópolis, Hortolândia, Itatiba, Jundiaí, Louveira, Nova Odessa, Paulínia, Sumaré, Valinhos, Várzea Paulista, Vinhedo]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 180, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: quinta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Sem regra da rota de sexta
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: rota de sexta, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Atibaia, Bragança Paulista, Campinas, Campo Limpo Paulista, Cosmópolis, Hortolândia, Itatiba, Jundiaí, Louveira, Nova Odessa, Paulínia, Sumaré, Valinhos, Várzea Paulista, Vinhedo]}
      - {tipo: periodo_vigencia, op: igual_a, valor: quinta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects da carteira irrestrita
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira irrestrita, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Arujá, Barueri, Caieiras, Cajamar, Carapicuíba, Diadema, Embu das Artes, Ferraz de Vasconcelos, Francisco Morato, Franco da Rocha, Guarulhos, Itaquaquecetuba, Jandira, Mairiporã, Mauá, Mogi das Cruzes, Osasco, Poá, Ribeirão Pires, Santana de Parnaíba, Santo André, São Bernardo do Campo, São Caetano do Sul, São Paulo, Suzano]}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Alta frequência da carteira irrestrita
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira irrestrita, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Arujá, Barueri, Caieiras, Cajamar, Carapicuíba, Diadema, Embu das Artes, Ferraz de Vasconcelos, Francisco Morato, Franco da Rocha, Guarulhos, Itaquaquecetuba, Jandira, Mairiporã, Mauá, Mogi das Cruzes, Osasco, Poá, Ribeirão Pires, Santana de Parnaíba, Santo André, São Bernardo do Campo, São Caetano do Sul, São Paulo, Suzano]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 7, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Regularidade da carteira irrestrita
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira irrestrita, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Arujá, Barueri, Caieiras, Cajamar, Carapicuíba, Diadema, Embu das Artes, Ferraz de Vasconcelos, Francisco Morato, Franco da Rocha, Guarulhos, Itaquaquecetuba, Jandira, Mairiporã, Mauá, Mogi das Cruzes, Osasco, Poá, Ribeirão Pires, Santana de Parnaíba, Santo André, São Bernardo do Campo, São Caetano do Sul, São Paulo, Suzano]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Risco de inatividade curva A da carteira irrestrita
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira irrestrita, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Arujá, Barueri, Caieiras, Cajamar, Carapicuíba, Diadema, Embu das Artes, Ferraz de Vasconcelos, Francisco Morato, Franco da Rocha, Guarulhos, Itaquaquecetuba, Jandira, Mairiporã, Mauá, Mogi das Cruzes, Osasco, Poá, Ribeirão Pires, Santana de Parnaíba, Santo André, São Bernardo do Campo, São Caetano do Sul, São Paulo, Suzano]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 120, unidade: dias, alcance: empresa}
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Risco de inatividade curva B da carteira irrestrita
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira irrestrita, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Arujá, Barueri, Caieiras, Cajamar, Carapicuíba, Diadema, Embu das Artes, Ferraz de Vasconcelos, Francisco Morato, Franco da Rocha, Guarulhos, Itaquaquecetuba, Jandira, Mairiporã, Mauá, Mogi das Cruzes, Osasco, Poá, Ribeirão Pires, Santana de Parnaíba, Santo André, São Bernardo do Campo, São Caetano do Sul, São Paulo, Suzano]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 120, unidade: dias, alcance: empresa}
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Risco de inatividade curva C da carteira irrestrita
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira irrestrita, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Arujá, Barueri, Caieiras, Cajamar, Carapicuíba, Diadema, Embu das Artes, Ferraz de Vasconcelos, Francisco Morato, Franco da Rocha, Guarulhos, Itaquaquecetuba, Jandira, Mairiporã, Mauá, Mogi das Cruzes, Osasco, Poá, Ribeirão Pires, Santana de Parnaíba, Santo André, São Bernardo do Campo, São Caetano do Sul, São Paulo, Suzano]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 120, unidade: dias, alcance: empresa}
      - {tipo: valor_cliente, op: igual_a, valor: curva C}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inativos da carteira irrestrita
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira irrestrita, alcance: vendedor}
      - {tipo: localizacao, op: igual_a, valor: [Arujá, Barueri, Caieiras, Cajamar, Carapicuíba, Diadema, Embu das Artes, Ferraz de Vasconcelos, Francisco Morato, Franco da Rocha, Guarulhos, Itaquaquecetuba, Jandira, Mairiporã, Mauá, Mogi das Cruzes, Osasco, Poá, Ribeirão Pires, Santana de Parnaíba, Santo André, São Bernardo do Campo, São Caetano do Sul, São Paulo, Suzano]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 180, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Cidade de São José do Rio Preto
    publico: televendas 2, VENDEDOR_01
    se:
      - {tipo: localizacao, op: igual_a, valor: [São José do Rio Preto]}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Irrestrito sem regra mapeada
    publico: televendas 2, VENDEDOR_01
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Prospects do televendas 1
    publico: televendas 1, todos os televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos com compra nos últimos 7 dias do televendas 1
    publico: televendas 1, todos os televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 7, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Ativos com compra entre 8 e 30 dias do televendas 1
    publico: televendas 1, todos os televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [8, 30], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos com compra entre 31 e 60 dias do televendas 1
    publico: televendas 1, todos os televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 45 dias}
  - nome: Ativos com compra entre 61 e 90 dias do televendas 1
    publico: televendas 1, todos os televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 70 dias}
  - nome: Ativos com compra entre 91 e 180 dias do televendas 1
    publico: televendas 1, todos os televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [91, 180], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Inativos do televendas 1
    publico: televendas 1, todos os televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 180, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - agendamento no dia anterior à rota
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Camila, vendedor 0000002 | vendedor | VENDEDOR_01 |
| carteira livre | jargao | conjunto de clientes compartilhado por um time ou vendedor |
| rota | jargao | roteiro de visitas por dia da semana |
| carteira irrestrita | jargao | clientes sem dia fixo de rota |
| prospect | jargao | cliente que nunca comprou |
| curva A, B e C | jargao | faixas de cliente por faturamento |
| televendas | jargao | atendimento por telefone |

## Lacunas

- A entrada não define os critérios de classificação das curvas A, B e C.
- A entrada não informa se as compras de 7 e 45 dias da carteira irrestrita e as faixas do televendas 1 consideram o vendedor ou qualquer vendedor.

## Ambiguidades

- Os seis perfis das rotas têm a mesma frequência semanal, o que torna a distinção entre eles irrelevante para a frequência.
- A regra de São José do Rio Preto e a regra final sem regra mapeada valem para todo o televendas 2, não só para a carteira irrestrita.
- "Agendamento no dia anterior à rota" é preferência de dia; registrada como critério de período por falta de campo próprio.
