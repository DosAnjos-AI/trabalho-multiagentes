---
id: regra_166
origem: simulacao/regra_166/entrada.md
gobr: simulacao/regra_166/regra_166.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente com tipo de cobrança DH e crédito igual ou menor que zero não é agendado
cliente com tipo de cobrança BK e crédito disponível abaixo de 199 reais não é agendado
cliente inadimplente não é agendado
cliente ativo é atendido a cada 7 dias
cliente inativo é atendido a cada 14 dias
cliente sem venda é atendido a cada 14 dias

## Estrutura

```yaml
publico: time de televendas
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
regras:
  - nome: Não agendar cobrança DH sem crédito
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: [DH]}
      - {tipo: situacao_financeira, op: menor_que, valor: 0, unidade: reais}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar cobrança BK com crédito abaixo de 199 reais
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: [BK]}
      - {tipo: situacao_financeira, op: menor_que, valor: 199, unidade: reais}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem venda
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - tipo de cobrança
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Nordil PB | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| carteira fixa | jargao | clientes vinculados a um vendedor ou time |
| tipo de cobrança DH, BK | jargao | modalidade de pagamento do cliente |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa o significado dos tipos de cobrança DH e BK.

## Ambiguidades

- "Crédito igual ou menor que zero" foi registrado como menor_que 0 por falta de operador "menor ou igual".
