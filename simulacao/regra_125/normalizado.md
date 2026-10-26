---
id: regra_125
origem: simulacao/regra_125/entrada.md
gobr: simulacao/regra_125/regra_125.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 4
procedencia: corpus_sintetico
---

## Regras

cliente ativo é atendido a cada 7 dias
cliente inativo e adimplente é atendido a cada 15 dias
cliente inativo e inadimplente não é agendado
prospect, sem venda, é atendido a cada 20 dias

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
regras:
  - nome: Ativos a cada 7 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos adimplentes a cada 15 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Não agendar inativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects a cada 20 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 20 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Cavalo Marinho | empresa_foco | EMPRESA_FOCO |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- nenhuma
