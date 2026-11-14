# Times de vendedores (manual seção 3, p.5-7)

Bloco `time "nome":` com uma ou mais linhas `vendedores <seleção>`. Linhas de um mesmo time somam (aditivo); vendedor repetido conta uma vez. O mesmo vendedor pode estar em times diferentes. Todo vendedor deve estar cadastrado no Govendas.

```
version 1.0

time "supervisor marcos":
       vendedores todostelevendas

time "supervisora maria":
       vendedores todosdecampo

time "vendedor avulso":
       vendedores porid("1020", "1021")
```

## Funções de seleção
| Função | Seleciona |
|---|---|
| `todos` | todos os vendedores cadastrados na empresa |
| `todostelevendas` | só vendedores do tipo televendas |
| `todosdecampo` | só vendedores do tipo campo (presencial) |
| `porid("id1", "id2", ...)` | vendedores pelos IDs, strings separadas por vírgula |

## Modificadores (opcionais, só para `todos`, `todostelevendas`, `todosdecampo`, nesta ordem)
| Modificador | Efeito |
|---|---|
| `dos supervisores("id1", "id2", ...)` | só vendedores dos supervisores informados |
| `do supervisor("id")` | variante singular |
| `ativados` | só vendedores habilitados a gerar agenda |
| `inativados` | só vendedores desabilitados (limpeza/análise) |
| `menos("id1", "id2", ...)` | exclui os IDs informados |

`ativados`/`inativados` referem-se ao cadastro do vendedor, não a cliente ativo/inativo.
Não implementado: "cadastrados no Govendas", "com muitos clientes", "com poucos clientes", "junto a supervisor com poucos vendedores".

## Exemplo com modificadores
```
time "supervisor marcos":
       vendedores todostelevendas
       vendedores todosdecampo
                    dos supervisores("13","14")
                    ativados
                    menos("345","567","432")
```
Todos os televendas (sem restrição) mais os vendedores de campo dos supervisores 13 e 14, ativados, menos 345, 567 e 432.

## Restrições
Nomes de times distintos no arquivo; vendedor repetido em times diferentes é permitido.
