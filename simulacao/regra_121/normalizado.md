---
id: regra_121
origem: simulacao/regra_121/entrada.md
gobr: simulacao/regra_121/regra_121.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 9
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente filial não é agendado
cliente reativado com a empresa é atendido a cada 3 dias
cliente com uma única compra com a empresa é atendido a cada 3 dias
cliente com compra nos últimos 30 dias usa a frequência do histórico, entre 3 e 21 dias
cliente com compra em até 60 dias é atendido a cada 14 dias
cliente com compra em até 90 dias é atendido a cada 21 dias
cliente com compra em até 120 dias é atendido a cada 14 dias
quem não se enquadrou nas regras anteriores é atendido a cada 7 dias

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
  - nome: Reativados com a empresa
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: voltou a comprar, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 3 dias}
  - nome: Compra única com a empresa
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 3 dias}
  - nome: Ativos recorrentes
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Compra em até 60 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra em até 90 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Compra em até 120 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 120, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Demais clientes
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - filial
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita Federal | jargao | cadastro encerrado no órgão fiscal |
| filial | jargao | unidade filial de um cliente |
| reativado | jargao | cliente que voltou a comprar |
| frequência do histórico | jargao | frequência calculada pelo histórico de compras |

## Lacunas

- A entrada não informa se as compras das faixas de 30, 60, 90 e 120 dias consideram o vendedor ou a empresa.

## Ambiguidades

- Os limites mínimo de 3 e máximo de 21 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
- As faixas "até 60", "até 90" e "até 120 dias" se sobrepõem; entende-se que cada uma vale para quem não caiu na anterior.
