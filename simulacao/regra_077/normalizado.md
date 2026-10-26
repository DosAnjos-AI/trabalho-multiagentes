---
id: regra_077
origem: simulacao/regra_077/entrada.md
gobr: simulacao/regra_077/regra_077.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente bloqueado não é agendado
cliente inadimplente não é agendado
cliente que comprou nos últimos 30 dias não é agendado
prospect é atendido a cada 14 dias
cliente ativo com a empresa é atendido a cada 7 dias
os demais clientes, inativos, são atendidos a cada 14 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar bloqueados
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: bloqueado}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar quem comprou nos últimos 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos com a empresa
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes, inativos
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - bloqueado
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| bloqueado | jargao | cliente com cadastro bloqueado |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa se a compra dos últimos 30 dias considera o vendedor ou qualquer vendedor da empresa.

## Ambiguidades

- "Bloqueado" foi classificado como situação de cadastro; pode se referir a bloqueio financeiro.
