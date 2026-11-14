# Resumo de conformidade da base .gobr

Entrada: `ENTREGA01/task02_entradas/regras_originais/`, 193 arquivos.
Falha = categoria `item_obrigatorio_ausente` ou `divergencia_com_manual`. `construcao_nao_documentada` nao e falha do arquivo.

## Arquivos

| Situacao | Arquivos |
|---|---|
| Sem nenhuma falha | 186 |
| Com ao menos uma falha | 7 |
| Total | 193 |

Arquivos sem nenhum achado, de nenhuma categoria: 75.

## Achados por item

| Item | Categoria | Achados | Arquivos |
|---|---|---:|---:|
| `parametros_tem_atendimento` | item_obrigatorio_ausente | 1 | 1 |
| `grafia_documentada` | divergencia_com_manual | 4 | 2 |
| `nomes_parametros_distintos` | divergencia_com_manual | 2 | 2 |
| `aspas_balanceadas` | divergencia_com_manual | 1 | 1 |
| `cabecalho_bem_formado` | divergencia_com_manual | 1 | 1 |
| `caractere_fora_do_lexico` | divergencia_com_manual | 1 | 1 |
| `parenteses_balanceados` | divergencia_com_manual | 1 | 1 |
| `vocabulario_do_manual` | construcao_nao_documentada | 301 | 116 |
| **Total** | | **312** | |

O total (312) e igual ao numero de linhas de dados de `laudo_conformidade.csv`.

## Achados por categoria

| Categoria | Achados |
|---|---:|
| item_obrigatorio_ausente | 1 |
| divergencia_com_manual | 10 |
| construcao_nao_documentada | 301 |

## Arquivos com falha

| Arquivo | Itens que falharam |
|---|---|
| regra_032.gobr | `parametros_tem_atendimento` (l.521), `parenteses_balanceados` (l.523) |
| regra_080.gobr | `cabecalho_bem_formado` (l.11), `nomes_parametros_distintos` (l.29) |
| regra_083.gobr | `nomes_parametros_distintos` (l.21) |
| regra_135.gobr | `grafia_documentada` (l.252), `grafia_documentada` (l.258), `grafia_documentada` (l.264) |
| regra_140.gobr | `caractere_fora_do_lexico` (l.131) |
| regra_221.gobr | `aspas_balanceadas` (l.48) |
| regra_228.gobr | `grafia_documentada` (l.26) |

## Itens verificaveis conferidos e sem nenhum achado

- `version_no_inicio`
- `version_unica`
- `ao_menos_um_time`
- `categoria_final_presente`
- `ordem_das_categorias`
- `categorias_terminais_exclusivas`
- `nomes_de_time_distintos`
- `nomes_carteira_segmentacao_distintos`
- `nomes_alertas_distintos`
- `time_tem_vendedores`
- `carteira_segmentacao_tem_clientes`
- `carteira_uma_segmentacao`
- `referencia_a_nome_definido`
- `parametros_tem_fonte`
- `parametros_ordem_das_etapas`
- `nao_agendar_exclusivo`
- `filtros_temporais_em_ordem`
- `horario_somente_em_alertas`
- `uma_regra_de_horario`
- `alerta_tem_etapas_obrigatorias`
- `alerta_ordem_das_etapas`

## Itens nao verificaveis (na lista, fora da conferencia)

- `configuracao_do_conjunto`: O conjunto tem nome, tipo de execucao, ID da empresa e flag de habilitado, fora do texto da regra.
- `vendedores_cadastrados`: Todo vendedor referenciado esta cadastrado no Govendas.
- `nomes_alertas_distintos_entre_conjuntos`: Nomes de alerta distintos entre conjuntos de regras diferentes da mesma empresa.
- `regra_por_time`: Regras se aplicam a times ou carteiras, nao a vendedor individual.
- `regrapadrao`: Alternativa 'regrapadrao' da gramatica: o manual nao descreve a sintaxe.
- `sintaxe_do_bloco_tags`: Bloco de tags: o manual lista gatilhos e filtros mas nao mostra a sintaxe do bloco.

## Arquivos sem nenhum achado

- regra_003.gobr
- regra_020.gobr
- regra_029.gobr
- regra_037.gobr
- regra_038.gobr
- regra_043.gobr
- regra_045.gobr
- regra_046.gobr
- regra_049.gobr
- regra_057.gobr
- regra_059.gobr
- regra_060.gobr
- regra_065.gobr
- regra_077.gobr
- regra_079.gobr
- regra_085.gobr
- regra_089.gobr
- regra_098.gobr
- regra_102.gobr
- regra_108.gobr
- regra_114.gobr
- regra_115.gobr
- regra_123.gobr
- regra_132.gobr
- regra_133.gobr
- regra_134.gobr
- regra_136.gobr
- regra_137.gobr
- regra_138.gobr
- regra_141.gobr
- regra_142.gobr
- regra_143.gobr
- regra_149.gobr
- regra_150.gobr
- regra_152.gobr
- regra_154.gobr
- regra_155.gobr
- regra_156.gobr
- regra_158.gobr
- regra_159.gobr
- regra_161.gobr
- regra_165.gobr
- regra_168.gobr
- regra_170.gobr
- regra_173.gobr
- regra_178.gobr
- regra_182.gobr
- regra_185.gobr
- regra_187.gobr
- regra_192.gobr
- regra_193.gobr
- regra_194.gobr
- regra_195.gobr
- regra_196.gobr
- regra_197.gobr
- regra_199.gobr
- regra_205.gobr
- regra_211.gobr
- regra_213.gobr
- regra_214.gobr
- regra_215.gobr
- regra_219.gobr
- regra_222.gobr
- regra_223.gobr
- regra_224.gobr
- regra_225.gobr
- regra_227.gobr
- regra_229.gobr
- regra_230.gobr
- regra_238.gobr
- regra_239.gobr
- regra_240.gobr
- regra_241.gobr
- regra_242.gobr
- regra_246.gobr
