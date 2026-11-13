# Avaliação subjetiva das 36 descrições (prompt_v2)

**Isto é leitura, não nota.** Escala de três níveis do critério v1 (seção 5), só para ler lado a lado. Não entra em nenhuma conta e não foi usada para justificar as medidas objetivas, nem o contrário.

Vazamento: contagem de `contar_vazamento.py` (saída em `comparacoes/_saida_contar_vazamento.json`). Duas listas:
- **sintaxe**: termos na forma da linguagem (`recencia de positivacao`, `positivação`, `ciclo de vida`, `definido como`, `media faturada`, `curva c com a empresa`, `prospect com o vendedor/a empresa`, `carteira fixa`, `carteira livre`, `ativados`, `nao agendar`, `global`);
- **nomes**: texto livre do `.gobr` copiado para a descrição (nomes de bloco ou de carteira: `sul_sudeste_centrooeste`, `norte_nordeste`, "Ative este novo cliente!", "pré-inativo", "Corporativo/ Consumidor", e "empresa toda" só na 020, onde é nome do time e da carteira).

"curva C", "com a empresa" e "com o vendedor" soltos não contam: são português de negócio (critério v1, seção 5). O inglês "days" no gpt-5-mini (97 vezes na 032) está anotado à parte: é defeito de idioma, não vocabulário GOBR.

## regra_020

| Modelo | Linguagem | Ordem | Vazamento (sintaxe / nomes) | Nota de leitura |
|---|---|---|---|---|
| gpt-6-luna | misto | n/a | 0 / 1 (`empresa toda`) | "clientes fixos vinculados à empresa toda": o nome da carteira entra como se fosse um lugar |
| gpt-5.4-mini | negócio | n/a | 0 / 0 | — |
| gpt-6-astra | negócio | n/a | 0 / 0 | — |
| gpt-4.1-mini | negócio | n/a | 1 / 1 | Enche linguiça ("sem distinção de segmento, faturamento ou qualquer outra condição") |
| gemini-3.8-flash | negócio | n/a | 0 / 0 | — |
| gpt-4o-mini | negócio | n/a | 1 / 0 | Tom de folheto ("garantindo que suas necessidades sejam atendidas") e uma condição que não existe ("independentemente da localização") |
| gemini-3.1-flash-lite | negócio | n/a | 1 / 0 | — |
| gemini-4-carbon | negócio | n/a | 0 / 0 | — |
| gemini-3.6-flash | negócio | n/a | 1 / 1 | — |
| gemini-3.5-flash-lite | negócio | n/a | 0 / 0 | — |
| gpt-5-mini | tradução | n/a | 0 / 3 | "o conjunto de clientes identificado como empresa toda", "não há outras filas": descreve o arquivo |
| gpt-6.1-terra | negócio | n/a | 0 / 0 | Uma frase, 12 palavras |

Ordem "n/a": três blocos em que a ordem do arquivo é a única ordem possível.

## regra_228

Aqui a ordem do arquivo **é** a prioridade, então segui-la é obrigatório; o item mede só se a descrição diz que é prioridade ou só enfileira.

| Modelo | Linguagem | Ordem | Vazamento (sintaxe / nomes) | Nota de leitura |
|---|---|---|---|---|
| gemini-3.8-flash | negócio | segue, dizendo que é prioridade | 0 / 0 | — |
| gpt-4o-mini | misto | segue | 4 / 0 | Contradição ("ainda estão no ciclo de prospect e fizeram a primeira compra"), inventa sentido ("curvas A e B", "não compram há mais de 180 dias") |
| gemini-3.1-flash-lite | negócio | segue, dizendo que é prioridade | 0 / 0 | "comprou com a gente": transforma o filtro do grupo em filtro da empresa |
| gemini-4-carbon | negócio | segue, explica que o primeiro encaixe vale | 0 / 0 | Diz "comprou com o próprio vendedor": troca o filtro do grupo pelo do vendedor |
| gemini-3.6-flash | negócio | segue | 1 / 0 | — |
| gemini-3.5-flash-lite | negócio | segue | 1 / 0 | "comprou com a empresa": troca o filtro |
| gpt-5-mini | misto | segue, explica que o primeiro encaixe vale | 2 / 1 | Parênteses técnicos ("contagem só com o próprio vendedor"), copia o nome "resgatar cliente inativo" |
| gpt-6.1-terra | negócio | segue | 0 / 0 | Curta e clara; "com o próprio vendedor" troca o filtro |
| gpt-6-luna | negócio | segue, explica que o primeiro encaixe vale | 0 / 0 | — |
| gpt-5.4-mini | **tradução** | segue o arquivo | 7 / 6 | Copia os 6 nomes dos blocos entre aspas e escreve "recencia de positivacao em 90 dias e curva c com a empresa" literal |
| gpt-6-astra | negócio | segue, explica que o primeiro encaixe vale | 0 / 0 | "com qualquer vendedor da empresa": troca o filtro |
| gpt-4.1-mini | misto | segue | 1 / 0 | Explica o que o arquivo não diz ("curva C, que são clientes com menor volume") e põe frase sem sentido ("sem divisão por carteira fixa") |

## regra_032

| Modelo | Linguagem | Ordem | Vazamento (sintaxe / nomes) | Nota de leitura |
|---|---|---|---|---|
| gemini-3.6-flash | misto | segue o arquivo | 3 / 0 | Enumera as 72 faixas; frase confusa na exceção ("a única exceção de alcance") |
| gemini-3.5-flash-lite | negócio | segue o arquivo | 2 / 13 | Tom de "a gente"; usa o rótulo "pré-inativo" dos nomes dos blocos 13 vezes; mistura as faixas do Norte num parágrafo difícil de seguir |
| gpt-5-mini | **tradução** | segue o arquivo, item por item | 10 / 32 (+97 "days") | Lista em tópicos com um tópico por bloco; nomes de carteira com sublinhado; mistura inglês ("150 days") |
| gpt-6.1-terra | negócio | **reorganiza** | 0 / 0 | Explica a estrutura uma vez (região -> etapa de compra -> faixa) e depois só os números por ramo. 443 palavras contra 900-1600 das outras |
| gpt-6-luna | negócio | segue o arquivo | 0 / 0 | Enumera tudo, mas em português simples ("sem exigência de faturamento") |
| gpt-5.4-mini | misto | parcial | 11 / 13 | Nomes de carteira com sublinhado; "150 dias sem positivação" diz o contrário do que quer dizer |
| gpt-6-astra | negócio | **reorganiza** | 0 / 0 | Explica os prazos por região antes dos ramos; diz que as carteiras não se excluem |
| gpt-4.1-mini | misto | parcial | 6 / 18 | Prolixa e repetitiva; "duas carteiras livres" literal; atribui à curva um papel que ela não tem ("independentemente da curva") |
| gemini-3.8-flash | negócio | segue o arquivo | 5 / 0 | Enumera as 72 faixas em frases de negócio; longa (1382 palavras) |
| gpt-4o-mini | negócio | parcial | 3 / 0 | Perde quase tudo: só dá duas faixas de MATCON e uma de inativos; o resto vira "ajustamos as faixas conforme o perfil" |
| gemini-3.1-flash-lite | negócio | reorganiza | 7 / 7 | Compacta, mas resume demais: "independentemente da curva" apaga as faixas de faturamento de pré-inativos e inativos |
| gemini-4-carbon | negócio | **reorganiza** | 0 / 0 | Explica a estrutura (região, ramo, três etapas, três faixas) e depois os números; aponta a exceção e o caso sem frequência |

## Posição na leitura de linguagem natural (1 = mais negócio)

Junta as três regras, com peso maior para a 032 (é a única em que dá para errar o tom de verdade).

| Posição | Modelo | Motivo curto |
|---|---|---|
| 1 | gpt-6.1-terra | Curta, reorganiza, zero vazamento |
| 2 | gemini-4-carbon | Reorganiza, zero vazamento; longa |
| 3 | gpt-6-astra | Reorganiza, zero vazamento |
| 4 | gpt-6-luna | Zero vazamento, mas a 032 enumera na ordem do arquivo |
| 5 | gemini-3.8-flash | Frases de negócio, enumera na ordem do arquivo |
| 6 | gemini-3.6-flash | Idem, com trechos confusos |
| 7 | gemini-3.5-flash-lite | Tom natural, rótulos copiados dos nomes |
| 8 | gemini-3.1-flash-lite | Natural, mas resume a ponto de mudar o sentido |
| 9 | gpt-4o-mini | Tom de folheto; perde conteúdo e inventa sentido |
| 10 | gpt-4.1-mini | Prolixa, explica o que o arquivo não diz, termos literais |
| 11 | gpt-5.4-mini | Copia nomes de bloco e filtros literais |
| 12 | gpt-5-mini | Um tópico por bloco, nomes com sublinhado, inglês misturado |
