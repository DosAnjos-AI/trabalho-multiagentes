# Carteiras e segmentações (manual seção 4, p.8-14 e 16-17)

- `carteira "nome":` é o conjunto definitivo de clientes de um vendedor; o gerador de agendas a consome. O GoBR só monta carteiras, não exclui cliente nem monta agenda.
- `segmentacao "nome":` é agrupamento auxiliar, não gera agenda. Serve de base para carteiras, parâmetros e tags.
- Use `carteira` quando o cliente deve aparecer na agenda; `segmentacao` para regras auxiliares.

## Exclusiva x livre
- `carteira "nome":` exclusiva: o cliente incluído sai do pool das carteiras definidas depois no arquivo.
- `carteira livre "nome":` não retira do pool; o cliente pode estar em outras carteiras.

## Estrutura
```
carteira "nome":
     clientes <seleção>
     quando <filtros>
```
O `quando` restringe o resultado (ver seção 6).

## Cenário 1 — fixa mais ruptura
```
time "superv marcos":
      vendedores todostelevendas
time "superv maria":
      vendedores todosdecampo

carteira "televendas fixa com ruptura de campo":
      clientes carteirafixa("superv marcos")
      clientes ruptura("superv maria" para "superv marcos")
                      de positivacao(90 dias)
```
Cliente em ruptura que também está na carteira fixa de outro televendas pode aparecer nas duas.

## Cenário 2 — filtro quando
```
carteira "televendas fixa com ruptura de campo":
      clientes ruptura("superv maria" para "superv marcos")
                      de positivacao(90 dias)
      clientes carteirafixa("superv marcos")
      quando recencia de visita entre 10 dias e 90 dias
```
Filtros com `quando` combinam com `e`:
```
      quando recencia de visita entre 10 dias e 90 dias
               e adimplentes
```

## Cenário 3 — carteiras separadas, a ordem importa
```
carteira "televendas fixa":
      clientes carteirafixa("superv marcos")

carteira "televendas com ruptura de campo":
      clientes ruptura("superv maria" para "superv marcos")
                       de positivacao(90 dias)
```
Cliente da primeira não está disponível para a segunda. Para dar prioridade à ruptura, inverter a ordem dos blocos.

## Cenário 4 — vários times (comentários com #)
```
time "vendedor avulso":
      vendedores porid("1020")

# Televendas recebem clientes fixos + ruptura de campo
carteira "televendas fixa com ruptura de campo":
      clientes carteirafixa("superv marcos")
      clientes ruptura("superv maria" para "superv marcos")
                      de positivacao(90 dias)

# Vendedor avulso recebe clientes em ruptura de visita do campo
carteira "vendedor 1020":
      clientes ruptura("superv maria" para "vendedor avulso")
                      de visita(1 mes)

# Campo recebe sua carteira fixa com o que sobrou
carteira "campo com carteira fixa":
      clientes carteirafixa("superv maria")
```
Invertendo as duas últimas, o campo toma tudo e o vendedor 1020 fica sem clientes.

## Carteira livre
```
carteira livre "televendas com ruptura de campo":
      clientes ruptura("superv maria" para "superv marcos")
                     de positivacao(90 dias)

carteira "campo fixo":
      clientes carteirafixa("superv maria")
```
Os clientes em ruptura aparecem nos televendas e também na carteira fixa do campo.

## Segmentação como fonte
```
segmentacao "carteiras adimplentes da superv maria":
      clientes carteirafixa("superv maria")
      quando adimplentes

carteira livre "campo com carteira fixa":
      clientes segmentados("carteiras adimplentes da superv maria")

carteira "vendedor 1020":
      clientes ruptura da segmentacao("carteiras adimplentes da superv maria" para "v
                      de visita(1 mes)
```
[CORTE NO MANUAL] A linha `clientes ruptura da segmentacao(...)` está cortada na margem da p.14 após `para "v`; o restante não é legível e não foi completado.

Em carteira só uma segmentação como fonte; em segmentação, várias.

## Restrições
- Aplicar regras a times, não a vendedor individual.
- Carteiras só adicionam clientes; a exclusão é indireta, pela ordem.
- Repetição dentro da mesma carteira: o cliente pode aparecer para vendedores diferentes (ex.: dois televendas recebem o mesmo cliente em ruptura, se ele pertencer às carteiras de ambos).
- Sem repetição entre carteiras normais consecutivas; carteiras livres não excluem.
- Segmentação pode vir de vários times e/ou segmentações; carteira, de vários times ou de uma única segmentação.
- Nomes de carteiras e segmentações distintos entre si.
- Padrão: time usado em parâmetros ou alertas sem carteira definida assume `carteirafixa` dele.
