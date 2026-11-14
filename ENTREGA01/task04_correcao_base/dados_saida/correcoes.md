# Registro de correcoes da base .gobr

Base original (somente leitura): `ENTREGA01/task02_entradas/regras_originais/`.
Base corrigida: `ENTREGA01/task04_correcao_base/dados_saida/base_corrigida/`.
Linha = numero na base original (na insercao, a linha que o texto novo ocupa).

| Tipo | Correcoes |
|---|---:|
| deterministica | 5 |
| inferencia | 5 |
| nao_inferivel | 1 |

## Correcoes deterministicas

### regra_140.gobr, linha 131 — `caractere_fora_do_lexico`

Antes:

```
    quando recencia de positivacao do vendedor em 21 dias\x01
```

Depois:

```
    quando recencia de positivacao do vendedor em 21 dias
```

Motivo: Remove o caractere de controle U+0001 no fim da linha; o lexico do manual (p.58) nao o admite.

### regra_135.gobr, linha 253 — `grafia_documentada`

Antes:

```
           e curva a com a empresa
```

Depois:

```
           e curva A com a empresa
```

Motivo: Manual escreve 'curva A com a empresa' (p.28); so a caixa muda.

### regra_135.gobr, linha 259 — `grafia_documentada`

Antes:

```
           e curva b com a empresa
```

Depois:

```
           e curva B com a empresa
```

Motivo: Manual escreve 'curva B com a empresa' (p.28); so a caixa muda.

### regra_135.gobr, linha 265 — `grafia_documentada`

Antes:

```
           e curva c com a empresa
```

Depois:

```
           e curva C com a empresa
```

Motivo: Manual escreve 'curva C com a empresa' (p.28); so a caixa muda.

### regra_228.gobr, linha 27 — `grafia_documentada`

Antes:

```
        e curva c com a empresa
```

Depois:

```
        e curva C com a empresa
```

Motivo: Manual escreve 'curva C com a empresa' (p.28); so a caixa muda.

## Correcoes por inferencia (revisar uma por uma)

### regra_032.gobr, linha 523 — `parenteses_balanceados`

Antes:

```
    quando ramo de atividade igual("CONS. FINAL"
```

Depois:

```
    quando ramo de atividade igual("CONS. FINAL")
```

Motivo: Fecha o parentese. As outras 17 linhas do segmento Corporativo/Consumidor no arquivo (l.229 a 281 e 471 a 517) sao 'quando ramo de atividade igual("CONS. FINAL")'; nao ha outro filtro em nenhum bloco 'Inativos Curva C' do arquivo (l.99-104, 159, 219, 279, 341, 401, 461).

### regra_032.gobr, linha 524 — `parametros_tem_atendimento`

Antes:

```
(linha inexistente: insercao)
```

Depois:

```
    frequencia de 28 dias
```

Motivo: Insere a frequencia apos a l.523. Nos 8 segmentos do arquivo, o bloco 'Inativos Curva C' de Norte/Nordeste repete a frequencia do mesmo segmento em Sul/Sudeste (14, 14, 21 nos tres primeiros); o de Corporativo/Consumidor Sul (l.279-282) usa 28 dias, e os Inativos Curva A e B de Norte Corporativo (l.509, 515) tambem usam 28 dias.

### regra_221.gobr, linha 48 — `aspas_balanceadas`

Antes:

```
        preferencia nos dias uteis e no sabado"
```

Depois:

```
        preferencia nos dias uteis e no sabado
```

Motivo: Remove a aspa solta. As outras 5 linhas de preferencia do arquivo sao exatamente 'preferencia nos dias uteis e no sabado', sem aspa; nada na linha abre string.

### regra_080.gobr, linha 11 — `cabecalho_bem_formado`

Antes:

```
parametros "Regra Padrao da Empresa Customizavel: mensal para inativos com cnae do erp que inicia com ("03","47","27")":
```

Depois:

```
parametros "Regra Padrao da Empresa Customizavel: mensal para inativos com cnae do erp que inicia com ('03','47','27')":
```

Motivo: Troca as aspas duplas internas por simples. O nome copia o filtro da l.13; a base usa aspa simples para citar dentro de nome (ex.: regra_132, 162 e 187, "Não agendar 'Inadimplentes'"). Texto do rotulo preservado.

### regra_083.gobr, linha 21 — `nomes_parametros_distintos`

Antes:

```
parametros "Regra Padrao do goVendas Customizavel - Frequencia de inativos":
```

Depois:

```
parametros "Regra Padrao do goVendas Customizavel - Frequencia de clientes sem vendas":
```

Motivo: Renomeia o segundo bloco. O corpo e 'quando sem venda' (nao 'inativos'); a regra_072 tem o mesmo modelo, com os mesmos 3 blocos e corpos na mesma ordem, e la o terceiro se chama 'Frequencia de clientes sem vendas'. Mantido o separador ' - ' da propria 083.

## Casos nao inferiveis (arquivo mantido)

### regra_080.gobr, linha 29 — `nomes_parametros_distintos`

Antes:

```
parametros "Regra Padrao da Empresa Customizavel: 15 dias para inativos":
```

Depois:

```
parametros "Regra Padrao da Empresa Customizavel: 15 dias para inativos":
```

Motivo: Bloco l.29-33 e copia byte a byte do bloco l.17-21 (mesmo nome, filtro, frequencia e preferencia). Nao ha no arquivo nem no modelo semelhante (regra_107) indicio da regra pretendida; renomear inventaria um nome e apagar mudaria o conteudo. Arquivo mantido.
