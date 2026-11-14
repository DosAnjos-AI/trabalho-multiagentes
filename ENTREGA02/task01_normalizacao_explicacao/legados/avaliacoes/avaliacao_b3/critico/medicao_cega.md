# Medicao cega (A/B/C) - escrita antes de abrir o mapa

Tudo em termos de A/B/C. Gabarito e regua congelados (hashes no relatorio). Scripts: `medir.py` (passo 6), `julgar.py` (passo 7). Julgamento mecanico contra `gabarito.md`; partes subjetivas marcadas.

## 1. Passo 6 - saida real de `medir.py`
```
=== A
id  valido sim    faltam  par(e/n) chaves sem_chave nao_resolve fluxo
037 True 1.0 [] 1/1 5 0 [] True
057 True 1.0 [] 1/1 5 0 [] False
148 True 1.0 [] 1/1 6 2 [] True
116 True 0.9956 [] 3/1 9 1 [] True
208 True 0.9963 [] 3/1 9 1 [] True
243 True 0.9952 [] 3/1 11 1 [] True
128 True 1.0 [] 3/3 12 0 [] True
158 True 1.0 [] 4/4 13 0 [] True
169 True 1.0 [] 4/4 11 0 [] True
191 True 0.9964 [] 3/1 9 2 [] True
fluxo emitido: 9 /10
=== B
id  valido sim    faltam  par(e/n) chaves sem_chave nao_resolve fluxo
037 True 1.0 [] 1/1 4 0 [] False
057 True 1.0 [] 1/1 5 0 [] False
148 True 1.0 [] 1/1 6 1 [] False
116 True 1.0 [] 3/3 9 1 [] False
208 True 1.0 [] 3/3 10 0 [] False
243 True 1.0 [] 3/3 11 1 [] False
128 True 1.0 [] 3/3 13 0 [] False
158 True 1.0 [] 4/4 12 0 [] False
169 True 1.0 [] 4/4 10 0 [] False
191 True 1.0 [] 3/3 10 1 [] False
fluxo emitido: 0 /10
=== C
id  valido sim    faltam  par(e/n) chaves sem_chave nao_resolve fluxo
037 True 1.0 [] 1/1 4 0 [] False
057 True 1.0 [] 1/1 5 0 [] False
148 True 1.0 [] 1/1 6 1 [] False
116 True 1.0 [] 3/3 8 1 [] False
208 True 1.0 [] 3/3 9 0 [] False
243 True 1.0 [] 3/3 10 1 [] False
128 True 1.0 [] 3/3 11 0 [] False
158 True 1.0 [] 4/4 11 0 [] False
169 True 1.0 [] 4/4 9 0 [] False
191 True 1.0 [] 3/3 8 2 [] False
fluxo emitido: 0 /10
```
Nenhuma saida invalida (cabecalhos exatos, sem cercas), nenhuma chave que nao resolve, nenhum valor perdido nas tres. Diferenca de palavras entre entrada e `explicacao_normalizada`: zero nas 30 (so espaco/quebra muda). A semelhanca < 1 em A vem de quebras de paragrafo fundidas (3 -> 1 em 116, 208, 243, 191).

## 2. Passo 7 - saida real de `julgar.py`
```
##### BASE
A: cobertura=8.49 precisao=9.24 fora=2/7=2.86 consistencia=9.07
B: cobertura=9.92 precisao=9.55 fora=2/4=5.00 consistencia=9.07
C: cobertura=8.49 precisao=9.04 fora=2/5=4.00 consistencia=9.07
##### SENSIBILIDADE (Cenario 3 aceito para OR)
A: cobertura=9.07 precisao=9.63 fora=2/7=2.86 consistencia=8.83
B: cobertura=9.92 precisao=9.55 fora=2/4=5.00 consistencia=9.01
C: cobertura=9.31 precisao=9.71 fora=2/5=4.00 consistencia=8.95

--- detalhe BASE por id
A 037 cob=1.00 prec=1.00 (4 ch) ac/den=0/0 NAO COBERTOS: [] INJUST: [] SC: []
A 057 cob=0.80 prec=0.60 (5 ch) ac/den=0/0 NAO COBERTOS: ['OR'] INJUST: ['04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa', '06-03-financeiros.md'] SC: []
A 148 cob=0.86 prec=1.00 (5 ch) ac/den=0/2 NAO COBERTOS: ['OR'] INJUST: [] SC: ['sem_chave: clientes sem vendas', 'sem_chave: prioridade entre situações']
A 116 cob=0.90 prec=1.00 (8 ch) ac/den=0/1 NAO COBERTOS: ['OR'] INJUST: [] SC: ['sem_chave: clientes sem vendas']
A 208 cob=0.80 prec=1.00 (8 ch) ac/den=0/1 NAO COBERTOS: ['OR', 'REC'] INJUST: [] SC: ['sem_chave: prioridade entre situações de atendimento']
A 243 cob=0.89 prec=0.90 (10 ch) ac/den=1/1 NAO COBERTOS: ['OR'] INJUST: ['04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa'] SC: ['sem_chave: mínimo e máximo da frequência do histórico']
A 128 cob=0.73 prec=0.91 (11 ch) ac/den=0/0 NAO COBERTOS: ['CON', 'OR', 'REC'] INJUST: ['07-01-parametros-estrutura-e-exemplos.md#Com restrição temporal'] SC: []
A 158 cob=0.91 prec=0.83 (12 ch) ac/den=0/0 NAO COBERTOS: ['OR'] INJUST: ['04-02-selecao-clientes-ruptura.md', '04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa'] SC: []
A 169 cob=0.83 prec=1.00 (10 ch) ac/den=0/0 NAO COBERTOS: ['CON', 'OR'] INJUST: [] SC: []
A 191 cob=0.78 prec=1.00 (8 ch) ac/den=1/2 NAO COBERTOS: ['OR', 'REC'] INJUST: [] SC: ['sem_chave: prioridade entre situações de atendimento', 'sem_chave: limites para frequência histórica']
B 037 cob=1.00 prec=1.00 (4 ch) ac/den=0/0 NAO COBERTOS: [] INJUST: [] SC: []
B 057 cob=1.00 prec=0.80 (5 ch) ac/den=0/0 NAO COBERTOS: [] INJUST: ['06-03-financeiros.md'] SC: []
B 148 cob=1.00 prec=1.00 (6 ch) ac/den=0/1 NAO COBERTOS: [] INJUST: [] SC: ['sem_chave: clientes sem vendas']
B 116 cob=1.00 prec=1.00 (9 ch) ac/den=0/1 NAO COBERTOS: [] INJUST: [] SC: ['sem_chave: clientes sem vendas']
B 208 cob=1.00 prec=1.00 (10 ch) ac/den=0/0 NAO COBERTOS: [] INJUST: [] SC: []
B 243 cob=1.00 prec=0.91 (11 ch) ac/den=1/1 NAO COBERTOS: [] INJUST: ['04-02-selecao-clientes-ruptura.md'] SC: ['sem_chave: mínimo e máximo na frequência do histórico']
B 128 cob=1.00 prec=0.92 (13 ch) ac/den=0/0 NAO COBERTOS: [] INJUST: ['07-01-parametros-estrutura-e-exemplos.md#Com restrição temporal'] SC: []
B 158 cob=1.00 prec=0.92 (12 ch) ac/den=0/0 NAO COBERTOS: [] INJUST: ['04-02-selecao-clientes-ruptura.md'] SC: []
B 169 cob=0.92 prec=1.00 (10 ch) ac/den=0/0 NAO COBERTOS: ['CON'] INJUST: [] SC: []
B 191 cob=1.00 prec=1.00 (10 ch) ac/den=1/1 NAO COBERTOS: [] INJUST: [] SC: ['sem_chave: limites mínimo e máximo da frequência histórica']
C 037 cob=1.00 prec=1.00 (4 ch) ac/den=0/0 NAO COBERTOS: [] INJUST: [] SC: []
C 057 cob=0.80 prec=0.60 (5 ch) ac/den=0/0 NAO COBERTOS: ['OR'] INJUST: ['04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa', '06-03-financeiros.md'] SC: []
C 148 cob=0.86 prec=0.83 (6 ch) ac/den=0/1 NAO COBERTOS: ['OR'] INJUST: ['04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa'] SC: ['sem_chave: clientes sem vendas']
C 116 cob=0.90 prec=1.00 (8 ch) ac/den=0/1 NAO COBERTOS: ['OR'] INJUST: [] SC: ['sem_chave: clientes sem vendas']
C 208 cob=0.80 prec=0.89 (9 ch) ac/den=0/0 NAO COBERTOS: ['OR', 'REC'] INJUST: ['04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa'] SC: []
C 243 cob=0.89 prec=0.90 (10 ch) ac/den=1/1 NAO COBERTOS: ['OR'] INJUST: ['04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa'] SC: ['sem_chave: limites mínimo e máximo da frequência histórica']
C 128 cob=0.73 prec=0.91 (11 ch) ac/den=0/0 NAO COBERTOS: ['CON', 'OR', 'REC'] INJUST: ['07-01-parametros-estrutura-e-exemplos.md#Com restrição temporal'] SC: []
C 158 cob=0.91 prec=0.91 (11 ch) ac/den=0/0 NAO COBERTOS: ['OR'] INJUST: ['04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa'] SC: []
C 169 cob=0.83 prec=1.00 (9 ch) ac/den=0/0 NAO COBERTOS: ['CON', 'OR'] INJUST: [] SC: []
C 191 cob=0.78 prec=1.00 (8 ch) ac/den=1/2 NAO COBERTOS: ['OR', 'REC'] INJUST: [] SC: ['sem_chave: prioridade pela primeira situação', 'sem_chave: limites mínimo e máximo da frequência histórica']

--- consistencia por tema (BASE)
A {'FF': 1.0, 'PF': 1.0, 'CF': 0.33, 'TM': 1.0, 'ATV': 1.0, 'OR': 1.0, 'PRO': 1.0, 'NA': 1.0, 'FIN': 1.0, 'NV': 1.0, 'CAD': 1.0, 'FH': 1.0, 'UNI': 1.0, 'REC': 0.5, 'FD': 1.0, 'FORA-LIM': 1.0, 'SEG': 0.5, 'CON': 1.0}
B {'FF': 1.0, 'PF': 1.0, 'CF': 0.33, 'TM': 1.0, 'ATV': 1.0, 'OR': 1.0, 'PRO': 1.0, 'NA': 1.0, 'FIN': 1.0, 'NV': 1.0, 'CAD': 1.0, 'FH': 1.0, 'UNI': 1.0, 'REC': 1.0, 'FD': 1.0, 'FORA-LIM': 1.0, 'SEG': 0.5, 'CON': 0.5}
C {'FF': 1.0, 'PF': 1.0, 'CF': 0.33, 'TM': 1.0, 'ATV': 1.0, 'OR': 1.0, 'PRO': 1.0, 'NA': 1.0, 'FIN': 1.0, 'NV': 1.0, 'CAD': 1.0, 'FH': 1.0, 'UNI': 1.0, 'REC': 0.5, 'FD': 1.0, 'FORA-LIM': 1.0, 'SEG': 0.5, 'CON': 1.0}
```
Notas BASE usam o gabarito exatamente como congelado. A secao SENSIBILIDADE e so informativa: aceita `04-01#Cenario 3` como chave de ordem (OR); nao substitui a nota.

## 3. Prosa pela regua (nota por arquivo)
| Versao | 037 | 057 | 148 | 116 | 208 | 243 | 128 | 158 | 169 | 191 | media |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10 | 10 | 10 | 8 | 8 | 8 | 10 | 10 | 10 | 8 | 9.2 |
| B | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10.0 |
| C | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10.0 |

Justificativa (A, 116/208/243/191): paragrafos da entrada 3 -> 1 (item 5 = 0; demais itens 2). [FATO: contagem do script, `par(e/n)` = 3/1.] Itens 2, 3 e 4 foram julgados por mim a partir do diff de palavras vazio (nenhuma palavra mudou) e da ausencia de cercas/cabecalhos; julgamento subjetivo apenas na leitura "nada acrescentado".

## 4. Casos que decidem (por versao)
Chaves nao justificadas (frase do texto que sustentaria):
- A, B, C em 057: `06-03-financeiros` - texto "estejam em dia ou inadimplentes"; o `.gobr` nao filtra por situacao financeira. Ambigua [HIPOTESE: se o gabarito aceitasse a mencao como tema, os tres ganham +0,2 em 057].
- A, B, C em 128: `07-01#Com restrição temporal` - sustentaria "a partir do dia 16 de cada mês", mas o tema DM aceita so `05-01#Dia do mês`. Nenhuma frase fala de "so em certos dias de execucao".
- A e C em 057, 243, 158; C em 148 e 208: `04-01#Cenário 3 — carteiras separadas, a ordem importa` usada como chave de ordem de prioridade. Texto: "primeiro ... Entre os demais" (057), "ordem de prioridade" (243), "vale a primeira" (148, 158). Nao justificada pelo gabarito porque o cenario trata ordem entre blocos `carteira`, e estas regras sao so `parametros` (manual 07-01 diz isso explicitamente). B usa `07-01#Ordem entre regras de parâmetros` nesses casos.
- B em 243 e A, B em 158: `04-02-selecao-clientes-ruptura` - frase: nenhuma (nao ha "clientes fixos" nem selecao de carteira nesses textos).
- `sem_chave` sem tema fora do manual: "clientes sem vendas" em 148 e 116 (A, B, C; o gabarito cobre o tema com `06-01`); "prioridade entre situacoes" em A (148, 208, 191) e "prioridade pela primeira situacao" em C (191) - o tema existe no manual (OR), logo `sem_chave` e erro.

Temas explicitos nao cobertos:
- OR: A e C em 057, 148, 116, 208, 243, 128, 158, 169, 191; B cobre todos. (frase: "vale a primeira" e similares.)
- REC: A e C em 208, 128, 191 (emitiram so `06-12-opcoes-de-tempo`, sem `06-02`). Frase: "neste mes / ultimos 30, 89, 120 dias" (208); "nos ultimos 60 dias" (128); "nos ultimos 7 dias" (191). Julgamento subjetivo sobre 06-12 nao ser equivalente de 06-02.
- CON: A e C em 128 e 169; B em 169. Frases: "que nao pertencam a nenhum dos seis grupos" (128), "Quem ja esta no primeiro grupo nao entra no segundo" (169).

Inconsistencias (media por tema, BASE; nota da coluna = media * 10): CF 0,33 nas tres (037 usa `04-02`; 128 e 169 usam combinacoes distintas de 04-01/04-02); SEG 0,50 nas tres; REC 0,50 em A e C; CON 0,50 em B. Os demais temas = 1,0.

## 5. Observacoes cegas
- Fluxo emitido ("Fluxo de uma regra"): ver coluna `fluxo emitido` no passo 6: A 9/10, B 0/10, C 0/10. Excluido de cobertura e precisao.
- [HIPOTESE] Pelo padrao de Fluxo (A 9/10) e de paragrafos fundidos, A parece ser uma versao sem a regra de transversalidade e com menos cuidado de formato; teste: abrir o mapa no passo 8. Nao ajustei notas.
- Ocorrencias de `sem_chave` que correspondem a FORA-LIM: A 243 e 191, B 243 e 191, C 243 e 191 (as tres acertam os dois ids).
