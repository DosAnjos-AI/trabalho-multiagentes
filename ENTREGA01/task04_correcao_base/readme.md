# Tarefa 04 — Validação do conferidor e correção da base `.gobr`

1. Valida o conferidor (`src/conferidor_gobr/`) contra 10 arquivos aprovados pelo laudo,
   conferidos manualmente item por item.
2. Validado, copia a base para uma pasta nova e corrige ali as 11 falhas do laudo da
   tarefa 03, registrando cada mudança.

A base original, `ENTREGA01/task02_entradas/regras_originais/`, é **somente leitura**: é a
referência para rever as inferências.

## Como rodar

A partir da raiz do projeto:

```
.venv/bin/python -B ENTREGA01/task04_correcao_base/script_correcao.py
```

Etapas em `config.ETAPAS`:

- `amostra`: sorteia 10 arquivos entre os aprovados, com semente fixa (`SEMENTE_AMOSTRA = 20261113`).
- `correcao`: só roda com `VALIDACAO_APROVADA = True`, valor que só se troca depois que a
  conferência manual (`dados_saida/amostra_validacao.md`) termina sem divergência. A etapa
  copia a base por bytes e confere o sha256 dos 193 arquivos. Depois aplica a tabela
  `CORRECOES`, conferindo o texto original de cada linha antes de trocar, grava o registro e
  confere a base corrigida.

O script para (`SystemExit`) se:
- a cópia não bater por sha256;
- uma linha não for a esperada;
- aparecer falha nova;
- sobrar falha que não seja `nao_inferivel`;
- os achados de construção não documentada mudarem.

A execução é reproduzível: duas rodadas produzem os mesmos bytes.

## O que entra

- `ENTREGA01/task02_entradas/regras_originais/*.gobr` (193 arquivos)
- o conferidor de `src/conferidor_gobr/`, sem nenhuma alteração

## O que sai (`dados_saida/`)

| Arquivo | Conteúdo |
|---|---|
| `amostra_validacao.md` | Conferência manual dos 10 arquivos, 29 itens cada, comparada com o laudo |
| `base_corrigida/` | Os 193 `.gobr`; só 7 diferem da base original |
| `correcoes.csv` | Uma linha por correção: arquivo, linha, item_obrigatorio, tipo, texto_original, texto_novo, motivo |
| `correcoes.md` | O mesmo registro agrupado por tipo, para revisão |
| `laudo_pos_correcao.csv` | O conferidor rodado sobre `base_corrigida/` |

`tipo` aceita só `deterministica`, `inferencia` e `nao_inferivel`.

## Lacunas declaradas

- **Cinco correções são inferência sem gabarito.** A base não pode ser testada no goVendas.
  Cada inferência saiu do próprio arquivo ou de arquivos do mesmo modelo, e o motivo está em
  `correcoes.md`, mas nenhuma é certeza. A revisão é do Mestre, uma por uma.
- **`regra_080.gobr` continua com nomes de parâmetros repetidos** (`nao_inferivel`). O
  segundo bloco "15 dias para inativos" é cópia exata do primeiro, e nada indica qual regra
  se pretendia ali.
- A coluna `linha` usa a numeração da base original. Na `regra_032` a inserção desloca em +1
  as linhas seguintes da base corrigida.
- A validação cobriu 10 de 186 arquivos aprovados e só pode revelar falso negativo nessa
  amostra. Os itens de alerta e horário não se aplicavam a nenhum dos 10.
- A correção de caixa (`curva A/B/C`) segue o manual. Não há teste no goVendas que diga se o
  interpretador real distingue a caixa.
