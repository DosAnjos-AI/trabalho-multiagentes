---
id: regra_076
origem: simulacao/regra_076/entrada.md
gobr: simulacao/regra_076/regra_076.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 10
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente bloqueado não é agendado
cliente inativo para a empresa não é agendado
cliente que comprou nos últimos 20 dias com qualquer vendedor não é agendado
cliente com rota programada para hoje é agendado a cada 1 dia
prospect é atendido a cada 7 dias
cliente com uma única compra com a empresa é atendido a cada 15 dias
cliente que comprou nos últimos 30 dias e tem intervalo histórico de compra menor que 30 dias usa a frequência do histórico, entre 5 e 30 dias
cliente com último pedido entre 31 e 90 dias é atendido a cada 15 dias
todo o restante, fora de rota, não é agendado

## Estrutura

```yaml
publico: vendedores de televendas ativos
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
  - nome: Não agendar inativos para a empresa
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo, alcance: empresa}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar quem comprou nos últimos 20 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 20, unidade: dias, alcance: empresa}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Rota programada para hoje
    se:
      - {tipo: agenda_rota, op: igual_a, valor: hoje, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Compra regularmente
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Em ruptura
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Fora de rota
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - bloqueado
  - frequência histórica de compra
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| bloqueado | jargao | cliente com cadastro bloqueado |
| rota | jargao | roteiro de visitas programado |
| prospect | jargao | cliente que nunca comprou |
| ruptura | jargao | cliente que parou de comprar |
| frequência histórica | jargao | intervalo médio entre compras |

## Lacunas

- A entrada não informa se as compras das regras "compra regularmente" e "ruptura" consideram o vendedor ou qualquer vendedor.

## Ambiguidades

- Os limites mínimo de 5 e máximo de 30 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
- "Bloqueado" foi classificado como situação de cadastro; pode se referir a bloqueio financeiro.
