# ARQUITETURA DO RETRIEVER

> Documento de arquitetura. Descreve **o que** o sistema é e **por que** foi
> desenhado assim. Para instruções de execução, ver `retriever/README.md`.

Estado em 10/11/2026. Branch `feature/indexacao-vetorial`.

---

## 1. O PROBLEMA

Transformar um pedido em português comum numa regra escrita em **GOBR**, a DSL de
parametrização do sistema Govendas.

| Entrada | Saída pretendida |
|---|---|
| "quero visitar os clientes do televendas que não compram há 90 dias duas vezes por semana" | Arquivo `.gobr` sintaticamente válido, com os blocos corretos |

O mecanismo é **RAG**: recuperar exemplos parecidos e as regras de sintaxe
pertinentes, e escrever a regra a partir desse contexto.

**Este componente recupera. Ele não escreve o `.gobr`.** A geração é outra
frente, ainda inexistente.

---

## 2. AS TRÊS FONTES, E POR QUE OS PAPÉIS NÃO SE MISTURAM

| Fonte | O que é | Papel | O que **não** faz |
|---|---|---|---|
| `govendas-rules.pdf` e `manual/` | Manual do Govendas Business Rules, 62 páginas, e os artefatos derivados dele | **Única** fonte de validade sintática | Não decide qual forma usar entre várias válidas |
| `simulacao/` | 249 pastas com pedido, normalizado e regra `.gobr` real | Evidência de uso: escolhe entre formas válidas | **Nunca** cria validade |
| `NORMALIZACAO.md` | O prompt que converte pedido livre em forma semi-estruturada | Define o contrato da consulta | Não define sintaxe de GOBR |

### Precedência entre manual e exemplos

Construída em três rodadas de auditoria, e custou retrabalho.

| Nível | Fonte | Decide |
|---|---|---|
| 1 | Manual | O que é **válido** |
| 2 | `simulacao/` | Qual forma **emitir**, entre as já válidas pelo nível 1 |

- Presença em volume no corpus autoriza **preferir** a forma.
- Ausência no corpus **não invalida** forma que o manual mostra. Ausência é
  desuso, nada além.
- Divergência entre manual e corpus não se resolve sozinha: vai a relatório.

---

## 3. AS DUAS RECUPERAÇÕES, E POR QUE SÃO DIFERENTES

O sistema recupera duas coisas, por dois mecanismos distintos. Misturá-los foi
considerado e descartado.

| O que se recupera | Mecanismo | Por quê |
|---|---|---|
| **Exemplos** — regras parecidas já escritas | Busca vetorial por similaridade | Não existe chave que diga "parecido". Similaridade é o único caminho |
| **Trechos do manual** — regras de sintaxe pertinentes | Chaveamento lógico por tabela | Regra de sintaxe se busca **por chave**, não por semelhança. Buscar sintaxe por similaridade devolve o trecho parecido, não o correto |

**O manual nunca entra no banco vetorial.** É decisão de desenho, não omissão.

---

## 4. A ASSIMETRIA QUE GOVERNA O DESENHO

O texto indexado **não pode ser mais rico que um pedido real**.

Se o índice contiver informação que um usuário nunca forneceria, a busca compara
coisas diferentes e degrada em produção. Isso já aconteceu uma vez: o normalizado
ficou maior que a própria regra `.gobr`, sinal de sobreajuste, e o formato foi
refeito.

Três consequências práticas:

| Consequência | Motivo |
|---|---|
| O vocabulário de critérios é **comercial e genérico**, deliberadamente não derivado da DSL nem do manual | O usuário pede em linguagem comercial, não em termos da DSL. Houve duas tentativas de puxar vocabulário do manual, ambas revertidas |
| O `.gobr` **nunca** é embeddado | Usá-lo como fonte do normalizado seria sobreajuste. Ele entra por caminho (`gobr_path`), e é lido só na geração |
| Só a seção de regras do normalizado vira vetor | O arquivo inteiro traz estrutura e dicionário que o pedido do usuário não tem |

---

## 5. FERRAMENTAS

| Camada | Escolha | Observação |
|---|---|---|
| Normalizador | `gpt-4.1-mini-2025-04-14`, temperatura 0 | Aceita texto e imagem. **Não** aceita áudio nesta versão |
| Banco vetorial | ChromaDB 1.5.9, embarcado e persistente | Coleção `regras_govendas`, 249 documentos, `hnsw:space: cosine` |
| Modelo de embedding | `intfloat/multilingual-e5-base`, 768 dimensões, CPU | Prefixos `passage:` na indexação e `query:` na consulta; truncamento em 512 tokens |
| Canal léxico | Índice de termo exato, 690 chaves | `indexacao/dados/indice_lexico.json` |
| Reranking | `cross-encoder/mmarco-mMiniLMv2-L12-H384-v1`, 471 MB | **Desligado por padrão.** Ver seção 8 |
| Ambiente | Python 3.12, CPU, sem GPU disponível | O banco **não é versionado**: clone limpo não tem índice |

---

## 6. O PIPELINE

```
pedido do usuário  (texto ou imagem)
  │
  ├─1─ NORMALIZAR        chamada ao LLM com o prompt de NORMALIZACAO.md
  │                      saída: forma semi-estruturada, formato antigo
  │
  ├─2─ VALIDAR           conformidade de contrato
  │                      recontagem obrigatória do total de regras
  │
  ├─3─ CONVERTER         módulo versionado escritor_v40.py, em memória
  │                      é aqui que a seção de regras passa a existir
  │
  ├─4─ EXTRAIR           seção de regras  +  lista de tipos de critério
  │                      +  termos do dicionário
  │
  ├─5─ PRÉ-FILTRO        canal léxico, termos do dicionário
  │                      saída: pool de candidatos
  │
  ├─6─ BUSCA VETORIAL    dentro do pool, prefixo query:
  │                      saída: top-N com similaridade e distância
  │
  ├─7─ DEDUP             por texto de regras idêntico
  │                      saída: top-N sem cópias
  │
  ├─8─ RERANKING         OPCIONAL, desligado por padrão
  │
  ├─9─ CHAVEAMENTO       parte fixa + seções do manual pelos tipos
  │                      resolvido por manual/03-mapa.md
  │
  └10─ SAÍDA             lista explícita + rastro persistido em JSON
```

### O que cada etapa produz

| Etapa | Produto | Nota |
|---|---|---|
| 1 | Forma semi-estruturada | **Gargalo de latência**: p50 de ~9,5 s. É também a única etapa não determinística |
| 2 | Mesmo objeto, com o total recontado | Sem essa recontagem, 44,6% dos pedidos se perdem na conversão |
| 3 | Forma final, com a seção de regras | Usa o módulo versionado, nunca uma montagem própria |
| 4 | Consulta, tipos e termos | Os três alimentam etapas diferentes |
| 5 | Pool de candidatos | Mediana de 112 de 249. Pool vazio cai para todos, e **registra** |
| 6 | Candidatos pontuados | ~1,6 ms. A busca não é o custo |
| 7 | Candidatos sem cópias | Pool de 9,85 para 6,32 documentos |
| 8 | Candidatos reordenados | Ver seção 8 |
| 9 | Arquivos do manual | Parte fixa sempre, mais os chaveados. Mediana de ~3.900 tokens |
| 10 | Lista final e rastro | O rastro é a forma canônica; o terminal é conveniência |

### Composição do contexto que irá ao gerador

Quando o gerador existir, ele receberá:

> exemplos recuperados (normalizado + `.gobr` lido pelo caminho do payload)
> + parte fixa do manual, sempre
> + seções do manual chaveadas pelos tipos do pedido

A parte fixa é `manual/02-invariantes.md` e `manual/03-secoes/10-gramatica.md`.
O arquivo `manual/01-conceitos.md` **não** entra: é prompt do normalizador, não
do gerador.

---

## 7. O QUE FOI DESCARTADO, E COM QUE FORÇA DE EVIDÊNCIA

Sem esta seção, alguém reabre estas discussões em alguns meses.

| Descartado | Medição | Veredito |
|---|---|---|
| **Pedido bruto como consulta** | recall@1 0,268 contra 0,341 do normalizado, nas 138 comparáveis | Normalizar a consulta ajuda |
| **Filtro duro por metadado** | **21,0% de falso negativo**: exclui o documento certo | Descartado. Falha silenciosa é o custo mais caro |
| **Um vetor por regra individual** | recall@1 0,116 contra 0,341. 1.720 vetores | Descartado com folga |
| **Manual em banco vetorial** | Decisão de desenho, não medição | Sintaxe se busca por chave |
| **Pré-filtro pelos termos da seção de regras** | 31% de falso negativo, contra **0%** pelos termos do dicionário | Descartado. A fonte de termos é o dicionário |

O pré-filtro léxico pelo dicionário é o que melhor pontuou: recall@1 0,391, zero
falso negativo, e pool mediano de 201 para 112.

**Ressalva de leitura obrigatória:** os pedidos e os normalizados do corpus são
**sintéticos, gerados por IA**. O "documento correto" é concordância entre duas
gerações probabilísticas, não verdade. A **ordem** entre as alternativas informa;
o valor absoluto, pouco.

---

## 8. POR QUE O RERANKING ESTÁ DESLIGADO

| Medição | Valor |
|---|---|
| Ganho em recall@1 sobre o melhor caminho | +0,016 |
| Na única observação detalhada | Levou o documento de origem da 3ª para a 9ª posição |
| Latência | p50 ~335 ms para um top-10, em CPU |

[HIPÓTESE] O cross-encoder foi treinado para pergunta contra passagem, e aqui os
dois lados são regra em prosa — caso diferente do que ele aprendeu. Confirmável
medindo por cobertura de construto, não por posição da origem.

Fica disponível por parâmetro, com a pontuação registrada no rastro, para ser
reavaliado quando houver métrica de alvo real.

---

## 9. PRINCÍPIOS DE FALHA

**Falha alta é barata; falha silenciosa é cara.** O pipeline falha alto em cinco
pontos, de propósito:

| Ponto | Comportamento |
|---|---|
| Entrada inválida ou ambígua | Falha, dizendo o que encontrou e o que aceita |
| Normalizado que não converte | Falha, dizendo o que recebeu, o que esperava e onde configurar |
| Seção de regras vazia | Falha. Consulta vazia recuperaria qualquer coisa |
| Tipo de critério fora da lista fechada | Falha, listando os aceitos. Erro de digitação não vira comportamento |
| Arquivo do manual citado no mapa e ausente | Falha, nomeando o arquivo |

Duas exceções deliberadas, que **registram** em vez de falhar:

- Pool léxico vazio cai para o conjunto completo, e marca isso no rastro. Pool
  vazio nunca pode virar resposta vazia.
- Pedido sem nenhum tipo de critério recebe só a parte fixa do manual. Nunca os
  18 arquivos "por garantia".

---

## 10. LIMITAÇÕES CONHECIDAS

| Limitação | Efeito |
|---|---|
| **O pipeline não é reproduzível** | Com o mesmo pedido, prompt, modelo, temperatura 0 e semente fixa, o normalizador devolve saídas diferentes. Pool de 112 contra 63 em duas execuções. Da normalização em diante, o caminho é determinístico |
| `capacidade` falta no mapa e na configuração | Todo pedido com limite de atendimentos **falha alto** hoje |
| Parâmetros de atendimento e itens transversais não são chaveados | Os arquivos de alerta e de tags nunca chegam ao gerador |
| Qualidade do manual recuperado nunca foi avaliada | Não existe gabarito: ninguém rotulou qual seção cada regra precisa |
| 7 grupos de cópias no corpus, o maior com 18 membros | Sem dedup, um exemplo ocupa o contexto inteiro |
| 5 de 249 documentos passam de 512 tokens | Truncados em silêncio pelo modelo de embedding |
| O banco não é versionado | Clone limpo não tem índice. Precisa ser reconstruído |

---

## 11. ADVERTÊNCIA OPERACIONAL

Abrir o banco com o cliente persistente do Chroma **regrava os arquivos ao
fechar**, mesmo em leitura. Já ocorreu uma vez, sem backup.

Toda leitura do banco é feita **por cópia**. Existe uma cópia de segurança, fora
do controle de versão.

---

## 12. O QUE AINDA NÃO EXISTE

| Componente | Estado |
|---|---|
| Gerador — montagem do prompt e emissão do `.gobr` | **Não existe** |
| Orquestração do agente | **Não existe** |
| Entrada por áudio | **Não existe.** Exigiria transcrição antes do normalizador |
| Métrica de alvo real — validade sintática e cobertura de construto do `.gobr` gerado | **Não existe.** É o que permitiria avaliar a recuperação pelo que importa |
