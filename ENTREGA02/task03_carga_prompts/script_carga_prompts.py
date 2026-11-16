"""Carga da tabela `prompts` no BigQuery: os 3 prompts em uso e os legados, uma linha por hash.

Uso (da raiz do projeto):
    .venv/bin/python -B ENTREGA02/task03_carga_prompts/script_carga_prompts.py --verificar
    .venv/bin/python -B ENTREGA02/task03_carga_prompts/script_carga_prompts.py --executar

Para em qualquer falha, sem corrigir em silencio e sem apagar tabela nem dados.
"""
import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import config as cfg

TABELA_BQ = f"{cfg.PROJETO}.{cfg.DATASET}.{cfg.TABELA}"
TABELA_EXEMPLOS_BQ = f"{cfg.PROJETO}.{cfg.DATASET}.{cfg.TABELA_EXEMPLOS}"
TABELA_BQ_CLI = f"{cfg.PROJETO}:{cfg.DATASET}.{cfg.TABELA}"

DDL = f"""CREATE TABLE IF NOT EXISTS `{TABELA_BQ}` (
  `hash` STRING NOT NULL,  -- palavra reservada no BigQuery: sempre entre crases
  arquivo STRING NOT NULL,
  tipo STRING NOT NULL,
  versao STRING NOT NULL,
  texto STRING NOT NULL,
  ativo BOOL NOT NULL
)"""


class ErroCarga(RuntimeError):
    """Divergencia de dado, validacao ou comando externo; o script para e reporta."""


def ler_prompts() -> list[dict]:
    """Passo 1: le os bytes, calcula o SHA-256 e valida a configuracao. Divergencia aborta."""
    linhas, vistos = [], {}
    for p in cfg.PROMPTS:
        caminho = Path(p["caminho"])
        if p["tipo"] not in cfg.TIPOS_ACEITOS:
            raise ErroCarga(f"tipo recebido: {p['tipo']!r} em {caminho.name}. Aceitos: {list(cfg.TIPOS_ACEITOS)}. "
                            f"Configure em ENTREGA02/task03_carga_prompts/config.py.")
        if not caminho.is_file():
            raise ErroCarga(f"arquivo nao existe: {caminho}")
        dados = caminho.read_bytes()
        h = hashlib.sha256(dados).hexdigest()
        if h in vistos:
            raise ErroCarga(f"hash repetido: {caminho} e {vistos[h]} (uma linha por hash).")
        vistos[h] = caminho
        # decodifica os bytes sem converter quebra de linha: o texto gravado precisa regerar o mesmo hash
        linhas.append({"hash": h, "arquivo": caminho.name, "tipo": p["tipo"], "versao": p["versao"],
                       "texto": dados.decode("utf-8"), "ativo": p["ativo"], "bytes": len(dados)})
    for tipo in cfg.TIPOS_ACEITOS:
        ativos = sum(1 for l in linhas if l["tipo"] == tipo and l["ativo"])
        if ativos != 1:
            raise ErroCarga(f"tipo {tipo!r} com {ativos} ativos na configuracao; esperado exatamente 1.")
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


def conferir_exemplos(linhas: list[dict]) -> None:
    """Os hashes dos 3 em uso precisam ser os distintos de `exemplos` (so leitura)."""
    saida = consulta(
        f"SELECT metadados_normalizado.hash_prompt AS n, metadados_normalizado.hash_auxiliar_manual AS a, "
        f"metadados_geracao.hash_prompt AS g FROM `{TABELA_EXEMPLOS_BQ}` GROUP BY ALL").splitlines()
    if len(saida) != 2:
        raise ErroCarga(f"exemplos tem {len(saida) - 1} combinacoes de hash de prompt; esperada 1:\n" + "\n".join(saida))
    n, a, g = saida[1].split(",")
    em_uso = {l["tipo"]: l["hash"] for l in linhas if l["ativo"]}
    esperado = {"normalizador": n, "auxiliar_manual": a, "geracao_explicacao": g}
    if em_uso != esperado:
        raise ErroCarga(f"hashes em uso {em_uso} diferem dos de exemplos {esperado}.")
    print("hashes dos 3 prompts em uso batem com os de `exemplos`")


def validar(linhas: list[dict]) -> bool:
    """Passo 8: cada validacao imprime a saida real e a conclusao."""
    t, e = f"`{TABELA_BQ}`", f"`{TABELA_EXEMPLOS_BQ}`"
    bytes_esperados = "\n".join(f"{l['arquivo']},{l['versao']},{l['bytes']}" for l in sorted(
        linhas, key=lambda x: (x["arquivo"], x["versao"])))
    ligacoes = (f"SELECT COUNTIF(n.hash IS NULL) AS sem_normalizador, COUNTIF(a.hash IS NULL) AS sem_auxiliar, "
                f"COUNTIF(g.hash IS NULL) AS sem_geracao, "
                f"COUNTIF(n.arquivo != x.metadados_normalizado.id_prompt) AS arquivo_normalizador_difere, "
                f"COUNTIF(a.arquivo != x.metadados_normalizado.id_auxiliar_manual) AS arquivo_auxiliar_difere, "
                f"COUNTIF(g.arquivo != x.metadados_geracao.arquivo_prompt) AS arquivo_geracao_difere FROM {e} x "
                f"LEFT JOIN {t} n ON n.hash = x.metadados_normalizado.hash_prompt AND n.tipo = 'normalizador' "
                f"LEFT JOIN {t} a ON a.hash = x.metadados_normalizado.hash_auxiliar_manual AND a.tipo = 'auxiliar_manual' "
                f"LEFT JOIN {t} g ON g.hash = x.metadados_geracao.hash_prompt AND g.tipo = 'geracao_explicacao'")
    checagens = [
        (f"COUNT(*) = {len(linhas)}", f"SELECT COUNT(*) AS n FROM {t}", lambda s: s.splitlines()[1] == str(len(linhas))),
        ("SHA256(texto) x hash: 0 divergencias",
         f"SELECT COUNTIF(TO_HEX(SHA256(CAST(texto AS BYTES))) != `hash`) AS div FROM {t}",
         lambda s: s.splitlines()[1] == "0"),
        ("bytes de texto por linha = bytes dos arquivos",
         f"SELECT arquivo, versao, LENGTH(CAST(texto AS BYTES)) AS bytes FROM {t} ORDER BY arquivo, versao",
         lambda s: "\n".join(s.splitlines()[1:]) == bytes_esperados),
        ("ligacoes com `exemplos` (linha existe e arquivo igual): tudo 0", ligacoes,
         lambda s: s.splitlines()[1] == "0,0,0,0,0,0"),
        ("ativo = true: exatamente 1 por tipo",
         f"SELECT tipo, COUNTIF(ativo) AS ativos FROM {t} GROUP BY tipo ORDER BY tipo",
         lambda s: s.splitlines()[1:] == [f"{x},1" for x in sorted(cfg.TIPOS_ACEITOS)]),
        ("hash com 64 caracteres em todas",
         f"SELECT COUNTIF(LENGTH(`hash`) = 64) AS ok FROM {t}", lambda s: s.splitlines()[1] == str(len(linhas))),
    ]
    todas = True
    for nome, sql, ok in checagens:
        saida = consulta(sql)
        passou = ok(saida)
        todas = todas and passou
        print(f"\n[{'PASSOU' if passou else 'FALHOU'}] {nome}\n{saida}")
    return todas


def main() -> int:
    ap = argparse.ArgumentParser(description="Carga da tabela prompts (em uso e legados) no BigQuery.")
    grupo = ap.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--verificar", action="store_true", help="passo 1: le, calcula hash e confere com `exemplos`; nao grava")
    grupo.add_argument("--executar", action="store_true", help="passos 1 e 4 a 8: monta o NDJSON, cria a tabela, carrega e valida")
    args = ap.parse_args()
    try:
        linhas = ler_prompts()
        print(f"leitura local ok: {len(linhas)} prompts, hashes distintos, 1 ativo por tipo")
        conferir_exemplos(linhas)
        if args.verificar:
            for l in linhas:
                print(f"{l['hash']}  {l['bytes']:>6}  {l['tipo']:<19} {l['versao']:<12} ativo={l['ativo']}  {l['arquivo']}")
            return 0
        pasta = cfg.CAMINHO_SAIDA / datetime.now().strftime("%Y%m%d-%H%M%S")
        pasta.mkdir(parents=True, exist_ok=True)
        ndjson = pasta / "prompts.ndjson"
        with ndjson.open("w", encoding="utf-8", newline="\n") as f:
            for l in linhas:
                f.write(json.dumps({k: l[k] for k in ("hash", "arquivo", "tipo", "versao", "texto", "ativo")},
                                   ensure_ascii=False) + "\n")
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
