# Parâmetros: estrutura e exemplos (manual 7.1, 7.3.1, 7.3.4-7.3.7, 7.3.11, 7.6; p.38-46)

A parametrização define como cada cliente é atendido (frequência, dias, rota). Não sobrepõe parametrização manual do usuário: aplica-se a clientes sem parametrização manual ou parametrizados só pelo GoBR antes.

## Fluxo de uma regra
1. Fonte de clientes (carteira, segmentação ou time já definidos).
2. Filtros temporais (opcional).
3. Filtros de clientes com `quando` (opcional).
4. Parâmetros de atendimento (frequência, preferência de dias, roteirização, fixação).
5. Regras de conflito, `sem choque` (opcional).

## Semanal básico
```
version 1.0

time "time alberto":
     vendedores todostelevendas ativados

carteira "carteira fixa":
     clientes carteirafixa("time alberto")

parametros "semanal para o alberto":
     da carteira("carteira fixa")
     quando inatividade de 90 dias
     frequencia semanal()
```
Sem preferência declarada: valor 1 de segunda a sexta, 0 em sábado e domingo.

## Remoção de agendamento (exclusivo)
```
parametros "remover inativos da agenda":
     da carteira("carteira fixa")
     quando inatividade de 90 dias
     nao agendar
```
Não combinar `nao agendar` com frequência ou preferência na mesma regra.

## Frequência e preferência dinâmicas
```
parametros "frequencia do vendedor + preferencia nos uteis":
     da carteira("carteira fixa")
     quando inatividade de 90 dias
     frequencia do vendedor
     preferência nos dias úteis
```
`frequencia do vendedor` usa a do vendedor (padrão 7 dias se não configurou). `preferência nos dias úteis` dá valor 2 de segunda a sexta, independente do vendedor.

## Cascata de fallbacks
```
parametros "frequencia com fallback":
     da carteira("carteira fixa")
     quando inatividade de 90 dias
     frequencia do vendedor ou de qualquer vendedor ou de 35 dias
     preferência do historico ou remover
```
Frequência: vendedor, senão qualquer vendedor, senão 35 dias. Preferência: calculada do histórico de visitas; sem histórico suficiente, remove o parâmetro.

## Com restrição temporal
```
parametros "semanal dias uteis":
     da carteira("carteira fixa")
     nos dias úteis
     quando inatividade de 90 dias
     frequencia semanal()
     preferencia na segunda e na terça
```
Em sábado ou domingo a parametrização é ignorada naquela passagem.

## Limpar parametrizações
```
limpar parametros "remover parametrizacao":
     da carteira("carteira fixa")
```
Remove as parametrizações dinâmicas aplicadas pelo GoBR aos clientes da carteira.

## Restrições
- Regras incrementais: criam ou atualizam, nunca excluem (exceto `limpar parametros`).
- Sem repetição: cliente parametrizado por regra anterior não é reprocessado; a ordem importa.
- Nomes de blocos de parâmetros distintos.
- Parametrizar times ou carteiras inteiras, não vendedores individuais.
