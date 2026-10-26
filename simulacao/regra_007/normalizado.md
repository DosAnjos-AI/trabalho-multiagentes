---
id: regra_007
origem: simulacao/regra_007/entrada.md
gobr: simulacao/regra_007/regra_007.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

cliente da carteira fixa inativo para o vendedor é contatado a cada 30 dias
cliente da carteira fixa ativo para o vendedor é contatado a cada 14 dias
cliente da carteira fixa que ainda não comprou é contatado a cada 7 dias

## Estrutura

```yaml
publico: vendedores de televendas
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
regras:
  - nome: Inativos a cada 30 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos a cada 14 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem venda a cada 7 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Nutri Distribuidora | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o que torna um cliente ativo ou inativo para o vendedor (prazo sem compra).

## Ambiguidades

- Não fica claro se "ainda não comprou" se refere à empresa toda ou ao vendedor.
