# Regras de frequência (manual 7.4, p.43-45)

## Fixa por período
| Regra | Equivale a |
|---|---|
| `diaria()` | 1 dia |
| `semanal()` | 7 dias |
| `quinzenal()` | 15 dias |
| `quinzenal('dd-mm-yyyy')` | 15 dias a partir da data pivot |
| `mensal()` | 30 dias |
| `bimestral()` | 60 dias |
| `bimestral('dd-mm-yyyy')` | 60 dias a partir da data pivot |
| `trimestral()` | 90 dias |
| `semestral()` | 180 dias |
| `anual()` | 365 dias |
| `de <N> dias` | N dias exatos |

## Modificadores de limite para frequência fixa
| Modificador | Efeito |
|---|---|
| `no máximo semanal()` | frequência não pode ser maior que 7 dias |
| `no mínimo mensal()` | frequência não pode ser menor que 30 dias |

## Dinâmica (baseada em dados existentes)
| Regra | Descrição |
|---|---|
| `do govendas` | frequência padrão do Govendas |
| `do vendedor` | a configurada pelo vendedor para o cliente |
| `do vendedor menos <N> dias` | a do vendedor menos N dias |
| `do vendedor mais <N> dias` | a do vendedor mais N dias |
| `do historico` | calculada pelo histórico de visitas |
| `de qualquer vendedor` | a configurada por qualquer vendedor para o cliente |
| `de ativos da empresa` | média dos clientes ativos da empresa |
| `de inativos da empresa` | média dos clientes inativos da empresa |
| `de ativos do vendedor` | média dos clientes ativos do vendedor |
| `de inativos do vendedor` | média dos clientes inativos do vendedor |
| `remover` | remove a configuração de frequência existente |

Fallbacks encadeados com `ou`: `frequencia do vendedor ou de qualquer vendedor ou de 35 dias`.
