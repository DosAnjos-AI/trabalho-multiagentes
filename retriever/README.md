# Retriever — como rodar

## O que o script faz

Lê um pedido em `ENTRADA/` e devolve a lista de exemplos de `simulacao/` e de
arquivos do `manual/` que iriam ao gerador. **Ele para na lista: não escreve `.gobr`.**

## Antes de rodar

- Ambiente virtual do projeto em `.venv/` (o mesmo da indexação; nada novo a instalar).
- Arquivo `.env` na raiz com a variável `CHAVE_OPENAI` preenchida. O valor nunca
  aparece na saída nem no rastro.
- O banco em `indexacao/dados/chroma/` precisa existir. O script só o lê, por cópia temporária.

## Como rodar

Da raiz do repositório:

```
.venv/bin/python retriever/rodar.py
```

Parâmetros opcionais:

| Parâmetro | Efeito |
|---|---|
| `--top-n N` | Quantos exemplos buscar antes do dedup. Padrão: 10 |
| `--rerank` | Liga o reranking por cross-encoder. Desligado por padrão |

O modo antigo continua valendo: `.venv/bin/python retriever/recuperar.py <arquivo> [--top-n N] [--rerank]`.

## O que colocar em `ENTRADA/`

**Exatamente um** arquivo com o pedido. `.gitkeep` e `LEIAME.txt` não contam.

| Tipo | Extensões |
|---|---|
| Texto | `.txt`, `.md` |
| Imagem | `.png`, `.jpg`, `.jpeg`, `.webp` |

**Áudio não é suportado nesta versão** (não há transcrição). Transcreva o pedido para `.txt`.

Depois de rodar, tire o arquivo de `ENTRADA/` antes do próximo pedido.

## O que sai, e onde

| Onde | O que é | Para que serve |
|---|---|---|
| `SAIDA/<timestamp UTC>_<arquivo>.txt` | O mesmo relatório que aparece no terminal | Ler o resultado depois, sem rodar de novo |
| `retriever/saidas/<timestamp>_ENTRADA.json` | Rastro completo: texto do pedido, normalizado, tempos, custo, candidatos | Auditar ou depurar a execução |

As duas pastas estão no `.gitignore`: guardam o texto completo dos pedidos. Um
relatório nunca é sobrescrito; no mesmo segundo, o segundo ganha sufixo `_2`.

## Como ler a saída

| Termo | Significado |
|---|---|
| similaridade | `1 - distância`. Quanto mais perto de 1, mais parecido com o pedido |
| distância | Distância de cosseno do Chroma entre o pedido e o exemplo. Menor é melhor |
| pool | Documentos que passaram no pré-filtro léxico (termos do dicionário). Vazio cai para todos os 249 |
| dedup | Exemplos com `## Regras` idêntico a um já listado são removidos; fica o de melhor pontuação |
| rerank | Nota do cross-encoder (só com `--rerank`). Maior é melhor; `antes->depois` mostra a mudança de posição |

## Quanto demora e quanto custa

- p50 de ~9,5 s por execução, quase tudo na normalização (chamada à API). A busca leva ~1,6 ms.
- Na casa de US$ 0,003 por execução (`gpt-4.1-mini`). Pedidos longos e imagens custam um pouco mais.
- O normalizador pode devolver resultados diferentes para o mesmo pedido, mesmo com temperatura 0.

## O que fazer quando falha

| Mensagem começa com | O que fazer |
|---|---|
| `ENTRADA/ está vazia` | Coloque o arquivo do pedido em `ENTRADA/` |
| `ENTRADA/ tem N arquivos` | Deixe só um; os nomes encontrados vêm listados |
| `extensão ... não aceita` ou `áudio ... não é suportado` | Converta para um dos formatos aceitos |
| `API de normalização falhou` ou `CHAVE_OPENAI ausente` | Confira `.env`, a chave e a conexão; a resposta da API vem na mensagem |
| `o normalizado não converte` | O modelo saiu do formato. Rode de novo; o texto recebido está no rastro JSON (`normalizacao.texto_bruto`) |

## O que o script não faz

- Não gera `.gobr` nem monta o prompt do gerador.
- Não reindexa e não escreve no banco.
- Não aceita áudio.
