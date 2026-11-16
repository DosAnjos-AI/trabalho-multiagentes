# conferidor_gobr

Conferidor determinístico de arquivos `.gobr` contra o manual original do goVendas
(`govendas-rules.pdf`, v0.89.0, gramática 1.0). Sem modelo de linguagem: o mesmo texto
produz sempre o mesmo laudo.

Usos previstos: sanear a base (tarefa 03), validar o `.gobr` que o modelo escrever, e servir
de ferramenta do agente.

## Arquivos

| Arquivo | Papel |
|---|---|
| `itens_obrigatorios.py` | Dados: a lista fechada de 35 itens (29 verificáveis), com origem e citação, e o vocabulário documentado (padrões por seção do manual) |
| `conferidor.py` | Código: `conferir(texto) -> Laudo`. Não imprime, não lê disco |
| `cli.py` | Embrulho de linha de comando |

## Como rodar

Como biblioteca (o agente chama assim, com texto em memória):

```python
import sys
sys.path.insert(0, "src")
from conferidor_gobr.conferidor import conferir

laudo = conferir(texto_gobr)
laudo.aprovado      # True se não há falha
laudo.falhas        # achados das categorias 1 e 2
laudo.achados       # todos, inclusive construcao_nao_documentada
```

Na linha de comando, a partir da raiz do projeto:

```
.venv/bin/python src/conferidor_gobr/cli.py caminho/regra.gobr
.venv/bin/python src/conferidor_gobr/cli.py --so-falhas caminho/*.gobr
cat regra.gobr | .venv/bin/python src/conferidor_gobr/cli.py -
```

Código de saída: 0 sem falha, 1 com falha, 2 erro de uso.

## O que entra e o que sai

Entra: o texto de um arquivo `.gobr` (`str`).

Sai: um `Laudo` com a lista de `Achado`. Cada achado tem:

| Campo | Conteúdo |
|---|---|
| `item` | identificador do item de `itens_obrigatorios.ITENS` |
| `categoria` | `item_obrigatorio_ausente`, `divergencia_com_manual` ou `construcao_nao_documentada` |
| `linha` | linha do texto, ou `None` quando o achado é do arquivo inteiro |
| `mensagem` | descrição curta |
| `construcao` | forma abstraída da construção (só na categoria 3), chave do inventário |
| `trecho` | texto original da cláusula |

`construcao_nao_documentada` **não é falha**: por decisão do Mestre, onde o manual não
documenta, o exemplo da base sobrepõe o manual. O achado existe para alimentar o inventário.

## Como a conferência funciona

1. Remove comentários (`#` fora de aspas) e linhas vazias.
2. A primeira linha significativa tem de ser `version 1.0`.
3. Cabeçalhos (`time`, `segmentacao`, `carteira`, `carteira livre`, `parametros`,
   `limpar parametros`, `alerta`) abrem blocos, com ou sem indentação.
4. Dentro do bloco, cada linha abre uma cláusula pela palavra inicial (`vendedores`,
   `clientes`, `quando`, `frequencia`, ...) ou continua a anterior. Linha que segue
   cláusula com aspas ou parêntese aberto, ou terminada em `e`/`ou`, é continuação.
5. Cada cláusula é normalizada (acento removido, espaço colapsado) e casada com o
   vocabulário: com a mesma caixa, a construção está documentada; só ignorando a caixa,
   é `grafia_documentada` (divergência); sem casar, é `vocabulario_do_manual` (não documentada).
   Filtros após `quando` são segmentados um a um, preferindo o maior filtro documentado.
6. Checagens de bloco (vendedores, clientes, fonte, atendimento, ordem das etapas) e de
   arquivo (ordem das categorias, nomes distintos, referências).

Controle feito na construção: os exemplos completos do manual (sec. 3.2, 3.4, 4.3.2, 4.5, 4.6.1,
5.1, 7.3.1 a 7.3.11, 8.2), transcritos, saem com zero achados; e uma mutação por item
verificável dispara exatamente aquele item.

## Lacunas declaradas

- **Itens não verificáveis** ficam na lista e fora da conferência: configuração do conjunto
  (nome, tipo de execução, empresa, habilitado; fora do texto), vendedores cadastrados,
  nomes de alerta distintos entre conjuntos, regra aplicada a time e não a vendedor,
  `regrapadrao`, sintaxe do bloco de tags.
- **Alertas**: `informe`, `descreva`, `entregue` e `pelos canais` são conferidos só por
  presença e ordem, não pelo vocabulário interno. A base não tem nenhum alerta.
- **Tags**: o manual não mostra a sintaxe do bloco; um cabeçalho `tags`/`tag` vira
  construção não documentada.
- **Generalizações**: onde o manual declara as opções por escrito, o vocabulário combina as
  opções (ex.: `recencia de visita|positivacao` x `global|do vendedor` x `fora da`, p.24;
  agenda padrão/ruptura/complementar, p.26; `com a empresa|com o vendedor` na curva ABC,
  p.29). A sec. 6.13 entra em todo `<<condicional de tempo>>`. Singular e plural de
  unidade (`1 dia`, `2 dias`) são aceitos.
- **Acento é livre** (p.58 aceita acento, e o manual usa as duas grafias). **Caixa não é**:
  `curva c` diverge de `curva C`.
- **Espaçamento** junto a parêntese e vírgula é ignorado (o manual não fixa regra), e
  indentação também.
- **Referências** só conferem se o nome existe em algum bloco do arquivo, não se o tipo do
  bloco referido é o esperado (ex.: `da carteira("x")` aceita `x` que seja time).
- **Parêntese não fechado** faz a cláusula engolir as linhas seguintes do mesmo bloco, até o
  próximo cabeçalho; as cláusulas engolidas deixam de ser conferidas individualmente.
- **Arquivo vazio ou só com comentários** sai com três falhas (`version_no_inicio`,
  `ao_menos_um_time`, `categoria_final_presente`), não com laudo vazio. Isso decorre dos
  itens, não de um caso especial.
- **Palavra-chave de cláusula desconhecida** no início de linha é tratada como continuação
  da cláusula anterior.

## Próximos passos definidos pelo Mestre

Registro, sem implementação. Serve para a etapa final não começar do zero.

1. O conferidor vai corrigir o que conseguir corrigir sozinho, e vai registrar o que
   identifica mas não consegue corrigir. O registro vai sair num formato que um modelo de
   linguagem consiga ler depois.
2. O conferidor vai devolver as próprias anotações, seja o documento corrigido, seja a lista
   dos erros mapeados. O modelo de linguagem vai usar esse retorno, junto com o prompt e os
   outros insumos, para reescrever o arquivo `.gobr`.
