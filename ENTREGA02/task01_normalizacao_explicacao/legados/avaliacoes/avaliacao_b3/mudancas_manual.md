# Mudancas no manual/ na rodada B3

Copia do manual antes da edicao: `manual_antes/` (nesta pasta). Nenhum arquivo ou titulo de secao foi renomeado ou apagado; so houve acrescimo.

| Arquivo | Secao | O que mudou | Motivo | Evidencia |
|---|---|---|---|---|
| `03-secoes/07-01-parametros-estrutura-e-exemplos.md` | `## Ordem entre regras de parametros` (nova, no fim do arquivo) | Quatro itens: (1) regras `parametros` valem na ordem do arquivo e o cliente ja parametrizado nao e reprocessado (fato ja escrito em "Restricoes" e em `02-invariantes.md`, p.46); (2) consequencia: com duas ou mais situacoes, vale a primeira, e o pedido que lista situacoes em sequencia vira regras na mesma ordem; (3) consequencia do fluxo (passo `quando` opcional) e do item 1, marcada como "sem exemplo no manual": regra sem `quando`, escrita por ultimo, pega o que sobrou ("todo o resto"); (4) remete a ordem entre blocos `carteira` ao "Cenario 3" de `04-01` e diz que em alertas a ordem nao importa | O auxiliar v1 so mapeava "prioridade" para o "Cenario 3" de carteiras, que trata de blocos `carteira`, nao de situacoes de atendimento; o texto de prioridade ficou sem destino unico no manual | Passo 3 (ii): v1 usou o Cenario 3 em 5 de 10, `sem_chave` em 3 de 10; v2 usou o Cenario 3 em 7 de 10 e `sem_chave` em 1. Passo 4: 14 dos 15 `.gobr` lidos tem blocos `parametros` cuja ordem decide o resultado. A sintese esta no relatorio da rodada |

Nao alterado: a secao `## Fluxo de uma regra` continua em `07-01` (as chaves do v1 continuam resolvendo). Ela deixa de ser chave do auxiliar v2 porque virou transversal (decisao no relatorio).

## Hashes (SHA-256)

- Conjunto do manual antes (`find . -type f | sort | xargs sha256sum | sha256sum`, dentro de `manual/`): `1473fc81d406966a568d35b7537f327b4f3326b7de5b366e805f5aeffacfa5f2`
- Conjunto do manual depois: `6f66d476f00124a461d7fee27caa34eea524879678435063eb2e8ffb4d8783b5`
- Unico arquivo diferente (`diff -rq manual avaliacao_b3/manual_antes`): `03-secoes/07-01-parametros-estrutura-e-exemplos.md`
  - antes: `e6c63524627d3a85f2618b3079f079277b8fe1ce836235003022297e4411d2ff`
  - depois: `f51c8d859ecc717d03c4956cfccbdb68d9c910fffde0f155d4afc37ce9d98657`
- Os 31 arquivos de `manual_antes/` e seus hashes: `cd manual_antes && find . -type f | sort | xargs sha256sum`.
