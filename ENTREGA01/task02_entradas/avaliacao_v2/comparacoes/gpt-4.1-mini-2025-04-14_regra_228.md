# Comparação: gpt-4.1-mini-2025-04-14, regra_228

Critério: `../../avaliacao_v1/CRITERIO_AVALIACAO_v1.md` com as extensões E1-E5 de `../RESULTADO_V2.md`. Original: `regras_originais/regra_228.gobr`. Reconstrução: `reconstrucoes/gpt-4.1-mini-2025-04-14/regra_228.gobr`. Números: `comparacoes/_saida_comparar_v2.json`, chave `gpt-4.1-mini-2025-04-14|228` (gerado por `comparar_v2.py`).

| Medida | Todos os blocos | Sem `time` |
|---|---|---|
| Regras capturadas | 7/7 | 6/6 |
| Regras inventadas | 0 | 0 |
| Regra inteira correta | 5/7 | 5/6 |
| Inteira correta com caixa estrita também em palavra-chave (leitura auxiliar) | 4/7 | 4/6 |

## Faltaram

Nenhuma.

## Inventadas

Nenhuma.

## Capturadas mas não inteiras corretas

- `time` "televendas": fonte: `vendedores todostelevendas` ⇄ `vendedores todostelevendas ativados`
- `parametros` "Ative este novo cliente!": quando: `no ciclo de vida prospect com o vendedor` ⇄ `prospects do vendedor`

Leitura de `⇄`: diferença simétrica entre o conjunto da reconstrução e o do original (o item que só existe em um dos lados). Em `fonte`, `T:n` é o n-ésimo time do arquivo e `C:...` é a definição da carteira.
