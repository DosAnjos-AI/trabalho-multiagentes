# Alertas: estrutura, informe e gatilhos (manual 8.1-8.4, p.47-51)

Alerta é acionado quando um gatilho é detectado para clientes num período. Não combinar `parametros` e `alerta` no mesmo conjunto de regras.

## Etapas
1. Clientes: carteira ou time. 2. Filtros temporais (inclui horário). 3. Filtros de clientes (`quando`, opcional). 4. Gatilho (`onde`). 5. Informações adicionais (`informe`). 6. Descrição (`descreva com o texto("...")`, opcional). 7. Alvo (`entregue para`). 8. Canais (`pelos canais`). 9. Tags (opcional).

## Exemplo completo
```
version 1.0

time "campo e televendas":
     vendedores todos

alerta "Whatsapp: Ruptura de positivação na agenda de hoje":
     do time("campo e televendas")
     nos dias uteis e de hora em hora a partir de '07:00'
     quando ativos para o vendedor
              e adimplentes
              e na agenda de hoje
              e recencia de visita entre 10 dias e 90 dias
     onde nao tem venda em 21 dias
     informe com 15 vendedores e com 5 clientes
              e com o nome do supervisor
              e com o codigo do vendedor
              e com o nome do vendedor
              e com o codigo do cliente
              e com o nome do cliente
     descreva com o texto("
Há clientes em ruptura de positivacao de 21 dias.
Analisado em $datahora$.
     ")
     entregue para gestor e redirecione("vagner@govendas.com")
    pelos canais govendas() e whatsapp("ruptura_vendedor_template1")
     e template com os valores(
              '$totalclientes$',
              '10',
              '21',
              '$nomeusuario$',
              'https://app.govendas.com/#/notificacao/{{id}}'
     )
```
`informe com 15 vendedores e com 5 clientes`: até 15 vendedores e 5 clientes por vendedor, com os atributos listados.

## Tipos de evento (informe)
| Tipo | Regra | Descrição |
|---|---|---|
| CUSTOM_TABLE | `informe` | tabela customizável com atributos manuais |
| CLIENT | `informe da carteira` | evento por cliente, atributos do vendedor automáticos |
| ITINER | `informe da agenda` | evento por item de agenda, atributos do vendedor automáticos |
| SUMMARIZED_SALESMAN | `informe resumo do supervisor` | resumo agrupado por supervisor (atributos fixos) |
| SUMMARIZED_SUPERVISOR | `informe resumo do gestor` | resumo agrupado por gestor (atributos fixos) |

## Gatilhos (após `onde`)
Visita e venda:
| Gatilho | Descrição |
|---|---|
| `tem venda em <N> dias` | teve venda nos últimos N dias |
| `não tem venda em <N> dias` | não teve venda nos últimos N dias |
| `tem visita em <N> dias` / `não tem visita em <N> dias` | com / sem visita nos últimos N dias |
| `tem venda do vendedor em <N> dias` / `não tem venda do vendedor em <N> dias` | com / sem venda com o vendedor específico |
| `tem visita da empresa em <N> dias` / `não tem visita da empresa em <N> dias` | com visita / sem visita de qualquer vendedor da empresa |

Frequência e parametrização:
| Gatilho | Descrição |
|---|---|
| `fora da frequencia de venda ou maior que <N> dias` | fora da frequência de venda parametrizada |
| `fora da frequencia de venda indicada ou maior que <N> dias` | considera a frequência indicada pelo histórico |
| `atendimento <N>% menor que o parametrizado` | volume abaixo do esperado |
| `não tem parametro` / `não tem parametro manual` | sem parâmetro / sem parametrização manual |
| `parametro de frequencia <N>% menor que o previsto` | frequência parametrizada abaixo da prevista |

Qualidade de atendimento:
| Gatilho | Descrição |
|---|---|
| `tem <N>% de visita remota em <periodo>` | percentual de visitas remotas no período |
| `tem <N>% de visita incerta em <periodo>` | percentual de visitas com localização incerta |
| `ultima positivacao <N>% menor que o ticket medio` | última venda abaixo do ticket médio |
| `não tem coordenada confiavel` | sem geolocalização válida |

Produtos:
| Gatilho | Descrição |
|---|---|
| `tem produtos com promoções sugeridas` | há produtos com promoção sugerida |
| `tem produtos sugeridos` | há produtos sugeridos |
