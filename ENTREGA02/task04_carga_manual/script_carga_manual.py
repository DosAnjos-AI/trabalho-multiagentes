"""Carga da tabela `manual` no BigQuery: 27 secoes de 03-secoes/ mais conceitos, invariantes e mapa (30 linhas).

Uso (da raiz do projeto):
    .venv/bin/python -B ENTREGA02/task04_carga_manual/script_carga_manual.py --verificar
    .venv/bin/python -B ENTREGA02/task04_carga_manual/script_carga_manual.py --executar

Para em qualquer falha, sem corrigir em silencio e sem apagar tabela nem dados.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime

import config as cfg

TABELA_BQ = f"{cfg.PROJETO}.{cfg.DATASET}.{cfg.TABELA}"
TABELA_EXEMPLOS_BQ = f"{cfg.PROJETO}.{cfg.DATASET}.{cfg.TABELA_EXEMPLOS}"
TABELA_BQ_CLI = f"{cfg.PROJETO}:{cfg.DATASET}.{cfg.TABELA}"

DDL = f"""CREATE TABLE IF NOT EXISTS `{TABELA_BQ}` (
  caminho STRING NOT NULL,
  tipo STRING NOT NULL,
  texto STRING NOT NULL,
  `hash` STRING NOT NULL  -- palavra reservada no BigQuery: sempre entre crases
)"""


class ErroCarga(RuntimeError):
    """Divergencia de dado, validacao ou comando externo; o script para e reporta."""


def ler_manual() -> list[dict]:
    """Passo 1: le os bytes, calcula o SHA-256 e confere total e unicidade. Divergencia aborta."""
    itens = [(p, cfg.TIPO_SECAO) for p in sorted(cfg.CAMINHO_SECOES.glob("*.md"))]
    if len(itens) != cfg.TOTAL_SECOES_ESPERADO:
        raise ErroCarga(f"{len(itens)} secoes em {cfg.CAMINHO_SECOES}; esperadas {cfg.TOTAL_SECOES_ESPERADO}.")
    itens += [(cfg.CAMINHO_MANUAL / nome, tipo) for nome, tipo in cfg.ARQUIVOS_RAIZ]
    linhas = []
    for caminho, tipo in itens:
        if not caminho.is_file():
            raise ErroCarga(f"arquivo nao existe: {caminho}")
        dados = caminho.read_bytes()
        # decodifica sem converter quebra de linha: o texto gravado precisa regerar o mesmo hash
        linhas.append({"caminho": caminho.relative_to(cfg.CAMINHO_MANUAL).as_posix(), "tipo": tipo,
                       "texto": dados.decode("utf-8"), "hash": hashlib.sha256(dados).hexdigest(), "bytes": len(dados)})
    if len(linhas) != cfg.TOTAL_ESPERADO or len({l["caminho"] for l in linhas}) != cfg.TOTAL_ESPERADO:
        raise ErroCarga(f"{len(linhas)} linhas, {len({l['caminho'] for l in linhas})} caminhos unicos; "
                        f"esperados {cfg.TOTAL_ESPERADO}.")
    return linhas


def bq(*args: str) -> str:
    """Roda o `bq` e devolve a saida; o aviso de urllib3 (stderr) so aparece se o comando falhar."""
    r = subprocess.run(["bq", f"--project_id={cfg.PROJETO}", f"--location={cfg.LOCALIZACAO_BQ}", *args],
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise ErroCarga(f"bq {' '.join(args)[:80]}... falhou (codigo {r.returncode}): {(r.stdout + r.stderr)[-600:]}")
    return r.stdout


def consulta(sql: str) -> str:
    return bq("query", "--nouse_legacy_sql", "--format=csv", sql).strip()


def conferir_caminhos(linhas: list[dict]) -> None:
    """Passo 2: caminhos de `exemplos` (leitura no BigQuery) e chaves do auxiliar precisam existir na lista lida."""
    existentes = {l["caminho"] for l in linhas}
    saida = consulta(f"SELECT DISTINCT r AS c FROM `{TABELA_EXEMPLOS_BQ}`, UNNEST(regras_extraidas) AS r").splitlines()[1:]
    de_exemplos = sorted(c for c in saida if c)
    aux = cfg.CAMINHO_AUXILIAR.read_text(encoding="utf-8").partition("## Sem entrada")[0]
    do_auxiliar = sorted({c.split("#")[0] for c in re.findall(r"^- chave: (.+)$", aux, flags=re.M)})
    faltam = [c for c in de_exemplos + do_auxiliar if c not in existentes]
    if faltam:
        raise ErroCarga(f"caminhos sem arquivo na lista lida: {sorted(set(faltam))}")
    print(f"caminhos conferidos: {len(de_exemplos)} de `exemplos` e {len(do_auxiliar)} do auxiliar, todos existem")


def validar(linhas: list[dict]) -> bool:
    """Passo 8: cada validacao imprime a saida real e a conclusao."""
    t, e = f"`{TABELA_BQ}`", f"`{TABELA_EXEMPLOS_BQ}`"
    n = str(len(linhas))
    bytes_esperados = [f"{l['caminho']},{l['bytes']}" for l in sorted(linhas, key=lambda x: x["caminho"])]
    contagem_tipos = {}
    for l in linhas:
        contagem_tipos[l["tipo"]] = contagem_tipos.get(l["tipo"], 0) + 1
    aux = cfg.CAMINHO_AUXILIAR.read_text(encoding="utf-8").partition("## Sem entrada")[0]
    chaves_aux = sorted({c.split("#")[0] for c in re.findall(r"^- chave: (.+)$", aux, flags=re.M)})
    lista_aux = ", ".join(f"'{c}'" for c in chaves_aux)
    checagens = [
        ("COUNT(*) e COUNT(DISTINCT caminho)", f"SELECT COUNT(*) AS n, COUNT(DISTINCT caminho) AS distintos FROM {t}",
         lambda s: s.splitlines()[1] == f"{n},{n}"),
        ("SHA256(texto) x `hash`: 0 divergencias",
         f"SELECT COUNTIF(TO_HEX(SHA256(CAST(texto AS BYTES))) != `hash`) AS div FROM {t}",
         lambda s: s.splitlines()[1] == "0"),
        ("bytes de texto por linha = bytes dos arquivos",
         f"SELECT caminho, LENGTH(CAST(texto AS BYTES)) AS bytes FROM {t} ORDER BY caminho",
         lambda s: s.splitlines()[1:] == bytes_esperados),
        ("caminhos distintos de `exemplos.regras_extraidas` sem linha em `manual`: 0",
         f"SELECT COUNT(DISTINCT r) AS sem_linha FROM {e}, UNNEST(regras_extraidas) AS r "
         f"WHERE r NOT IN (SELECT caminho FROM {t})", lambda s: s.splitlines()[1] == "0"),
        (f"caminhos-chave do auxiliar sem linha em `manual`: 0 (de {len(chaves_aux)})",
         f"SELECT COUNT(*) AS sem_linha FROM UNNEST([{lista_aux}]) AS c WHERE c NOT IN (SELECT caminho FROM {t})",
         lambda s: s.splitlines()[1] == "0"),
        ("linhas por tipo", f"SELECT tipo, COUNT(*) AS n FROM {t} GROUP BY tipo ORDER BY tipo",
         lambda s: s.splitlines()[1:] == [f"{k},{v}" for k, v in sorted(contagem_tipos.items())]),
        ("`hash` com 64 caracteres em todas", f"SELECT COUNTIF(LENGTH(`hash`) = 64) AS ok FROM {t}",
         lambda s: s.splitlines()[1] == n),
    ]
    todas = True
    for nome, sql, ok in checagens:
        saida = consulta(sql)
        passou = ok(saida)
        todas = todas and passou
        print(f"\n[{'PASSOU' if passou else 'FALHOU'}] {nome}\n{saida}")
    return todas


def main() -> int:
    ap = argparse.ArgumentParser(description="Carga da tabela manual (30 linhas) no BigQuery.")
    grupo = ap.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--verificar", action="store_true", help="passos 1 e 2: le, calcula hash e confere caminhos; nao grava")
    grupo.add_argument("--executar", action="store_true", help="passos 1, 2 e 4 a 8: monta o NDJSON, cria a tabela, carrega e valida")
    args = ap.parse_args()
    try:
        linhas = ler_manual()
        print(f"leitura local ok: {len(linhas)} linhas, caminhos unicos")
        conferir_caminhos(linhas)
        if args.verificar:
            for l in linhas:
                print(f"{l['hash']}  {l['bytes']:>5}  {l['tipo']:<11} {l['caminho']}")
            return 0
        pasta = cfg.CAMINHO_SAIDA / datetime.now().strftime("%Y%m%d-%H%M%S")
        pasta.mkdir(parents=True, exist_ok=True)
        ndjson = pasta / "manual.ndjson"
        with ndjson.open("w", encoding="utf-8", newline="\n") as f:
            for l in linhas:
                f.write(json.dumps({k: l[k] for k in ("caminho", "tipo", "texto", "hash")}, ensure_ascii=False) + "\n")
        print(f"gravado {ndjson}")
        bq("query", "--nouse_legacy_sql", DDL)
        print(f"tabela {TABELA_BQ}: CREATE TABLE IF NOT EXISTS executado")
        antes = consulta(f"SELECT COUNT(*) AS n FROM `{TABELA_BQ}`").splitlines()[1]
        if antes != "0":
            raise ErroCarga(f"trava: a tabela {TABELA_BQ} ja tem {antes} linhas (esperado 0). Nada foi carregado.")
        print("trava: COUNT(*) antes da carga = 0")
        print(bq("load", "--source_format=NEWLINE_DELIMITED_JSON", "--noautodetect", TABELA_BQ_CLI, str(ndjson)).strip()[-200:])
        return 0 if validar(linhas) else 1
    except ErroCarga as e:
        print(f"PAROU: {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
