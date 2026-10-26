---
id: regra_205
origem: simulacao/regra_205/entrada.md
gobr: simulacao/regra_205/regra_205.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

clientes de Ponta Grossa são atendidos semanalmente, preferindo quinta e segunda
clientes das cidades da rota de terça são atendidos semanalmente, na terça
clientes das cidades da rota de quarta são atendidos semanalmente, na quarta
clientes das cidades da rota de sexta são atendidos semanalmente, na sexta
prospect com o vendedor é atendido a cada 28 dias
cliente sem compra há mais de 90 dias é atendido a cada 14 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Rota de quinta ou segunda
    se:
      - {tipo: localizacao, op: igual_a, valor: [Ponta Grossa]}
      - {tipo: periodo_vigencia, op: igual_a, valor: [quinta, segunda], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de terça
    se:
      - {tipo: localizacao, op: igual_a, valor: [Arapoti, Guamiranga, Imbituva, Ipiranga, Itararé, Ivaí, Jaguariaíva, Piraí do Sul, Prudentópolis, Sengés, Wenceslau Braz, Santo Antônio da Platina]}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de quarta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Caçador, Cândido de Abreu, Canoinhas, Imbaú, Lapa, Ortigueira, Porto Amazonas, Porto União, Reserva, São João do Triunfo, São Mateus do Sul, Telêmaco Borba, Tibagi, Três Barras, União da Vitória, Ventania]}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de sexta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Carambeí, Castro, Curitiba, Guarapuava, Imbituva, Ipiranga, Irati, Ivaí, Palmeira, Pitanga, Prudentópolis, Rebouças, Rio Azul, Teixeira Soares, Turvo, Adrianópolis, Agudos do Sul, Almirante Tamandaré, Araucária, Balsa Nova, Bocaiúva do Sul, Campina Grande do Sul, Campo do Tenente, Campo Largo, Campo Magro, Cerro Azul, Colombo, Contenda, Doutor Ulysses, Fazenda Rio Grande, Itaperuçu, Lapa, Mandirituba, Pien, Pinhais, Piraquara, Quatro Barras, Rio Branco do Sul, Rio Negro, São José dos Pinhais, Quitandinha, Tijucas do Sul, Tunas do Paraná]}
      - {tipo: periodo_vigencia, op: igual_a, valor: sexta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects do vendedor
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - rota por cidade
  - preferência de dias da semana
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| rota | jargao | roteiro de atendimento por cidade e dia |
| carteira livre | jargao | conjunto de clientes compartilhado |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não traz regra residual para clientes fora das rotas e dos perfis.

## Ambiguidades

- Algumas cidades aparecem em mais de uma rota (por exemplo, Imbituva, Ipiranga, Ivaí, Prudentópolis e Lapa).
- "Semanal" foi registrado como 7 dias pela convenção de periodicidade.
