import sys; sys.path.insert(0, sys.argv[1])
from gen032 import gera
def rec(reg, g, t, i, dias):
    return None if t == "inativo" else f"recencia de positivacao global em {dias} dias"
print(gera(sys.argv[2], {"prospect": "no ciclo de vida prospect com a empresa", "rec": rec}))
