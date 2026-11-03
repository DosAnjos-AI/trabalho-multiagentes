# Filtros de frequência e parâmetros (manual 6.8, p.29-30)

| Filtro | Descrição |
|---|---|
| `não tem parametro` | cliente sem nenhuma parametrização |
| `não tem parametro manual` | sem parametrização feita manualmente por usuário |
| `fora da frequencia de venda ou maior que <N> dias` | recência atual fora da frequência de venda calculada, ou maior que N dias |
| `fora da frequencia de venda indicada <condicional de tempo>` | recência fora da frequência ideal, analisando as movimentações no período |
| `frequencia historica maior que <N> dias` | frequência histórica do cliente maior que N dias |
| `frequencia historica menor que <N> dias ou indefinida` | menor que N dias ou não foi possível calcular |
| `frequencia historica entre <N> dias e <Y> dias` | frequência histórica entre N e Y dias |
| `atendimentos <N>% menor que o parametrizado` | volume de atendimentos abaixo do esperado |
| `atendimentos <N>% maior que o parametrizado` | volume acima do esperado |
| `a ultima positivacao <N>% menor que o ticket medio` | última venda menor que o ticket médio |
| `a ultima positivacao <N>% maior que o ticket medio` | última venda maior que o ticket médio |
| `parametro de frequencia <N>% menor que o previsto` | parametrização atual com frequência menor que a prevista/calculada |
| `parametro de frequencia <N>% maior que o previsto` | parametrização atual com frequência maior que a prevista/calculada |

- `fora da frequencia de venda` tem as opções `indicada` e `ou maior que`.
- `frequencia historica` pode incluir `ou indefinida`.
- `<tempo>` e `<condicional de tempo>`: ver 06-12-opcoes-de-tempo.md.
