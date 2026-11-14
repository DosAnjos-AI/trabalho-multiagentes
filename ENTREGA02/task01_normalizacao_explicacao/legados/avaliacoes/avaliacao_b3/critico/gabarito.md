# Gabarito por tema (escrito antes de abrir qualquer saida)

Base: `entrada_NNN.md` + `regra_NNN.gobr` dos 10 ids, `manual/` atual, `regras_para_normalizador_v1.md` (dicionario).
Marcas: [FATO] = texto e `.gobr` lidos; [HIPOTESE] = juizo meu.
Prefixo de todas as chaves: `03-secoes/` (relativo a `manual/`). Chave aceitavel pode vir com ou sem `#Secao`, desde que o arquivo e a secao existam.

## 1. Dicionario de temas e conjuntos de chaves aceitaveis (passo 2)

Todas as secoes foram conferidas contra os titulos reais do manual atual (`grep '^#'` nos arquivos).

| Codigo | Tema | Chaves aceitaveis (qualquer uma conta) |
|---|---|---|
| TM | Time de vendedores (todos, televendas, campo, por id, habilitados=`ativados`) | `03-01-times.md` |
| CF | Clientes fixos / carteira fixa como fonte | `04-02-selecao-clientes-ruptura.md`; `04-01-carteiras-e-segmentacoes.md` (qualquer secao) |
| SEG | Grupo auxiliar (segmentacao) e/ou cliente em mais de um grupo | `04-01-carteiras-e-segmentacoes.md#Segmentação como fonte`; `...#Exclusiva x livre`; `...#Cenário 3 — carteiras separadas, a ordem importa` |
| CON | Cliente pertence / nao pertence a grupo (contido) | `06-09-segmentacao-contido.md` |
| RUP | Ruptura de um time para outro | `04-02-selecao-clientes-ruptura.md#Opções para ruptura (após a função)` (ou o arquivo inteiro) |
| FF | Frequencia fixa (a cada N dias) | `07-03-frequencia.md#Fixa por período` (ou o arquivo inteiro) |
| FD | Frequencia dinamica (intervalo do historico do cliente) | `07-03-frequencia.md#Dinâmica (baseada em dados existentes)`; `07-01-parametros-estrutura-e-exemplos.md#Frequência e preferência dinâmicas` |
| PF | Preferencia de dia da semana (dias uteis, sabado) | `07-02-preferencia-dia-semana.md`; `07-01-parametros-estrutura-e-exemplos.md#Semanal básico` |
| NA | Nao agendar | `07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)` |
| OR | Ordem de prioridade entre situacoes ("vale a primeira") | `07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros`; `07-01-...#Restrições` |
| CH | Sem coincidir com outra equipe (sem choque) | `07-04-conflito-pivot-rota.md#Evitar choque entre televendas e campo` (ou o arquivo) |
| FIN | Adimplente / inadimplente | `06-03-financeiros.md` |
| CAD | Cadastro: baixada na Receita, filial, bloqueado, pessoa juridica | `06-05-localizacao-classificacao.md` |
| PRO | Nunca comprou / prospect | `06-01-atividade-inatividade.md`; `06-07-curva-abc-ciclo-de-vida.md` |
| UNI | Compra unica | `06-01-atividade-inatividade.md` |
| ATV | Ativo / inativo para o vendedor | `06-01-atividade-inatividade.md` |
| NV | "Sem vendas" / "sem venda em N dias" | `06-01-atividade-inatividade.md`; `06-07-curva-abc-ciclo-de-vida.md` |
| REC | Recencia de compra (ultimos N dias, entre N e M, fora do periodo, neste mes; vendedor ou empresa) | `06-02-recencia-visita-positivacao.md` |
| FH | Filtro de frequencia historica (menor que / entre) | `06-08-frequencia-e-parametros.md` |
| CDR | Cadastrado ha N dias | `06-11-outros-filtros.md` |
| DM | A partir do dia N do mes | `05-01-filtros-temporais-calendario.md#Dia do mês` (ou o arquivo) |

Regras de pontuacao do dicionario:
- `06-12-opcoes-de-tempo.md` (vocabulario de janela de tempo) conta como **justificada** na precisao quando o texto traz janela de tempo, mas **nao** satisfaz sozinha o tema REC na cobertura. [HIPOTESE: 06-12 nao e equivalente de 06-02; teste: ler os dois arquivos.]
- `03-secoes/07-01-...#Fluxo de uma regra`: fora da cobertura e da precisao (instrucao 4.3).
- `02-01-exemplos-e-estrutura-geral.md` e `01-01-visao-geral-e-execucao.md`: nenhum id traz tema que as justifique (nao ha pedido de tipo de execucao nem de esqueleto no texto). Se emitidas, contam como nao justificadas (aplicacao literal da regra); registro a contagem a parte para sensibilidade. [HIPOTESE: sao chaves transversais.]
- Um mesmo arquivo pode cobrir varios temas (ex.: `06-01` cobre PRO, UNI, ATV, NV; `06-05` cobre CAD). Uma chave a cobre todos os temas dela.

**Fora do manual** (lista "Fora do manual" do dicionario):
- `no maximo` / `no minimo` depois de frequencia `do historico`: nao documentado (manual so documenta limite para frequencia fixa). Codigo **FORA-LIM**.
- `do historico mais N dias`: o manual traz `do vendedor mais N dias`, nao `do historico mais N`. Tratado dentro de FORA-LIM.
- `sem venda` / `sem vendas` isolados (sintaxe) sao fora do manual, mas o **tema** de negocio (cliente sem compras) e coberto por `06-01` (`sem venda ou prospects`) em linguagem natural. Por isso NV e tema explicito com chaves, e NAO tema fora do manual. [HIPOTESE: se uma versao emitir `sem_chave` para "sem vendas" nao conta acerto em FORA; teste: o `.gobr` de 148 usa `sem venda` isolado.]

## 2. Gabarito por id

### 037 [FATO]
Texto: "Todos os vendedores atendem seus clientes fixos a cada 30 dias, de preferencia em dias uteis."
- Explicitos: TM ("Todos os vendedores"), CF ("clientes fixos"), FF ("a cada 30 dias"), PF ("dias uteis").
- Implicitos (so o .gobr): time "empresa toda"; carteira propria sobre `carteirafixa("empresa toda")`; estrutura `da carteira(...)`.
- Fora do manual: nenhum.

### 057 [FATO]
Texto: televendas habilitados; nunca compraram com a empresa a cada 30; ativos para o proprio vendedor a cada 25, "em dia ou inadimplentes"; demais a cada 30.
- Explicitos: TM ("televendas habilitados"), PRO ("nunca compraram com a empresa"), ATV ("ativos para o proprio vendedor"), FF, OR ("primeiro ... Entre os demais").
- Ambiguo [HIPOTESE]: "estejam em dia ou inadimplentes" menciona situacao financeira, mas o `.gobr` nao filtra por ela (regra vale para ambos). Nao e tema explicito; emissao de FIN conta como nao justificada, anotada como ambigua. Teste: o `.gobr` nao tem `adimplentes` nem `inadimplentes`.
- Implicitos: ciclo de vida prospect "com a empresa"; regra final sem `quando` (fallback).
- Fora do manual: nenhum.

### 148 [FATO]
Texto: televendas habilitados; nao agendar inadimplentes; semanal para ativos para o vendedor; 14 dias inativos para o vendedor; 14 dias "clientes sem vendas"; vale a primeira.
- Explicitos: TM, NA, FIN, ATV (ativos e inativos para o vendedor), FF (semanal e 14 dias), NV ("sem vendas"), OR.
- Implicitos: sintaxe `sem venda` isolada no `.gobr` (fora do manual como sintaxe); `quinzenal()` no lugar de "14 dias".
- Fora do manual: nenhum (ver nota NV).

### 116 [FATO]
Texto: todos televendas e todos de campo; nao agendar filiais; televendas 7 dias, dias uteis e sabado, sem coincidir com o campo; campo por ativos/inativos para o vendedor x adimplentes/inadimplentes (7, 14, 30, 60); sem vendas 7.
- Explicitos: TM (televendas e campo), CAD (filiais), NA, FF, PF (dias uteis e sabado), CH ("sem coincidir com a equipe de campo"), ATV, FIN, NV, OR ("Primeiro ... Para os demais").
- Implicitos: `do time("televendas","campo")` com dois times numa regra.
- Fora do manual: nenhum.

### 208 [FATO]
Texto: televendas habilitados; nao agendar baixada, inadimplentes, bloqueados, filiais; prospect do vendedor 7; compra unica 14; comprou neste mes e freq historica entre 90 e 120 -> 14; ultimos 30 -> 14; 89 -> 7; 120 -> 3; vale a primeira; demais nao agendados.
- Explicitos: TM, NA, CAD (baixada, bloqueados, filiais), FIN, PRO ("ainda nao comprou com o proprio vendedor"), UNI ("unica compra"), REC ("neste mes", "ultimos 30/89/120 dias"), FH ("frequencia historica entre 90 e 120 dias"), FF, OR.
- Implicitos: `recencia de positivacao no mes`; regra final "Nao mapeados" com `nao agendar`.
- Discrepancia registrada: texto diz "quem comprou nos ultimos 120 dias" e o `.gobr` usa `recencia ... em 120 dias` (coerente); sem divergencia penalizavel.
- Fora do manual: nenhum.

### 243 [FATO]
Texto: televendas habilitados; PJ nunca compraram com o proprio vendedor 21; compraram ultimos 20 dias 3; ultima compra entre 20 e 33 dias: "intervalo do historico do cliente acrescido de 2 dias, minimo 20 e maximo 33"; preferir dias uteis e sabado; demais PJ e outros nao agendados.
- Explicitos: TM, CAD ("pessoas juridicas"), PRO, REC, FD ("intervalo do historico do cliente"), PF, FF, NA, OR ("ordem de prioridade").
- Fora do manual: FORA-LIM ("acrescido de 2 dias, respeitando o minimo de 20 e o maximo de 33") -> resposta correta `sem_chave`.
- Implicitos: `frequencia do historico mais 2 dias ou no minimo ... e no maximo ...` (sintaxe); regras de `nao agendar` finais.

### 128 [FATO]
Texto: vendedor 291 atende os clientes fixos dos externos 283 e 279 (seis pares); mesmo cliente em mais de um grupo; nao agendar baixada na Receita primeiro; por grupo: nunca comprou 7; comprou ultimos 60 dias 5, a partir do dia 16; ultimos 90 dias 7; demais 7; depois clientes que nao receberam tratamento e nao pertencem a nenhum dos seis grupos; sobra nao agendada.
- Explicitos: TM (vendedores por id, externos por id), CF ("clientes fixos"), SEG ("um mesmo cliente pode aparecer em mais de um desses grupos"), CON ("que nao pertencam a nenhum dos seis grupos"), CAD (baixada), NA, PRO, REC (60, 90 dias), DM ("a partir do dia 16"), FF, OR.
- Implicitos: seis segmentacoes de carteira fixa dos externos; `recencia de positivacao global`; `contido na segmentacao` repetido.
- Discrepancia registrada [FATO]: o rotulo "A partir do dia 20" no `.gobr` diverge do `a partir do dia 16` do texto e do codigo; o texto sustenta 16. Nao penalizada.
- Fora do manual: nenhum.

### 158 [FATO]
Texto: televendas; nao agendar inadimplentes e baixada; nunca comprou com a empresa 30; compra unica + ultimos 45 dias + cadastrado ha 120 dias -> 21; ultimos 45 dias e frequencia historica menor que 30 -> 14; ultimos 120 e freq historica menor que 120 -> 30; ultima compra entre 45 e 70 -> 30; entre 71 e 120 -> 21; nao comprou nos ultimos 120 -> 30; vale a primeira.
- Explicitos: TM, FIN, CAD (baixada), NA, PRO, UNI, REC (45, 120, entre 45 e 70, entre 71 e 120, fora de 120), CDR ("cadastrado ha 120 dias"), FH ("intervalo historico entre compras menor que 30/120"), FF, OR.
- Implicitos: `fora da recencia de positivacao global` para "nao comprou nos ultimos 120".
- Fora do manual: nenhum.

### 169 [FATO]
Texto: vendedor 341 e duas equipes de televendas; clientes adimplentes que passam do 341 para a equipe 1 por ruptura de compra em 7 dias, alem de prospects; outro grupo: fixos da equipe 1 adimplentes sem venda em 7 dias; quem ja esta no primeiro nao entra no segundo; prioridade 14 dias para nunca comprou / 30, 60, 90 dias / entre 90 e 180; depois nao agendar quem comprou nos ultimos 7 dias e inadimplentes; entre os sem tratamento, nao agendar a equipe 1, a equipe 2 a cada 14.
- Explicitos: TM (por id, duas equipes e fornecedor), RUP ("passam do vendedor 341 para ela por ruptura de compra em 7 dias"), CF ("clientes fixos dessa equipe"), SEG ("separamos ... em outro grupo"), CON ("quem ja esta no primeiro grupo nao entra no segundo"), FIN ("em dia com os pagamentos", "inadimplentes"), PRO ("prospects", "nunca compraram"), NV ("nao tiveram venda em 7 dias"), REC (30/60/90, entre 90 e 180, ultimos 7 dias), NA, FF, OR ("prioridade", "Depois disso", "Entre os que ainda nao receberam tratamento").
- Implicitos: carteira "televendas consumidor" com `quando`; `da segmentacao ... e da carteira ...`; `quando adimplentes` dentro da segmentacao; sintaxe `ou prospects`.
- Discrepancia registrada [FATO]: rotulos do `.gobr` ("compra entre 7d e 30d") vs `recencia ... em 30 dias`; texto sustenta "ultimos 30 dias". Nao penalizada.
- Fora do manual: nenhum.

### 191 [FATO]
Texto: televendas habilitados; nao agendar baixada e inadimplentes; nunca comprou 21; vendedor ultimos 7 dias 21; ultimos 30 dias: intervalo habitual entre as compras + 3 dias, minimo 14 e maximo 30; 45 dias 7; 60 dias 7; demais 7; vale a primeira.
- Explicitos: TM, CAD (baixada), FIN, NA, PRO, REC (7, 30, 45, 60), FD ("intervalo habitual entre suas compras"), FF, OR.
- Fora do manual: FORA-LIM ("acrescido de 3 dias, respeitando o minimo de 14 e o maximo de 30") -> `sem_chave`.
- Implicitos: `frequencia do historico mais 3 dias ou no minimo ... e no maximo ...`; regra final sem `quando`.

## 3. Resumo de contagem de temas explicitos (denominador da cobertura)
037: 4 | 057: 5 | 148: 7 | 116: 10 | 208: 10 | 243: 9 | 128: 11 | 158: 11 | 169: 12 | 191: 9. Fora do manual: 243 e 191 (1 tema cada).
Total explicito: 88 temas; fora do manual: 2.

## 4. Temas que aparecem em 2+ ids (usados na consistencia)
TM(10), FF(10), OR(9: todos menos 037), NA(8), PRO(7), REC(6), FIN(6), CAD(6), PF(3: 037, 116, 243), ATV(3), NV(3), CF(3), UNI(2), FH(2), FD(2), FORA-LIM(2), SEG(2), CON(2).
(Contagens exatas conferidas por script no passo 7; este bloco e orientativo.)
