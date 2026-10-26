---
id: regra_187
origem: simulacao/regra_187/entrada.md
gobr: simulacao/regra_187/regra_187.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 11
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente filial não é agendado
cliente inadimplente não é agendado
cliente cadastrado há 60 dias não é agendado
cliente que comprou com a empresa nos últimos 60 dias não é agendado
prospect é atendido a cada 14 dias
cliente com compra em até 90 dias é atendido a cada 7 dias
cliente com compra em até 120 dias é atendido a cada 7 dias
cliente com compra em até 180 dias é atendido a cada 14 dias
cliente com compra em até 360 dias é atendido a cada 21 dias
os demais clientes são atendidos a cada 28 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar cadastrados há 60 dias
    se:
      - {tipo: situacao_cadastro, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar quem comprou nos últimos 60 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias, alcance: empresa}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos recentes
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos médios
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 120, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos antigos
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 180, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Requalificação de inativos
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 360, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Requalificar do zero
    se: []
    entao: {acao: agendar, frequencia: fixa 28 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - filial
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| filial | jargao | unidade filial de um cliente |
| requalificação | jargao | reavaliação do perfil do cliente |

## Lacunas

- A entrada não informa se as compras das faixas consideram o vendedor ou a empresa.

## Ambiguidades

- "Cadastrado há 60 dias" foi registrado como cadastro recente, dentro de 60 dias, pelo contexto de não agendar recém-cadastrados; pode ser lido como cadastro há mais de 60 dias.
- As faixas "até 90", "até 120", "até 180" e "até 360 dias" se sobrepõem e, com a exclusão de quem comprou em 60 dias, valem para quem não caiu na faixa anterior.
