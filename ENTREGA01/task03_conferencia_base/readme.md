# Tarefa 03 — Conferência da base `.gobr` contra o manual

Confere os 193 arquivos `.gobr` deduplicados contra a lista fechada de itens obrigatórios
extraída do manual original (`govendas-rules.pdf`), e grava o laudo de conformidade e o
inventário das construções que o manual não documenta.

Esta tarefa **só confere e relata**. Nenhum arquivo `.gobr` é criado, alterado ou apagado.
A correção é decisão do Mestre.

A conferência vive em `src/conferidor_gobr/`; este script só lê a pasta, chama
`conferir()` e grava os resultados.

## Como rodar

A partir da raiz do projeto:

```
.venv/bin/python ENTREGA01/task03_conferencia_base/script_conferencia.py
```

Etapas (em `config.ETAPAS`, validadas antes de qualquer leitura):

1. `calibracao` — três casos conhecidos; se algum falha, o script aborta sem gravar nada:
   - `regra_032.gobr` tem de acusar `parenteses_balanceados` e `parametros_tem_atendimento`;
   - `regra_228.gobr` tem de acusar `curva c` como `grafia_documentada` / `divergencia_com_manual`;
   - zero achados de `version_no_inicio` e `version_unica` nos 193 arquivos.
2. `conferencia` — grava laudo, resumo e inventário. Exige `calibracao`.
3. `cenarios` — grava três textos `.txt` de teste e imprime o laudo de cada um.

## O que entra

`ENTREGA01/task02_entradas/regras_originais/*.gobr`. Contagem diferente de 193 aborta.

## O que sai (`dados_saida/`)

| Arquivo | Conteúdo |
|---|---|
| `laudo_conformidade.csv` | Uma linha por achado: arquivo, item, categoria, linha, mensagem, construcao (só na categoria 3) |
| `resumo_conformidade.md` | Arquivos sem falha e com falha, contagem por item e por categoria, arquivos sem achado |
| `inventario_nao_documentado.csv` | Uma linha por construção: construção, quantidade de arquivos, ocorrências, arquivos |
| `inventario_nao_documentado.md` | Construções da mais usada para a menos usada, com exemplo real |
| `cenario_*.txt` | Textos de teste do cenário não previsto (extensão `.txt` de propósito) |

Saída reproduzível: duas execuções seguidas produzem os mesmos bytes (sem data no conteúdo).

Coerência conferida pelo script: soma do resumo = linhas do laudo; ocorrências do
inventário = achados `construcao_nao_documentada` do laudo. A soma das quantidades de
arquivos por construção é menor que as ocorrências porque um arquivo repete a mesma
construção em vários blocos.

## Lacunas declaradas

- As lacunas do instrumento estão em `src/conferidor_gobr/readme.md`.
- Itens não verificáveis da lista não entram na conferência (ver o resumo).
- A base não tem alerta, tag nem `limpar parametros`; os itens de alerta foram testados só
  com exemplos do manual e mutações, não com a base.
