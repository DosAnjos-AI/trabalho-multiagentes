# Regua da qualidade da prosa (0 a 10), escrita antes de abrir qualquer saida

Aplica-se por arquivo, sobre a secao `## explicacao_normalizada` comparada com `entrada_NNN.md`.
Cinco itens verificaveis, peso igual (2 pontos cada). Cada item vale 2 (cumpre), 1 (cumpre em parte, defeito pequeno e localizado) ou 0 (nao cumpre).

| # | Item | 2 pontos | 1 ponto | 0 ponto |
|---|---|---|---|---|
| 1 | Preserva valores e nomes (numeros, ids, nomes proprios, termos de negocio como "baixada na Receita Federal", "habilitados") | Nenhum valor ou termo de negocio perdido ou alterado | Um valor/termo perdido ou trocado por sinonimo que muda pouco o sentido | Dois ou mais perdidos, ou qualquer alteracao de numero |
| 2 | Preserva a ordem das ideias e a logica de prioridade ("primeiro", "depois", "vale a primeira") | Mesma ordem e mesmas relacoes | Um trecho reordenado sem mudar a logica | Ordem muda a prioridade ou perde-se o marcador de ordem |
| 3 | Remove so ruido (saudacao, redundancia); nao acrescenta nem resume | Nada acrescentado, nada resumido alem de ruido | Pequeno acrescimo/explicacao ou corte de uma frase nao essencial | Acrescenta informacao nova, resume ou corta conteudo de negocio |
| 4 | Prosa legivel, sem cercas de codigo, sem cabecalhos extras, sem listas ou marcadores que o original nao tinha | Texto corrido legivel e sem artefatos | Um artefato leve (um marcador, uma quebra estranha) | Cercas de codigo, cabecalhos extras ou texto ilegivel |
| 5 | Quebras de paragrafo preservadas (mesma quantidade de paragrafos da entrada, +-0) | Mesmo numero de paragrafos | Diferenca de 1 paragrafo | Diferenca de 2 ou mais, ou texto fundido/fragmentado |

Nota do arquivo = soma dos cinco itens (0 a 10).
- **10**: todos os itens cumprem integralmente (texto igual ou so com ruido removido).
- **5**: exemplo tipico: um valor perdido (item 1 = 0), ordem preservada (2), leve resumo (1), legivel (2), paragrafos iguais (0) ... = 5.
- **0**: todos os itens falham (valor alterado, ordem trocada, conteudo inventado, cercas de codigo, texto fundido).

Nota da coluna por versao = media das notas dos 10 arquivos.
Verificacao: itens 1 e 5 e parte do 4 sao checados por script (valores, contagem de paragrafos, cercas); itens 2 e 3 e o resto do 4 sao julgamento meu (subjetivo), registrado com uma linha quando o arquivo nao e 10.
Obs.: a "fidelidade do texto" (coluna propria) usa so valores perdidos; o item 1 aqui reaproveita a mesma medida mas tambem olha termos de negocio. Sobreposicao declarada.
