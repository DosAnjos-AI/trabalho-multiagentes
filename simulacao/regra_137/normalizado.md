---
id: regra_137
origem: simulacao/regra_137/entrada.md
gobr: simulacao/regra_137/regra_137.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

prospect é atendido a cada 14 dias
cliente ativo é atendido a cada 21 dias
todo o restante, os inativos, é atendido a cada 14 dias

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns: []
regras:
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Demais clientes, inativos
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Fênix Distribuidora | empresa_foco | EMPRESA_FOCO |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz sobre qual carteira os vendedores trabalham.
- A entrada não define o prazo que caracteriza o cliente ativo.

## Ambiguidades

- nenhuma
