# Exemplos de regras de negócio e estrutura geral do arquivo (manual seção 2, p.3-4)

A linguagem gorules é uma DSL (linguagem de domínio específico) que liga o discurso da equipe de vendas ao motor de regras do Govendas. O processador roda sempre que as regras precisam ser aplicadas: gerar agenda, parametrizar clientes ou disparar alertas.

## Exemplos de regras de negócio que a linguagem expressa (2.1, p.3)
- "Os vendedores de campo devem visitar todos os clientes ativos dentro do mês."
- "Um cliente ativo é aquele que comprou nos últimos 90 dias."
- "Os televendas devem ligar para todos os clientes visitados pelos vendedores de campo no dia posterior à visita, somente se houver venda."
- "Os vendedores do supervisor X que atendem a cidade Y devem visitar seus clientes em um período máximo de 7 dias."
- "Um cliente ativo independente do vendedor não deve ficar mais de 15 dias sem atendimento."
- "Na primeira sexta-feira de todo mês, os televendas devem ligar para os inativos dos vendedores de campo."

## Estrutura geral (2.2, p.3-4)
Todo arquivo começa com a declaração de versão e pode conter até quatro categorias de regras, usadas em sequência:
```
version 1.0

# 1. Definição de times de vendedores
time "nome do time":
       vendedores <seleção>

# 2. Definição de segmentações (opcional)
segmentacao "nome da segmentação":
       clientes <seleção>
       quando <filtros>

# 3. Definição de carteiras OU parametrizações OU alertas OU tags
carteira "nome da carteira":
       clientes <seleção>
       quando <filtros>
```
A tabela das categorias (`time`, `segmentacao`, `carteira`, `parametros`, `alertas`, `tags`) e o propósito de cada uma estão em `02-invariantes.md`, seção "Categorias".
