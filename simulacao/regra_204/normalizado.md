---
id: regra_204
origem: simulacao/regra_204/entrada.md
gobr: simulacao/regra_204/regra_204.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente com venda nos últimos 7 dias não é agendado
cliente com compra nos últimos 30 dias é atendido a cada 14 dias
cliente com compra entre 31 e 60 dias é atendido a cada 14 dias
cliente com compra entre 61 e 90 dias é atendido a cada 7 dias
clientes inativos são atendidos a cada 21 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar venda nos últimos 7 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 7, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Manter regularidade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Garantir compra da carteira
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Risco de inatividade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos
    se: []
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| positivação da carteira | jargao | conseguir compra dos clientes da carteira |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- A regra de inativos não tem critério próprio e funciona como regra residual.
