# Funções de seleção de clientes e opções de ruptura (manual 4.6, p.15-16)

Usadas após a palavra-chave `clientes`.

| Função | Seleciona |
|---|---|
| `carteirafixa(<time>)` | clientes da carteira fixa (portfólio permanente) de cada vendedor do time |
| `carteiraacessivel(<time>)` | clientes da carteira acessível de cada vendedor do time |
| `carteiraruptura(<time>)` | clientes da carteira de ruptura pré-calculada de cada vendedor do time |
| `portfolio(<time>)` | portfólio completo dos vendedores do time |
| `inativos(<time>, <tempo de inatividade>)` | clientes inativos há pelo menos o tempo informado |
| `segmentados(<segmentacao>)` | clientes de uma segmentação já definida |
| `ruptura(<time_origem> para <time_destino>)` | clientes do time de origem em ruptura, associados ao time de destino |
| `ruptura da segmentacao(<segmentacao> para <time>)` | clientes de uma segmentação em ruptura, associados ao time de destino |
| `todos(<time>)` | todos os clientes do sistema para o time |

## Opções para ruptura (após a função)
| Opção | Significado |
|---|---|
| `de positivacao(<tempo>)` | sem compra/positivação há pelo menos o tempo |
| `de positivacao(<tempo>) ou prospects` | idem, incluindo prospects (nunca compraram) |
| `de visita(<tempo>)` | sem visita há pelo menos o tempo |
| `de visita(<tempo>) ou prospects` | idem, incluindo prospects |
| `de inativos(<time>, <tempo>)` | inativos de um time específico há pelo menos o tempo |
| `de inativos(<time>, <tempo>) ou prospects` | idem, incluindo prospects |

Combinar opções com `e` (as duas valem ao mesmo tempo):
```
carteira "ruptura de campo":
      clientes ruptura("superv maria" para "superv marcos")
                      de positivacao(90 dias)
                      e de visita(30 dias)
```
`<tempo>`: ver 06-12-opcoes-de-tempo.md.
