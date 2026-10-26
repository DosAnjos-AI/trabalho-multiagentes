---
id: regra_238
origem: simulacao/regra_238/entrada.md
gobr: simulacao/regra_238/regra_238.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

cliente com compra com qualquer vendedor nos últimos 59 dias é atendido a cada 14 dias
cliente com compra em até 89 dias é atendido a cada 14 dias
os inativos são atendidos a cada 14 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Manter relacionamento
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 59, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Manter regularidade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 89, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Resgate do inativo
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| compra global | jargao | compra com qualquer vendedor da empresa |
| resgate | jargao | reativação de cliente inativo |

## Lacunas

- A entrada não informa se a regra de 89 dias considera compras com o vendedor ou com a empresa.

## Ambiguidades

- As três faixas têm a mesma frequência de 14 dias.
