# Comparação: gemini-3.5-flash-lite, regra_032

Critério: `../../avaliacao_v1/CRITERIO_AVALIACAO_v1.md` com as extensões E1-E5 de `../RESULTADO_V2.md`. Original: `regras_originais/regra_032.gobr`. Reconstrução: `reconstrucoes/gemini-3.5-flash-lite/regra_032.gobr`. Números: `comparacoes/_saida_comparar_v2.json`, chave `gemini-3.5-flash-lite|032` (gerado por `comparar_v2.py`).

| Medida | Todos os blocos | Sem `time` |
|---|---|---|
| Regras capturadas | 78/78 | 77/77 |
| Regras inventadas | 1 | 1 |
| Regra inteira correta | 73/78 | 72/77 |
| Inteira correta com caixa estrita também em palavra-chave (leitura auxiliar) | 73/78 | 72/77 |

## Faltaram

Nenhuma.

## Inventadas

- `parametros` "prospects norte nordeste" — quando: `no ciclo de vida prospect com a empresa` — frequencia de 14 dias

## Capturadas mas não inteiras corretas

- `carteira livre` "sul_sudeste_centrooeste": cat: `carteira` ⇄ `carteira livre`
- `carteira livre` "norte_nordeste": cat: `carteira` ⇄ `carteira livre`
- `parametros` "Prospects": fonte: `C:clientes carteirafixa(T:0)?uf do estado igual("AC","AP","AM","PA","RO","RR","TO","AL","BA","CE","MA","PB","PE","PI","RN","SE")`
- `parametros` "Pré-inativos Curva C (Sul, Sudeste e Centro-Oeste - Matcon, Ferragista, Agropecuária e Home Center)": quando: `recencia de positivacao em 150 dias` ⇄ `recencia de positivacao global em 150 dias`
- `parametros` "Inativos Curva C (Norte e Nordeste - Corporativo/ Consumidor)": params: `frequencia de 28 dias`

Leitura de `⇄`: diferença simétrica entre o conjunto da reconstrução e o do original (o item que só existe em um dos lados). Em `fonte`, `T:n` é o n-ésimo time do arquivo e `C:...` é a definição da carteira.
