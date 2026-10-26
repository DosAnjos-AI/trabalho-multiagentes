---
id: regra_242
origem: simulacao/regra_242/entrada.md
gobr: simulacao/regra_242/regra_242.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente com intervalo histórico de 0 a 30 dias e sem compra entre 20 e 30 dias é atendido a cada 21 dias
cliente com intervalo histórico de 31 a 60 dias e sem compra entre 29 e 44 dias é atendido a cada 21 dias
cliente com intervalo histórico de 31 a 60 dias e sem compra entre 44 e 60 dias é atendido a cada 21 dias
cliente com intervalo histórico de 61 a 90 dias e sem compra entre 61 e 90 dias é atendido a cada 15 dias
cliente com intervalo histórico de 61 a 90 dias e sem compra entre 90 e 180 dias é atendido a cada 21 dias
cliente com intervalo histórico de 91 a 180 dias e sem compra entre 44 e 120 dias é atendido a cada 21 dias
cliente com intervalo histórico de 91 a 180 dias e sem compra entre 120 e 180 dias é atendido a cada 15 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Intervalo de 0 a 30 dias, sem compra entre 20 e 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [0, 30], unidade: dias, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [20, 30], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Intervalo de 31 a 60 dias, sem compra entre 29 e 44 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [29, 44], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Intervalo de 31 a 60 dias, sem compra entre 44 e 60 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [44, 60], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Intervalo de 61 a 90 dias, sem compra entre 61 e 90 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [61, 90], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Intervalo de 61 a 90 dias, sem compra entre 90 e 180 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [90, 180], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Intervalo de 91 a 180 dias, sem compra entre 44 e 120 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [91, 180], unidade: dias, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [44, 120], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Intervalo de 91 a 180 dias, sem compra entre 120 e 180 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [91, 180], unidade: dias, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [120, 180], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario:
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| frequência histórica | jargao | intervalo médio entre compras |

## Lacunas

- A entrada não traz regra residual para clientes fora das combinações descritas.

## Ambiguidades

- O intervalo histórico de compra não tem tipo próprio e foi registrado como tempo_sem_comprar, ao lado da recência.
- "Sem compra entre X e Y dias" foi registrado como ausência de compra na janela (fora_de).
- As janelas de recência se tocam nos limites (44, 60, 90, 120), o que deixa a classificação dos limites dependente da ordem de avaliação.
