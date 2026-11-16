# task01_normalizacao_explicacao

Normaliza uma explicacao (texto de negocio): limpa o texto sem mudar o conteudo e lista as chaves do
`manual/` que a regra exige. A mesma funcao `normalizar` serve ao corpus (193 explicacoes sinteticas)
e a mensagem de um usuario; so muda quem chama. Estado: 193 de 193 normalizados com a versao ativa (v3).

## Versao ativa

| Item | Valor | SHA-256 |
|---|---|---|
| Prompt | `prompt_normalizador_v3.md` | `ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a` |
| Auxiliar do manual | `regras_para_normalizador_v2.md` | `5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971` |
| Script | `script_normalizacao.py` | `11a7324e300f51851a9b2e6cf3eb9572a60b292f9b211c4931b241a8c2ef9082` |
| Modelo | `gpt-6.1-terra` (temperatura padrao 1, nao enviada) | - |

Esses hashes sao gravados em cada `normalizado_NNN.md` (`hash_prompt`, `hash_auxiliar_manual`, `hash_normalizador`).

## Arquivos ativos

| Arquivo | O que faz |
|---|---|
| `config.py` | Caminhos, modelo e precos, versoes, teto de gasto, validacao |
| `script_normalizacao.py` | Normaliza o lote ou uma funcao `normalizar` avulsa; valida a resposta e grava |
| `verificar_chaves.py` | Confere as chaves do auxiliar contra o `manual/`; o script importa dele a lista de chaves validas |
| `prompt_normalizador_v3.md` | Prompt enviado ao modelo |
| `regras_para_normalizador_v2.md` | Auxiliar do manual enviado inteiro ao modelo |
| `legados/` | Versoes antigas e saida paga de avaliacoes (ver `legados/LEIA-ME.md`) |

## Entrada e saida

- Entrada: `dados/processados/regras_entradas/entrada_NNN.md` (so leitura). O bloco de metadados do topo nao vai
  ao modelo; arquivo sem esse bloco, ou com `---` a mais, e rejeitado com mensagem.
- Saida: `dados/processados/regras_normalizadas/normalizado_NNN.md`, com 17 campos de metadados escritos pelo
  script e as secoes `## explicacao_normalizada` e `## regras_extraidas`.
- Formato de `## regras_extraidas`: o modelo devolve uma chave por linha; o script valida (chave exata do auxiliar)
  e grava um objeto JSON `{"regras_extraidas": [arquivos do manual, sem #Titulo, sem repeticao], "sem_chave": [textos]}`.
  Conversao sem LLM (`converter_regras`). Os 193 normalizados existentes foram convertidos com
  `script_normalizacao.py --converter-existentes` (`--simular` mostra sem gravar; idempotente). Os `hash_normalizador`
  gravados neles sao do script anterior a conversao.
- Resposta invalida: nao grava o `normalizado_*.md`; a resposta crua vai para `rejeitados/` (nesta pasta, criada so se houver rejeicao).

## Uso (da raiz do projeto)

```
.venv/bin/python -B ENTREGA02/task01_normalizacao_explicacao/script_normalizacao.py --estimar                       # sem chamada paga
.venv/bin/python -B ENTREGA02/task01_normalizacao_explicacao/script_normalizacao.py --estimar --ids 037,057          # estimativa so desses ids
.venv/bin/python -B -u ENTREGA02/task01_normalizacao_explicacao/script_normalizacao.py --executar --ids 003,007,008  # lote PAGO, so esses ids
.venv/bin/python -B ENTREGA02/task01_normalizacao_explicacao/script_normalizacao.py --executar                      # lote PAGO, todos os ids sem normalizado
.venv/bin/python -B ENTREGA02/task01_normalizacao_explicacao/verificar_chaves.py                                    # auxiliar x manual
```

O lote de fechamento rodou `--executar --ids` com a lista dos 176 ids sem normalizado (menos os 7 pendentes).
Sem `--ids`, o lote pega todo id com `entrada_NNN.md` e sem `normalizado_NNN.md`, inclusive os pendentes.

## Teto de gasto e chave

- `TETO_GASTO_USD` no `config.py` esta em `0.20`. Nao ha valor padrao para lote: quem roda um novo lote deve
  definir o teto depois de ver o `--estimar`. O script para antes de estourar o teto.
- A chave `CHAVE_OPENAI` fica no `.env` da raiz (ignorado pelo git). O script a le e nunca a imprime.
- Arquivo `normalizado_NNN.md` existente e pulado: isso e a retomada. Nunca se sobrescreve. Para refazer um id,
  mova o arquivo antigo para fora da pasta antes.

## O que valida

- Config antes de qualquer leitura ou chamada (valor recebido, aceitos e arquivo onde configurar).
- Resposta: cabecalhos exatos e unicos, nada antes ou depois, chaves existentes no auxiliar (comparacao exata),
  sem repeticao, `sem_chave:` com descricao, resposta nao cortada.
- Projecao de custo antes de cada chamada; para antes de estourar o teto.
- Fim do lote: sucessos, pulados e rejeitados; codigo de saida diferente de zero se houve rejeitado.

## Como regenerar uma explicacao e normaliza-la depois

1. Regenere a `entrada_NNN.md` (task02, ver `ENTREGA01/task02_entradas/readme.md`) e coloque em `regras_entradas/`.
2. Se ja existir `normalizado_NNN.md` desse id, mova-o para fora de `regras_normalizadas/`.
3. Defina o teto no `config.py`, rode `--estimar --ids NNN` e depois `--executar --ids NNN`.

## O que `legados/` guarda e por que

Saida paga nunca se apaga: os 10 normalizados do v1 (`saida_v1/`) e os das avaliacoes (v2, v3) ficam la, junto
com prompts antigos, auxiliar v1 e o registro da avaliacao que escolheu o v3. Detalhe em `legados/LEIA-ME.md`.
