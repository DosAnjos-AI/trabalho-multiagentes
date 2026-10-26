---
id: regra_008
origem: simulacao/regra_008/entrada.md
gobr: simulacao/regra_008/regra_008.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 4
procedencia: corpus_sintetico
---

## Regras

cliente adimplente da carteira da capital é visitado a cada 14 dias
cliente da carteira da capital que ainda não tem venda é visitado a cada 14 dias
cliente inadimplente da carteira da capital é visitado a cada 30 dias
todo cliente da carteira do interior é visitado a cada 30 dias

## Estrutura

```yaml
publico: vendedores de campo, divididos entre time da capital e time do interior
comuns: []
regras:
  - nome: Adimplentes da capital
    publico: time da capital, todos os vendedores de campo exceto VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do time da capital, alcance: grupo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem venda da capital
    publico: time da capital, todos os vendedores de campo exceto VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do time da capital, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inadimplentes da capital
    publico: time da capital, todos os vendedores de campo exceto VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do time da capital, alcance: grupo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Todos os clientes do interior
    publico: time do interior, VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do time do interior, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| NB PI | empresa_foco | EMPRESA_FOCO |
| vendedor de ID 35 | vendedor | VENDEDOR_01 |
| vendedor de ID 34 | vendedor | VENDEDOR_02 |
| carteira fixa | jargao | clientes vinculados a um vendedor ou time |
| adimplente | jargao | cliente sem pendência financeira |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| vendedor de campo | jargao | vendedor que atende presencialmente |

## Lacunas

- A entrada não informa o que acontece com clientes da capital que não se enquadram em adimplente, inadimplente ou sem venda.

## Ambiguidades

- nenhuma
