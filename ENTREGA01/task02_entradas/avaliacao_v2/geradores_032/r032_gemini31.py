import sys; sys.path.insert(0, sys.argv[1])
from gen032 import gera
def rec(reg, g, t, i, dias):
    return None if t == "inativo" else f"recencia de positivacao global em {dias} dias"
col = {("matcon", "pre"), ("matcon", "inativo"), ("epi", "pre"), ("epi", "inativo"),
       ("consfinal", "ativo"), ("consfinal", "pre"), ("consfinal", "inativo")}
print(gera(sys.argv[2], {"prospect": "no ciclo de vida prospect com a empresa", "prospect_por": "time", "rec": rec,
    "time": "vendedores todostelevendas", "colapsa": col}))
