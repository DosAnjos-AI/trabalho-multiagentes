---
id: regra_114
origem: simulacao/regra_114/entrada.md
gobr: simulacao/regra_114/regra_114.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 13
procedencia: corpus_sintetico
---

## Regras

todos os clientes de VENDEDOR_07 são atendidos a cada 15 dias, em dia útil
cliente que comprou nos últimos 30 dias não é agendado
os demais clientes são atendidos a cada 14 dias
cliente que comprou nos últimos 30 dias não é agendado
cliente bloqueado não é agendado
os demais clientes são atendidos a cada 14 dias
cliente inativo e inadimplente do interior não é agendado
os demais clientes do interior são atendidos a cada 30 dias, em dia útil
cliente inativo e inadimplente da capital não é agendado
cliente ativo e inadimplente da capital é atendido a cada 30 dias, em dia útil
os demais clientes da capital são atendidos a cada 14 dias, em dia útil
cliente ativo do televendas é atendido a cada 15 dias, em dia útil
os demais clientes, inativos e prospects, são atendidos a cada 7 dias, em dia útil

## Estrutura

```yaml
publico: times de interior, capital, televendas, time exclusivo e times de ruptura
comuns: []
regras:
  - nome: Todos os clientes de VENDEDOR_07
    publico: VENDEDOR_07
    se:
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Ruptura de VENDEDOR_06, não agendar quem comprou nos últimos 30 dias
    publico: time de ruptura, VENDEDOR_06
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ruptura de VENDEDOR_06, demais clientes
    publico: time de ruptura, VENDEDOR_06
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ruptura de VENDEDOR_08, não agendar quem comprou nos últimos 30 dias
    publico: time de ruptura, VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ruptura de VENDEDOR_08, não agendar bloqueados
    publico: time de ruptura, VENDEDOR_08
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: bloqueado}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ruptura de VENDEDOR_08, demais clientes
    publico: time de ruptura, VENDEDOR_08
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar inativos inadimplentes do interior
    publico: time do interior, VENDEDOR_01 a VENDEDOR_05
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Demais clientes do interior
    publico: time do interior, VENDEDOR_01 a VENDEDOR_05
    se:
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar inativos inadimplentes da capital
    publico: time da capital, vendedores de campo exceto VENDEDOR_01 a VENDEDOR_06
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos inadimplentes da capital
    publico: time da capital, vendedores de campo exceto VENDEDOR_01 a VENDEDOR_06
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Demais clientes da capital
    publico: time da capital, vendedores de campo exceto VENDEDOR_01 a VENDEDOR_06
    se:
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos do televendas
    publico: televendas, exceto VENDEDOR_07 e VENDEDOR_08
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Demais clientes do televendas
    publico: televendas, exceto VENDEDOR_07 e VENDEDOR_08
    se:
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - preferência por dia útil
  - bloqueado
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Pet Nobre | empresa_foco | EMPRESA_FOCO |
| vendedor 39 | vendedor | VENDEDOR_01 |
| vendedor 16 | vendedor | VENDEDOR_02 |
| vendedor 40 | vendedor | VENDEDOR_03 |
| vendedor 6 | vendedor | VENDEDOR_04 |
| vendedor 45 | vendedor | VENDEDOR_05 |
| vendedor 55 | vendedor | VENDEDOR_06 |
| Jamile, ID 4 | vendedor | VENDEDOR_07 |
| Elizangela, vendedor 54 | vendedor | VENDEDOR_08 |
| televendas | jargao | atendimento por telefone |
| ruptura | jargao | carteira de clientes que pararam de comprar |
| bloqueado | jargao | cliente com cadastro bloqueado |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.
- A entrada não informa se a compra dos últimos 30 dias nas rupturas considera o vendedor ou qualquer vendedor.

## Ambiguidades

- O time de ruptura de VENDEDOR_06 é descrito como "da Jamile também", sem esclarecer se VENDEDOR_06 é outro identificador da mesma pessoa que VENDEDOR_07.
- "Preferência por dia útil" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
