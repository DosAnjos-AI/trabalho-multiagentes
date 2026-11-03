# Alertas: variáveis, canais, alvos e restrições (manual 8.5-8.8, p.51-54)

Variáveis, sempre entre `$`, usadas em `descreva com o texto(...)` e `template com os valores(...)`.

| Grupo | Variáveis |
|---|---|
| Fixas | `$data$`, `$hora$`, `$datahora$` |
| Usuário alvo | `$nomeusuario$`, `$primeironomeusuario$`, `$emailusuario$`, `$telefoneusuario$`, `$tipousuario$` (vendedor, supervisor, gestor), `$diasparainativos$`, `$maximovisitas$`, `$idvendedor$`, `$tipovendedor$` (campo, televendas), `$semagenda$` |
| Clientes do evento | `$totalclientes$`, `$totalagendados$`, `$totalvendedores$`, `$somaticketmedio$`, `$idusuario$` |
| Produtos | `$totalprodutos$`, `$totalcondicoes$`, `$qtddeclientes$` |

## Canais (`pelos canais`)
| Canal | Sintaxe |
|---|---|
| Govendas App | `govendas()` |
| WhatsApp | `whatsapp("nome_do_template")` |

Valores do template WhatsApp: `e template com os valores('$totalclientes$', '10', '$nomeusuario$', 'https://app.govendas.com/#/...')`.

## Alvos (`entregue`)
`para o vendedor` (vendedor da carteira), `para o supervisor`, `para o gestor`. Redirecionar para e-mail: `e redirecione("email@exemplo.com")`. Nomes de supervisores e vendedores só aparecem se cadastrados no Govendas.

## Restrições
- Alerta é por time ou carteira, nunca por vendedor individual.
- O gatilho define a prioridade: clientes ordenados pela temporalidade do gatilho.
- Eventos não exclusivos: um cliente pode acionar vários alertas.
- A ordem dos alertas não importa.
- Nomes de alerta distintos, inclusive entre conjuntos de regras da mesma empresa.
