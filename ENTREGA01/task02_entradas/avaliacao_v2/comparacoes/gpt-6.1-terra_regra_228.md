# Comparação: gpt-6.1-terra, regra_228

Critério: `../../avaliacao_v1/CRITERIO_AVALIACAO_v1.md` com as extensões E1-E5 de `../RESULTADO_V2.md`. Original: `regras_originais/regra_228.gobr`. Reconstrução: `reconstrucoes/gpt-6.1-terra/regra_228.gobr`. Números: `comparacoes/_saida_comparar_v2.json`, chave `gpt-6.1-terra|228` (gerado por `comparar_v2.py`).

| Medida | Todos os blocos | Sem `time` |
|---|---|---|
| Regras capturadas | 7/7 | 6/6 |
| Regras inventadas | 0 | 0 |
| Regra inteira correta | 3/7 | 2/6 |
| Inteira correta com caixa estrita também em palavra-chave (leitura auxiliar) | 3/7 | 2/6 |

## Faltaram

Nenhuma.

## Inventadas

Nenhuma.

## Capturadas mas não inteiras corretas

- `parametros` "Ative este novo cliente!": quando: `no ciclo de vida prospect com o vendedor` ⇄ `prospects do vendedor`
- `parametros` "Compra com regularidade! (Curva C)": quando: `recencia de positivacao do vendedor em 90 dias` ⇄ `recencia de positivacao em 90 dias`
- `parametros` "Compra com regularidade! (Curva A e B)": quando: `recencia de positivacao do vendedor em 90 dias` ⇄ `recencia de positivacao em 90 dias`
- `parametros` "Cliente caminhando para inatividade!": quando: `recencia de positivacao do vendedor entre 91 dias e 180 dias` ⇄ `recencia de positivacao entre 91 dias e 180 dias`

Leitura de `⇄`: diferença simétrica entre o conjunto da reconstrução e o do original (o item que só existe em um dos lados). Em `fonte`, `T:n` é o n-ésimo time do arquivo e `C:...` é a definição da carteira.
