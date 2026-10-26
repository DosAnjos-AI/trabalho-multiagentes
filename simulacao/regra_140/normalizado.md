---
id: regra_140
origem: simulacao/regra_140/entrada.md
gobr: simulacao/regra_140/regra_140.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 30
procedencia: corpus_sintetico
---

## Regras

cliente pessoa física não é agendado
cliente filial não é agendado
cliente inadimplente não é agendado
cliente dos cinco grupos de rota que teve visita nos últimos 3 dias não é agendado
cliente sem venda com o vendedor nas rotas de dia variável é atendido semanalmente
cliente com compra nos últimos 21 dias nas rotas de dia variável é atendido semanalmente
cliente com compra entre 21 e 41 dias nas rotas de dia variável é atendido semanalmente
cliente com compra entre 41 e 90 dias nas rotas de dia variável é atendido semanalmente
cliente sem compra há mais de 90 dias nas rotas de dia variável é atendido semanalmente
cliente sem venda com o vendedor nas rotas 3 e 4 é atendido semanalmente, na segunda, com frequência fixa
cliente com compra nos últimos 21 dias nas rotas 3 e 4 é atendido semanalmente, na segunda, com frequência fixa
cliente com compra entre 21 e 41 dias nas rotas 3 e 4 é atendido semanalmente, na segunda, com frequência fixa
cliente com compra entre 41 e 90 dias nas rotas 3 e 4 é atendido semanalmente, na segunda, com frequência fixa
cliente sem compra há mais de 90 dias nas rotas 3 e 4 é atendido semanalmente, na segunda, com frequência fixa
cliente sem venda com o vendedor na rota 5 é atendido semanalmente, na terça, com frequência fixa
cliente com compra nos últimos 21 dias na rota 5 é atendido semanalmente, na terça, com frequência fixa
cliente com compra entre 21 e 41 dias na rota 5 é atendido semanalmente, na terça, com frequência fixa
cliente com compra entre 41 e 90 dias na rota 5 é atendido semanalmente, na terça, com frequência fixa
cliente sem compra há mais de 90 dias na rota 5 é atendido semanalmente, na terça, com frequência fixa
cliente sem venda com o vendedor na rota 6 é atendido semanalmente, na quarta, com frequência fixa
cliente com compra nos últimos 21 dias na rota 6 é atendido semanalmente, na quarta, com frequência fixa
cliente com compra entre 21 e 41 dias na rota 6 é atendido semanalmente, na quarta, com frequência fixa
cliente com compra entre 41 e 90 dias na rota 6 é atendido semanalmente, na quarta, com frequência fixa
cliente sem compra há mais de 90 dias na rota 6 é atendido semanalmente, na quarta, com frequência fixa
cliente sem venda com o vendedor na rota 7 é atendido semanalmente, na sexta, com frequência fixa
cliente com compra nos últimos 21 dias na rota 7 é atendido semanalmente, na sexta, com frequência fixa
cliente com compra entre 21 e 41 dias na rota 7 é atendido semanalmente, na sexta, com frequência fixa
cliente com compra entre 41 e 90 dias na rota 7 é atendido semanalmente, na sexta, com frequência fixa
cliente sem compra há mais de 90 dias na rota 7 é atendido semanalmente, na sexta, com frequência fixa
qualquer cliente do televendas sem rota associada é atendido semanalmente

## Estrutura

```yaml
publico: time de televendas
comuns: []
regras:
  - nome: Não agendar pessoa física
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa física}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar com visita recente
    se:
      - {tipo: identificacao, op: igual_a, valor: ['8', '9', '10', '11', '3', '4', '5', '6', '7']}
      - {tipo: tempo_sem_visita, op: dentro_de, valor: 3, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Rotas 8 a 11, primeira compra
    se:
      - {tipo: identificacao, op: igual_a, valor: ['8', '9', '10', '11']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, terça, quarta, quinta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rotas 8 a 11, compra regular
    se:
      - {tipo: identificacao, op: igual_a, valor: ['8', '9', '10', '11']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 21, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, terça, quarta, quinta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rotas 8 a 11, estimular regularidade
    se:
      - {tipo: identificacao, op: igual_a, valor: ['8', '9', '10', '11']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [21, 41], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, terça, quarta, quinta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rotas 8 a 11, risco de inatividade
    se:
      - {tipo: identificacao, op: igual_a, valor: ['8', '9', '10', '11']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [41, 90], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, terça, quarta, quinta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rotas 8 a 11, sem compra há mais de 90 dias
    se:
      - {tipo: identificacao, op: igual_a, valor: ['8', '9', '10', '11']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, terça, quarta, quinta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rotas 3 e 4, primeira compra
    se:
      - {tipo: identificacao, op: igual_a, valor: ['3', '4']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rotas 3 e 4, compra regular
    se:
      - {tipo: identificacao, op: igual_a, valor: ['3', '4']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 21, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rotas 3 e 4, estimular regularidade
    se:
      - {tipo: identificacao, op: igual_a, valor: ['3', '4']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [21, 41], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rotas 3 e 4, risco de inatividade
    se:
      - {tipo: identificacao, op: igual_a, valor: ['3', '4']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [41, 90], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rotas 3 e 4, sem compra há mais de 90 dias
    se:
      - {tipo: identificacao, op: igual_a, valor: ['3', '4']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 5, primeira compra
    se:
      - {tipo: identificacao, op: igual_a, valor: ['5']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 5, compra regular
    se:
      - {tipo: identificacao, op: igual_a, valor: ['5']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 21, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 5, estimular regularidade
    se:
      - {tipo: identificacao, op: igual_a, valor: ['5']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [21, 41], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 5, risco de inatividade
    se:
      - {tipo: identificacao, op: igual_a, valor: ['5']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [41, 90], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 5, sem compra há mais de 90 dias
    se:
      - {tipo: identificacao, op: igual_a, valor: ['5']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 6, primeira compra
    se:
      - {tipo: identificacao, op: igual_a, valor: ['6']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 6, compra regular
    se:
      - {tipo: identificacao, op: igual_a, valor: ['6']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 21, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 6, estimular regularidade
    se:
      - {tipo: identificacao, op: igual_a, valor: ['6']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [21, 41], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 6, risco de inatividade
    se:
      - {tipo: identificacao, op: igual_a, valor: ['6']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [41, 90], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 6, sem compra há mais de 90 dias
    se:
      - {tipo: identificacao, op: igual_a, valor: ['6']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 7, primeira compra
    se:
      - {tipo: identificacao, op: igual_a, valor: ['7']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 7, compra regular
    se:
      - {tipo: identificacao, op: igual_a, valor: ['7']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 21, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 7, estimular regularidade
    se:
      - {tipo: identificacao, op: igual_a, valor: ['7']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [21, 41], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 7, risco de inatividade
    se:
      - {tipo: identificacao, op: igual_a, valor: ['7']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [41, 90], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota 7, sem compra há mais de 90 dias
    se:
      - {tipo: identificacao, op: igual_a, valor: ['7']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Clientes sem rota associada
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - pessoa física
  - filial
  - código de rota
  - frequência fixa rígida
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| rota | jargao | roteiro de atendimento identificado por código |
| filial | jargao | unidade filial de um cliente |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| parametrização fixa | jargao | frequência travada, sem ajuste automático |

## Lacunas

- A entrada não informa se as faixas de compra de 21 a 41 dias e de 41 a 90 dias consideram o vendedor ou qualquer vendedor da empresa.

## Ambiguidades

- As faixas "nos últimos 21 dias", "entre 21 e 41" e "entre 41 e 90 dias" compartilham os limites 21 e 41.
- As cinco situações de cada rota têm a mesma frequência semanal, o que torna a distinção entre elas irrelevante para a frequência.
- Os dias preferenciais das rotas fixas são preferências de agendamento; registrados como critério de período por falta de campo próprio.
