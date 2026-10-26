# Indexação vetorial das regras (formato 4.0)

Converte os 249 `simulacao/regra_NNN/normalizado.md` do formato 3.1 para o 4.0 e indexa a seção
`## Regras` de cada um num Chroma persistente, com payload apontando para o `.gobr` (só a string do
caminho; nenhum `.gobr` é aberto). Também monta um índice léxico a partir dos dicionários.

## Instalação

Python 3.12. Execute da raiz do projeto:

```bash
python3 -m venv .venv
.venv/bin/pip install -r indexacao/requirements.txt
```

O `requirements.txt` fixa `torch` na build CPU (`2.14.1+cpu`); em outra máquina, instale o `torch`
equivalente antes (`--index-url https://download.pytorch.org/whl/cpu`). Na primeira execução de
`02_indexar.py` o modelo `intfloat/multilingual-e5-base` (~1 GB) é baixado do HuggingFace para
`~/.cache/huggingface`, fora do repositório.

## Ordem de execução

| Passo | Script | O que faz |
|---|---|---|
| 1 | `scripts/01_converter.py` | Converte 3.1 -> 4.0, substituindo o arquivo no mesmo caminho. Valida cada resultado (YAML abre, sem âncoras, linhas de `## Regras` = `total_regras`) antes de gravar. Não é reexecutável sobre arquivos já convertidos (falha por `versao_padrao`). |
| 2 | `scripts/02_indexar.py` | Embedda só `## Regras` (prefixo `passage:`), faz `upsert` no Chroma (id `regra_NNN`) e grava `dados/indice_lexico.json`. Idempotente. |
| 3 | `scripts/03_teste_fumaca.py` | Embedda (`query:`) o texto de `## Regras` da `regra_166` e confere que ela volta em 1º. |

```bash
.venv/bin/python indexacao/scripts/01_converter.py
.venv/bin/python indexacao/scripts/02_indexar.py
.venv/bin/python indexacao/scripts/03_teste_fumaca.py
```

## Estrutura

- `config.py`: caminhos, modelo, coleção, dimensão, lote e vocabulário de critérios (único lugar com constantes).
- `conversao/`: `leitor_v31`, `escritor_v40`, `leitor_v40` (usado por validação e indexação).
- `indice/`: `embeddings` (modelo e prefixos), `vetorial` (criar, inserir, upsert, atualizar, remover, consultar), `lexico`.
- `dados/`: `chroma/` (banco persistente, ignorado pelo git) e `indice_lexico.json`.

## Metadados por documento no Chroma

`crit_<tipo>` (12 booleanos: presença em `comuns` ou em qualquer `se`), `total_regras`, `procedencia`,
`gobr_path`, `normalizado_path`. O texto armazenado é exatamente a seção `## Regras`.

## Decisões a conhecer

- Arquivo com uma única regra não tem critério içado para `comuns` (içar deixaria a regra com `se` vazio).
- Documentos com texto de `## Regras` idêntico recebem a mesma distância numa consulta; a ordem entre eles é arbitrária.
