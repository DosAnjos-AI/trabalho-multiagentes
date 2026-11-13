# Critério de avaliação v1 (documento de trabalho)

Escrito em 2026-11-13, **antes** de ler qualquer descrição `entrada_{id}.md` e antes de abrir qualquer `.gobr` de teste. Material lido até aqui: `manual/`, os 3 pares de `exemplos/`.

## 1. Unidade de contagem: "regra"

Uma **regra** é um bloco de nível superior do `.gobr`, identificado pela palavra-chave de cabeçalho:
`time`, `segmentacao`, `carteira`, `carteira livre`, `parametros`, `limpar parametros`, `alerta`, `tags`.

Não contam: a linha `version 1.0`, comentários `#`, linhas em branco.

Os números são dados em dois recortes, para não deixar o time (trivial) inflar o resultado:
- **todos os blocos**;
- **só blocos de regra de negócio** (`segmentacao`, `carteira`, `parametros`, `limpar parametros`, `alerta`, `tags`), sem `time`.

## 2. As três medidas objetivas

| Medida | Definição |
|---|---|
| Regras capturadas | Blocos do original que têm par na reconstrução (critério de "mesma regra" abaixo). Formato `capturadas / total do original` |
| Regras inventadas | Blocos da reconstrução sem par no original |
| Regra inteira correta | Pares que batem em **todos** os componentes (critério de "inteira correta" abaixo). Formato `corretas / total do original` |

## 3. Quando duas regras são "a mesma regra" (pareamento)

Um bloco reconstruído R e um bloco original O formam par se **todas** valem:

1. **Mesma categoria** (`parametros` com `parametros`, `carteira` com `carteira`/`carteira livre`, etc.). `limpar parametros` é categoria própria.
2. **Mesmo papel de negócio**: R e O selecionam o mesmo grupo de clientes no sentido de negócio — o mesmo conceito de filtro principal (ex.: "recência de compra", "prospect", "baixado na Receita", "inadimplente") ou, para blocos sem filtro, o mesmo papel (ex.: "regra de sobra/fallback no fim"). Valores numéricos diferentes **não** impedem o par (impedem só o "inteira correta").
   - Para `time`: mesmo conjunto-base de vendedores (todos / televendas / campo / por id).
3. **Pareamento um-para-um.** Cada bloco original pareia com no máximo um reconstruído e vice-versa. Havendo mais de um candidato, vale o de maior número de componentes iguais; empate, o mais próximo na ordem do arquivo.

O **nome** entre aspas não entra no pareamento: é texto livre.

## 4. Quando uma regra está "inteira correta"

Um par é **inteiro correto** se todos os componentes abaixo são equivalentes:

| Componente | Equivalência aceita |
|---|---|
| Categoria e modificador (`livre`) | idêntico |
| Fonte (`do time(...)`, `da carteira(...)`, `clientes ...`) | mesma função e mesmo alvo (alvo pareado pelo papel, já que nomes de time/carteira são livres) |
| Filtros temporais de calendário | mesmo conjunto de filtros com mesmos valores |
| Cada filtro do `quando` | mesmo filtro do manual, mesma variante (`global`, `do vendedor`, `com a empresa`...), mesmo operador, mesmos valores. Ordem dos filtros dentro do `quando` não importa (o manual diz que todos valem ao mesmo tempo) |
| Parâmetros de atendimento | mesmos parâmetros e mesmos valores. Aceita equivalência declarada no manual: `semanal()` = `de 7 dias`, `quinzenal()` = `de 15 dias`, `mensal()` = `de 30 dias`, etc. |
| `nao agendar`, `restrito`, `roteirizavel`, `fixo`, `sem choque` | presença e valores idênticos |
| Alertas: gatilho, `informe`, `entregue`, `pelos canais`, valores do template | mesmos itens e mesmos valores; o texto livre de `descreva com o texto(...)` vale se tiver as mesmas variáveis `$...$` e o mesmo sentido |
| Posição relativa | Onde a ordem muda o resultado (`parametros` entre si; `carteira` exclusiva entre si), o par precisa manter a mesma posição relativa aos demais pares da mesma categoria. Se a reconstrução troca a ordem de dois blocos cuja seleção se sobrepõe, os dois deixam de ser "inteiros corretos" |

Diferenças que **não** contam: nome do bloco, comentários, indentação, espaço em `do time ("x")`, grafia com/sem acento em palavra-chave (o parser aceita as duas, `manual/02-invariantes.md`).

Diferenças que **contam** mesmo parecendo próximas: trocar um filtro por outro de sentido vizinho que o manual define de forma diferente (ex.: `recencia de positivacao em 60 dias` × `recencia de positivacao global em 60 dias` × `atividade de 60 dias` × `inatividade de 60 dias`). O manual distingue esses filtros; tratar como iguais esconderia exatamente a perda que se quer medir.

## 5. Avaliação subjetiva (separada, sem nota)

Leitura qualitativa de cada descrição, em três itens, com escala de três níveis só para facilitar a leitura lado a lado (não entra em nenhuma conta):

| Item | O que se julga | Escala |
|---|---|---|
| Linguagem natural | Soa como alguém do comercial descrevendo o negócio, ou como o arquivo traduzido linha a linha? | negócio / misto / tradução |
| Apego à ordem do `.gobr` | Segue a ordem dos blocos do arquivo, ou reorganiza como quem explica (por objetivo, por grupo de clientes)? | reorganiza / parcial / segue o arquivo |
| Vazamento de vocabulário | Termos da linguagem GOBR no texto (palavras-chave, nomes de função, sintaxe) | lista literal dos termos encontrados |

Termo de negócio que coincide com palavra-chave (ex.: "prospect", "inadimplente", "frequência") **não** é vazamento por si só; é vazamento quando aparece na forma da linguagem (ex.: "recência de positivação global", "carteira fixa" como nome de função, `nao agendar`, "fixo", "roteirizável" usados como termo técnico).

## 6. O que esta avaliação não mede, e por quê

- **Validade sintática pelo parser real.** Não há parser GoBR disponível no projeto; a reconstrução é julgada contra o original, não executada.
- **Equivalência de resultado sobre dados reais.** Duas regras com filtros diferentes podem selecionar os mesmos clientes numa base específica; sem base de clientes, só a forma é comparável.
- **A capacidade de um agente automático.** Quem reconstrói é um único leitor (Claude), com o mesmo material fixo. Mede se a descrição basta para *este* leitor; outro leitor pode acertar mais ou menos.
- **Variância.** Cada combinação modelo × regra tem uma única descrição; não há repetições, então diferenças pequenas entre modelos podem ser ruído.
- **Qualidade do texto livre de alertas** além da presença das variáveis e do sentido.
- **Se a descrição é útil para um humano.** Só se mede a reconstrução.

## 7. Viés declarado

O avaliador é o mesmo que reconstrói. A ordem fixa (critério -> reconstrução gravada -> gabarito) é o contrapeso: depois de gravadas, as reconstruções não são alteradas.
