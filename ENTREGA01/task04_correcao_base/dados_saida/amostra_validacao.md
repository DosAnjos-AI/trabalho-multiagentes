# Amostra de validacao do conferidor

Conferencia manual (leitura do Executor, sem executar o script) de 10 arquivos sorteados entre os 186 que o
laudo da tarefa 03 aprovou sem falha. Semente `20261113` (`config.SEMENTE_AMOSTRA`).
Depois da leitura, cada resultado foi comparado com `ENTREGA01/task03_conferencia_base/dados_saida/laudo_conformidade.csv`.

`nao cumpre` em `vocabulario_do_manual` e categoria `construcao_nao_documentada`: nao e falha do arquivo.

## Resultado

| Arquivo | Falhas pela leitura | Falhas no laudo | Nao documentadas pela leitura | No laudo | Divergencia |
|---|---:|---:|---:|---:|---|
| regra_008.gobr | 0 | 0 | 1 | 1 | nao |
| regra_020.gobr | 0 | 0 | 0 | 0 | nao |
| regra_050.gobr | 0 | 0 | 1 | 1 | nao |
| regra_059.gobr | 0 | 0 | 0 | 0 | nao |
| regra_070.gobr | 0 | 0 | 2 | 2 | nao |
| regra_086.gobr | 0 | 0 | 1 | 1 | nao |
| regra_151.gobr | 0 | 0 | 2 | 2 | nao |
| regra_175.gobr | 0 | 0 | 1 | 1 | nao |
| regra_189.gobr | 0 | 0 | 3 | 3 | nao |
| regra_223.gobr | 0 | 0 | 0 | 0 | nao |

Divergencias: 0 em 10 arquivos (290 conferencias). As linhas das construcoes nao documentadas tambem coincidem com o laudo.

## regra_008.gobr

| # | Item | Leitura | Nota |
|---:|---|---|---|
| 1 | `version_no_inicio` | cumpre | linha 1 vazia; primeira significativa e version 1.0 (l.2) |
| 2 | `version_unica` | cumpre |  |
| 3 | `ao_menos_um_time` | cumpre |  |
| 4 | `categoria_final_presente` | cumpre |  |
| 5 | `ordem_das_categorias` | cumpre |  |
| 6 | `categorias_terminais_exclusivas` | cumpre |  |
| 7 | `cabecalho_bem_formado` | cumpre |  |
| 8 | `aspas_balanceadas` | cumpre |  |
| 9 | `parenteses_balanceados` | cumpre |  |
| 10 | `caractere_fora_do_lexico` | cumpre |  |
| 11 | `nomes_de_time_distintos` | cumpre | 'time interior', 'time capital' |
| 12 | `nomes_carteira_segmentacao_distintos` | cumpre | 'carteira capital', 'carteira interior' |
| 13 | `nomes_parametros_distintos` | cumpre | 4 nomes, todos diferentes |
| 14 | `nomes_alertas_distintos` | nao se aplica | sem alerta |
| 15 | `time_tem_vendedores` | cumpre |  |
| 16 | `carteira_segmentacao_tem_clientes` | cumpre |  |
| 17 | `carteira_uma_segmentacao` | cumpre |  |
| 18 | `referencia_a_nome_definido` | cumpre | carteirafixa e da carteira apontam para nomes definidos |
| 19 | `parametros_tem_fonte` | cumpre |  |
| 20 | `parametros_tem_atendimento` | cumpre |  |
| 21 | `parametros_ordem_das_etapas` | cumpre |  |
| 22 | `nao_agendar_exclusivo` | nao se aplica | sem nao agendar |
| 23 | `filtros_temporais_em_ordem` | nao se aplica | sem filtro temporal |
| 24 | `horario_somente_em_alertas` | nao se aplica | sem filtro de horario |
| 25 | `uma_regra_de_horario` | nao se aplica | sem filtro de horario |
| 26 | `alerta_tem_etapas_obrigatorias` | nao se aplica | sem alerta |
| 27 | `alerta_ordem_das_etapas` | nao se aplica | sem alerta |
| 28 | `grafia_documentada` | cumpre |  |
| 29 | `vocabulario_do_manual` | nao cumpre | l.24 'quando sem venda' (manual so tem 'sem venda ou prospects'); categoria 3, nao e falha |

Divergencia com o laudo: nao. O laudo registra 1 achado(s), todos `construcao_nao_documentada`, nas mesmas linhas da leitura.

## regra_020.gobr

| # | Item | Leitura | Nota |
|---:|---|---|---|
| 1 | `version_no_inicio` | cumpre |  |
| 2 | `version_unica` | cumpre |  |
| 3 | `ao_menos_um_time` | cumpre |  |
| 4 | `categoria_final_presente` | cumpre |  |
| 5 | `ordem_das_categorias` | cumpre |  |
| 6 | `categorias_terminais_exclusivas` | cumpre |  |
| 7 | `cabecalho_bem_formado` | cumpre |  |
| 8 | `aspas_balanceadas` | cumpre |  |
| 9 | `parenteses_balanceados` | cumpre |  |
| 10 | `caractere_fora_do_lexico` | cumpre |  |
| 11 | `nomes_de_time_distintos` | cumpre | um time |
| 12 | `nomes_carteira_segmentacao_distintos` | cumpre | uma carteira; o nome repete o do time, o que o manual nao proibe (p.7 e p.17 comparam so dentro da categoria) |
| 13 | `nomes_parametros_distintos` | cumpre | um bloco |
| 14 | `nomes_alertas_distintos` | nao se aplica | sem alerta |
| 15 | `time_tem_vendedores` | cumpre |  |
| 16 | `carteira_segmentacao_tem_clientes` | cumpre |  |
| 17 | `carteira_uma_segmentacao` | cumpre |  |
| 18 | `referencia_a_nome_definido` | cumpre |  |
| 19 | `parametros_tem_fonte` | cumpre |  |
| 20 | `parametros_tem_atendimento` | cumpre |  |
| 21 | `parametros_ordem_das_etapas` | cumpre |  |
| 22 | `nao_agendar_exclusivo` | nao se aplica | sem nao agendar |
| 23 | `filtros_temporais_em_ordem` | nao se aplica | sem filtro temporal |
| 24 | `horario_somente_em_alertas` | nao se aplica | sem filtro de horario |
| 25 | `uma_regra_de_horario` | nao se aplica | sem filtro de horario |
| 26 | `alerta_tem_etapas_obrigatorias` | nao se aplica | sem alerta |
| 27 | `alerta_ordem_das_etapas` | nao se aplica | sem alerta |
| 28 | `grafia_documentada` | cumpre |  |
| 29 | `vocabulario_do_manual` | cumpre |  |

Divergencia com o laudo: nao. O laudo registra 0 achado(s), todos `construcao_nao_documentada`, nas mesmas linhas da leitura.

## regra_050.gobr

| # | Item | Leitura | Nota |
|---:|---|---|---|
| 1 | `version_no_inicio` | cumpre |  |
| 2 | `version_unica` | cumpre |  |
| 3 | `ao_menos_um_time` | cumpre |  |
| 4 | `categoria_final_presente` | cumpre |  |
| 5 | `ordem_das_categorias` | cumpre |  |
| 6 | `categorias_terminais_exclusivas` | cumpre |  |
| 7 | `cabecalho_bem_formado` | cumpre |  |
| 8 | `aspas_balanceadas` | cumpre |  |
| 9 | `parenteses_balanceados` | cumpre |  |
| 10 | `caractere_fora_do_lexico` | cumpre |  |
| 11 | `nomes_de_time_distintos` | cumpre |  |
| 12 | `nomes_carteira_segmentacao_distintos` | cumpre | uma carteira, mesmo nome do time (permitido) |
| 13 | `nomes_parametros_distintos` | cumpre | 4 nomes diferentes |
| 14 | `nomes_alertas_distintos` | nao se aplica | sem alerta |
| 15 | `time_tem_vendedores` | cumpre |  |
| 16 | `carteira_segmentacao_tem_clientes` | cumpre |  |
| 17 | `carteira_uma_segmentacao` | cumpre |  |
| 18 | `referencia_a_nome_definido` | cumpre |  |
| 19 | `parametros_tem_fonte` | cumpre |  |
| 20 | `parametros_tem_atendimento` | cumpre |  |
| 21 | `parametros_ordem_das_etapas` | cumpre |  |
| 22 | `nao_agendar_exclusivo` | cumpre | l.23 nao agendar sem frequencia nem preferencia no bloco |
| 23 | `filtros_temporais_em_ordem` | nao se aplica | sem filtro temporal |
| 24 | `horario_somente_em_alertas` | nao se aplica | sem filtro de horario |
| 25 | `uma_regra_de_horario` | nao se aplica | sem filtro de horario |
| 26 | `alerta_tem_etapas_obrigatorias` | nao se aplica | sem alerta |
| 27 | `alerta_ordem_das_etapas` | nao se aplica | sem alerta |
| 28 | `grafia_documentada` | cumpre |  |
| 29 | `vocabulario_do_manual` | nao cumpre | l.27 'sem venda'; categoria 3 |

Divergencia com o laudo: nao. O laudo registra 1 achado(s), todos `construcao_nao_documentada`, nas mesmas linhas da leitura.

## regra_059.gobr

| # | Item | Leitura | Nota |
|---:|---|---|---|
| 1 | `version_no_inicio` | cumpre | l.2 e comentario; primeira significativa e version 1.0 (l.3) |
| 2 | `version_unica` | cumpre |  |
| 3 | `ao_menos_um_time` | cumpre |  |
| 4 | `categoria_final_presente` | cumpre | parametros; a gramatica admite times + parametros sem carteira |
| 5 | `ordem_das_categorias` | cumpre |  |
| 6 | `categorias_terminais_exclusivas` | cumpre |  |
| 7 | `cabecalho_bem_formado` | cumpre |  |
| 8 | `aspas_balanceadas` | cumpre |  |
| 9 | `parenteses_balanceados` | cumpre |  |
| 10 | `caractere_fora_do_lexico` | cumpre |  |
| 11 | `nomes_de_time_distintos` | cumpre |  |
| 12 | `nomes_carteira_segmentacao_distintos` | nao se aplica | sem carteira nem segmentacao |
| 13 | `nomes_parametros_distintos` | cumpre | 11 nomes, conferidos um a um, todos diferentes |
| 14 | `nomes_alertas_distintos` | nao se aplica | sem alerta |
| 15 | `time_tem_vendedores` | cumpre |  |
| 16 | `carteira_segmentacao_tem_clientes` | nao se aplica | sem carteira nem segmentacao |
| 17 | `carteira_uma_segmentacao` | nao se aplica | sem carteira |
| 18 | `referencia_a_nome_definido` | cumpre | do time("televendas") definido |
| 19 | `parametros_tem_fonte` | cumpre |  |
| 20 | `parametros_tem_atendimento` | cumpre |  |
| 21 | `parametros_ordem_das_etapas` | cumpre |  |
| 22 | `nao_agendar_exclusivo` | cumpre | l.13 bloco so com nao agendar |
| 23 | `filtros_temporais_em_ordem` | nao se aplica | sem filtro temporal |
| 24 | `horario_somente_em_alertas` | nao se aplica | sem filtro de horario |
| 25 | `uma_regra_de_horario` | nao se aplica | sem filtro de horario |
| 26 | `alerta_tem_etapas_obrigatorias` | nao se aplica | sem alerta |
| 27 | `alerta_ordem_das_etapas` | nao se aplica | sem alerta |
| 28 | `grafia_documentada` | cumpre |  |
| 29 | `vocabulario_do_manual` | cumpre | ramo de atividade igual/diferente, no ciclo de vida prospect com a empresa, ativos para o vendedor: todos no manual |

Divergencia com o laudo: nao. O laudo registra 0 achado(s), todos `construcao_nao_documentada`, nas mesmas linhas da leitura.

## regra_070.gobr

| # | Item | Leitura | Nota |
|---:|---|---|---|
| 1 | `version_no_inicio` | cumpre |  |
| 2 | `version_unica` | cumpre |  |
| 3 | `ao_menos_um_time` | cumpre |  |
| 4 | `categoria_final_presente` | cumpre |  |
| 5 | `ordem_das_categorias` | cumpre |  |
| 6 | `categorias_terminais_exclusivas` | cumpre |  |
| 7 | `cabecalho_bem_formado` | cumpre |  |
| 8 | `aspas_balanceadas` | cumpre |  |
| 9 | `parenteses_balanceados` | cumpre |  |
| 10 | `caractere_fora_do_lexico` | cumpre |  |
| 11 | `nomes_de_time_distintos` | cumpre | 'televendas', 'campo' |
| 12 | `nomes_carteira_segmentacao_distintos` | cumpre |  |
| 13 | `nomes_parametros_distintos` | cumpre | 7 nomes diferentes |
| 14 | `nomes_alertas_distintos` | nao se aplica | sem alerta |
| 15 | `time_tem_vendedores` | cumpre |  |
| 16 | `carteira_segmentacao_tem_clientes` | cumpre |  |
| 17 | `carteira_uma_segmentacao` | cumpre |  |
| 18 | `referencia_a_nome_definido` | cumpre | 'televendas', 'carteira televendas', 'campo' definidos |
| 19 | `parametros_tem_fonte` | cumpre |  |
| 20 | `parametros_tem_atendimento` | cumpre |  |
| 21 | `parametros_ordem_das_etapas` | cumpre |  |
| 22 | `nao_agendar_exclusivo` | cumpre | l.16 e l.52: blocos com nao agendar sem frequencia/preferencia |
| 23 | `filtros_temporais_em_ordem` | nao se aplica | sem filtro temporal |
| 24 | `horario_somente_em_alertas` | nao se aplica | sem filtro de horario |
| 25 | `uma_regra_de_horario` | nao se aplica | sem filtro de horario |
| 26 | `alerta_tem_etapas_obrigatorias` | nao se aplica | sem alerta |
| 27 | `alerta_ordem_das_etapas` | nao se aplica | sem alerta |
| 28 | `grafia_documentada` | cumpre |  |
| 29 | `vocabulario_do_manual` | nao cumpre | l.32 e l.51 'sem venda'; categoria 3 |

Divergencia com o laudo: nao. O laudo registra 2 achado(s), todos `construcao_nao_documentada`, nas mesmas linhas da leitura.

## regra_086.gobr

| # | Item | Leitura | Nota |
|---:|---|---|---|
| 1 | `version_no_inicio` | cumpre |  |
| 2 | `version_unica` | cumpre |  |
| 3 | `ao_menos_um_time` | cumpre |  |
| 4 | `categoria_final_presente` | cumpre |  |
| 5 | `ordem_das_categorias` | cumpre |  |
| 6 | `categorias_terminais_exclusivas` | cumpre |  |
| 7 | `cabecalho_bem_formado` | cumpre |  |
| 8 | `aspas_balanceadas` | cumpre |  |
| 9 | `parenteses_balanceados` | cumpre |  |
| 10 | `caractere_fora_do_lexico` | cumpre |  |
| 11 | `nomes_de_time_distintos` | cumpre |  |
| 12 | `nomes_carteira_segmentacao_distintos` | cumpre |  |
| 13 | `nomes_parametros_distintos` | cumpre | 5 nomes diferentes |
| 14 | `nomes_alertas_distintos` | nao se aplica | sem alerta |
| 15 | `time_tem_vendedores` | cumpre |  |
| 16 | `carteira_segmentacao_tem_clientes` | cumpre |  |
| 17 | `carteira_uma_segmentacao` | cumpre |  |
| 18 | `referencia_a_nome_definido` | cumpre |  |
| 19 | `parametros_tem_fonte` | cumpre |  |
| 20 | `parametros_tem_atendimento` | cumpre |  |
| 21 | `parametros_ordem_das_etapas` | cumpre |  |
| 22 | `nao_agendar_exclusivo` | nao se aplica | sem nao agendar |
| 23 | `filtros_temporais_em_ordem` | nao se aplica | sem filtro temporal |
| 24 | `horario_somente_em_alertas` | nao se aplica | sem filtro de horario |
| 25 | `uma_regra_de_horario` | nao se aplica | sem filtro de horario |
| 26 | `alerta_tem_etapas_obrigatorias` | nao se aplica | sem alerta |
| 27 | `alerta_ordem_das_etapas` | nao se aplica | sem alerta |
| 28 | `grafia_documentada` | cumpre |  |
| 29 | `vocabulario_do_manual` | nao cumpre | l.32 'sem venda'; categoria 3 |

Divergencia com o laudo: nao. O laudo registra 1 achado(s), todos `construcao_nao_documentada`, nas mesmas linhas da leitura.

## regra_151.gobr

| # | Item | Leitura | Nota |
|---:|---|---|---|
| 1 | `version_no_inicio` | cumpre |  |
| 2 | `version_unica` | cumpre |  |
| 3 | `ao_menos_um_time` | cumpre |  |
| 4 | `categoria_final_presente` | cumpre |  |
| 5 | `ordem_das_categorias` | cumpre | time, time, segmentacao, carteira, parametros |
| 6 | `categorias_terminais_exclusivas` | cumpre |  |
| 7 | `cabecalho_bem_formado` | cumpre |  |
| 8 | `aspas_balanceadas` | cumpre |  |
| 9 | `parenteses_balanceados` | cumpre |  |
| 10 | `caractere_fora_do_lexico` | cumpre |  |
| 11 | `nomes_de_time_distintos` | cumpre | 'de campo', 'televendas' |
| 12 | `nomes_carteira_segmentacao_distintos` | cumpre | 'cliente de ruptura', 'televendas fixa com ruptura de campo' |
| 13 | `nomes_parametros_distintos` | cumpre |  |
| 14 | `nomes_alertas_distintos` | nao se aplica | sem alerta |
| 15 | `time_tem_vendedores` | cumpre |  |
| 16 | `carteira_segmentacao_tem_clientes` | cumpre |  |
| 17 | `carteira_uma_segmentacao` | cumpre | carteira usa ruptura de time, nenhuma segmentacao |
| 18 | `referencia_a_nome_definido` | cumpre | 'de campo', 'televendas', a carteira e a segmentacao referida em contido na segmentacao estao definidos |
| 19 | `parametros_tem_fonte` | cumpre |  |
| 20 | `parametros_tem_atendimento` | cumpre |  |
| 21 | `parametros_ordem_das_etapas` | cumpre | fonte (l.22), temporal (l.23), quando (l.24), nao agendar (l.25) |
| 22 | `nao_agendar_exclusivo` | cumpre | bloco so com nao agendar |
| 23 | `filtros_temporais_em_ordem` | cumpre | um unico filtro, 'na ultima semana' (semana do mes) |
| 24 | `horario_somente_em_alertas` | nao se aplica | sem filtro de horario |
| 25 | `uma_regra_de_horario` | nao se aplica | sem filtro de horario |
| 26 | `alerta_tem_etapas_obrigatorias` | nao se aplica | sem alerta |
| 27 | `alerta_ordem_das_etapas` | nao se aplica | sem alerta |
| 28 | `grafia_documentada` | cumpre |  |
| 29 | `vocabulario_do_manual` | nao cumpre | l.15 'tem venda em 60 dias' (manual exige 'do vendedor'/'da empresa'); l.19 'de positivacao(entre 7 dias e 60 dias)' (manual: de positivacao(<<tempo>>)); categoria 3 |

Divergencia com o laudo: nao. O laudo registra 2 achado(s), todos `construcao_nao_documentada`, nas mesmas linhas da leitura.

## regra_175.gobr

| # | Item | Leitura | Nota |
|---:|---|---|---|
| 1 | `version_no_inicio` | cumpre | l.2 comentario; version na l.3 |
| 2 | `version_unica` | cumpre |  |
| 3 | `ao_menos_um_time` | cumpre |  |
| 4 | `categoria_final_presente` | cumpre |  |
| 5 | `ordem_das_categorias` | cumpre |  |
| 6 | `categorias_terminais_exclusivas` | cumpre |  |
| 7 | `cabecalho_bem_formado` | cumpre |  |
| 8 | `aspas_balanceadas` | cumpre |  |
| 9 | `parenteses_balanceados` | cumpre |  |
| 10 | `caractere_fora_do_lexico` | cumpre |  |
| 11 | `nomes_de_time_distintos` | cumpre |  |
| 12 | `nomes_carteira_segmentacao_distintos` | cumpre | uma carteira livre |
| 13 | `nomes_parametros_distintos` | cumpre | 8 nomes diferentes |
| 14 | `nomes_alertas_distintos` | nao se aplica | sem alerta |
| 15 | `time_tem_vendedores` | cumpre |  |
| 16 | `carteira_segmentacao_tem_clientes` | cumpre |  |
| 17 | `carteira_uma_segmentacao` | cumpre |  |
| 18 | `referencia_a_nome_definido` | cumpre | 'activity_in', 'televendas' definidos |
| 19 | `parametros_tem_fonte` | cumpre |  |
| 20 | `parametros_tem_atendimento` | cumpre |  |
| 21 | `parametros_ordem_das_etapas` | cumpre |  |
| 22 | `nao_agendar_exclusivo` | cumpre | 4 blocos com nao agendar, nenhum com frequencia/preferencia |
| 23 | `filtros_temporais_em_ordem` | nao se aplica | sem filtro temporal |
| 24 | `horario_somente_em_alertas` | nao se aplica | sem filtro de horario |
| 25 | `uma_regra_de_horario` | nao se aplica | sem filtro de horario |
| 26 | `alerta_tem_etapas_obrigatorias` | nao se aplica | sem alerta |
| 27 | `alerta_ordem_das_etapas` | nao se aplica | sem alerta |
| 28 | `grafia_documentada` | cumpre |  |
| 29 | `vocabulario_do_manual` | nao cumpre | l.23 'quando e o cliente filial' (manual: 'cliente filial'); demais (no ano anterior, entre datas) documentados; categoria 3 |

Divergencia com o laudo: nao. O laudo registra 1 achado(s), todos `construcao_nao_documentada`, nas mesmas linhas da leitura.

## regra_189.gobr

| # | Item | Leitura | Nota |
|---:|---|---|---|
| 1 | `version_no_inicio` | cumpre | l.2 comentario; version na l.3 |
| 2 | `version_unica` | cumpre |  |
| 3 | `ao_menos_um_time` | cumpre |  |
| 4 | `categoria_final_presente` | cumpre | so parametros |
| 5 | `ordem_das_categorias` | cumpre |  |
| 6 | `categorias_terminais_exclusivas` | cumpre |  |
| 7 | `cabecalho_bem_formado` | cumpre |  |
| 8 | `aspas_balanceadas` | cumpre |  |
| 9 | `parenteses_balanceados` | cumpre |  |
| 10 | `caractere_fora_do_lexico` | cumpre |  |
| 11 | `nomes_de_time_distintos` | cumpre |  |
| 12 | `nomes_carteira_segmentacao_distintos` | nao se aplica | sem carteira nem segmentacao |
| 13 | `nomes_parametros_distintos` | cumpre | 7 nomes diferentes |
| 14 | `nomes_alertas_distintos` | nao se aplica | sem alerta |
| 15 | `time_tem_vendedores` | cumpre |  |
| 16 | `carteira_segmentacao_tem_clientes` | nao se aplica | sem carteira nem segmentacao |
| 17 | `carteira_uma_segmentacao` | nao se aplica | sem carteira |
| 18 | `referencia_a_nome_definido` | cumpre |  |
| 19 | `parametros_tem_fonte` | cumpre |  |
| 20 | `parametros_tem_atendimento` | cumpre |  |
| 21 | `parametros_ordem_das_etapas` | cumpre | fonte, quando, frequencia, preferencia, fixo em todos os blocos |
| 22 | `nao_agendar_exclusivo` | nao se aplica | sem nao agendar |
| 23 | `filtros_temporais_em_ordem` | nao se aplica | sem filtro temporal |
| 24 | `horario_somente_em_alertas` | nao se aplica | sem filtro de horario |
| 25 | `uma_regra_de_horario` | nao se aplica | sem filtro de horario |
| 26 | `alerta_tem_etapas_obrigatorias` | nao se aplica | sem alerta |
| 27 | `alerta_ordem_das_etapas` | nao se aplica | sem alerta |
| 28 | `grafia_documentada` | cumpre | acento em 'não' é livre (p.58); nenhuma caixa divergente |
| 29 | `vocabulario_do_manual` | nao cumpre | l.30 'tem venda da empresa no ano passado'; l.37 'sem venda do vendedor'; l.48 'do historico ou no minimo ... e no maximo ...'; categoria 3 |

Divergencia com o laudo: nao. O laudo registra 3 achado(s), todos `construcao_nao_documentada`, nas mesmas linhas da leitura.

## regra_223.gobr

| # | Item | Leitura | Nota |
|---:|---|---|---|
| 1 | `version_no_inicio` | cumpre | l.2 comentario; version na l.3 |
| 2 | `version_unica` | cumpre |  |
| 3 | `ao_menos_um_time` | cumpre |  |
| 4 | `categoria_final_presente` | cumpre | so parametros |
| 5 | `ordem_das_categorias` | cumpre |  |
| 6 | `categorias_terminais_exclusivas` | cumpre |  |
| 7 | `cabecalho_bem_formado` | cumpre |  |
| 8 | `aspas_balanceadas` | cumpre |  |
| 9 | `parenteses_balanceados` | cumpre |  |
| 10 | `caractere_fora_do_lexico` | cumpre |  |
| 11 | `nomes_de_time_distintos` | cumpre | 'ativacao', 'generalista', 'construtora' |
| 12 | `nomes_carteira_segmentacao_distintos` | nao se aplica | sem carteira nem segmentacao |
| 13 | `nomes_parametros_distintos` | cumpre | 5 nomes diferentes |
| 14 | `nomes_alertas_distintos` | nao se aplica | sem alerta |
| 15 | `time_tem_vendedores` | cumpre |  |
| 16 | `carteira_segmentacao_tem_clientes` | nao se aplica | sem carteira nem segmentacao |
| 17 | `carteira_uma_segmentacao` | nao se aplica | sem carteira |
| 18 | `referencia_a_nome_definido` | cumpre |  |
| 19 | `parametros_tem_fonte` | cumpre |  |
| 20 | `parametros_tem_atendimento` | cumpre |  |
| 21 | `parametros_ordem_das_etapas` | cumpre |  |
| 22 | `nao_agendar_exclusivo` | cumpre | l.32 bloco so com nao agendar |
| 23 | `filtros_temporais_em_ordem` | nao se aplica | sem filtro temporal |
| 24 | `horario_somente_em_alertas` | nao se aplica | sem filtro de horario |
| 25 | `uma_regra_de_horario` | nao se aplica | sem filtro de horario |
| 26 | `alerta_tem_etapas_obrigatorias` | nao se aplica | sem alerta |
| 27 | `alerta_ordem_das_etapas` | nao se aplica | sem alerta |
| 28 | `grafia_documentada` | cumpre |  |
| 29 | `vocabulario_do_manual` | cumpre | recencia de positivacao em 30 dias / na semana: documentados |

Divergencia com o laudo: nao. O laudo registra 0 achado(s), todos `construcao_nao_documentada`, nas mesmas linhas da leitura.
