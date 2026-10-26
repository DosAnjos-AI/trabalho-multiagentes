---
id: regra_179
origem: simulacao/regra_179/entrada.md
gobr: simulacao/regra_179/regra_179.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 16
procedencia: corpus_sintetico
---

## Regras

prospect com o vendedor, em qualquer das três carteiras, é atendido a cada 7 dias
construtora com uma única compra é atendida a cada 14 dias
cliente de material de construção ou demais segmentos com uma única compra é atendido a cada 7 dias
cliente de material de construção ou demais com última compra entre 7 e 30 dias usa o histórico, entre 7 e 30 dias
construtora com venda nos últimos 30 dias é atendida a cada 7 dias
construtora sem venda nos últimos 30 dias é atendida a cada 14 dias
cliente de material de construção com compra entre 30 e 60 dias é atendido a cada 7 dias
construtora ou demais com compra entre 30 e 60 dias é atendido a cada 14 dias
cliente de material de construção com compra entre 60 e 89 dias é atendido a cada 7 dias
construtora com compra entre 60 e 89 dias é atendida a cada 14 dias
cliente dos demais segmentos com compra entre 60 e 89 dias é atendido a cada 21 dias
cliente de material de construção com compra entre 90 e 179 dias é atendido a cada 7 dias
construtora com compra entre 90 e 179 dias é atendida a cada 21 dias
cliente dos demais segmentos com compra entre 90 e 179 dias é atendido a cada 14 dias
cliente de material de construção ou demais sem compra há mais de 180 dias é atendido a cada 14 dias
construtora sem compra há mais de 180 dias é atendida a cada 28 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Prospects de todos os segmentos
    se:
      - {tipo: carteira, op: igual_a, valor: [construtora, material de construção, demais segmentos], alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Compra única, construtora
    se:
      - {tipo: segmento, op: igual_a, valor: ['10207004', '10301009', '10101016', '10301016', '10207001', '10301010', '10207002', '10301011', '10207003', '10301015', '10205001', '10205002', '10204002']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra única, exceto construtora
    se:
      - {tipo: segmento, op: fora_de, valor: ['10207004', '10301009', '10101016', '10301016', '10207001', '10301010', '10207002', '10301011', '10207003', '10301015', '10205001', '10205002', '10204002']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Compra regular, exceto construtora
    se:
      - {tipo: segmento, op: fora_de, valor: ['10207004', '10301009', '10101016', '10301016', '10207001', '10301010', '10207002', '10301011', '10207003', '10301015', '10205001', '10205002', '10204002']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [7, 30], unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Compra regular, construtora com venda em 30 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['10207004', '10301009', '10101016', '10301016', '10207001', '10301010', '10207002', '10301011', '10207003', '10301015', '10205001', '10205002', '10204002']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Compra regular, construtora sem venda em 30 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['10207004', '10301009', '10101016', '10301016', '10207001', '10301010', '10207002', '10301011', '10207003', '10301015', '10205001', '10205002', '10204002']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Estimular regularidade, material de construção
    se:
      - {tipo: segmento, op: igual_a, valor: ['10103004', '10202002', '10201004', '10201006', '10201009', '10201003', '10201011', '10201005', '10201002', '10201001', '10101013', '10103003', '10102004', '10202005', '10201007', '10205003', '10301001', '10101019', '10301019', '10301002', '10301007', '10301004', '10101006', '10301006']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [30, 60], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Estimular regularidade, exceto material de construção
    se:
      - {tipo: segmento, op: fora_de, valor: ['10103004', '10202002', '10201004', '10201006', '10201009', '10201003', '10201011', '10201005', '10201002', '10201001', '10101013', '10103003', '10102004', '10202005', '10201007', '10205003', '10301001', '10101019', '10301019', '10301002', '10301007', '10301004', '10101006', '10301006']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [30, 60], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Caminhando para inatividade, material de construção
    se:
      - {tipo: segmento, op: igual_a, valor: ['10103004', '10202002', '10201004', '10201006', '10201009', '10201003', '10201011', '10201005', '10201002', '10201001', '10101013', '10103003', '10102004', '10202005', '10201007', '10205003', '10301001', '10101019', '10301019', '10301002', '10301007', '10301004', '10101006', '10301006']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 89], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Caminhando para inatividade, construtora
    se:
      - {tipo: segmento, op: igual_a, valor: ['10207004', '10301009', '10101016', '10301016', '10207001', '10301010', '10207002', '10301011', '10207003', '10301015', '10205001', '10205002', '10204002']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 89], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Caminhando para inatividade, demais segmentos
    se:
      - {tipo: segmento, op: fora_de, valor: ['10207004', '10301009', '10101016', '10301016', '10207001', '10301010', '10207002', '10301011', '10207003', '10301015', '10205001', '10205002', '10204002', '10103004', '10202002', '10201004', '10201006', '10201009', '10201003', '10201011', '10201005', '10201002', '10201001', '10101013', '10103003', '10102004', '10202005', '10201007', '10205003', '10301001', '10101019', '10301019', '10301002', '10301007', '10301004', '10101006', '10301006']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 89], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Resgate de inativo, material de construção
    se:
      - {tipo: segmento, op: igual_a, valor: ['10103004', '10202002', '10201004', '10201006', '10201009', '10201003', '10201011', '10201005', '10201002', '10201001', '10101013', '10103003', '10102004', '10202005', '10201007', '10205003', '10301001', '10101019', '10301019', '10301002', '10301007', '10301004', '10101006', '10301006']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [90, 179], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Resgate de inativo, construtora
    se:
      - {tipo: segmento, op: igual_a, valor: ['10207004', '10301009', '10101016', '10301016', '10207001', '10301010', '10207002', '10301011', '10207003', '10301015', '10205001', '10205002', '10204002']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [90, 179], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Resgate de inativo, demais segmentos
    se:
      - {tipo: segmento, op: fora_de, valor: ['10207004', '10301009', '10101016', '10301016', '10207001', '10301010', '10207002', '10301011', '10207003', '10301015', '10205001', '10205002', '10204002', '10103004', '10202002', '10201004', '10201006', '10201009', '10201003', '10201011', '10201005', '10201002', '10201001', '10101013', '10103003', '10102004', '10202005', '10201007', '10205003', '10301001', '10101019', '10301019', '10301002', '10301007', '10301004', '10101006', '10301006']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [90, 179], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Requalificar e resgatar, exceto construtora
    se:
      - {tipo: segmento, op: fora_de, valor: ['10207004', '10301009', '10101016', '10301016', '10207001', '10301010', '10207002', '10301011', '10207003', '10301015', '10205001', '10205002', '10204002']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 180, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Requalificar e resgatar, construtora
    se:
      - {tipo: segmento, op: igual_a, valor: ['10207004', '10301009', '10101016', '10301016', '10207001', '10301010', '10207002', '10301011', '10207003', '10301015', '10205001', '10205002', '10204002']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 180, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 28 dias}
termos_fora_vocabulario:
  - carteira livre por código de ramo
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| carteira livre | jargao | conjunto de clientes compartilhado |
| matcon | jargao | material de construção |
| ramo de atividade | jargao | segmento do cliente |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa o significado dos códigos de ramo de atividade.

## Ambiguidades

- As faixas "entre 7 e 30", "entre 30 e 60", "entre 60 e 89" e "entre 90 e 179 dias" compartilham limites.
- Os limites de 7 e 30 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
