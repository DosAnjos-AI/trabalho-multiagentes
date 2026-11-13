# Resultado da validação v2 (reconstrução cega)

Data: 2026-11-13. Reconstrutor e avaliador: Claude (esta sessão), lendo uma descrição por vez com o material fixo (`manual/`, `govendas-rules.pdf`, os 3 pares de `exemplos/`).

## Ressalva obrigatória

O `prompt_v2` foi escrito por Claude, em outra sessão, **já conhecendo os gabaritos das três regras de teste**. A comparação v1 contra v2 está enviesada a favor do v2. O número vale como sinal, não como prova. Prova exigiria medir o v2 em regras que ninguém viu.

Outros vieses: o reconstrutor é o mesmo que avalia (critério v1, seção 7); cada combinação modelo × regra tem uma descrição só, sem repetição; a avaliação subjetiva foi escrita depois de ver os números (a ordem dos passos pedia isso).

## De onde vêm os números

| Arquivo | Conteúdo | Comando |
|---|---|---|
| `comparacoes/_saida_comparar_v2.json` | as três medidas, os pares, o que faltou e o que foi inventado | `.venv/bin/python ENTREGA01/task02_entradas/avaliacao_v2/comparar_v2.py` |
| `comparacoes/_saida_comparar_v2_caixa_estrita.json` | idem, com caixa estrita também em palavra-chave | mesmo comando com `--caixa-estrita` |
| `comparacoes/_saida_contar_vazamento.json` | custo, palavras e termos de vazamento por descrição | `.venv/bin/python ENTREGA01/task02_entradas/avaliacao_v2/contar_vazamento.py` |
| `comparacoes/{modelo}_regra_{id}.md` | uma comparação por descrição, gerada a partir do primeiro JSON | — |
| `HASHES_RECONSTRUCOES.txt` | sha256 das 36 reconstruções, gravado às 18:54:29, antes de abrir qualquer gabarito | `sha256sum -c HASHES_RECONSTRUCOES.txt` dentro de `avaliacao_v2/`: 36 OK depois da comparação |

Total de blocos dos originais: 020 = 3, 228 = 7, 032 = 78, **soma 88** (85 sem `time`).

## Extensões do critério v1 (declaradas)

| Id | Extensão | Por quê |
|---|---|---|
| E1 | Caixa de palavra-chave fora de aspas não conta; valores entre aspas são comparados literais | Decidido em `ORDEM_DE_TRABALHO.md` antes de ver o gabarito: o manual não declara diferença de caixa em palavra-chave (p.58 só fala de tags). Valores são dado do cadastro, e o estrito da v1 também os comparava literais. Efeito: só `curva C` × `curva c` na 228 (-1 em 6 modelos no estrito, coluna auxiliar nos arquivos de comparação) |
| E2 | Parêntese não fechado no fim de bloco é fechado na normalização | O último bloco do gabarito 032 está truncado: `quando ramo de atividade igual("CONS. FINAL"` sem `)` e sem frequência. Conta como bloco; a reconstrução é inteira correta se tiver só o filtro de ramo e nenhum parâmetro |
| E3 | Fonte com várias carteiras (`da carteira("a","b")`) vira conjunto; pareia com fonte que contenha uma delas ou com `do time` do mesmo time | O gabarito 032 usa essa forma no bloco de prospects; o critério v1 não previa fonte múltipla |
| E4 | Filtro de estado `inativos`/`inatividade` não define papel no pareamento | Bloco de inativos/sobra pareia com bloco de inativos/sobra, com ou sem esse filtro; a diferença conta só no "inteira correta" |
| E5 | Papel do time = posição no arquivo; papel da carteira = definição dela | Sem isso, errar o time (`ativados`) derrubava o pareamento de todo bloco que o usa, contando o mesmo erro dezenas de vezes |

## Tabela de decisão

Medidas somadas nas três regras, com o detalhe `020/228/032` entre parênteses. Total do original = 88.

| Modelo | Fornecedor | Faixa | Capturadas | Inventadas | Inteira correta | Linguagem natural (posição) | Vazamento (sintaxe + nomes) | Custo das 3 descrições (US$) | Posição de leitura 020/228/032 |
|---|---|---|---|---|---|---|---|---|---|
| gpt-6-luna | openai | mais barato | 88 (3/7/78) | 1 (0/0/1) | **86** (3/7/76) | 4 | 1 (0 + 1) | 0,003957 | 1/9/5 |
| gemini-3.8-flash | gemini | intermediário (derivada) | 88 (3/7/78) | 1 (0/0/1) | 84 (3/7/74) | 5 | 5 (5 + 0) | 0,047937 | 5/1/9 |
| gpt-4.1-mini-2025-04-14 | openai | mais barato (derivada) | 88 (3/7/78) | 1 (0/0/1) | 83 (3/5/75) | 10 | 27 (8 + 19) | 0,008993 | 4/12/8 |
| gemini-4-carbon | gemini | melhor | 88 (3/7/78) | 1 (0/0/1) | 82 (3/3/76) | 2 | 0 | 0,164602 | 8/4/12 |
| gpt-6-astra | openai | melhor | 88 (3/7/78) | 1 (0/0/1) | 82 (3/3/76) | 3 | 0 | 0,227620 | 3/11/7 |
| gpt-6.1-terra | openai | intermediário | 88 (3/7/78) | 1 (0/0/1) | 80 (3/3/74) | **1** | 0 | 0,019702 | 12/8/4 |
| gemini-3.5-flash-lite | gemini | mais barato (derivada) | 88 (3/7/78) | 1 (0/0/1) | 79 (3/3/73) | 7 | 16 (3 + 13) | 0,008967 | 10/6/2 |
| gemini-3.6-flash | gemini | intermediário | 88 (3/7/78) | 1 (0/0/1) | 60 (3/7/50) | 6 | 6 (5 + 1) | 0,071592 | 9/5/1 |
| gpt-5-mini-2025-08-07 | openai | mais barato (derivada) | 88 (3/7/78) | 1 (0/0/1) | 56 (3/3/50) | 12 | 48 (12 + 36), mais 97 "days" | 0,026686 | 11/7/3 |
| gemini-3.1-flash-lite | gemini | mais barato | 60 (3/7/50) | 0 | 50 (3/3/44) | 8 | 15 (8 + 7) | 0,005210 | 7/3/11 |
| gpt-5.4-mini-2026-03-17 | openai | intermediário (derivada) | 88 (3/7/78) | 1 (0/0/1) | 37 (3/7/27) | 11 | 37 (18 + 19) | 0,017293 | 2/10/6 |
| gpt-4o-mini-2024-07-18 | openai | mais barato (derivada) | 19 (3/7/9) | 1 (0/0/1) | 13 (3/6/4) | 9 | 8 (8 + 0) | 0,002559 | 6/2/10 |

Recorte sem `time` (inteira correta / 85): luna 83, 3.8-flash 81, 4.1-mini 81, carbon 79, astra 79, terra 77, 3.5-flash-lite 76, 3.6-flash 57, 5-mini 53, 3.1-flash-lite 49, 5.4-mini 34, 4o-mini 10.

Posição de leitura não explica a ordem: o primeiro colocado leu em 1/9/5 e o último em 6/2/10; os três que leram por último na 032 (posições 10, 11, 12) tiveram 4, 44 e 76.

## O que separou os modelos

**regra_020:** 3/3 em todos. Não discrimina.

**regra_228, filtro de recência do grupo.** O original usa `recencia de positivacao em 90 dias` (compra com algum vendedor do grupo do dono do cliente). Os seis modelos que escreveram só "comprou nos últimos 90 dias" acertaram os três blocos. Os seis que tentaram dizer com quem foi a compra erraram os três, nos dois sentidos: "com qualquer vendedor da empresa" (astra, 5-mini, 3.5-flash-lite, 3.1-flash-lite) vira `global`; "com o próprio vendedor" (carbon, terra) vira `do vendedor`. **A variante do grupo não tem expressão de negócio natural**, e o modelo que tenta ser preciso erra.

**regra_228, prospect.** O original usa `no ciclo de vida prospect com o vendedor`. Quem escreveu "nunca comprou com o vendedor" ou "prospect do vendedor" foi reconstruído como `prospects do vendedor`, que o manual define à parte (-1 em terra, astra, carbon, 3.5-flash-lite, 5-mini, 4.1-mini).

**regra_032.** Com o v2, os valores de ramo e UF chegaram literais em 11 das 12 descrições (o gpt-4o-mini quase não chega a citá-los). Isso era o grosso da perda na v1. O que resta:
- `carteira livre`: perdida em 3.6-flash, 3.5-flash-lite, 5-mini, terra, 5.4-mini, 3.8-flash, 3.1-flash-lite, 4o-mini (-2 cada). Astra, carbon, luna e 4.1-mini disseram que um cliente pode estar nos dois grupos.
- prospects: o original é **um** bloco com duas carteiras como fonte. Reconstruí dois blocos em 11 modelos (inventada = 1) e um bloco `do time` no 3.1-flash-lite. Nenhum ficou inteiro correto. Três descrições diziam "os dois grupos juntos" (astra, 4.1-mini, carbon) e mesmo assim separei: **é erro do reconstrutor**, ajudado por o manual não documentar fonte com várias carteiras.
- a exceção `recencia de positivacao em 150 dias` (do grupo): seis descrições (3.6-flash, terra, luna, astra, 3.8-flash, carbon) disseram "só com o próprio vendedor do cliente", reconstruído como `do vendedor`. Mesma lacuna de vocabulário da 228.
- **gpt-5.4-mini** não disse "com qualquer vendedor da empresa" nas faixas de compra: 47 blocos sem `global`. Perda real da descrição.
- **gemini-3.1-flash-lite** escreveu "independentemente da curva" no lugar das faixas de faturamento: 28 blocos deixam de existir.
- **gpt-4o-mini** descreveu 3 das 72 faixas.

### Escolhas do reconstrutor que mudam o número

| Escolha | Modelos afetados | Efeito |
|---|---|---|
| "os inativos desses ramos" / "classificado como inativo" lido como filtro `inativos` | gemini-3.6-flash, gpt-5-mini | -24 cada na 032. Lendo como "os que sobraram", os dois teriam 74 na 032 (84 e 80 no total) |
| Prospects da 032 em dois blocos | 11 modelos | +1 inventada em cada; o mesmo para todos, não muda a ordem entre eles |
| "próprio vendedor" lido como `do vendedor` | 228: carbon, terra; 032: seis modelos | -3 na 228, -1 na 032. Ler como recência do grupo reproduziria o original, mas não é o que o texto diz |

A primeira linha é a mais pesada: dois modelos caem do meio da tabela para o fundo por uma interpretação minha. Fica registrada como dado, sem ajustar a reconstrução.

### Leitura auxiliar: o "78"

O prompt desta rodada cita "de 3 para 57 acertos em 78". Percebi durante a reconstrução da 032 que 78 batia com uma contagem possível dos blocos. Não usei: as reconstruções da 032 têm 79 blocos (os prospects em dois), e a decisão de separar foi tomada antes de perceber.

## Comparação v1 × v2 (só os 4 modelos que têm as duas)

**Enviesada a favor do v2** (ver Ressalva). Fonte v1: `avaliacao_v1/ANALISE_PROMPT_V1.md` e `avaliacao_v1/comparacoes/`. As duas rodadas comparam valores entre aspas literais; a v1 não declara regra para caixa de palavra-chave, então a coluna da v2 com caixa estrita vai junto.

| Modelo | Capturadas v1 → v2 | Inventadas v1 → v2 | Inteira correta v1 (020/228/032) | Inteira correta v2 (020/228/032) | v2, caixa estrita |
|---|---|---|---|---|---|
| gpt-6-luna | 88 → 88 | 0 → 1 | 12 (3/6/3); 66 ignorando caixa dos valores | **86** (3/7/76) | 85 |
| gpt-6.1-terra | 88 → 88 | 0 → 1 | 12 (3/6/3); 30 ignorando caixa | **80** (3/3/74) | 80 |
| gemini-3.5-flash-lite | 86 → 88 | 0 → 1 | 9 (3/4/2) | **79** (3/3/73) | 79 |
| gemini-3.6-flash | 88 → 88 | 0 → 1 | **82** (3/6/73) | 60 (3/7/50) | 59 |

- Três dos quatro sobem muito, quase tudo pela 032: os valores de ramo agora vêm literais.
- O gemini-3.6-flash **cai** de 82 para 60. A perda vem da leitura "inativos = filtro" (-24, tabela acima). Sem ela teria 84, e ficaria no mesmo patamar.
- Na 228, luna e 3.6-flash sobem de 6 para 7; terra e 3.5-flash-lite descem de 6/4 para 3, porque o v2 os levou a qualificar a recência ("com o próprio vendedor", "com a empresa").
- A inventada nova (0 → 1) é o bloco de prospects que eu separei em dois, não o modelo.

## Quando a medida objetiva e a leitura subjetiva discordam

- **gpt-4.1-mini**: 3º na medida objetiva (83), 10º na leitura. Acerta porque enumera tudo; o texto é prolixo, repete e usa "carteiras livres" e "pré-inativo" literais.
- **gpt-6-luna** (1º objetivo, 4º na leitura) e **gemini-3.8-flash** (2º e 5º): ganham na 032 enumerando as 72 faixas **na ordem do arquivo**, só que com palavras de negócio.
- **gpt-6.1-terra**: 1º na leitura (reorganiza, 443 palavras contra 1000-1600 das outras), 6º no objetivo (80).

**O padrão da v1 se repete em parte, e é preciso dizer:** o que mais pontua é descrever o arquivo bloco a bloco. O que muda em relação à v1 é que copiar o **vocabulário** não ajuda mais. Os dois que mais copiaram termos e nomes (gpt-5-mini e gpt-5.4-mini) estão entre os últimos, e os que reorganizam (terra, carbon, astra) ficam a 4-6 blocos do primeiro. A distância entre "explica como alguém do negócio" e "enumera o arquivo" caiu de dezenas de blocos para poucos.

## Recomendação

**Padronizar `gpt-6-luna` com o `prompt_v2`.**

- Maior inteira correta (86/88), zero vazamento de sintaxe e 1 nome copiado, e a descrição mais barata das três primeiras (US$ 0,0040 pelas três, contra 0,048 do 3.8-flash e 0,009 do 4.1-mini).
- **Risco declarado:**
  1. Na 032 a luna enumera na ordem do arquivo. É o comportamento que torna a ferramenta menos útil para quem descreve o negócio do zero. Se a prioridade for o texto parecer de uma pessoa, a escolha é `gpt-6.1-terra` (1º na leitura, 80/88, US$ 0,020), aceitando perder a recência do grupo na 228.
  2. Temperatura fixa em 1 pelo modelo, e uma descrição por regra: a variância não foi medida. Uma segunda amostra pode mudar a posição.
  3. O v2 foi escrito conhecendo estes três gabaritos. A vantagem pode não se manter em regras novas.
  4. Nenhuma descrição resolve a recência do grupo (`recencia de positivacao` sem `global` nem `do vendedor`) sem quase copiar o filtro. É limite da relação linguagem natural → GOBR, e nenhum modelo nem prompt testado aqui resolve.

## Integridade

| Item | Valor | Fonte |
|---|---|---|
| Modelos na validação | 12 | `MAPA_VALIDACAO_V2.md` |
| Modelos com as 3 descrições completas | 12 | idem; 36 arquivos lidos |
| Reconstruções gravadas | 36 | `HASHES_RECONSTRUCOES.txt` (36 linhas) |
| Descrições vazias, truncadas ou ilegíveis | 0 | todas terminam em frase completa. A do gpt-4o-mini na 032 está **incompleta de conteúdo** (3 de 72 faixas), mas não cortada: o texto fecha normalmente |
| Hash das regras nas descrições | os 3 `hash_regra_sha256` dos metadados batem com `sha256sum regras_originais/regra_{020,228,032}.gobr` | — |
| Reconstruções alteradas depois do gabarito | nenhuma | `sha256sum -c` 36/36 OK |
