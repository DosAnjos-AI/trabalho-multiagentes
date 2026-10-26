---
id: regra_207
origem: simulacao/regra_207/entrada.md
gobr: simulacao/regra_207/regra_207.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente pessoa física não é agendado
cliente sem pedido com a empresa é atendido a cada 14 dias
cliente com compra nos últimos 14 dias usa o histórico acrescido de 7 dias, com máximo de 14 dias
cliente com compra entre 14 e 30 dias é atendido a cada 14 dias
cliente com último pedido entre 30 e 45 dias é atendido a cada 21 dias
cliente com compra entre 45 e 90 dias é atendido a cada 14 dias
cliente sem compra há mais de 90 dias é atendido a cada 28 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar pessoa física
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa física}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem pedido com a empresa
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Alta regularidade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 14, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Manter regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [14, 30], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem pedido entre 30 e 45 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [30, 45], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Risco de ficar inativo
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [45, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Resgate de inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
termos_fora_vocabulario:
  - pessoa física
  - frequência pelo histórico com acréscimo e teto
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| CPF | jargao | cliente pessoa física |
| frequência do histórico | jargao | frequência calculada pelo histórico de compras |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- O acréscimo de 7 dias com teto de 14 dias na frequência pelo histórico não tem campo próprio e foi registrado apenas na descrição.
