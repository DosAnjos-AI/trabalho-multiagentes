"""Carga dos 193 exemplos sinteticos na tabela `exemplos` do BigQuery, com embeddings (formato B).

Uso (da raiz do projeto):
    .venv/bin/python -B ENTREGA02/task02_carga_exemplos/script_carga_exemplos.py --estimar
    .venv/bin/python -B ENTREGA02/task02_carga_exemplos/script_carga_exemplos.py --executar
    .venv/bin/python -B ENTREGA02/task02_carga_exemplos/script_carga_exemplos.py --executar --retomar <pasta de saida>

Para em qualquer falha, sem corrigir em silencio e sem apagar tabela nem dados.
"""
import argparse
import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import google.auth
import google.auth.transport.requests
import requests

import config as cfg

TABELA_BQ = f"{cfg.PROJETO}.{cfg.DATASET}.{cfg.TABELA}"          # forma SQL (entre crases)
TABELA_BQ_CLI = f"{cfg.PROJETO}:{cfg.DATASET}.{cfg.TABELA}"      # forma do `bq load`

CAMPOS_NORMALIZADO = ("origem", "tipo_entrada", "id_sessao_turno", "id_explicacao", "id_prompt", "hash_prompt",
                      "id_auxiliar_manual", "hash_auxiliar_manual", "versao_normalizador", "hash_normalizador",
                      "modelo", "temperatura", "tokens_entrada", "tokens_saida", "custo_usd", "tempo_segundos",
                      "timestamp")
CAMPOS_ENTRADA = ("regra_id", "arquivo_regra", "hash_regra_sha256", "arquivo_prompt", "hash_prompt_sha256", "modelo",
                  "fornecedor", "temperatura", "tokens_entrada", "tokens_saida", "custo_usd", "tempo_segundos",
                  "timestamp")

DDL = f"""CREATE TABLE IF NOT EXISTS `{TABELA_BQ}` (
  exemplo_id STRING NOT NULL,
  origem STRING NOT NULL,
  regra_id STRING,
  id_sessao_turno STRING,
  entrada STRING,
  explicacao_normalizada STRING NOT NULL,
  regras_extraidas ARRAY<STRING>,
  sem_chave ARRAY<STRING>,
  gobr STRING,
  hash_gobr STRING,
  embedding ARRAY<FLOAT64>,
  embedding_modelo STRING NOT NULL,
  hash_texto_embedding STRING NOT NULL,
  metadados_normalizado STRUCT<
    tipo_entrada STRING, id_explicacao STRING, id_prompt STRING, hash_prompt STRING, id_auxiliar_manual STRING,
    hash_auxiliar_manual STRING, versao_normalizador STRING, hash_normalizador STRING, modelo STRING,
    temperatura STRING, tokens_entrada INT64, tokens_saida INT64, custo_usd NUMERIC, tempo_segundos FLOAT64,
    timestamp TIMESTAMP> NOT NULL,
  metadados_geracao STRUCT<
    arquivo_prompt STRING, hash_prompt STRING, modelo STRING, fornecedor STRING, temperatura STRING,
    tokens_entrada INT64, tokens_saida INT64, custo_usd NUMERIC, tempo_segundos FLOAT64, timestamp TIMESTAMP>
)"""


class ErroCarga(RuntimeError):
    """Divergencia de dado, validacao ou comando externo; o script para e reporta."""


def sha256_texto(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def ler_bloco(texto: str, campos: tuple[str, ...], origem: str) -> tuple[dict, str]:
    """Bloco `---` do topo (campo: valor) e o que vem depois. Exige exatamente os campos esperados, na ordem."""
    linhas = texto.split("\n")
    if linhas[0] != "---" or "---" not in linhas[1:]:
        raise ErroCarga(f"{origem}: sem bloco de metadados no topo.")
    fim = linhas.index("---", 1)
    pares = [linha.split(": ", 1) for linha in linhas[1:fim]]
    if tuple(p[0] for p in pares) != campos:
        raise ErroCarga(f"{origem}: campos {[p[0] for p in pares]}; esperados {list(campos)}.")
    bloco = {k: (None if v == "null" else v) for k, v in pares}
    return bloco, "\n".join(linhas[fim + 1:])


def ler_exemplos() -> list[dict]:
    """Passo 2: le e valida os 193 localmente. Qualquer divergencia aborta."""
    exemplos = []
    for caminho in sorted(cfg.CAMINHO_NORMALIZADOS.glob("normalizado_*.md")):
        n = caminho.stem.removeprefix("normalizado_")
        norm, corpo = ler_bloco(caminho.read_bytes().decode("utf-8"), CAMPOS_NORMALIZADO, caminho.name)
        explicacao = corpo.split("## explicacao_normalizada\n", 1)[1].split("\n## regras_extraidas", 1)[0].strip()
        json_regras = json.loads(corpo.split("## regras_extraidas\n", 1)[1])
        arq_entrada = cfg.CAMINHO_ENTRADAS / f"entrada_{n}.md"
        ent, corpo_entrada = ler_bloco(arq_entrada.read_bytes().decode("utf-8"), CAMPOS_ENTRADA, arq_entrada.name)
        arq_gobr = cfg.CAMINHO_GOBR / f"regra_{n}.gobr"
        bytes_gobr = arq_gobr.read_bytes()
        erros = []
        if norm["origem"] != "sintetico" or norm["id_sessao_turno"] is not None:
            erros.append("origem/id_sessao_turno inesperados")
        if norm["id_explicacao"] != f"entrada_{n}.md" or ent["regra_id"] != n or ent["arquivo_regra"] != arq_gobr.name:
            erros.append("ids inconsistentes entre normalizado, entrada e gobr")
        if hashlib.sha256(bytes_gobr).hexdigest() != ent["hash_regra_sha256"]:
            erros.append("hash do .gobr diverge de hash_regra_sha256")
        if set(json_regras) != {"regras_extraidas", "sem_chave"}:
            erros.append(f"chaves do JSON de regras: {sorted(json_regras)}")
        if not explicacao:
            erros.append("explicacao_normalizada vazia")
        if erros:
            raise ErroCarga(f"{caminho.name}: " + "; ".join(erros))
        exemplos.append({"n": n, "norm": norm, "ent": ent, "entrada": corpo_entrada.strip(), "explicacao": explicacao,
                         "regras": json_regras["regras_extraidas"], "sem_chave": json_regras["sem_chave"],
                         "gobr": bytes_gobr.decode("utf-8")})
    if len(exemplos) != cfg.TOTAL_ESPERADO:
        raise ErroCarga(f"{len(exemplos)} normalizados lidos em {cfg.CAMINHO_NORMALIZADOS}; esperados {cfg.TOTAL_ESPERADO}.")
    return exemplos


def texto_embedding(explicacao: str) -> str:
    """Texto exato enviado ao modelo: prefixo B mais a explicacao normalizada."""
    return cfg.PREFIXO_EMBEDDING + explicacao


def preparar_cache(pasta: Path, exemplos: list[dict], retomar: bool) -> dict[str, dict]:
    """Cache {id: registro}. Em execucao nova, copia as linhas B do teste cujo texto bate pelo hash."""
    arquivo = pasta / "embeddings.jsonl"
    if retomar:
        cache = {}
        for linha in arquivo.read_text(encoding="utf-8").splitlines():
            r = json.loads(linha)
            cache[r["id"]] = r
        return cache
    pasta.mkdir(parents=True, exist_ok=True)
    esperado = {e["n"]: sha256_texto(texto_embedding(e["explicacao"])) for e in exemplos}
    cache = {}
    for linha in cfg.CAMINHO_CACHE_TESTE.read_text(encoding="utf-8").splitlines():
        r = json.loads(linha)
        if r["chave"] == cfg.CHAVE_FORMATO_B_NO_TESTE and esperado.get(r["id"]) == r["hash_texto"]:
            cache[r["id"]] = {"id": r["id"], "hash_texto": r["hash_texto"], "tokens": r["tokens"], "vetor": r["vetor"]}
    with arquivo.open("w", encoding="utf-8", newline="\n") as f:
        for r in cache.values():
            f.write(json.dumps(r) + "\n")
    return cache


def projetar(exemplos: list[dict], faltantes: int) -> float:
    """Passo 3: projecao pessimista (so do que falta gerar) e conferencia do teto."""
    chars = sum(len(texto_embedding(e["explicacao"])) for e in exemplos) * faltantes / len(exemplos)
    tokens = chars / cfg.CARACTERES_POR_TOKEN_PESSIMISTA
    custo = tokens / 1e6 * cfg.USD_POR_MILHAO
    print(f"embeddings a gerar={faltantes} tokens_projetados={tokens:,.0f} custo_usd_projetado={custo:.4f} "
          f"teto_usd={cfg.TETO_GASTO_USD} (preco de referencia: HIPOTESE)")
    if custo > cfg.TETO_GASTO_USD:
        raise ErroCarga(f"projecao US$ {custo:.4f} acima do teto US$ {cfg.TETO_GASTO_USD}. Ajuste TETO_GASTO_USD em config.py.")
    return custo


def chamar_api(sessao: requests.Session, credenciais, texto: str) -> tuple[list[float], int]:
    corpo = {"content": {"parts": [{"text": texto}]}, "outputDimensionality": cfg.DIMENSOES}
    for tentativa in range(1, cfg.TENTATIVAS_API + 1):
        if not credenciais.valid:
            credenciais.refresh(google.auth.transport.requests.Request())
        r = sessao.post(cfg.ENDPOINT, json=corpo, timeout=60, headers={
            "Authorization": f"Bearer {credenciais.token}", "x-goog-user-project": cfg.PROJETO})
        if r.status_code == 200:
            j = r.json()
            return j["embedding"]["values"], int(j["usageMetadata"]["promptTokenCount"])
        if r.status_code in (429, 500, 502, 503, 504) and tentativa < cfg.TENTATIVAS_API:
            time.sleep(2 ** tentativa)
            continue
        raise ErroCarga(f"embedContent HTTP {r.status_code}: {r.text[:300]}")


def gerar_faltantes(pasta: Path, exemplos: list[dict], cache: dict[str, dict]) -> int:
    """Passo 4: gera so o que falta, gravando cada vetor logo apos a chamada. Devolve tokens novos."""
    faltam = [e for e in exemplos if e["n"] not in cache]
    if not faltam:
        return 0
    credenciais, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    sessao = requests.Session()
    tokens_novos = 0
    with (pasta / "embeddings.jsonl").open("a", encoding="utf-8", newline="\n") as f:
        for e in faltam:
            if tokens_novos / 1e6 * cfg.USD_POR_MILHAO > cfg.TETO_GASTO_USD:
                raise ErroCarga("teto de gasto atingido durante a geracao; cache preservado.")
            texto = texto_embedding(e["explicacao"])
            vetor, tok = chamar_api(sessao, credenciais, texto)
            r = {"id": e["n"], "hash_texto": sha256_texto(texto), "tokens": tok, "vetor": vetor}
            f.write(json.dumps(r) + "\n")
            f.flush()
            cache[e["n"]] = r
            tokens_novos += tok
    return tokens_novos


def montar_registro(e: dict, emb: dict) -> dict:
    """Uma linha do NDJSON, com os tipos do schema aprovado."""
    n, ent = e["n"], e["ent"]
    norm = {k: e["norm"][k] for k in CAMPOS_NORMALIZADO if k not in ("origem", "id_sessao_turno")}
    geracao = {"arquivo_prompt": ent["arquivo_prompt"], "hash_prompt": ent["hash_prompt_sha256"],
               **{k: ent[k] for k in ("modelo", "fornecedor", "temperatura", "tokens_entrada", "tokens_saida",
                                      "custo_usd", "tempo_segundos", "timestamp")}}
    for bloco in (norm, geracao):
        for k in ("tokens_entrada", "tokens_saida"):
            bloco[k] = int(bloco[k])
        bloco["tempo_segundos"] = float(bloco["tempo_segundos"])
    return {"exemplo_id": f"sintetico:{n}", "origem": e["norm"]["origem"], "regra_id": ent["regra_id"],
            "id_sessao_turno": e["norm"]["id_sessao_turno"], "entrada": e["entrada"],
            "explicacao_normalizada": e["explicacao"], "regras_extraidas": e["regras"], "sem_chave": e["sem_chave"],
            "gobr": e["gobr"], "hash_gobr": ent["hash_regra_sha256"], "embedding": emb["vetor"],
            "embedding_modelo": cfg.MODELO_EMBEDDING, "hash_texto_embedding": emb["hash_texto"],
            "metadados_normalizado": norm, "metadados_geracao": geracao}


def bq(*args: str) -> str:
    """Roda o `bq` e devolve a saida; o aviso de urllib3 (stderr) so aparece se o comando falhar."""
    r = subprocess.run(["bq", f"--project_id={cfg.PROJETO}", f"--location={cfg.LOCALIZACAO_BQ}", *args],
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise ErroCarga(f"bq {' '.join(args)[:80]}... falhou (codigo {r.returncode}): {(r.stdout + r.stderr)[-600:]}")
    return r.stdout


def consulta(sql: str) -> str:
    return bq("query", "--nouse_legacy_sql", "--format=csv", sql).strip()


def validar(exemplos: list[dict]) -> bool:
    """Passo 9: cada validacao imprime a consulta, a saida real e a conclusao."""
    t = f"`{TABELA_BQ}`"
    soma_regras = sum(len(e["regras"]) for e in exemplos)
    soma_sem = sum(len(e["sem_chave"]) for e in exemplos)
    ids = ", ".join(f"'sintetico:{i}'" for i in cfg.IDS_VECTOR_SEARCH)
    prefixo = cfg.PREFIXO_EMBEDDING
    checagens = [
        ("COUNT(*) = 193", f"SELECT COUNT(*) AS n FROM {t}", lambda s: s.splitlines()[1] == "193"),
        ("sha256(gobr) x hash_gobr: 0 divergencias",
         f"SELECT COUNTIF(TO_HEX(SHA256(CAST(gobr AS BYTES))) != hash_gobr) AS div FROM {t}",
         lambda s: s.splitlines()[1] == "0"),
        ("ARRAY_LENGTH(embedding) = 3072 nos 193",
         f"SELECT COUNTIF(ARRAY_LENGTH(embedding) = {cfg.DIMENSOES}) AS ok FROM {t}",
         lambda s: s.splitlines()[1] == "193"),
        ("sha256(prefixo B + explicacao) x hash_texto_embedding: 0 divergencias",
         f"SELECT COUNTIF(TO_HEX(SHA256(CAST(CONCAT('{prefixo}', explicacao_normalizada) AS BYTES))) "
         f"!= hash_texto_embedding) AS div FROM {t}", lambda s: s.splitlines()[1] == "0"),
        (f"somas regras_extraidas={soma_regras} e sem_chave={soma_sem} (dos arquivos)",
         f"SELECT SUM(ARRAY_LENGTH(regras_extraidas)) AS regras, SUM(ARRAY_LENGTH(sem_chave)) AS sem_chave FROM {t}",
         lambda s: s.splitlines()[1] == f"{soma_regras},{soma_sem}"),
        ("metadados_geracao NULL = 0 e 1 hash_prompt distinto",
         f"SELECT COUNTIF(metadados_geracao IS NULL) AS nulos, "
         f"COUNT(DISTINCT metadados_geracao.hash_prompt) AS hashes FROM {t}", lambda s: s.splitlines()[1] == "0,1"),
        ("VECTOR_SEARCH COSINE: top-1 = o proprio exemplo (3 exemplos)",
         f"SELECT query.exemplo_id AS consulta, base.exemplo_id AS top1, distance FROM VECTOR_SEARCH("
         f"(SELECT exemplo_id, embedding FROM {t} WHERE origem = 'sintetico'), 'embedding', "
         f"(SELECT exemplo_id, embedding FROM {t} WHERE exemplo_id IN ({ids})), top_k => 1, "
         f"distance_type => 'COSINE', options => '{{\"use_brute_force\": true}}') ORDER BY consulta",
         lambda s: len(s.splitlines()) == 4 and all(l.split(",")[0] == l.split(",")[1] for l in s.splitlines()[1:])),
    ]
    todas = True
    for nome, sql, ok in checagens:
        saida = consulta(sql)
        passou = ok(saida)
        todas = todas and passou
        print(f"\n[{'PASSOU' if passou else 'FALHOU'}] {nome}\n{saida}")
    return todas


def main() -> int:
    ap = argparse.ArgumentParser(description="Carga da tabela exemplos (193 sinteticos) no BigQuery.")
    grupo = ap.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--estimar", action="store_true", help="passos 2 e 3: valida e projeta; nao grava nem chama a API")
    grupo.add_argument("--executar", action="store_true", help="passos 2 a 9 (cria a tabela e carrega)")
    ap.add_argument("--retomar", help="nome de uma pasta existente em saida/ para continuar o cache")
    args = ap.parse_args()
    try:
        exemplos = ler_exemplos()
        print(f"leitura local ok: {len(exemplos)} exemplos, ids consistentes, hash do .gobr conferido")
        if args.estimar:
            cache_teste = {json.loads(l)["id"] for l in cfg.CAMINHO_CACHE_TESTE.read_text(encoding="utf-8").splitlines()
                           if json.loads(l)["chave"] == cfg.CHAVE_FORMATO_B_NO_TESTE}
            reaproveitaveis = sum(1 for e in exemplos if e["n"] in cache_teste)
            projetar(exemplos, len(exemplos) - reaproveitaveis)
            return 0
        retomar = args.retomar is not None
        pasta = cfg.CAMINHO_SAIDA / (args.retomar if retomar else
                                     f"{datetime.now().strftime('%Y%m%d-%H%M%S')}_{cfg.MODELO_EMBEDDING}_{cfg.DIMENSOES}")
        cache = preparar_cache(pasta, exemplos, retomar)
        print(f"pasta de saida: {pasta}\nembeddings reaproveitados do teste/cache: {len(cache)} de {len(exemplos)}")
        projetar(exemplos, len(exemplos) - len(cache))
        tokens_novos = gerar_faltantes(pasta, exemplos, cache)
        tokens_total = sum(r["tokens"] for r in cache.values())
        print(f"tokens novos={tokens_novos} (US$ {tokens_novos / 1e6 * cfg.USD_POR_MILHAO:.6f}); "
              f"tokens nos {len(cache)} vetores={tokens_total} (US$ {tokens_total / 1e6 * cfg.USD_POR_MILHAO:.6f})")
        ndjson = pasta / "exemplos.ndjson"
        with ndjson.open("w", encoding="utf-8", newline="\n") as f:
            for e in exemplos:
                f.write(json.dumps(montar_registro(e, cache[e["n"]]), ensure_ascii=False) + "\n")
        print(f"gravado {ndjson}")
        bq("query", "--nouse_legacy_sql", DDL)
        print(f"tabela {TABELA_BQ}: CREATE TABLE IF NOT EXISTS executado")
        antes = consulta(f"SELECT COUNT(*) AS n FROM `{TABELA_BQ}`").splitlines()[1]
        if antes != "0":
            raise ErroCarga(f"trava: a tabela {TABELA_BQ} ja tem {antes} linhas (esperado 0). Nada foi carregado.")
        print("trava: COUNT(*) antes da carga = 0")
        print(bq("load", "--source_format=NEWLINE_DELIMITED_JSON", "--noautodetect", TABELA_BQ_CLI, str(ndjson)).strip()[-200:])
        return 0 if validar(exemplos) else 1
    except ErroCarga as e:
        print(f"PAROU: {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
