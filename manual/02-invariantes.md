# Invariantes de todo arquivo gorules (manual v0.89.0, gramática 1.0)
Páginas pela numeração impressa do manual. "Observado" = presente nos exemplos do manual, sem regra declarada.

## Forma
- Primeira linha: `version 1.0`, obrigatória (p.5, p.57).
- Bloco: palavra-chave e nome entre aspas duplas (p.5); dois-pontos no fim do cabeçalho (observado, p.5-48).
- Corpo indentado sob o cabeçalho; continuação de cláusula indentada mais fundo (observado, p.5-48; o manual não declara regra de indentação).
- String: letras, números, espaços, acentos e símbolos, menos `"` (p.58).
- Comentário: `#` até o fim da linha, em qualquer ponto (p.5, p.58).
- Tipos: inteiro `90`; real `3.5` ou `100,00`; hora `'07:00'`; data `'dd-mm-yyyy'` ou `'yyyy-mm-dd'`; tag `@nometag` (p.57-58).
- Grafia (preferência de escrita, não regra de validade): em palavra-chave de cláusula, emitir sem acento, a convenção comprovada em `referencias/`. Uso fora de aspas, sem × com acento: `frequencia` 1460×23, `recencia` 487×0, `positivacao` 472×1, `preferencia` 300×0, `nao` 277×13, `uteis` 169×0, `sabado` 51×0, `no maximo` 42×3, `terca` 30×2, `no minimo` 26×3. Forma acentuada não é erro: o parser aceita acento (p.58) e o manual usa as duas grafias, ex. `positivacao` (p.9) e `positivação` (p.24), `nao agendar` (p.40) e `não tem venda` (p.50). Os arquivos de `03-secoes/` reproduzem a grafia do manual; ao emitir, vale esta preferência.
- Grafia, ressalvas: `terca`, `no maximo`, `no minimo`, `contem`, `rotulo` sem acento não aparecem no manual (só `terça` p.19, `no máximo`/`no mínimo` p.44, `contém` e `rótulo` p.26-27); a preferência vem só do uso em `referencias/`. `mes`/`mês` não tem uso dominante (2×3): as duas estão no manual (`1 mes` p.12, `no mês` p.34). Texto entre aspas é nome livre, fora desta regra.
- Nomes distintos: times no arquivo (p.7); carteiras e segmentações entre si (p.17); blocos de parâmetros (p.46); alertas em toda a empresa, inclusive entre conjuntos de regras (p.54).

## Categorias (p.4)
| Categoria | Propósito |
|---|---|
| `time` | grupo de vendedores com as mesmas regras comerciais |
| `segmentacao` | carteira virtual auxiliar de clientes; não gera agenda |
| `carteira` | carteira definitiva dos vendedores; usada para gerar agendas |
| `parametros` | parâmetros de atendimento (frequência, preferência de dias, roteirização) |
| `alertas` | alertas para vendedores, supervisores e gestores |
| `tags` | marcações nos clientes para filtros e segmentações |

## Ordem entre blocos (gramática, p.57)
- `version`, depois `regrapadrao` ou: times, segmentações e um destes grupos: só carteiras; só parâmetros; carteiras + parâmetros; só alertas; carteiras + alertas; só tags; carteiras + tags. O manual não explica `regrapadrao`.
- Pelo menos um time (p.57); segmentação é opcional (p.4).
- Parâmetros e alertas nunca no mesmo conjunto de regras (p.47).
- `carteira "x":` é exclusiva: o cliente incluído sai do pool das carteiras seguintes; a ordem decide (p.8, p.11, p.17). `carteira livre "x":` não retira do pool (p.9, p.16).
- Time usado em parâmetros ou alertas sem carteira correspondente assume a carteira fixa dele (p.17).
- Parâmetros: cliente parametrizado por regra anterior não é reprocessado; a ordem importa (p.46).
- Alertas: a ordem não importa; o mesmo cliente pode disparar vários (p.54).

## Combinação com `e`
- Filtros temporais da mesma família: `e` vale como OU. `no dia 2 e no dia 12` = dia 2 ou dia 12; `no domingo e na segunda` = domingo ou segunda. Entre famílias diferentes, todas valem (p.18).
- Filtros de cliente após `quando`: todos valem ao mesmo tempo; cada filtro novo entra com `e` (p.10, p.22).
- Opções de ruptura unidas com `e`: valem simultaneamente (p.16).

## Ordem dentro do bloco
- Filtros temporais: (1) dia do mês, (2) dia da semana, (3) semana do mês, (4) mês do ano, (5) horário; nenhum é obrigatório (p.18).
- Horário só em alertas, uma forma por vez: `às` ou `de hora em hora` (p.20-21).
- Parâmetros: fonte; filtros temporais (opcional); `quando` (opcional); parâmetros de atendimento; conflito `sem choque` (opcional) (p.38, p.42).
- Alerta: fonte; filtros temporais; `quando` (opcional); `onde <gatilho>`; `informe`; `descreva com o texto(...)` (opcional); `entregue`; `pelos canais`; tags (opcional) (p.47).

## Fontes e campos por categoria
- `time`: uma ou mais linhas `vendedores <seleção>`, que somam (p.5, p.7).
- `segmentacao` e `carteira`: `clientes <seleção>` (p.4); `quando` opcional (p.9). Segmentação pode juntar várias segmentações; carteira, uma só (p.14, p.16).
- Fonte de parâmetros: carteira, segmentação ou time (p.38). Formas: `da carteira("x")` (p.39-43); `do time("x")` (forma da p.48, e da p.42 dentro de `parametros`, em `sem choque ... do time(...)`; fonte de `parametros` em 963 linhas de `referencias/`, contra 732 de `da carteira`); `na carteira("x")` (p.18; ausente de `referencias/`, válida pelo manual). O manual não mostra a forma para segmentação.
- Parâmetros de atendimento (etapa não marcada como opcional, ao contrário das demais; nenhum parâmetro individual é declarado obrigatório, p.38): `frequencia ...` (p.43-45); `preferencia ...` (p.38-42); `nao agendar`, exclusivo, sem frequência nem preferência na mesma regra (p.40); `restrito` + `a partir da ... semana` ou `ate a ... semana` (p.42, p.45); `roteirizavel`, `fixo` (p.43); `sem choque ...` (p.42).
- `limpar parametros "x":` leva só a fonte (p.43).
- Fonte de alerta: carteiras ou times (p.47). Formas mostradas: `do time("x")` (p.48) e `na carteira("x")` (p.18).
- `tags`: o manual lista gatilhos e filtros (p.55-56), mas não mostra a sintaxe do bloco.
- Regras para times ou carteiras, não para vendedor individual (p.16, p.46); em alerta, nunca (p.54). Vendedor isolado vira time com `porid` (exemplos p.5, p.12).
