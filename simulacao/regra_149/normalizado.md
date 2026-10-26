---
id: regra_149
origem: simulacao/regra_149/entrada.md
gobr: simulacao/regra_149/regra_149.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente que comprou nos últimos 7 dias não é agendado
prospect é atendido a cada 14 dias, preferindo dias úteis e sábado
ativo com compra entre 7 e 30 dias é atendido a cada 14 dias, preferindo dias úteis e sábado
ativo com compra entre 30 e 60 dias é atendido a cada 14 dias, preferindo dias úteis e sábado
ativo com compra entre 60 e 90 dias é atendido a cada 14 dias, preferindo dias úteis e sábado
inativos são atendidos a cada 14 dias, preferindo dias úteis e sábado

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar quem comprou nos últimos 7 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 7, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos com compra entre 7 e 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [7, 30], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos com compra entre 30 e 60 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [30, 60], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos com compra entre 60 e 90 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 90], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos
    se:
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - preferência por dias úteis e sábado
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Goiás Clean | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- As faixas de compra compartilham os limites 7, 30 e 60 dias.
- Todas as faixas com frequência têm o mesmo valor de 14 dias.
