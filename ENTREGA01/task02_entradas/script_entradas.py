"""Gera descricoes de negocio em linguagem natural a partir de arquivos .gobr."""
import hashlib
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import config

CAMPOS_METADADOS = (
    "regra_id", "arquivo_regra", "hash_regra_sha256", "arquivo_prompt",
    "hash_prompt_sha256", "modelo", "fornecedor", "temperatura",
    "tokens_entrada", "tokens_saida", "custo_usd", "tempo_segundos", "timestamp",
)


def carregar_env() -> None:
    """Carrega o .env para os.environ sem sobrescrever variaveis ja definidas."""
    if not config.CAMINHO_ENV.exists():
        return
    for linha in config.CAMINHO_ENV.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#") or "=" not in linha:
            continue
        chave, valor = linha.split("=", 1)
        os.environ.setdefault(chave.strip(), valor.strip().strip("\"'"))


def validar_config() -> None:
    """Falha antes de qualquer chamada paga se a configuracao estiver invalida."""
    arq = "ENTREGA01/task02_entradas/config.py"
    for nome in config.MODELOS_ATIVOS:
        if nome not in config.MODELOS:
            raise ValueError(
                f"Modelo ativo {nome!r} fora da lista. Aceitos: {sorted(config.MODELOS)}. "
                f"Configure MODELOS_ATIVOS em {arq}."
            )
    if not config.TETO_GASTO_USD or config.TETO_GASTO_USD <= 0:
        raise ValueError(
            f"TETO_GASTO_USD recebido: {config.TETO_GASTO_USD!r}. Aceita numero maior que zero, "
            f"em dolares. Configure em {arq}."
        )
    if config.QUANTIDADE_REGRAS < 1:
        raise ValueError(
            f"QUANTIDADE_REGRAS recebido: {config.QUANTIDADE_REGRAS!r}. Aceita inteiro >= 1. "
            f"Configure em {arq}."
        )
    if config.PASTA_RETOMADA:
        if not Path(config.PASTA_RETOMADA).is_dir():
            raise ValueError(
                f"PASTA_RETOMADA recebido: {config.PASTA_RETOMADA!r}. Aceita pasta de saida ja existente "
                f"ou vazio. Configure em {arq}."
            )
        if len(config.MODELOS_ATIVOS) != 1:
            raise ValueError(
                f"PASTA_RETOMADA exige um unico modelo em MODELOS_ATIVOS; recebido {config.MODELOS_ATIVOS}. "
                f"Configure em {arq}."
            )
    carregar_env()
    for nome in config.MODELOS_ATIVOS:
        forn = config.MODELOS[nome]["fornecedor"]
        var = config.VARIAVEL_CHAVE[forn]
        if not os.environ.get(var, "").strip():
            raise ValueError(
                f"Chave de API ausente ou vazia para {forn!r}. Variavel esperada: {var}. "
                f"Defina em {config.CAMINHO_ENV} (arquivo .env da raiz)."
            )
    if not config.CAMINHO_PROMPT.exists():
        raise ValueError(f"Prompt nao encontrado em {config.CAMINHO_PROMPT}. Configure CAMINHO_PROMPT em {arq}.")


def sha256_bytes(caminho: Path) -> str:
    """Hash sha256 do conteudo em bytes do arquivo (o nome nao entra)."""
    return hashlib.sha256(caminho.read_bytes()).hexdigest()


def id_regra(caminho: Path) -> str:
    """Extrai o identificador numerico do nome regra_NNN.gobr."""
    return re.search(r"(\d+)", caminho.stem).group(1)


def contar_regras(caminho: Path) -> int:
    """Conta os blocos de parametros (as regras de atendimento) do .gobr."""
    texto = caminho.read_text(encoding="utf-8")
    return len(re.findall(r"^parametros ", texto, flags=re.MULTILINE))


def escolher_regras() -> list[tuple[Path, int]]:
    """Escolhe regras espalhadas por numero de blocos: menor, mediana, maior (para 3)."""
    todas = sorted(
        ((a, contar_regras(a)) for a in config.CAMINHO_REGRAS.glob("*.gobr")),
        key=lambda t: (t[1], int(id_regra(t[0]))),
    )
    n = config.QUANTIDADE_REGRAS
    if n == 1:
        indices = [0]
    else:
        indices = [round(i * (len(todas) - 1) / (n - 1)) for i in range(n)]
    return [todas[i] for i in indices]


def custo(modelo: str, tok_in: int, tok_out: int) -> float:
    """Custo em dolares a partir dos tokens informados pela API."""
    m = config.MODELOS[modelo]
    return (tok_in * m["entrada_por_milhao"] + tok_out * m["saida_por_milhao"]) / 1_000_000


def projetar_custo(modelo: str, texto_entrada: str) -> float:
    """Projecao pessimista da proxima chamada: entrada estimada + saida no limite maximo."""
    tok_in = len(texto_entrada) // 2  # estimativa conservadora, so para o teto
    return custo(modelo, tok_in, config.MAX_TOKENS_SAIDA)


def chamar_openai(modelo: str, prompt: str, gobr: str) -> tuple[str, int, int, bool]:
    """Chama a OpenAI e devolve (texto, tokens_entrada, tokens_saida, cortada)."""
    from openai import OpenAI

    cliente = OpenAI(api_key=os.environ[config.VARIAVEL_CHAVE["openai"]])
    r = cliente.chat.completions.create(
        model=modelo,
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": gobr}],
        # modelos da OpenAI desta lista so aceitam a temperatura padrao (1): nao enviar
        max_completion_tokens=config.MAX_TOKENS_SAIDA,
    )
    # finish_reason "length": a resposta parou no limite de tokens e o texto esta incompleto
    cortada = r.choices[0].finish_reason == "length"
    return r.choices[0].message.content or "", r.usage.prompt_tokens, r.usage.completion_tokens, cortada


def chamar_gemini(modelo: str, prompt: str, gobr: str) -> tuple[str, int, int, bool]:
    """Chama o Gemini e devolve (texto, tokens_entrada, tokens_saida incluindo raciocinio, cortada)."""
    from google import genai
    from google.genai import types

    cliente = genai.Client(api_key=os.environ[config.VARIAVEL_CHAVE["gemini"]])
    r = cliente.models.generate_content(
        model=modelo,
        contents=gobr,
        config=types.GenerateContentConfig(
            system_instruction=prompt,
            temperature=config.TEMPERATURA,
            max_output_tokens=config.MAX_TOKENS_SAIDA,
        ),
    )
    u = r.usage_metadata
    saida = (u.candidates_token_count or 0) + (u.thoughts_token_count or 0)
    # finish_reason MAX_TOKENS: a resposta parou no limite de tokens e o texto esta incompleto
    motivo = r.candidates[0].finish_reason if r.candidates else None
    cortada = "MAX_TOKENS" in str(motivo)
    return r.text or "", u.prompt_token_count or 0, saida, cortada


def rotulo_temperatura(modelo: str) -> str:
    """Diz o que aconteceu com a temperatura: valor enviado, imposto pelo modelo ou nao enviado."""
    m = config.MODELOS[modelo]
    if m["fornecedor"] == "gemini":
        return str(config.TEMPERATURA)
    if m.get("temperatura_aceita") == (1.0, 1.0):
        return "1.0 (padrao imposto pelo modelo)"
    return "nao enviada pelo script (a API usa o padrao 1.0; o modelo aceitaria outro valor)"


def montar_metadados(valores: dict) -> str:
    """Monta o bloco de metadados na ordem fixa."""
    linhas = ["---"] + [f"{c}: {valores[c]}" for c in CAMPOS_METADADOS] + ["---"]
    return "\n".join(linhas) + "\n\n"


def main() -> int:
    validar_config()
    prompt_texto = config.CAMINHO_PROMPT.read_text(encoding="utf-8")
    hash_prompt = sha256_bytes(config.CAMINHO_PROMPT)
    regras = escolher_regras()
    carimbo = datetime.now().strftime("%Y%m%d-%H%M%S")
    # retomada: escreve na pasta indicada e pula regra que ja tem ficha gravada la
    retomada = Path(config.PASTA_RETOMADA) if config.PASTA_RETOMADA else None
    puladas = 0
    gasto = 0.0
    erros: list[str] = []
    parou_teto = False
    print("regras escolhidas:", [(a.name, n) for a, n in regras])

    for caminho, _n in regras:
        if parou_teto:
            break
        rid = id_regra(caminho)
        gobr = caminho.read_text(encoding="utf-8")
        hash_regra = sha256_bytes(caminho)
        for modelo in config.MODELOS_ATIVOS:
            if retomada:
                pasta = retomada / f"regra_{rid}"
            else:
                pasta = config.CAMINHO_SAIDA / f"{carimbo}_{modelo}_{config.VERSAO_PROMPT}" / f"regra_{rid}"
            if (pasta / f"entrada_{rid}.md").exists():
                puladas += 1
                print(f"pulada {modelo} regra_{rid}: ficha ja existe em {pasta}")
                continue
            projecao = projetar_custo(modelo, prompt_texto + gobr)
            if gasto + projecao > config.TETO_GASTO_USD:
                print(f"TETO: gasto {gasto:.4f} + projecao {projecao:.4f} > {config.TETO_GASTO_USD} USD. Parando.")
                parou_teto = True
                break
            forn = config.MODELOS[modelo]["fornecedor"]
            chamar = chamar_openai if forn == "openai" else chamar_gemini
            inicio = time.monotonic()
            try:
                texto, tok_in, tok_out, cortada = chamar(modelo, prompt_texto, gobr)
            except Exception as e:  # falha de um modelo nao derruba a rodada
                erros.append(f"{modelo} regra_{rid}: {type(e).__name__}: {str(e)[:300]}")
                print("ERRO", erros[-1])
                continue
            tempo = time.monotonic() - inicio
            c = custo(modelo, tok_in, tok_out)
            gasto += c
            pasta.mkdir(parents=True, exist_ok=True)
            (pasta / caminho.name).write_bytes(caminho.read_bytes())
            meta = montar_metadados({
                "regra_id": rid, "arquivo_regra": caminho.name, "hash_regra_sha256": hash_regra,
                "arquivo_prompt": config.CAMINHO_PROMPT.name, "hash_prompt_sha256": hash_prompt,
                "modelo": modelo, "fornecedor": forn,
                "temperatura": rotulo_temperatura(modelo),
                "tokens_entrada": tok_in, "tokens_saida": tok_out, "custo_usd": f"{c:.6f}",
                "tempo_segundos": f"{tempo:.2f}",
                "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
            })
            aviso = ""
            if cortada:
                aviso = (f"> **AVISO: RESPOSTA CORTADA.** O modelo parou no limite de {config.MAX_TOKENS_SAIDA} "
                         "tokens de saida. O texto abaixo esta incompleto e nao deve ser usado.\n\n")
                erros.append(f"{modelo} regra_{rid}: RESPOSTA CORTADA no limite de {config.MAX_TOKENS_SAIDA} tokens")
                print("CORTADA", erros[-1])
            # grava logo apos a chamada, antes de seguir para a proxima
            (pasta / f"entrada_{rid}.md").write_text(meta + aviso + texto.strip() + "\n", encoding="utf-8", newline="\n")
            print(f"ok {modelo} regra_{rid} in={tok_in} out={tok_out} usd={c:.6f} t={tempo:.1f}s")

    for e in erros:
        print("FALHA", e)
    print(f"gasto_total_usd={gasto:.6f} erros={len(erros)} puladas={puladas} teto_atingido={parou_teto}")
    return 1 if parou_teto else 0


if __name__ == "__main__":
    sys.exit(main())
