---
id: regra_212
origem: simulacao/regra_212/entrada.md
gobr: simulacao/regra_212/regra_212.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 9
procedencia: corpus_sintetico
---

## Regras

cliente com rota nos próximos 7 dias não é agendado
cliente que comprou com a empresa nos últimos 14 dias não é agendado
cliente com rota há 7 dias, visita na semana anterior e pedido entre 14 e 30 dias é atendido a cada 7 dias
cliente com rota há 7 dias, visita na semana anterior e pedido entre 31 e 60 dias é atendido a cada 20 dias
cliente que nunca fez pedido é atendido a cada 14 dias
cliente que comprou no ano passado e tem última compra entre 180 e 360 dias é atendido a cada 14 dias
cliente com último pedido entre 61 e 90 dias é atendido a cada 7 dias
cliente com último pedido entre 91 e 180 dias é atendido a cada 7 dias
os demais clientes são atendidos a cada 7 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar com rota nos próximos 7 dias
    se:
      - {tipo: agenda_rota, op: dentro_de, valor: 7, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar quem comprou nos últimos 14 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 14, unidade: dias, alcance: empresa}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Manter regularidade
    se:
      - {tipo: agenda_rota, op: igual_a, valor: 7, unidade: dias}
      - {tipo: tempo_sem_visita, op: igual_a, valor: semana anterior, unidade: periodo_nomeado, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: entre, valor: [14, 30], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Garantir regularidade e relacionamento
    se:
      - {tipo: agenda_rota, op: igual_a, valor: 7, unidade: dias}
      - {tipo: tempo_sem_visita, op: igual_a, valor: semana anterior, unidade: periodo_nomeado, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 20 dias}
  - nome: Ativar cliente que nunca fez pedido
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativar cliente do ano passado
    se:
      - {tipo: periodo_vigencia, op: igual_a, valor: ano anterior, unidade: periodo_nomeado, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: entre, valor: [180, 360], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Caminhando para a inatividade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Resgate
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [91, 180], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - rota realizada há dias
  - compra no ano anterior
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| rota | jargao | roteiro de visitas programado |
| resgate | jargao | reativação de cliente inativo |

## Lacunas

- A entrada não diz se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- "Rota há 7 dias" foi registrado como rota realizada exatamente 7 dias atrás; pode ser lido como rota nos últimos 7 dias.
