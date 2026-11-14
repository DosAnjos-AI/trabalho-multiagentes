# Gramática gorules, versão 1.0 (manual seção 10, p.57-58)

Implementada em ANTLR. Estrutura de alto nível:
```
gorules:
    version
    (
         regrapadrao |
         times segmentacoes
         (
             carteiras |
             parametros |
             carteiras parametros |
             alertas |
             carteiras alertas |
             tags |
             carteiras tags
         )
    )
    end
```
Arquivo válido: começa com `version 1.0`, define pelo menos um time, e contém uma das combinações: só carteiras; só parâmetros; carteiras com parâmetros; só alertas; carteiras com alertas; só tags; carteiras com tags.

## Tipos básicos
| Tipo | Formato | Exemplos |
|---|---|---|
| String | texto entre aspas duplas | `"supervisor marcos"` |
| Inteiro | sequência de dígitos | `90`, `30` |
| Real | dígitos com `.` ou `,` | `3.5`, `100,00` |
| Hora | `'hh:mm'` | `'07:00'`, `'18:30'` |
| Data DMY | `'dd-mm-yyyy'` | `'01-01-2025'` |
| Data YMD | `'yyyy-mm-dd'` | `'2025-01-01'` |
| Tag | `@nometag` | `@ruptura`, `@inativo` |
| Variável | identificador | `frequenciaBase` |

## Regras lexicais
- Comentário: `#` até o fim da linha.
- Aceita caracteres acentuados do português.
- Strings aceitam letras, números, espaços e símbolos, exceto `"`.
- Nomes de variáveis começam com letra e podem ter letras e números.
- Tags de clientes começam com `@` e usam só letras minúsculas e números.
