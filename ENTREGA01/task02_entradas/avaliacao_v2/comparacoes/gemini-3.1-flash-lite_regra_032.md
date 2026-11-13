# Comparação: gemini-3.1-flash-lite, regra_032

Critério: `../../avaliacao_v1/CRITERIO_AVALIACAO_v1.md` com as extensões E1-E5 de `../RESULTADO_V2.md`. Original: `regras_originais/regra_032.gobr`. Reconstrução: `reconstrucoes/gemini-3.1-flash-lite/regra_032.gobr`. Números: `comparacoes/_saida_comparar_v2.json`, chave `gemini-3.1-flash-lite|032` (gerado por `comparar_v2.py`).

| Medida | Todos os blocos | Sem `time` |
|---|---|---|
| Regras capturadas | 50/78 | 49/77 |
| Regras inventadas | 0 | 0 |
| Regra inteira correta | 44/78 | 44/77 |
| Inteira correta com caixa estrita também em palavra-chave (leitura auxiliar) | 44/78 | 44/77 |

## Faltaram

- `parametros` "Pré-inativos Curva A (Sul, Sudeste e Centro-Oeste - Matcon, Ferragista, Agropecuária e Home Center)" — quando: `ramo de atividade igual("MATCON","FERRAGISTA","AGROPECUARIA","HOME CENTER") e recencia de positivacao global em 150 dias e media faturada no ano com a empresa maior que r$ 25000` — frequencia de 14 dias
- `parametros` "Pré-inativos Curva B (Sul, Sudeste e Centro-Oeste - Matcon, Ferragista, Agropecuária e Home Center)" — quando: `ramo de atividade igual("MATCON","FERRAGISTA","AGROPECUARIA","HOME CENTER") e recencia de positivacao global em 150 dias e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 14 dias
- `parametros` "Inativos Curva A (Sul, Sudeste e Centro-Oeste - Matcon, Ferragista, Agropecuária e Home Center)" — quando: `ramo de atividade igual("MATCON","FERRAGISTA","AGROPECUARIA","HOME CENTER") e media faturada no ano com a empresa maior que r$ 25000` — frequencia de 14 dias
- `parametros` "Inativos Curva B (Sul, Sudeste e Centro-Oeste - Matcon, Ferragista, Agropecuária e Home Center)" — quando: `ramo de atividade igual("MATCON","FERRAGISTA","AGROPECUARIA","HOME CENTER") e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 14 dias
- `parametros` "Pré-inativos Curva A (Sul, Sudeste e Centro-Oeste - EPI e Licitação)" — quando: `ramo de atividade igual("EPI","LICITACAO") e recencia de positivacao global em 150 dias e media faturada no ano com a empresa maior que r$ 25000` — frequencia de 14 dias
- `parametros` "Pré-inativos Curva B (Sul, Sudeste e Centro-Oeste - EPI e Licitação)" — quando: `ramo de atividade igual("EPI","LICITACAO") e recencia de positivacao global em 150 dias e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 14 dias
- `parametros` "Inativos Curva A (Sul, Sudeste e Centro-Oeste - EPI e Licitação)" — quando: `ramo de atividade igual("EPI","LICITACAO") e media faturada no ano com a empresa maior que r$ 25000` — frequencia de 14 dias
- `parametros` "Inativos Curva B (Sul, Sudeste e Centro-Oeste - EPI e Licitação)" — quando: `ramo de atividade igual("EPI","LICITACAO") e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 14 dias
- `parametros` "Ativos Curva A (Sul, Sudeste e Centro-Oeste - Corporativo/ Consumidor)" — quando: `ramo de atividade igual("CONS. FINAL") e recencia de positivacao global em 120 dias e media faturada no ano com a empresa maior que r$ 15000` — frequencia de 28 dias
- `parametros` "Ativos Curva B (Sul, Sudeste e Centro-Oeste - Corporativo/ Consumidor)" — quando: `ramo de atividade igual("CONS. FINAL") e recencia de positivacao global em 120 dias e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 28 dias
- `parametros` "Pré-inativos Curva A (Sul, Sudeste e Centro-Oeste - Corporativo/ Consumidor)" — quando: `ramo de atividade igual("CONS. FINAL") e recencia de positivacao global em 150 dias e media faturada no ano com a empresa maior que r$ 15000` — frequencia de 14 dias
- `parametros` "Pré-inativos Curva B (Sul, Sudeste e Centro-Oeste - Corporativo/ Consumidor)" — quando: `ramo de atividade igual("CONS. FINAL") e recencia de positivacao global em 150 dias e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 14 dias
- `parametros` "Inativos Curva A (Sul, Sudeste e Centro-Oeste - Corporativo/ Consumidor)" — quando: `ramo de atividade igual("CONS. FINAL") e media faturada no ano com a empresa maior que r$ 15000` — frequencia de 28 dias
- `parametros` "Inativos Curva B (Sul, Sudeste e Centro-Oeste - Corporativo/ Consumidor)" — quando: `ramo de atividade igual("CONS. FINAL") e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 28 dias
- `parametros` "Pré-inativos Curva A (Norte e Nordeste - Matcon, Ferragista, Agropecuária e Home Center)" — quando: `ramo de atividade igual("MATCON","FERRAGISTA","AGROPECUARIA","HOME CENTER") e recencia de positivacao global em 180 dias e media faturada no ano com a empresa maior que r$ 25000` — frequencia de 14 dias
- `parametros` "Pré-inativos Curva B (Norte e Nordeste - Matcon, Ferragista, Agropecuária e Home Center)" — quando: `ramo de atividade igual("MATCON","FERRAGISTA","AGROPECUARIA","HOME CENTER") e recencia de positivacao global em 180 dias e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 14 dias
- `parametros` "Inativos Curva A (Norte e Nordeste - Matcon, Ferragista, Agropecuária e Home Center)" — quando: `ramo de atividade igual("MATCON","FERRAGISTA","AGROPECUARIA","HOME CENTER") e media faturada no ano com a empresa maior que r$ 25000` — frequencia de 14 dias
- `parametros` "Inativos Curva B (Norte e Nordeste - Matcon, Ferragista, Agropecuária e Home Center)" — quando: `ramo de atividade igual("MATCON","FERRAGISTA","AGROPECUARIA","HOME CENTER") e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 14 dias
- `parametros` "Pré-inativos Curva A (Norte e Nordeste - EPI e Licitação)" — quando: `ramo de atividade igual("EPI","LICITACAO") e recencia de positivacao global em 180 dias e media faturada no ano com a empresa maior que r$ 25000` — frequencia de 14 dias
- `parametros` "Pré-inativos Curva B (Norte e Nordeste - EPI e Licitação)" — quando: `ramo de atividade igual("EPI","LICITACAO") e recencia de positivacao global em 180 dias e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 14 dias
- `parametros` "Inativos Curva A (Norte e Nordeste - EPI e Licitação)" — quando: `ramo de atividade igual("EPI","LICITACAO") e media faturada no ano com a empresa maior que r$ 25000` — frequencia de 14 dias
- `parametros` "Inativos Curva B (Norte e Nordeste - EPI e Licitação)" — quando: `ramo de atividade igual("EPI","LICITACAO") e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 14 dias
- `parametros` "Ativos Curva A (Norte e Nordeste - Corporativo/ Consumidor)" — quando: `ramo de atividade igual("CONS. FINAL") e recencia de positivacao global em 150 dias e media faturada no ano com a empresa maior que r$ 15000` — frequencia de 28 dias
- `parametros` "Ativos Curva B (Norte e Nordeste - Corporativo/ Consumidor)" — quando: `ramo de atividade igual("CONS. FINAL") e recencia de positivacao global em 150 dias e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 28 dias
- `parametros` "Pré-inativos Curva A (Norte e Nordeste - Corporativo/ Consumidor)" — quando: `ramo de atividade igual("CONS. FINAL") e recencia de positivacao global em 180 dias e media faturada no ano com a empresa maior que r$ 15000` — frequencia de 14 dias
- `parametros` "Pré-inativos Curva B (Norte e Nordeste - Corporativo/ Consumidor)" — quando: `ramo de atividade igual("CONS. FINAL") e recencia de positivacao global em 180 dias e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 14 dias
- `parametros` "Inativos Curva A (Norte e Nordeste - Corporativo/ Consumidor)" — quando: `ramo de atividade igual("CONS. FINAL") e media faturada no ano com a empresa maior que r$ 15000` — frequencia de 28 dias
- `parametros` "Inativos Curva B (Norte e Nordeste - Corporativo/ Consumidor)" — quando: `ramo de atividade igual("CONS. FINAL") e media faturada no ano com a empresa maior que r$ 10000` — frequencia de 28 dias

## Inventadas

Nenhuma.

## Capturadas mas não inteiras corretas

- `time` "televendas": fonte: `vendedores todostelevendas` ⇄ `vendedores todostelevendas ativados`
- `carteira livre` "sul_sudeste_centrooeste": cat: `carteira` ⇄ `carteira livre`
- `carteira livre` "norte_nordeste": cat: `carteira` ⇄ `carteira livre`
- `parametros` "Prospects": fonte: `C:clientes carteirafixa(T:0)?uf do estado igual("AC","AP","AM","PA","RO","RR","TO","AL","BA","CE","MA","PB","PE","PI","RN","SE")` ⇄ `C:clientes carteirafixa(T:0)?uf do estado igual("PR","SC","RS","SP","RJ","MG","ES","GO","MT","MS","DF")` ⇄ `T:0`
- `parametros` "Pré-inativos Curva C (Sul, Sudeste e Centro-Oeste - Matcon, Ferragista, Agropecuária e Home Center)": quando: `recencia de positivacao em 150 dias` ⇄ `recencia de positivacao global em 150 dias`
- `parametros` "Inativos Curva C (Norte e Nordeste - Corporativo/ Consumidor)": params: `frequencia de 28 dias`

Leitura de `⇄`: diferença simétrica entre o conjunto da reconstrução e o do original (o item que só existe em um dos lados). Em `fonte`, `T:n` é o n-ésimo time do arquivo e `C:...` é a definição da carteira.
