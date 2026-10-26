---
id: regra_115
origem: simulacao/regra_115/entrada.md
gobr: simulacao/regra_115/regra_115.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 2
procedencia: corpus_sintetico
---

## Regras

todos os clientes do time de atacado são atendidos a cada 7 dias
todos os clientes do time de salmão são atendidos a cada 2 dias

## Estrutura

```yaml
publico: time de atacado e time de salmão
comuns: []
regras:
  - nome: Todos os clientes do atacado
    publico: time de atacado, VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Todos os clientes do salmão
    publico: time de salmão, VENDEDOR_04, VENDEDOR_05 e VENDEDOR_06
    se: []
    entao: {acao: agendar, frequencia: fixa 2 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Frigoforte | empresa_foco | EMPRESA_FOCO |
| vendedor 510 | vendedor | VENDEDOR_01 |
| vendedor 617 | vendedor | VENDEDOR_02 |
| vendedor 596 | vendedor | VENDEDOR_03 |
| vendedor 613 | vendedor | VENDEDOR_04 |
| vendedor 614 | vendedor | VENDEDOR_05 |
| vendedor 568 | vendedor | VENDEDOR_06 |
| atacado | jargao | venda em grande volume |

## Lacunas

- A entrada não diz sobre qual carteira os times trabalham nem se são de televendas ou campo.

## Ambiguidades

- nenhuma
