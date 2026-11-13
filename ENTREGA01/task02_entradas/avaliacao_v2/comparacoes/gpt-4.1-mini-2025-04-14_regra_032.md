# Comparação: gpt-4.1-mini-2025-04-14, regra_032

Critério: `../../avaliacao_v1/CRITERIO_AVALIACAO_v1.md` com as extensões E1-E5 de `../RESULTADO_V2.md`. Original: `regras_originais/regra_032.gobr`. Reconstrução: `reconstrucoes/gpt-4.1-mini-2025-04-14/regra_032.gobr`. Números: `comparacoes/_saida_comparar_v2.json`, chave `gpt-4.1-mini-2025-04-14|032` (gerado por `comparar_v2.py`).

| Medida | Todos os blocos | Sem `time` |
|---|---|---|
| Regras capturadas | 78/78 | 77/77 |
| Regras inventadas | 1 | 1 |
| Regra inteira correta | 75/78 | 74/77 |
| Inteira correta com caixa estrita também em palavra-chave (leitura auxiliar) | 75/78 | 74/77 |

## Faltaram

Nenhuma.

## Inventadas

- `parametros` "prospects norte nordeste" — quando: `prospects da empresa` — frequencia de 14 dias

## Capturadas mas não inteiras corretas

- `parametros` "Prospects": fonte: `C:clientes carteirafixa(T:0)?uf do estado igual("AC","AP","AM","PA","RO","RR","TO","AL","BA","CE","MA","PB","PE","PI","RN","SE")`; quando: `no ciclo de vida prospect com a empresa` ⇄ `prospects da empresa`
- `parametros` "Pré-inativos Curva C (Sul, Sudeste e Centro-Oeste - Matcon, Ferragista, Agropecuária e Home Center)": quando: `recencia de positivacao em 150 dias` ⇄ `recencia de positivacao global em 150 dias`
- `parametros` "Inativos Curva C (Norte e Nordeste - Corporativo/ Consumidor)": params: `frequencia de 28 dias`

Leitura de `⇄`: diferença simétrica entre o conjunto da reconstrução e o do original (o item que só existe em um dos lados). Em `fonte`, `T:n` é o n-ésimo time do arquivo e `C:...` é a definição da carteira.
