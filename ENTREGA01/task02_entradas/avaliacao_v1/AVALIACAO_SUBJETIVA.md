# Avaliação subjetiva das 12 descrições (prompt_v1)

Leitura, não nota. Escala definida em `CRITERIO_AVALIACAO_v1.md`, seção 5. Nada aqui entra nas medidas objetivas, e as medidas objetivas não foram usadas para justificar nenhum julgamento abaixo.

Ordem em que as descrições foram lidas (relevante porque a leitura de uma contamina a seguinte da mesma regra):
- regra_020: luna, terra, flash-lite, flash
- regra_228: terra, flash-lite, flash, luna
- regra_032: flash-lite, flash, luna, terra

## regra_020 (1 regra simples)

| Modelo | Linguagem natural | Ordem | Vazamento de vocabulário |
|---|---|---|---|
| gpt-6-luna | negócio | n/a (uma regra) | nenhum |
| gpt-6.1-terra | negócio | n/a | nenhum |
| gemini-3.5-flash-lite | misto | n/a | "regra padrão e customizável" (pedaço do nome do bloco tratado como conceito); "com uma frequência de 7 dias" |
| gemini-3.6-flash | misto | n/a | cita o nome do bloco inteiro entre aspas; "carteira fixa" |

Leitura: os dois GPT resolvem em uma ou duas frases, como alguém falaria. Os dois Gemini acrescentam enchimento ("nossa operação com a empresa toda", "orientação geral") e o flash cola o nome técnico do bloco. Para uma regra trivial, todos bastam.

## regra_228 (6 situações em cascata)

| Modelo | Linguagem natural | Ordem | Vazamento de vocabulário |
|---|---|---|---|
| gpt-6.1-terra | negócio | segue o arquivo | "prospects para o vendedor", "única compra com esse vendedor", "curva C da empresa" (decalques de `no ciclo de vida prospect com o vendedor`, `unica compra com o vendedor`, `curva c com a empresa`) |
| gemini-3.5-flash-lite | negócio | segue o arquivo, mas com agrupamento narrativo ("começando a comprar", "compram com regularidade", "dando uma sumida") | baixo: nomes de situação entre aspas. Acrescenta inferências que não estão no arquivo: "novos cadastros", "ou seja, as curvas A e B", "primeira compra" no lugar de "única compra" |
| gemini-3.6-flash | misto | segue o arquivo | alto: "prospect no seu ciclo de vida com o vendedor", "Curva C com a empresa", "única compra com o vendedor" |
| gpt-6-luna | tradução | segue o arquivo | médio, mais **comentário sobre o arquivo**: "A regra chamada 'Curva A e B' não especifica a curva como condição", "na regra de resgate" |

Leitura: o flash-lite é o mais agradável de ler e o que mais parece uma pessoa explicando; também é o que mais inventa interpretação. O luna fala do arquivo, não do negócio. Todos seguem a ordem do arquivo; aqui a ordem é a prioridade, então seguir é correto.

## regra_032 (75 parâmetros, 2 carteiras)

| Modelo | Linguagem natural | Ordem | Vazamento de vocabulário |
|---|---|---|---|
| gemini-3.5-flash-lite | negócio | segue o arquivo (genéricas, Sul/Sudeste/CO, Norte/Nordeste) | baixo: "ciclo de vida de prospect com a empresa", "Curva A/B/C" tratada como condição. Contradições internas: "ativos com 150 dias sem compra"; "inativos, que são os clientes sem limite recente de compra" |
| gemini-3.6-flash | tradução | segue o arquivo bloco a bloco: os 72 nomes de bloco aparecem entre parênteses, na ordem do arquivo | alto: "carteira de Sul...", "recência de compra (positivação global)", "média faturada no ano com a empresa", códigos `MATCON`, `CONS. FINAL` |
| gpt-6-luna | tradução | segue o arquivo bloco a bloco | alto: "positivação global", "média faturada no ano com a empresa", "sem condição de recência", e comentário sobre o arquivo: "sem a indicação de que seja global", "não especifica intervalo de visita" |
| gpt-6.1-terra | negócio | reorganiza: primeiro os prazos por região, depois as faixas por grupo de ramo, juntando as duas regiões | médio: "média faturada no ano com a empresa"; troca "global" por "compras com todos os vendedores" (boa paráfrase); traduz códigos (`MATCON` vira "material de construção") |

Leitura: é a regra que separa os modelos. O terra é o único que escreve como alguém que entende o padrão e o explica uma vez só, comprimindo 72 situações em quatro parágrafos. O flash e o luna escrevem uma linha de texto por bloco; são longos, repetitivos e, no caso do flash, praticamente uma listagem do arquivo em prosa. O flash-lite fica no meio: escreve bem, mas reinterpreta.

## Síntese da leitura

- Mais natural: **gpt-6.1-terra** (melhor na 032, bom nas outras), seguido de **gemini-3.5-flash-lite**.
- Menos natural: **gemini-3.6-flash** e **gpt-6-luna**, ambos espelham o arquivo nas regras longas e vazam vocabulário; o luna ainda comenta o próprio arquivo.
- Ordem: só o terra reorganizou de verdade, e só na 032. Na 228 todos seguiram o arquivo, o que ali coincide com a prioridade.
