---
id: regra_138
origem: simulacao/regra_138/entrada.md
gobr: simulacao/regra_138/regra_138.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 2
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
todos os outros clientes, adimplentes, são atendidos a cada 7 dias

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Demais clientes a cada 7 dias
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| American Farma | empresa_foco | EMPRESA_FOCO |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz sobre qual carteira os vendedores trabalham.

## Ambiguidades

- nenhuma
