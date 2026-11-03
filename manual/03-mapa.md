# Mapa tipo de critério -> arquivos de 03-secoes/

Cada tipo do vocabulário aponta para os arquivos a recuperar. Um tipo pode ter vários arquivos; um arquivo pode servir a vários tipos. Os arquivos de calendário e tempo são pré-requisito de muitos tipos e entram sempre que o pedido citar janela de tempo.

## Critérios de seleção
| Tipo | Arquivos de 03-secoes/ |
|---|---|
| tempo_sem_comprar | 06-01-atividade-inatividade, 06-02-recencia-visita-positivacao, 06-10-ruptura, 06-11-outros-filtros, 06-12-opcoes-de-tempo, 06-08-frequencia-e-parametros |
| tempo_sem_visita | 06-02-recencia-visita-positivacao, 06-01-atividade-inatividade, 06-11-outros-filtros, 06-12-opcoes-de-tempo, 04-02-selecao-clientes-ruptura |
| estagio_relacionamento | 06-01-atividade-inatividade, 06-07-curva-abc-ciclo-de-vida |
| carteira | 04-01-carteiras-e-segmentacoes, 04-02-selecao-clientes-ruptura, 03-01-times, 06-10-ruptura |
| situacao_financeira | 06-03-financeiros |
| situacao_cadastro | 06-05-localizacao-classificacao, 06-11-outros-filtros |
| valor_cliente | 06-03-financeiros, 06-07-curva-abc-ciclo-de-vida, 06-11-outros-filtros |
| localizacao | 06-05-localizacao-classificacao |
| agenda_rota | 06-04-agenda, 06-11-outros-filtros, 07-04-conflito-pivot-rota |
| segmento | 06-05-localizacao-classificacao, 06-06-classificacao-por-id, 06-09-segmentacao-contido, 04-01-carteiras-e-segmentacoes |
| periodo_vigencia | 05-01-filtros-temporais-calendario, 05-02-filtros-de-horario-alertas, 07-04-conflito-pivot-rota |
| identificacao | 06-06-classificacao-por-id, 03-01-times |

## Parâmetros de atendimento (01-conceitos.md, seção "Parâmetros de atendimento")
| Parâmetro | Arquivos de 03-secoes/ |
|---|---|
| intervalo_atendimento | 07-03-frequencia, 07-01-parametros-estrutura-e-exemplos |
| dias_preferidos | 07-02-preferencia-dia-semana |
| restricao_semana | 07-04-conflito-pivot-rota |
| roteirizacao | 07-04-conflito-pivot-rota |
| rigidez | 07-04-conflito-pivot-rota |
| retirada_agenda | 07-01-parametros-estrutura-e-exemplos |
| conflito_canais | 07-04-conflito-pivot-rota |
| limpeza | 07-01-parametros-estrutura-e-exemplos |

## Arquivos de uso transversal (recuperar por estrutura do pedido, não por tipo)
- 07-01-parametros-estrutura-e-exemplos: todo pedido de parâmetros de atendimento (estrutura e restrições).
- 08-01-alertas-estrutura-e-gatilhos, 08-02-alertas-entrega-e-variaveis: pedido de alerta.
- 09-01-tags, 10-gramatica: referência; não atendem a nenhum critério de seleção nem parâmetro de atendimento.
