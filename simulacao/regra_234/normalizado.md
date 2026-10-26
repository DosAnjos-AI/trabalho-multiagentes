---
id: regra_234
origem: simulacao/regra_234/entrada.md
gobr: simulacao/regra_234/regra_234.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente com queda de faturamento acima de 5% é atendido a cada 3 dias
cliente há mais de 1138 dias sem comprar não é agendado
clientes de Goiânia usam a frequência média dos inativos da empresa, preferindo dias úteis, sábado e domingo
cliente ativo usa a frequência média dos ativos da empresa, preferindo dias úteis, sábado e domingo
cliente inativo usa a frequência média dos inativos da empresa, preferindo dias úteis, sábado e domingo
cliente sem vendas usa a frequência média dos inativos da empresa, preferindo dias úteis, sábado e domingo
os demais clientes são atendidos a cada 7 dias, preferindo dias úteis

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
regras:
  - nome: Queda de faturamento
    se:
      - {tipo: valor_cliente, op: maior_que, valor: 5, unidade: percentual}
    entao: {acao: agendar, frequencia: fixa 3 dias}
  - nome: Não agendar mais de 1138 dias sem comprar
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 1138, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Teste de Goiânia
    se:
      - {tipo: localizacao, op: igual_a, valor: [Goiânia]}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado, domingo], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Clientes ativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado, domingo], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Clientes inativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado, domingo], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Clientes sem vendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado, domingo], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Regra padrão
    se:
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - queda de faturamento
  - preferência de dias da semana
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| goVendas | jargao | plataforma de vendas |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| queda de faturamento | jargao | redução percentual do valor comprado |
| sem vendas | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa o período de referência da queda de faturamento nem o valor em dias das médias da empresa.

## Ambiguidades

- A regra de Goiânia é descrita como teste; não fica claro se é provisória.
