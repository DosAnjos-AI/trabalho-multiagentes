# task02_entradas

Esta tarefa transforma cada regra `.gobr` em uma ficha em linguagem natural.
A ficha é o texto que uma pessoa do negócio escreveria para pedir aquela regra.
A ficha precisa soar natural.
A ficha também precisa ser completa o bastante para alguém reconstruir a regra a partir dela.

O script chama um modelo de linguagem (OpenAI ou Gemini) uma vez por regra.
Cada chamada custa dinheiro real.

## Decisão: modelo e prompt

| Item | Escolha |
|---|---|
| Modelo | `gpt-6.1-terra` |
| Prompt | `prompt_v2.md` |
| Segunda opção | `gpt-6-luna` com o mesmo `prompt_v2.md`, só se o `gpt-6.1-terra` falhar de forma que impeça a execução |

O Mestre escolheu o `gpt-6.1-terra` porque o modelo escreveu o texto mais natural dos 12 testados, sem nenhum vazamento de sintaxe ou de nomes do arquivo.
O modelo reconstruiu 80 de 88 blocos inteiros corretos, a 6 blocos do primeiro colocado, por cerca de US$ 0,02 pelas três regras de teste.

O lote oficial das 193 fichas está em `dados/processados/regras_entradas/`.
As outras pastas de `regras_explicadas/` são das rodadas de validação.

## Como a avaliação foi feita

1. Três regras serviram de teste: a menor (`regra_020`, 3 blocos), a mediana (`regra_228`, 7 blocos) e a maior (`regra_032`, 78 blocos). As três somam 88 blocos.
2. Cada um dos 12 modelos gerou uma ficha para cada regra de teste com o `prompt_v2.md`.
3. Um reconstrutor leu cada ficha sozinha e escreveu de volta um `.gobr`. O reconstrutor não olhou o arquivo original. Essa é a reconstrução às cegas.
4. O reconstrutor gravou o hash das 36 reconstruções antes de abrir qualquer original. O hash prova que nenhuma reconstrução mudou depois da comparação.
5. Um script comparou cada reconstrução com o original, bloco a bloco.
6. O avaliador também ordenou as fichas pela naturalidade do texto, sem olhar os números.

Os detalhes estão em `avaliacao_v2/RESULTADO_V2.md`. A rodada anterior, com o `prompt_v1`, está em `avaliacao_v1/`.

## Tabela de decisão

Nesta tabela, "regra" quer dizer um bloco do arquivo `.gobr`. O rodapé abaixo da tabela explica a contagem.

| Modelo | Fornecedor | Faixa | Preço US$/milhão (entrada / saída) | Regras recuperadas, de 88 | Regras perfeitas com o prompt v1, de 88 | Regras perfeitas com o prompt v2, de 88 | Nota de linguagem humana (posição, 1 = melhor) | Nota de ausência de jargão técnico (ocorrências, 0 = melhor) | Nota de economia (custo das 3 fichas, US$) |
|---|---|---|---|---|---|---|---|---|---|
| gpt-6-luna | openai | barato | 0,10 / 0,50 | 88 | 12 | **86** | 4 | 1 | 0,003957 |
| gemini-3.8-flash | gemini | intermediário | 0,75 / 3,75 | 88 | não testado | 84 | 5 | 5 | 0,047937 |
| gpt-4.1-mini-2025-04-14 | openai | barato | 0,40 / 1,60 | 88 | não testado | 83 | 10 | 27 | 0,008993 |
| gemini-4-carbon | gemini | melhor | 2,00 / 10,00 | 88 | não testado | 82 | 2 | 0 | 0,164602 |
| gpt-6-astra | openai | melhor | 10,00 / 50,00 | 88 | não testado | 82 | 3 | 0 | 0,227620 |
| **gpt-6.1-terra** | openai | intermediário | 1,00 / 5,00 | 88 | 12 | 80 | **1** | 0 | 0,019702 |
| gemini-3.5-flash-lite | gemini | barato | 0,30 / 2,50 | 88 | 9 | 79 | 7 | 16 | 0,008967 |
| gemini-3.6-flash | gemini | intermediário | 0,75 / 3,75 | 88 | 82 | 60 | 6 | 6 | 0,071592 |
| gpt-5-mini-2025-08-07 | openai | barato | 0,25 / 2,00 | 88 | não testado | 56 | 12 | 48 | 0,026686 |
| gemini-3.1-flash-lite | gemini | barato | 0,25 / 1,50 | 60 | não testado | 50 | 8 | 15 | 0,005210 |
| gpt-5.4-mini-2026-03-17 | openai | intermediário | 0,75 / 4,50 | 88 | não testado | 37 | 11 | 37 | 0,017293 |
| gpt-4o-mini-2024-07-18 | openai | barato | 0,15 / 0,60 | 19 | não testado | 13 | 9 | 8 | 0,002559 |

### Rodapé da tabela

**Os números são somatório.** Todos os números de regras da tabela são o somatório das 3 regras analisadas. Os números não são a média. Os números também não são o resultado de uma regra só.

**Blocos de cada arquivo de regra:**

| Arquivo da regra | Blocos no arquivo | Papel no teste |
|---|---|---|
| `regra_020.gobr` | 3 | Regra pequena |
| `regra_228.gobr` | 7 | Regra média |
| `regra_032.gobr` | 78 | Regra grande, a maior do corpus |
| Total | 88 | É este 88 que aparece como denominador na tabela |

**Dois critérios de contagem.** A escolha das 3 regras de teste contou só os blocos chamados `parametros`. Por esse critério, os arquivos têm 1, 6 e 75 blocos. A avaliação contou todos os blocos: `time`, `carteira` e `parametros`. Por esse critério, os arquivos têm 3, 7 e 78 blocos. Os dois números estão certos, cada um no seu critério. O denominador 88 vem do segundo critério.

**Significado de cada campo:**

- **Modelo**: o campo mostra o identificador exato que o script enviou à API.
- **Fornecedor**: o campo mostra a empresa dona do modelo.
- **Faixa**: o campo mostra a posição do modelo na tabela de preços do próprio fornecedor. "Barato" é o piso de custo. "Intermediário" é o modelo de trabalho. "Melhor" é o teto de qualidade. Os modelos mini e o `gemini-3.8-flash` receberam a faixa mais próxima do preço deles.
- **Preço US$/milhão**: o campo mostra quanto o fornecedor cobra por 1 milhão de tokens de entrada e por 1 milhão de tokens de saída, em dólares. A consulta foi feita em 2026-11-13.
- **Regras recuperadas, de 88**: o campo conta quantos dos 88 blocos do original apareceram na reconstrução, mesmo com algum detalhe errado. O valor 88 significa que a ficha não esqueceu nenhum bloco.
- **Regras perfeitas com o prompt v1, de 88**: o campo conta quantos blocos a reconstrução acertou por inteiro com o `prompt_v1`. Acertar por inteiro exige fonte, filtros, frequência e parâmetros iguais ao original. Só quatro modelos rodaram com o `prompt_v1`. Os outros aparecem como "não testado".
- **Regras perfeitas com o prompt v2, de 88**: o campo conta a mesma coisa com o `prompt_v2`, que é o prompt atual. Este campo é a medida principal de fidelidade da ficha.
- **Nota de linguagem humana**: o campo mostra a posição do modelo, de 1 a 12, na leitura subjetiva da naturalidade do texto. A posição 1 é o texto que mais parece escrito por uma pessoa do negócio.
- **Nota de ausência de jargão técnico**: o campo conta quantas vezes a ficha copiou sintaxe do GOBR ou nomes internos do arquivo, como nomes de carteira. O valor 0 é o ideal.
- **Nota de economia**: o campo mostra o valor em dólares pago pelas três chamadas. O script calculou o valor a partir dos tokens que a API informou.

**Limite de uma nota geral.** Esta tabela não tem nota geral ponderada. A avaliação não definiu pesos. Os pesos de uma nota geral seriam escolha de quem monta a tabela, e não medição. Mudando os pesos, muda o primeiro lugar. Uma nota geral também não distingue perder um bloco inteiro de errar um detalhe do bloco. Por isso, um modelo com valor baixo em "Regras recuperadas" deve ser lido por aquela coluna, e não por uma nota.

**Medida fora da tabela.** A medida "inventadas" conta blocos que a reconstrução criou sem existirem no original. A medida não aparece na tabela porque não separa os modelos. Onze modelos tiveram 1 bloco inventado, e um modelo teve 0. O bloco inventado é erro do avaliador (ver ressalva 3).

## Ressalvas

1. **O `prompt_v2` favorece a si mesmo.** O autor do `prompt_v2` escreveu o prompt já conhecendo as três regras de teste. Por isso a comparação entre v1 e v2 favorece o v2. A vantagem do v2 pode não se repetir em regras novas.
2. **Uma ficha por regra.** Cada modelo gerou uma única ficha por regra. A avaliação não mediu a variância. Uma segunda ficha do mesmo modelo pode dar outro número.
3. **Dois erros do avaliador afetaram números específicos.**
   - O avaliador leu "os inativos desses ramos" como um filtro de inativos. Essa leitura tirou 24 blocos do `gemini-3.6-flash` e 24 do `gpt-5-mini` na `regra_032`. Com a outra leitura, os dois teriam 84 e 80.
   - O avaliador separou em dois o bloco de prospects da `regra_032`, que no original é um bloco só. Esse erro criou 1 bloco inventado em 11 modelos e impediu que qualquer modelo acertasse esse bloco por inteiro. O erro vale igual para todos e não muda a ordem.
   - Os dois erros estão registrados em `avaliacao_v2/RESULTADO_V2.md`, seção "Escolhas do reconstrutor que mudam o número".

## Como rodar

O interpretador é o `.venv/bin/python` da raiz do projeto.
O `python3` do sistema não serve, porque os SDKs `openai` e `google-genai` só estão instalados no `.venv`.

    cd ENTREGA01/task02_entradas
    ../../.venv/bin/python -u script_entradas.py

A opção `-u` faz o progresso aparecer no terminal a cada regra, inclusive quando a saída vai para um arquivo de log.

As chaves de API ficam no `.env` da raiz, que o git não versiona: `CHAVE_OPENAI` e `CHAVE_GEMINI`.
O script nunca imprime nem grava as chaves.

**A pasta de saída nunca é apagada.** Cada ficha custou dinheiro. Cada execução cria uma pasta nova com timestamp, a menos que `PASTA_RETOMADA` esteja preenchida.

### Entrada e saída

- Entrada: `dados/processados/regras_gobr/`, com os 193 `.gobr` deduplicados da task01, e o prompt de `CAMINHO_PROMPT`.
- Saída: `regras_explicadas/{timestamp}_{modelo}_{versao_prompt}/regra_{id}/`.
- Cada pasta de regra tem a ficha `entrada_{id}.md` e a cópia byte a byte `regra_{id}.gobr`.
- `prompt_legados/` guarda os prompts antigos, para comparação.

### O que o script faz

1. O script valida o `config.py` e as chaves antes de qualquer chamada paga.
2. Para cada regra, o script projeta o custo da próxima chamada no pior caso. Se o gasto somado à projeção passar de `TETO_GASTO_USD`, o script para.
3. O script envia o prompt como instrução e o `.gobr` como mensagem.
4. O script grava a ficha logo depois da chamada. Uma queda no meio não perde as fichas já pagas.
5. Se a chamada falhar, o script registra o erro e segue para a próxima regra.
6. Se a resposta for cortada no limite de tokens, o script grava a ficha com um aviso "RESPOSTA CORTADA" logo abaixo do bloco de metadados, registra a regra na lista de falhas e segue.
7. No fim, o script lista todas as falhas e imprime o gasto total.

### Chaves do `config.py`

| Chave | O que controla | Efeito de mudar |
|---|---|---|
| `CAMINHO_ENV` | Local do `.env` com as chaves | Outro arquivo de chaves |
| `VARIAVEL_CHAVE` | Nome da variável de chave de cada fornecedor | O script procura outra variável no `.env` |
| `CAMINHO_REGRAS` | Pasta dos `.gobr` de entrada | Outra entrada |
| `CAMINHO_SAIDA` | Pasta raiz das fichas | As pastas novas vão para outro lugar |
| `CAMINHO_PROMPT` | Arquivo de prompt | Outro prompt. As fichas registram o nome e o hash do prompt usado |
| `MODELOS` | Catálogo: fornecedor, faixa, preço e temperatura aceita | Preço errado gera custo e teto errados. Reconferir o preço antes de lote grande |
| `MODELOS_ATIVOS` | Quais modelos rodam | Cada modelo a mais multiplica as chamadas e o custo. Nome fora de `MODELOS` aborta antes de qualquer chamada |
| `TEMPERATURA` | Temperatura enviada ao Gemini | Não afeta a OpenAI. O script nunca envia temperatura para a OpenAI |
| `TETO_GASTO_USD` | Teto de gasto por execução, em dólares | Teto baixo para o lote antes do fim. Zero ou negativo aborta |
| `MAX_TOKENS_SAIDA` | Limite de tokens de saída por chamada | Valor baixo corta fichas longas. O valor também entra na projeção de custo |
| `VERSAO_PROMPT` | Rótulo da versão do prompt | Muda só o nome da pasta de saída |
| `QUANTIDADE_REGRAS` | Quantas regras rodam | 193 roda todas. Um número menor escolhe regras espalhadas por tamanho. 3 escolhe a menor, a mediana e a maior |
| `PASTA_RETOMADA` | Pasta de saída já existente, para retomar | Vazia: o script cria pasta nova. Preenchida: o script escreve nessa pasta e pula toda regra que já tem `entrada_{id}.md`. Exige um único modelo em `MODELOS_ATIVOS` |

### Retomar depois de uma queda

1. Copie o caminho da pasta criada, por exemplo `regras_explicadas/20261113-192952_gpt-6.1-terra_v2`.
2. Preencha `PASTA_RETOMADA` com esse caminho no `config.py`.
3. Rode o script de novo. O script pula as regras prontas e completa o resto.
4. Esvazie `PASTA_RETOMADA` depois. Assim a próxima execução não escreve na pasta antiga.

Uma ficha cortada também conta como pronta na retomada. Para refazer uma ficha cortada, mova a ficha para fora da pasta antes de retomar.

### Bloco de metadados de `entrada_{id}.md`

O bloco fica entre `---`, nesta ordem: `regra_id`, `arquivo_regra`, `hash_regra_sha256`, `arquivo_prompt`, `hash_prompt_sha256`, `modelo`, `fornecedor`, `temperatura`, `tokens_entrada`, `tokens_saida`, `custo_usd`, `tempo_segundos`, `timestamp`.

- Os hashes são sha256 do conteúdo em bytes. O nome do arquivo não entra no hash.
- `temperatura` registra o que aconteceu. "1.0 (padrao imposto pelo modelo)" vale para modelos que só aceitam 1. "nao enviada pelo script" vale para modelos da OpenAI que aceitariam outro valor. Nos modelos Gemini, o campo mostra o valor enviado.
- `custo_usd` vem dos tokens informados pela API. Nos modelos Gemini, os tokens de raciocínio contam como saída.
- `timestamp` usa o formato ISO-8601 com fuso.
- O texto da ficha vem depois do bloco.
