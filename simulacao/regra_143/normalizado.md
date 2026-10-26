---
id: regra_143
origem: simulacao/regra_143/entrada.md
gobr: simulacao/regra_143/regra_143.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 9
procedencia: corpus_sintetico
---

## Regras

cliente filial não é agendado
cliente que comprou nos últimos 30 dias com a empresa não é agendado
prospect é atendido a cada 28 dias
ativo de curva A sem compra entre 30 e 45 dias é atendido a cada 7 dias
ativo de curva B sem compra entre 30 e 45 dias é atendido a cada 14 dias
ativo de curva C ou demais, sem compra entre 30 e 45 dias, é atendido a cada 21 dias
ativo sem compra entre 45 e 60 dias é atendido a cada 14 dias
ativo sem compra há mais de 60 dias é atendido a cada 7 dias
inativos são atendidos a cada 7 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar quem comprou nos últimos 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: empresa}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Ativos sem compra entre 30 e 45 dias, curva A
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [30, 45], unidade: dias}
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos sem compra entre 30 e 45 dias, curva B
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [30, 45], unidade: dias}
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos sem compra entre 30 e 45 dias, curva C ou demais
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [30, 45], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Ativos sem compra entre 45 e 60 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [45, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos sem compra há mais de 60 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - filial
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| filial | jargao | unidade filial de um cliente |
| prospect | jargao | cliente que nunca comprou |
| curva A, B e C | jargao | faixas de cliente por faturamento |

## Lacunas

- A entrada não define os critérios das curvas A, B e C.

## Ambiguidades

- "Sem compra entre 30 e 45 dias" foi registrado como ausência de compra na janela de 30 a 45 dias (fora_de); pode também ser lido como última compra ocorrida entre 30 e 45 dias.
- A regra de inativos não tem critério próprio e funciona como regra residual.
