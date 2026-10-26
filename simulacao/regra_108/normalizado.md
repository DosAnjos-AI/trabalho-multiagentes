---
id: regra_108
origem: simulacao/regra_108/entrada.md
gobr: simulacao/regra_108/regra_108.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 10
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente que nunca comprou com o vendedor é atendido a cada 7 dias
construtora com uma única compra com o vendedor é atendida a cada 21 dias
qualquer outro cliente com uma única compra com o vendedor é atendido a cada 7 dias
cliente com intervalo histórico de compra menor que 11 dias é atendido a cada 7 dias
construtora cuja última compra com o vendedor foi há 60 a 89 dias é atendida a cada 14 dias
construtora cuja última compra foi há 11 a 59 dias é atendida a cada 21 dias
cliente inativo para o vendedor, com última compra há mais de 90 dias, é atendido a cada 21 dias
cliente cuja última compra com o vendedor ficou fora dos últimos 90 dias é atendido a cada 7 dias
os demais clientes são atendidos a cada 7 dias

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospect do vendedor
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Construtora com compra única
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
      - {tipo: segmento, op: igual_a, valor: ['37']}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Demais clientes com compra única
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Intervalo histórico menor que 11 dias
    se:
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 11, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Construtora com última compra há 60 a 89 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 89], unidade: dias, alcance: vendedor}
      - {tipo: segmento, op: igual_a, valor: ['37']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Construtora com última compra há 11 a 59 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [11, 59], unidade: dias}
      - {tipo: segmento, op: igual_a, valor: ['37']}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Inativos para o vendedor
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Última compra fora dos últimos 90 dias
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Diferpan | empresa_foco | EMPRESA_FOCO |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| prospect | jargao | cliente que nunca comprou |
| ramo 37 | jargao | segmento de construtoras |
| frequência histórica | jargao | intervalo médio entre compras |

## Lacunas

- A entrada não diz se a construtora com última compra há 11 a 59 dias considera compras com o vendedor ou com a empresa.
- A entrada não diz sobre qual carteira os vendedores trabalham.

## Ambiguidades

- A regra "última compra fora dos últimos 90 dias" (7 dias) sobrepõe a regra de inativos com última compra há mais de 90 dias (21 dias); a ordem de avaliação define qual se aplica.
