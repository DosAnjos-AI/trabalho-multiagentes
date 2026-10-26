---
id: regra_228
origem: simulacao/regra_228/entrada.md
gobr: simulacao/regra_228/regra_228.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

prospect com o vendedor é atendido a cada 28 dias
cliente com uma única compra com o vendedor é atendido a cada 21 dias
cliente de curva C com compra nos últimos 90 dias é atendido a cada 7 dias
os demais clientes, curvas A e B, com compra nos últimos 90 dias são atendidos a cada 14 dias
cliente com compra entre 91 e 180 dias é atendido a cada 28 dias
os inativos são atendidos a cada 45 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Ativar novo cliente
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Compra regular, curva C
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
      - {tipo: valor_cliente, op: igual_a, valor: curva C}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Compra regular, curvas A e B
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Caminhando para a inatividade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [91, 180], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Resgate de inativo
    se: []
    entao: {acao: agendar, frequencia: fixa 45 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |
| curva A, B e C | jargao | faixas de cliente por faturamento |

## Lacunas

- A entrada não define os critérios das curvas A, B e C.

## Ambiguidades

- A regra das curvas A e B não traz critério explícito de curva; funciona como residual dos clientes com compra nos últimos 90 dias.
