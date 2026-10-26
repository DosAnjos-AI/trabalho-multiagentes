---
id: regra_170
origem: simulacao/regra_170/entrada.md
gobr: simulacao/regra_170/regra_170.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

distribuidor ativo para o vendedor e sem compra há mais de 60 dias é atendido quinzenalmente
cliente sem compra com a empresa há mais de 10 dias e com intervalo histórico menor que 7 dias é atendido a cada 21 dias
distribuidor ativo com vendas nos últimos 60 dias não é agendado
cliente ativo sem vendas há mais de 30 dias é atendido quinzenalmente
cliente ativo com vendas nos últimos 30 dias não é agendado
inativos e prospects são atendidos mensalmente

## Estrutura

```yaml
publico: todos os vendedores
comuns: []
regras:
  - nome: Distribuidor sem compra há mais de 60 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: vendedor}
      - {tipo: segmento, op: igual_a, valor: [distribuidor]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Compra com regularidade
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 10, unidade: dias, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 7, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Não agendar distribuidor com vendas recentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: vendedor}
      - {tipo: segmento, op: igual_a, valor: [distribuidor]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos sem vendas há mais de 30 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Não agendar ativos com vendas recentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Inativos e prospects
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| ramo distribuidor | jargao | segmento de distribuidores |
| frequência histórica | jargao | intervalo médio entre compras |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz sobre qual carteira os vendedores trabalham.

## Ambiguidades

- "Quinzenal" e "mensal" foram registrados como 15 e 30 dias pela convenção de periodicidade.
