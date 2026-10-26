---
id: regra_213
origem: simulacao/regra_213/entrada.md
gobr: simulacao/regra_213/regra_213.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 12
procedencia: corpus_sintetico
---

## Regras

cliente filial não é agendado
cliente ativo da rota de segunda é atendido semanalmente, na segunda, com frequência fixa
os demais clientes da rota de segunda são atendidos a cada 28 dias, na segunda, com frequência fixa
cliente ativo da rota de terça é atendido semanalmente, na terça, com frequência fixa
os demais clientes da rota de terça são atendidos a cada 28 dias, na terça, com frequência fixa
cliente ativo da rota de quarta é atendido semanalmente, na quarta, com frequência fixa
os demais clientes da rota de quarta são atendidos a cada 28 dias, na quarta, com frequência fixa
cliente ativo da rota de quinta é atendido semanalmente, na quinta, com frequência fixa
os demais clientes da rota de quinta são atendidos a cada 28 dias, na quinta, com frequência fixa
cliente ativo da rota de sexta é atendido semanalmente, na sexta, com frequência fixa
os demais clientes da rota de sexta são atendidos a cada 28 dias, na sexta, com frequência fixa
clientes das rotas 10 e 11, de Curitiba, são atendidos semanalmente, sem dia definido

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos da rota de segunda
    se:
      - {tipo: identificacao, op: igual_a, valor: ['24', '523', '524', '525', '526']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos da rota de segunda
    se:
      - {tipo: identificacao, op: igual_a, valor: ['24', '523', '524', '525', '526']}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Ativos da rota de terça
    se:
      - {tipo: identificacao, op: igual_a, valor: ['3', '4', '17', '500', '512', '514', '515']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos da rota de terça
    se:
      - {tipo: identificacao, op: igual_a, valor: ['3', '4', '17', '500', '512', '514', '515']}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Ativos da rota de quarta
    se:
      - {tipo: identificacao, op: igual_a, valor: ['502', '530', '531']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos da rota de quarta
    se:
      - {tipo: identificacao, op: igual_a, valor: ['502', '530', '531']}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Ativos da rota de quinta
    se:
      - {tipo: identificacao, op: igual_a, valor: ['20', '501', '504', '505', '506', '508', '513', '516', '527', '528']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: quinta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos da rota de quinta
    se:
      - {tipo: identificacao, op: igual_a, valor: ['20', '501', '504', '505', '506', '508', '513', '516', '527', '528']}
      - {tipo: periodo_vigencia, op: igual_a, valor: quinta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Ativos da rota de sexta
    se:
      - {tipo: identificacao, op: igual_a, valor: ['5', '19', '510', '511', '521']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos da rota de sexta
    se:
      - {tipo: identificacao, op: igual_a, valor: ['5', '19', '510', '511', '521']}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Carteira de Curitiba
    se:
      - {tipo: identificacao, op: igual_a, valor: ['10', '11']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - filial
  - código de rota
  - frequência fixa rígida
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| código de rota | jargao | identificador do roteiro de atendimento |
| filial | jargao | unidade filial de um cliente |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- "Semanal" foi registrado como 7 dias pela convenção de periodicidade.
- As regras de inativos não trazem critério explícito de inatividade e funcionam como residuais de cada rota.
