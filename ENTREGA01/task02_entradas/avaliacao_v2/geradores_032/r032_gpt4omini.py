import sys; sys.path.insert(0, sys.argv[1])
from fmt import bloco, grava
from gen032 import SUL, NOR, RAMOS
B = [bloco('time "televendas"', ["vendedores todostelevendas ativados"])]
B.append(bloco('carteira "sul sudeste centro-oeste"', ['clientes carteirafixa("televendas")'], [f"uf do estado igual({SUL})"]))
B.append(bloco('carteira "norte nordeste"', ['clientes carteirafixa("televendas")'], [f"uf do estado igual({NOR})"]))
B.append(bloco('parametros "baixados na receita"', ['do time("televendas")'], ["status na receita federal definido como baixada"], ["nao agendar"]))
for c in ("sul sudeste centro-oeste", "norte nordeste"):
    B.append(bloco(f'parametros "prospects {c}"', [f'da carteira("{c}")'], ["no ciclo de vida prospect com a empresa"], ["frequencia de 14 dias"]))
r = f'ramo de atividade igual({RAMOS["matcon"]})'
src = ['da carteira("sul sudeste centro-oeste")']
B.append(bloco('parametros "matcon ativos curva A"', src, [r, "recencia de positivacao em 120 dias", "media faturada no ano com a empresa maior que R$ 25000"], ["frequencia de 14 dias"]))
B.append(bloco('parametros "matcon ativos curva B"', src, [r, "recencia de positivacao em 120 dias", "media faturada no ano com a empresa maior que R$ 10000"], ["frequencia de 21 dias"]))
B.append(bloco('parametros "matcon inativos acima de 25000"', src, [r, "media faturada no ano com a empresa maior que R$ 25000"], ["frequencia de 14 dias"]))
B.append(bloco('parametros "restante"', ['do time("televendas")'], None, ["nao agendar"]))
grava(sys.argv[2], B); print(len(B))
