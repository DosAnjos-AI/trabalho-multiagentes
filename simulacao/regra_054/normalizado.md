---
id: regra_054
origem: simulacao/regra_054/entrada.md
gobr: simulacao/regra_054/regra_054.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

cliente sem venda é atendido a cada 14 dias
cliente adimplente é atendido a cada 30 dias
cliente inadimplente não é agendado

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns: []
regras:
  - nome: Sem venda a cada 14 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Adimplentes a cada 30 dias
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| sem venda | jargao | cliente que nunca comprou |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não informa sobre qual carteira os vendedores trabalham.

## Ambiguidades

- nenhuma
