# Registro de correções do manual/

Páginas do PDF `govendas-rules.pdf` (página do PDF = página impressa + 4). Cada linha: arquivo, o que mudou, motivo.

| Arquivo | O que mudou | Motivo | Página do PDF |
|---|---|---|---|
| `03-secoes/04-01-carteiras-e-segmentacoes.md` | Linha `clientes ruptura da segmentacao(...)` completada com `para "vendedor avulso")`; removida a nota `[CORTE NO MANUAL]` | O PDF contém a linha inteira, mas ela passa da margem direita da página e a extração padrão a corta em `"ve`. Extraída com área de leitura maior (`pdftotext -raw -x 0 -y 0 -W 1500 -H 842 -f 18 -l 18`). Única linha cortada do PDF inteiro | 18 (impressa 14) |
| `03-secoes/06-04-agenda.md` | Frase de abertura volta a dizer "presente em agendas passadas" | A condensação tinha apagado "passadas" | 29 (impressa 25) |
| `03-secoes/06-11-outros-filtros.md` | Descrição de `sem perfil com o vendedor` e `sem perfil com a empresa` volta ao texto do PDF ("não está marcado para não agendar ... ou foi excluído ou consta como baixado"), com aviso de que a leitura lógica do "ou" não é declarada | A reescrita trocava "ou" por "nem ... nem", interpretação que o PDF não faz | 35 (impressa 31) |
| `01-conceitos.md` | Bullet "Teto ou piso sobre intervalo calculado pelo histórico" sai de "Não expressável" e vai para nova seção "Não documentado no manual" | O PDF não diz que a construção é impossível; só documenta `no máximo`/`no mínimo` para frequência fixa. "Não expressável" afirmava mais do que o PDF | 48 (impressa 44) |
| `02-invariantes.md` | Referência de grafia e contagens de fonte de parâmetros passam de `referencias/` para `simulacao/` (4 ocorrências) | `referencias/` não existe no repositório; `simulacao/` existe | não se aplica |
| `02-invariantes.md` | Bullets de tipos, string e comentário trocados por ponteiro para `10-gramatica.md`; bullet de combinações de blocos idem | Redundância com `10-gramatica.md`, que é a cópia fiel da seção 10 do PDF | 61-62 |
| `03-mapa.md` | `06-10-ruptura` acrescentado ao tipo `tempo_sem_visita`; novos arquivos 01-01 e 02-01 listados como transversais | `06-10-ruptura` contém "sem contato no último agendamento", que `01-conceitos.md` classifica como `tempo_sem_visita` | 35 |
| `03-secoes/01-01-visao-geral-e-execucao.md` (novo) | Capítulo 1: finalidade do GoBR, configuração de um conjunto de regras, tabela de tipos de execução | Capítulo ausente do manual parseado | 5-6 |
| `03-secoes/02-01-exemplos-e-estrutura-geral.md` (novo) | Seção 2.1 (seis exemplos de regra de negócio) e esqueleto da seção 2.2 | Seção ausente; o esqueleto de 2.2 não estava em nenhum arquivo | 7-8 |
| `03-secoes/07-01-parametros-estrutura-e-exemplos.md` | Seção nova "Ordem entre regras de parâmetros": regras `parametros` valem na ordem do arquivo; cliente já parametrizado não é reprocessado | Regra de ordem ausente do manual parseado; o normalizador a usa para ligar pedidos em sequência ("primeiro... depois") a uma chave | 46 |

## Verificado e não alterado
- Contagens de grafia em `02-invariantes.md`: as formas acentuadas (23, 0, 1, 0, 13, 0, 0, 2) reproduzem em `simulacao/`; as formas sem acento divergem em até 2,3% do número do manual (ex.: `frequencia` 1474 medido contra 1460 escrito), conforme o tratamento de comentários. Números mantidos; método da contagem original desconhecido.
- Contagem "30 arquivos" da ata para teto/piso: 30 arquivos de `dados/processados/regras_gobr/` contêm `no maximo`/`no minimo` fora de comentário; 26 deles logo após `do historico ou`. Nenhum número de corpus entrou no manual.
- Contagem de fonte de parâmetros em `02-invariantes.md` (963 `do time(` contra 732 `da carteira(`): em `simulacao/` medi 954 e 723 (linhas que começam com a forma). Diferença de 9 nas duas; números do manual mantidos, método original desconhecido.
