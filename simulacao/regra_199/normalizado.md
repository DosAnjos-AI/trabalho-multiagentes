---
id: regra_199
origem: simulacao/regra_199/entrada.md
gobr: simulacao/regra_199/regra_199.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente bloqueado não é agendado
prospect é atendido a cada 30 dias
cliente com uma única compra com a empresa e compra nos últimos 40 dias é atendido a cada 30 dias
cliente ativo para o vendedor com intervalo histórico menor que 21 dias é atendido a cada 90 dias
cliente com compra entre 31 e 59 dias é atendido a cada 30 dias
cliente com compra entre 60 e 89 dias é atendido a cada 21 dias
cliente sem compra há mais de 90 dias é atendido a cada 45 dias

## Estrutura

```yaml
publico: time de televendas
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar bloqueados
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: bloqueado}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 40, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativo que compra regularmente
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 21, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 90 dias}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 59], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Em ruptura
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 89], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 45 dias}
termos_fora_vocabulario:
  - bloqueado
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| bloqueado | jargao | cliente com cadastro bloqueado |
| prospect | jargao | cliente que nunca comprou |
| frequência histórica | jargao | intervalo médio entre compras |
| ruptura | jargao | cliente que parou de comprar |

## Lacunas

- A entrada não diz se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- O cliente que compra regularmente recebe a frequência mais espaçada (90 dias), o que pode indicar inversão de intenção; foi mantido como declarado.
