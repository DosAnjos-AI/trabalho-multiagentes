---
id: regra_156
origem: simulacao/regra_156/entrada.md
gobr: simulacao/regra_156/regra_156.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
prospect é atendido a cada 14 dias
cliente com uma única compra com o vendedor é atendido a cada 10 dias
cliente ativo é atendido a cada 7 dias
os demais clientes, inativos, são atendidos a cada 14 dias

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra única
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Ativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes, inativos
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Tropical Color | empresa_foco | EMPRESA_FOCO |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz sobre qual carteira os vendedores trabalham.
- A entrada não define o prazo que caracteriza o cliente ativo.

## Ambiguidades

- nenhuma
