import sys; sys.path.insert(0, sys.argv[1])
from fmt import bloco, grava, fat

SUL = '"PR", "SC", "RS", "SP", "RJ", "MG", "ES", "GO", "MT", "MS", "DF"'
NOR = '"AC", "AP", "AM", "PA", "RO", "RR", "TO", "AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"'
B = []
B.append(bloco('time "televendas"', ["vendedores todostelevendas ativados"]))
B.append(bloco('carteira "sul sudeste centro-oeste"', ['clientes carteirafixa("televendas")'], [f"uf do estado igual({SUL})"]))
B.append(bloco('carteira "norte nordeste"', ['clientes carteirafixa("televendas")'], [f"uf do estado igual({NOR})"]))
B.append(bloco('parametros "baixados na receita"', ['do time("televendas")'], ["status na receita federal definido como baixada"], ["nao agendar"]))
for c in ("sul sudeste centro-oeste", "norte nordeste"):
    B.append(bloco(f'parametros "prospects {c}"', [f'da carteira("{c}")'], ["prospects da empresa"], ["frequencia de 14 dias"]))

G1 = 'ramo de atividade igual("MATCON", "FERRAGISTA", "AGROPECUARIA", "HOME CENTER")'
EPI = 'ramo de atividade igual("EPI", "LICITACAO")'
ATA = 'ramo de atividade igual("ATACADO")'
CF = 'ramo de atividade igual("CONS. FINAL")'

def faixas(cart, ramo, nome, rec, lim, freqs, recs=None):
    """rec: filtro de recencia (ou None); lim: limites de faturamento + None; freqs: frequencias (None = sem frequencia)."""
    for i, (v, f) in enumerate(zip(lim, freqs)):
        r = recs[i] if recs else rec
        q = [ramo] + ([r] if r else []) + ([fat("media faturada", v)] if v else [])
        dep = [f"frequencia de {f} dias"] if f else []
        B.append(bloco(f'parametros "{cart} {nome} {v or "demais"}"', [f'da carteira("{cart}")'], q, dep))

g = lambda n: f"recencia de positivacao global em {n} dias"
for cart, a, b in (("sul sudeste centro-oeste", 120, 150), ("norte nordeste", 150, 180)):
    L1 = [25000, 10000, None]
    faixas(cart, G1, f"matcon {a}", g(a), L1, [14, 21, 28])
    if cart.startswith("sul"):
        faixas(cart, G1, f"matcon {b}", None, L1, [14, 14, 14], recs=[g(b), g(b), f"recencia de positivacao do vendedor em {b} dias"])
    else:
        faixas(cart, G1, f"matcon {b}", g(b), L1, [14, 14, 14])
    faixas(cart, G1, "matcon inativos", "inativos", L1, [14, 14, 14])
    faixas(cart, EPI, f"epi {a}", g(a), L1, [14, 21, 28])
    faixas(cart, EPI, f"epi {b}", g(b), L1, [14, 14, 14])
    faixas(cart, EPI, "epi inativos", "inativos", L1, [14, 14, 14])
    L2 = [50000, 25000, None]
    faixas(cart, ATA, f"atacado {a}", g(a), L2, [10, 14, 21])
    faixas(cart, ATA, f"atacado {b}", g(b), L2, [7, 10, 14])
    faixas(cart, ATA, "atacado inativos", "inativos", L2, [10, 10, 21])
    L3 = [15000, 10000, None]
    faixas(cart, CF, f"cons final {a}", g(a), L3, [28, 28, 28])
    faixas(cart, CF, f"cons final {b}", g(b), L3, [14, 14, 14])
    faixas(cart, CF, "cons final inativos", "inativos", L3, [28, 28, None] if cart.startswith("norte") else [28, 28, 28])
B.append(bloco('parametros "restante"', ['do time("televendas")'], None, ["nao agendar"]))
grava(sys.argv[2], B)
print(len(B))
