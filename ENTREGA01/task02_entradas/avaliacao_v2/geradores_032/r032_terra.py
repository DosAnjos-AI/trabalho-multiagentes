import sys; sys.path.insert(0, sys.argv[1])
from gen032 import gera
def rec(reg, g, t, i, dias):
    if t == "inativo": return None
    if reg == "sul" and g == "matcon" and t == "pre" and i == 2: return f"recencia de positivacao do vendedor em {dias} dias"
    return f"recencia de positivacao global em {dias} dias"
print(gera(sys.argv[2], {"prospect": "prospects da empresa", "rec": rec,
    "freq": {("norte", "consfinal"): ([28, 28, 28], [14, 14, 14], [28, 28, None])}}))
