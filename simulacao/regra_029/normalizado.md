---
id: regra_029
origem: simulacao/regra_029/entrada.md
gobr: simulacao/regra_029/regra_029.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 2
procedencia: corpus_sintetico
---

## Regras

cliente da carteira fixa inativo e inadimplente não é agendado
todos os demais clientes da carteira fixa são atendidos a cada 14 dias

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
regras:
  - nome: Não agendar inativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Demais clientes a cada 14 dias
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Trilha | empresa_foco | EMPRESA_FOCO |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não define o prazo que caracteriza o cliente inativo.

## Ambiguidades

- nenhuma
