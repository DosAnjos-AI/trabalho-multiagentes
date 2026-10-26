---
id: regra_236
origem: simulacao/regra_236/entrada.md
gobr: simulacao/regra_236/regra_236.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente da região de rota todo dia com compra no último dia é atendido semanalmente, a cada 7 dias
cliente da região de rota todo dia sem venda recente é atendido a cada 2 dias
cliente da região sem compra na semana é atendido semanalmente, a cada 7 dias, na segunda, quarta e sexta
cliente da região sem compra na semana é atendido semanalmente, a cada 7 dias, na terça e quinta
cliente fora dessas regras não é agendado

## Estrutura

```yaml
publico: vendedores de televendas ativos, por região
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    publico: vendedores de televendas ativos
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Rota todo dia, com venda recente
    publico: vendedores de televendas ativos, região de rota todo dia
    se:
      - {tipo: localizacao, op: igual_a, valor: [Barra Mansa, Volta Redonda, Resende, Queimados, Itatiaia, São João de Meriti, Nova Iguaçu, Mesquita, Belford Roxo, Porto Real, Rio de Janeiro - Centro, Rio de Janeiro - Pavuna]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 1, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota todo dia
    publico: vendedores de televendas ativos, região de rota todo dia
    se:
      - {tipo: localizacao, op: igual_a, valor: [Barra Mansa, Volta Redonda, Resende, Queimados, Itatiaia, São João de Meriti, Nova Iguaçu, Mesquita, Belford Roxo, Porto Real, Rio de Janeiro - Centro, Rio de Janeiro - Pavuna]}
    entao: {acao: agendar, frequencia: fixa 2 dias}
  - nome: Rota segunda, quarta e sexta
    publico: vendedores de televendas ativos, região de segunda, quarta e sexta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Itaguaí, Seropédica, Visconde de Mauá, Rio de Janeiro - Santa Cruz, Rio de Janeiro - Realengo, Rio de Janeiro - Campo Grande, Rio de Janeiro - Bangu, Rio de Janeiro - Jacarepaguá, Rio de Janeiro - Taquara, Rio de Janeiro - Freguesia, Rio de Janeiro - Sepetiba, Rio de Janeiro - Cosmos, Rio de Janeiro - Cosme Velho, Rio de Janeiro - Tijuca, Rio de Janeiro - Barra da Tijuca, Rio de Janeiro - Méier, Rio de Janeiro - Madureira, Rio de Janeiro - Irajá, Rio de Janeiro - Vila da Penha, Rio de Janeiro - Penha, Rio de Janeiro - Ilha do Governador, Rio de Janeiro - Cachambi]}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [semana atual], unidade: periodo_nomeado}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, quarta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota terça e quinta
    publico: vendedores de televendas ativos, região de terça e quinta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Barra do Piraí, Vassouras, Miguel Pereira, Valença, Paty do Alferes, Rio Claro, Mangaratiba, Parati, Piraí, Bananal, Mendes, Três Rios, Pontal, Paracambi, Rio de Janeiro - Guaratiba, Rio de Janeiro - Pereque, Angra dos Reis - Guaratiba, Angra dos Reis - Pereque, São Paulo]}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [semana atual], unidade: periodo_nomeado}
      - {tipo: periodo_vigencia, op: igual_a, valor: [terça, quinta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Não agendar fora das regras
    publico: vendedores de televendas ativos
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - carteira livre
  - bairro
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| carteira livre | jargao | agrupamento de clientes por filtro, sem vínculo fixo |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| rota | jargao | roteiro de visitas programado |

## Lacunas

- A entrada resume a lista de bairros de segunda, quarta e sexta e menciona variações de grafia sem enumerá-las.
- A entrada não diz se os bairros Guaratiba e Pereque pertencem ao Rio, a Angra dos Reis ou a ambas.

## Ambiguidades

- "Semanal" foi convertido em 7 dias.
- Bairros foram registrados no critério de localização no formato "cidade - bairro".
- A preferência por dias da semana foi registrada como critério de período de vigência.
- A regra de rota todo dia sem venda recente não declara critério de recência; funciona como residual da região.
