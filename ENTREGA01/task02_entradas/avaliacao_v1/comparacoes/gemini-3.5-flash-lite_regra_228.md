# Comparação: gemini-3.5-flash-lite, regra_228

Critério: `../CRITERIO_AVALIACAO_v1.md`. Original: `regras_originais/regra_228.gobr`. Reconstrução: `reconstrucoes/gemini-3.5-flash-lite/regra_228.gobr`.

| Medida | Todos os blocos | Sem `time` |
|---|---|---|
| Regras capturadas | 7/7 | 6/6 |
| Regras inventadas | 0 | 0 |
| Regra inteira correta | 4/7 | 4/6 |

## Faltaram

Nenhuma.

## Inventadas

Nenhuma.

## Capturadas mas não inteiras corretas

- `time "televendas"`: faltou `ativados`; a descrição diz só "nosso pessoal do televendas", sem mencionar vendedores ativos
- `Cliente ativado!`: original `unica compra com o vendedor`; a descrição diz "já fizeram a primeira compra com o vendedor" e usa o rótulo "Cliente ativado!", o que levou a `no ciclo de vida ativado com o vendedor`
- `Cliente caminhando para inatividade!`: `recencia de positivacao entre 91 dias e 180 dias` (original) x `recencia de positivacao em 180 dias` (reconstrução). **Erro do reconstrutor, não da descrição**: a descrição dizia "entre 91 e 180" com clareza; escolhi a forma em cascata copiando o padrão dos exemplos (`RegraMaxlub`).

## Notas

- `curva c` (original) x `curva C` (reconstrução) foi tratado como grafia de palavra-chave, na mesma classe de acento, e não conta como diferença.
