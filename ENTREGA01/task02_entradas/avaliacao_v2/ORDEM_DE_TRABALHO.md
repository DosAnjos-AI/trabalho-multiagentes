# Ordem de trabalho da validação v2 (reconstrução cega)

Gravado em 2026-11-13, **antes** de ler qualquer `entrada_{id}.md` e antes de abrir qualquer `.gobr` de teste.
Material lido até aqui: `avaliacao_v1/CRITERIO_AVALIACAO_v1.md`, `MAPA_VALIDACAO_V2.md`, `manual/` (todos os arquivos), texto de `govendas-rules.pdf` (busca de maiúsculas e regras léxicas, p.57-58), os 3 pares de `exemplos/`.

## Sequência das regras

1. `regra_020` (12 descrições)
2. `regra_228` (12 descrições)
3. `regra_032` (12 descrições)

## Ordem dos modelos em cada regra

Ordem-base embaralhada com `random.seed(2026)` sobre a lista do mapa (para não agrupar por fornecedor). `regra_228` = base rotacionada em 4; `regra_032` = base rotacionada em 8. Cada modelo cai uma vez no terço inicial (1-4), uma no meio (5-8) e uma no final (9-12).

| Posição | regra_020 | regra_228 | regra_032 |
|---|---|---|---|
| 1 | gpt-6-luna | gemini-3.8-flash | gemini-3.6-flash |
| 2 | gpt-5.4-mini-2026-03-17 | gpt-4o-mini-2024-07-18 | gemini-3.5-flash-lite |
| 3 | gpt-6-astra | gemini-3.1-flash-lite | gpt-5-mini-2025-08-07 |
| 4 | gpt-4.1-mini-2025-04-14 | gemini-4-carbon | gpt-6.1-terra |
| 5 | gemini-3.8-flash | gemini-3.6-flash | gpt-6-luna |
| 6 | gpt-4o-mini-2024-07-18 | gemini-3.5-flash-lite | gpt-5.4-mini-2026-03-17 |
| 7 | gemini-3.1-flash-lite | gpt-5-mini-2025-08-07 | gpt-6-astra |
| 8 | gemini-4-carbon | gpt-6.1-terra | gpt-4.1-mini-2025-04-14 |
| 9 | gemini-3.6-flash | gpt-6-luna | gemini-3.8-flash |
| 10 | gemini-3.5-flash-lite | gpt-5.4-mini-2026-03-17 | gpt-4o-mini-2024-07-18 |
| 11 | gpt-5-mini-2025-08-07 | gpt-6-astra | gemini-3.1-flash-lite |
| 12 | gpt-6.1-terra | gpt-4.1-mini-2025-04-14 | gemini-4-carbon |

## Decisão sobre maiúsculas (tomada antes de ver qualquer resultado)

**Pergunta:** a linguagem GOBR diferencia maiúsculas de minúsculas em palavras-chave?

**Resposta do manual:** não declara. Fontes:
- `govendas-rules.pdf` p.58, "Regras lexicais importantes": fala de comentários, acentos, strings, nomes de variáveis e diz que **tags** usam "apenas letras minúsculas e números". Nada sobre palavras-chave.
- `manual/03-secoes/10-gramatica.md` e `manual/02-invariantes.md`: idem; a única regra de caixa é a das tags.
- Busca por "maiúscul", "minúscul", "case", "sensitiv", "caixa" no texto do PDF: só a frase das tags (linha 3095 do `pdftotext -layout`).
- Todos os exemplos do manual e de `exemplos/` escrevem palavras-chave em minúsculas; maiúsculas só aparecem em texto entre aspas (nome livre).

**Decisão de contagem:** diferença só de maiúscula/minúscula em palavra-chave **não conta** como diferença (mesmo tratamento que o critério v1 dá a acento em palavra-chave). Texto entre aspas já é livre pelo critério v1. Exceção: nome de tag `@...` com maiúscula seria inválido pelo manual (p.58) e conta. Isto é **extensão declarada** do critério v1 (o v1 não trata caixa). Se algum par só ficar "inteiro correto" por causa desta decisão, isso será registrado no arquivo de comparação.
