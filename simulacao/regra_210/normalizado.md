---
id: regra_210
origem: simulacao/regra_210/entrada.md
gobr: simulacao/regra_210/regra_210.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente filial não é agendado
cliente inadimplente não é agendado
cliente bloqueado não é agendado
cliente com uma única compra com o vendedor é atendido a cada 30 dias
cliente com compra entre 181 e 365 dias é atendido a cada 30 dias
cliente sem compra há mais de 365 dias é atendido a cada 30 dias
o restante, ativo fidelizado, é atendido a cada 30 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar bloqueados
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: bloqueado}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Cliente esquecido
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [181, 365], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 365, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativo fidelizado
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - filial
  - bloqueado
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| filial | jargao | unidade filial de um cliente |
| bloqueado | jargao | cliente com cadastro bloqueado |
| fidelizado | jargao | cliente que compra com constância |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- Todas as regras de agendamento têm a mesma frequência de 30 dias.
