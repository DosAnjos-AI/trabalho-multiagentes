---
id: regra_159
origem: simulacao/regra_159/entrada.md
gobr: simulacao/regra_159/regra_159.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente com faturamento no ano abaixo de 10 mil reais ou indefinido é atendido a cada 45 dias
cliente com faturamento no ano acima de 30 mil reais é atendido a cada 15 dias
os demais clientes, curva B, são atendidos a cada 30 dias
cliente com faturamento no ano abaixo de 5 mil reais ou indefinido é atendido a cada 45 dias
cliente com faturamento no ano acima de 20 mil reais é atendido a cada 15 dias
os demais clientes, curva B, são atendidos a cada 30 dias
cliente ativo é atendido semanalmente
os demais clientes são atendidos a cada 15 dias

## Estrutura

```yaml
publico: segmento bebê, segmento pet e todos os vendedores
comuns: []
regras:
  - nome: Curva C do segmento bebê
    publico: segmento bebê, VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: valor_cliente, op: menor_que, valor: 10000, unidade: reais, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 45 dias}
  - nome: Curva A do segmento bebê
    publico: segmento bebê, VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: valor_cliente, op: maior_que, valor: 30000, unidade: reais, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Curva B do segmento bebê
    publico: segmento bebê, VENDEDOR_01 e VENDEDOR_02
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Curva C do segmento pet
    publico: segmento pet, VENDEDOR_03 e VENDEDOR_04
    se:
      - {tipo: valor_cliente, op: menor_que, valor: 5000, unidade: reais, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 45 dias}
  - nome: Curva A do segmento pet
    publico: segmento pet, VENDEDOR_03 e VENDEDOR_04
    se:
      - {tipo: valor_cliente, op: maior_que, valor: 20000, unidade: reais, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Curva B do segmento pet
    publico: segmento pet, VENDEDOR_03 e VENDEDOR_04
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos, regra padrão
    publico: todos os vendedores
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes, regra padrão
    publico: todos os vendedores
    se: []
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario:
  - faturamento indefinido
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Brasgroup | empresa_foco | EMPRESA_FOCO |
| vendedor 2095 | vendedor | VENDEDOR_01 |
| vendedor 2152 | vendedor | VENDEDOR_02 |
| vendedor 2150 | vendedor | VENDEDOR_03 |
| vendedor 2151 | vendedor | VENDEDOR_04 |
| goVendas | jargao | plataforma de vendas |
| baby | jargao | segmento de produtos para bebê |
| curva A, B e C | jargao | faixas de cliente por faturamento |

## Lacunas

- A entrada não diz sobre qual carteira os times trabalham.

## Ambiguidades

- A condição "ou indefinido" da curva C não tem operador próprio; foi registrada apenas na descrição.
- "Semanal" para ativos foi registrado como 7 dias pela convenção de periodicidade.
- Os vendedores dos segmentos também pertencem ao time de todos os vendedores.
