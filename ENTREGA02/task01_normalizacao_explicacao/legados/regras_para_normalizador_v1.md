# Regras de sintaxe GOBR para o normalizador

Uso: ler o texto do usuário, reconhecer os temas abaixo e listar as chaves (`chave`) das regras que o texto exige. A chave é um caminho relativo a `manual/`; `#Titulo` aponta uma seção do arquivo. Página do PDF = página impressa + 4. "forma da tabela" = sintaxe copiada de uma tabela do manual (o manual não traz exemplo completo). Tema fora das regras abaixo: não inventar chave.

## A. Estrutura e execução

### Tipo de execução do conjunto
- chave: 03-secoes/01-01-visao-geral-e-execucao.md
- faz: define quando o conjunto de regras roda (DAILY, HOURLY, WEEKLY, DETACHED, ONLUNCH, DAWN, DARK, HALFANHOUR, SHORTLY). Fica fora do texto GOBR.
- no texto: "rodar toda madrugada", "toda hora", "só quando eu pedir", "a cada 15 minutos".
- gobr: sem exemplo no manual (PDF p.6)

### Times de vendedores
- chave: 03-secoes/03-01-times.md
- faz: agrupa vendedores (todos, só televendas, só campo, por id, por supervisor, só ativados, menos alguns).
- no texto: "os vendedores de televendas", "o pessoal de campo do supervisor tal", "o vendedor de código tal".
- gobr: `vendedores todostelevendas` / `vendedores porid("1020", "1021")` (PDF p.9)

### Estrutura do arquivo e exemplos de regra
- chave: 03-secoes/02-01-exemplos-e-estrutura-geral.md
- faz: esqueleto time, segmentação, carteira; frases de negócio que a linguagem expressa.
- no texto: qualquer pedido; entrega transversal.
- gobr: `time "nome do time":` (PDF p.8)

## B. Carteiras e segmentações

### Carteira exclusiva e carteira livre
- chave: 03-secoes/04-01-carteiras-e-segmentacoes.md#Exclusiva x livre
- faz: carteira normal retira o cliente das carteiras seguintes; `carteira livre` não retira.
- no texto: "o mesmo cliente pode aparecer em mais de uma carteira", "sem tirar o cliente da outra".
- gobr: `carteira livre "televendas com ruptura de campo":` (PDF p.17)

### Ordem de prioridade entre carteiras
- chave: 03-secoes/04-01-carteiras-e-segmentacoes.md#Cenário 3 — carteiras separadas, a ordem importa
- faz: o cliente fica na primeira carteira que o pega; inverter a ordem inverte a prioridade.
- no texto: "primeiro atende a fixa, depois o que sobrar", "a ruptura tem prioridade".
- gobr: sem exemplo isolado; ver os dois blocos `carteira` do PDF p.15

### Segmentação (grupo auxiliar de clientes)
- chave: 03-secoes/04-01-carteiras-e-segmentacoes.md#Segmentação como fonte
- faz: grupo de clientes que não gera agenda, usado como base de carteira, parâmetro ou tag.
- no texto: "separar os clientes adimplentes para usar depois", "um grupo só para controle".
- gobr: `segmentacao "carteiras adimplentes da superv maria":` (PDF p.18)

### Escolher os clientes da carteira
- chave: 03-secoes/04-02-selecao-clientes-ruptura.md
- faz: funções carteirafixa, carteiraacessivel, carteiraruptura, portfolio, inativos, segmentados, todos.
- no texto: "os clientes fixos do time", "todos os clientes", "os inativos do time há tanto tempo".
- gobr: `clientes carteirafixa("superv marcos")` (PDF p.13)

### Ruptura de um time para outro
- chave: 03-secoes/04-02-selecao-clientes-ruptura.md#Opções para ruptura (após a função)
- faz: passa clientes parados (sem compra, sem visita ou inativos) de um time para outro; `ou prospects` inclui quem nunca comprou.
- no texto: "clientes do campo sem comprar há 90 dias vão para os televendas".
- gobr: `clientes ruptura("superv maria" para "superv marcos")` / `de positivacao(90 dias)` (PDF p.13)

## C. Filtros de calendário e horário (valem para parâmetros e alertas)

### Dia do mês
- chave: 03-secoes/05-01-filtros-temporais-calendario.md#Dia do mês
- faz: restringe a regra a dias do mês.
- no texto: "só no dia 10", "a partir do dia 12", "no último dia do mês".
- gobr: `a partir do dia 12` (PDF p.23)

### Dia da semana
- chave: 03-secoes/05-01-filtros-temporais-calendario.md#Dia da semana
- faz: restringe a dias da semana, dias úteis ou fim de semana.
- no texto: "só às segundas", "em dias úteis", "no fim de semana".
- gobr: `nos dias uteis` (PDF p.23)

### Semana ou quinzena do mês
- chave: 03-secoes/05-01-filtros-temporais-calendario.md#Semana do mês
- faz: primeira a quarta semana, última semana, primeira ou segunda quinzena.
- no texto: "na primeira semana do mês", "na segunda quinzena".
- gobr: `na primeira semana` (PDF p.23)

### Mês, bimestre, trimestre ou semestre
- chave: 03-secoes/05-01-filtros-temporais-calendario.md#Mês do ano
- faz: restringe a meses individuais ou períodos do ano.
- no texto: "no segundo semestre", "em dezembro", "no último trimestre".
- gobr: `no segundo semestre` (PDF p.24)

### Horário de disparo (só alertas)
- chave: 03-secoes/05-02-filtros-de-horario-alertas.md
- faz: hora exata ou de hora em hora (dia todo, entre horas ou a partir de uma hora). Uma forma por vez.
- no texto: "avisar às 15h", "de hora em hora a partir das 7h".
- gobr: `nos dias uteis e de hora em hora a partir de '07:00'` (PDF p.22)

## D. Filtros de cliente (após `quando`, combinados com `e`)

### Cliente ativo ou inativo
- chave: 03-secoes/06-01-atividade-inatividade.md
- faz: ativo/inativo (critério padrão, do vendedor ou da empresa); inativo há N dias.
- no texto: "cliente ativo", "parado há mais de 90 dias sem comprar".
- gobr: `inatividade de <<N>> dias` (PDF p.26)

### Cliente que nunca comprou ou comprou uma vez
- chave: 03-secoes/06-01-atividade-inatividade.md
- faz: prospect (do vendedor ou da empresa), `sem venda ou prospects`, compra única.
- no texto: "prospects", "só comprou uma vez com a gente".
- gobr: `unica compra com o vendedor` (PDF p.27)

### Comprou (ou não) em um período
- chave: 03-secoes/06-01-atividade-inatividade.md
- faz: tem venda ou não tem venda do vendedor/empresa num período; atividade no período.
- no texto: "comprou nos últimos dias com qualquer vendedor", "sem compra neste mês".
- gobr: `tem venda da empresa <<condicional de tempo>>` (PDF p.27)

### Visitas remotas ou incertas
- chave: 03-secoes/06-01-atividade-inatividade.md
- faz: percentual mínimo de visitas remotas (ou de natureza incerta) num período.
- no texto: "clientes atendidos só por telefone em boa parte das visitas".
- gobr: `tem <<N>>% de visita remota <<tempo>>` (PDF p.27)

### Recência de visita ou de compra
- chave: 03-secoes/06-02-recencia-visita-positivacao.md
- faz: última visita/compra dentro ou fora de um intervalo (do grupo, do vendedor ou global).
- no texto: "visitado há mais de 10 e menos de 90 dias", "última compra fora desse prazo".
- gobr: `recencia de visita entre 10 dias e 90 dias` (PDF p.26)

### Situação financeira e crédito
- chave: 03-secoes/06-03-financeiros.md
- faz: adimplente/inadimplente, crédito disponível, limite de crédito, percentual de crédito.
- no texto: "sem pendência financeira", "com limite de crédito acima de tal valor".
- gobr: `adimplentes` / `com limite de R$ <<valor>> de credito` (PDF p.28)

### Ticket médio e faturamento
- chave: 03-secoes/06-03-financeiros.md
- faz: ticket médio, total faturado ou média faturada por período, com faixa de valores; `ou indefinido` inclui valor desconhecido.
- no texto: "ticket médio acima de 3 mil", "faturou entre 8 e 12 mil no semestre".
- gobr: `com ticket medio maior que R$ <<valor>>` (PDF p.29)

### Agenda
- chave: 03-secoes/06-04-agenda.md
- faz: cliente já agendado (hoje, ontem, semana), fora da agenda, agendável ou não, reagendado.
- no texto: "já está na agenda de hoje", "não foi agendado nos últimos 5 dias".
- gobr: `na agenda de hoje` / `fora da agenda padrão em 5 dias` (PDF p.29-30)

### Localização (cidade, bairro, estado, rota)
- chave: 03-secoes/06-05-localizacao-classificacao.md
- faz: filtros de texto (igual, diferente, contém, inicia com) sobre cidade, bairro, UF, nome da rota.
- no texto: "clientes de Goiânia", "dos estados SP e MG", "fora do bairro tal".
- gobr: `nome da cidade igual("cidade1", "cidade2")` (PDF p.30)

### Tipo e situação do cadastro
- chave: 03-secoes/06-05-localizacao-classificacao.md
- faz: pessoa física/jurídica, matriz/filial, excluído, bloqueado, situação na Receita (ativa, suspensa, inapta, baixada).
- no texto: "só pessoa jurídica", "que não estejam bloqueados", "empresa baixada na Receita".
- gobr: `pessoa fisica` / `bloqueados` (PDF p.31)

### CNAE, nota, rótulo e coordenada
- chave: 03-secoes/06-05-localizacao-classificacao.md
- faz: CNAE (Govendas, Receita, ERP), conteúdo ou nome da nota, rótulo de classificação, coordenada confiável.
- no texto: "do CNAE tal", "com geolocalização válida".
- gobr: `cnae da receita igual(...)` / `tem coordenada confiavel` (PDF p.31-32)

### Seleção por código
- chave: 03-secoes/06-06-classificacao-por-id.md
- faz: igual ou diferente sobre id de ramo, rota, cliente, cliente principal, pagamento, cobrança.
- no texto: "ramo de atividade 12", "clientes de códigos tais", "rotas fora de 4, 7 e 14".
- gobr: `ramo de atividade igual("1", "12")` (PDF p.32)

### Curva ABC e ciclo de vida
- chave: 03-secoes/06-07-curva-abc-ciclo-de-vida.md
- faz: curva A/B/C com a empresa ou com o vendedor; ciclo de vida ativo, inativo, prospect, ativado, reativado.
- no texto: "cliente curva A", "cliente reativado, que voltou a comprar".
- gobr: `curva A com a empresa` / `no ciclo de vida reativado com a empresa` (PDF p.32-33)

### Frequência histórica e parâmetros atuais
- chave: 03-secoes/06-08-frequencia-e-parametros.md
- faz: cliente fora do ritmo de compra, frequência histórica maior/menor/entre, sem parâmetro, atendimentos abaixo do esperado.
- no texto: "fora do ritmo normal de compra dele", "ainda sem parametrização".
- gobr: `frequencia historica maior que <<N>> dias` (PDF p.33)

### Contido em segmentação
- chave: 03-secoes/06-09-segmentacao-contido.md
- faz: cliente pertence (ou não) a uma segmentação já definida.
- no texto: "que estejam no grupo tal", "que não estejam no grupo tal".
- gobr: `contido na segmentacao("nome1", "nome2")` (PDF p.34)

### Ruptura global e contato no agendamento
- chave: 03-secoes/06-10-ruptura.md
- faz: ruptura global por faixa (bimestre 30-60 dias, trimestre 61-90, semestre 91-180, ano 181-365); sem contato no(s) último(s) agendamento(s).
- no texto: "sem comprar entre 61 e 90 dias", "nas últimas 3 vezes que foi agendado ninguém falou com ele".
- gobr: `em ruptura global do trimestre` (PDF p.35)

### Número de compras e queda de faturamento
- chave: 03-secoes/06-11-outros-filtros.md
- faz: total de compras (vendedor ou empresa, em período ou total); queda de faturamento maior ou menor que N%.
- no texto: "pelo menos 5 compras com o vendedor", "queda de faturamento acima de 20%".
- gobr: `total de compras com o vendedor maior que <<N>>` / `queda de faturamento maior que <<N>>%` (PDF p.35-36)

### Cadastro recente e cliente elegível
- chave: 03-secoes/06-11-outros-filtros.md
- faz: cadastrado há pelo menos N dias ou desde uma data; elegível (não excluído, ativo, marcado para agendar).
- no texto: "cadastrado há pelo menos 60 dias", "só clientes elegíveis".
- gobr: `cadastrado faz 90 dias` / `elegivel` (PDF p.36)

### Positivado hoje, atendimento remoto, sem perfil
- chave: 03-secoes/06-11-outros-filtros.md
- faz: positivado hoje; atendimento remoto em N dias; `sem perfil` (texto do PDF ambíguo; ver manual).
- no texto: "que já comprou hoje", "teve atendimento remoto nos últimos 5 dias".
- gobr: `positivado de hoje` / `atendimento remoto em 5 dias` (PDF p.35)

### Datas de rota e de visita do representante
- chave: 03-secoes/06-11-outros-filtros.md
- faz: data de rota ou de visita de vendedor externo (ERP) em janela passada ou futura.
- no texto: "com rota programada nos próximos 2 dias", "visitado pelo representante na semana passada".
- gobr: `data da rota no mês anterior` (PDF p.36)

### Janelas de tempo (N dias, mês anterior, próximos N dias)
- chave: 03-secoes/06-12-opcoes-de-tempo.md
- faz: vocabulário de tempo usado dentro dos filtros: `<N> dias`, períodos fixos, `entre ... e ...`, `há N dias atras`, `nos proximos N dias`.
- no texto: qualquer janela de tempo ("últimos 30 dias", "no mês passado", "daqui a 2 semanas").
- gobr: `nos proximos <<N>> dias` / `no mês anterior` (PDF p.40-41)

## E. Parâmetros de atendimento

### Regra de parâmetros (estrutura)
- chave: 03-secoes/07-01-parametros-estrutura-e-exemplos.md#Fluxo de uma regra
- faz: aplica frequência, preferência de dia, rota a uma carteira; não sobrepõe ajuste manual do usuário.
- no texto: "os clientes dessa carteira devem ser atendidos toda semana".
- gobr: `da carteira("carteira fixa")` / `quando inatividade de 90 dias` / `frequencia semanal()` (PDF p.43)

### Frequência fixa
- chave: 03-secoes/07-03-frequencia.md#Fixa por período
- faz: `diaria()`, `semanal()`, `quinzenal()`, `mensal()`, `bimestral()`, `trimestral()`, `semestral()`, `anual()` ou `de <N> dias`.
- no texto: "atender toda semana", "uma vez por mês", "a cada 20 dias".
- gobr: `frequencia mensal()` (PDF p.43); `de <<N>> dias` (PDF p.48)

### Teto ou piso da frequência fixa
- chave: 03-secoes/07-03-frequencia.md#Modificadores de limite para frequência fixa
- faz: `no máximo` / `no mínimo` sobre frequência fixa. Sobre frequência do histórico: não documentado.
- no texto: "no máximo uma semana entre atendimentos".
- gobr: `no máximo semanal()` (PDF p.48)

### Frequência dinâmica e cascata
- chave: 03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
- faz: usa a do vendedor (mais/menos N dias), do histórico, de qualquer vendedor, média de ativos/inativos; `ou` encadeia alternativas; `remover` apaga.
- no texto: "manter o intervalo que o vendedor já usa; se não tiver, 35 dias".
- gobr: `frequencia do vendedor ou de qualquer vendedor ou de 35 dias` (PDF p.45)

### Preferência de dia da semana
- chave: 03-secoes/07-02-preferencia-dia-semana.md
- faz: valor 0 (não visitar) a 3 (prioritário) por dia; `maior`, `normal`, `menor`; `do historico`, `nos dias uteis`.
- no texto: "prefere segunda e terça", "prioridade alta na segunda, baixa na terça", "nunca no sábado".
- gobr: `preferencia na segunda e na terça` (PDF p.43)

### Não agendar (retirar da agenda)
- chave: 03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
- faz: marca o cliente para não aparecer na agenda; não combina com frequência ou preferência na mesma regra.
- no texto: "esses clientes saem da agenda", "não precisa visitar".
- gobr: `nao agendar` (PDF p.44)

### Parâmetro só em certos dias de execução
- chave: 03-secoes/07-01-parametros-estrutura-e-exemplos.md#Com restrição temporal
- faz: filtro de calendário entre a fonte e o `quando`; fora do dia a regra é ignorada.
- no texto: "só aplicar em dias úteis".
- gobr: `nos dias úteis` (PDF p.45)

### Limpar parâmetros (corpus não tem exemplo)
- chave: 03-secoes/07-01-parametros-estrutura-e-exemplos.md#Limpar parametrizações
- faz: remove parametrizações dinâmicas aplicadas pelo GoBR numa carteira; bloco próprio só com a fonte.
- no texto: "zerar os ajustes automáticos antes de aplicar de novo".
- gobr: `limpar parametros "remover parametrizacao":` / `da carteira("carteira fixa")` (PDF p.47)

### Evitar choque entre televendas e campo
- chave: 03-secoes/07-04-conflito-pivot-rota.md#Evitar choque entre televendas e campo
- faz: `sem choque`: preferência de dias não coincide com a de outra carteira; refina por rota ou pasta.
- no texto: "o cliente não pode receber ligação e visita no mesmo dia".
- gobr: `sem choque na carteira("carteira campo")` (PDF p.46)

### Semana de início no mês (pivot)
- chave: 03-secoes/07-04-conflito-pivot-rota.md#Semana pivot (restrito)
- faz: `restrito` a partir de (ou até) a N-ésima semana do mês.
- no texto: "só entra na agenda a partir da segunda semana do mês".
- gobr: `restrito a partir da segunda semana` (PDF p.46)

### Roteirização e atendimento fixo
- chave: 03-secoes/07-04-conflito-pivot-rota.md#Roteirização e fixação
- faz: `roteirizavel` inclui na otimização de rota presencial; `fixo` endurece frequência e preferência. Sem indicação: não roteirizavel, não fixo.
- no texto: "entra na rota de visita", "atendimento fixo, sem remanejar".
- gobr: `roteirizavel` / `fixo` (PDF p.47)

## F. Alertas (nunca no mesmo conjunto de parâmetros)

### Alerta: estrutura e gatilho
- chave: 03-secoes/08-01-alertas-estrutura-e-gatilhos.md#Etapas
- faz: fonte (time ou carteira), calendário/horário, `quando`, `onde <gatilho>`, `informe`, `entregue`, `pelos canais`.
- no texto: "avisar o gestor quando ...", "alertar o vendedor se o cliente ...".
- gobr: `onde nao tem venda em 21 dias` (PDF p.52)

### Gatilhos de alerta
- chave: 03-secoes/08-01-alertas-estrutura-e-gatilhos.md#Gatilhos (após `onde`)
- faz: venda/visita nos últimos N dias, fora da frequência, sem parâmetro, visita remota ou incerta, ticket, coordenada, produtos sugeridos.
- no texto: "cliente sem visita há 15 dias", "sem coordenada confiável".
- gobr: `não tem visita em <<N>> dias` (PDF p.54)

### Conteúdo do alerta (informe e tipo de evento)
- chave: 03-secoes/08-01-alertas-estrutura-e-gatilhos.md#Tipos de evento (informe)
- faz: tabela personalizada, evento por cliente, por agenda, ou resumo por supervisor/gestor.
- no texto: "mostrar até 5 clientes por vendedor com nome e código".
- gobr: `informe com 15 vendedores e com 5 clientes` (PDF p.52)

### Texto, variáveis, canais e destinatário do alerta
- chave: 03-secoes/08-02-alertas-entrega-e-variaveis.md
- faz: `descreva com o texto(...)` com variáveis `$...$`; `entregue para` vendedor/supervisor/gestor; canais govendas() e whatsapp(template); redirecionar por e-mail.
- no texto: "mandar pelo WhatsApp e pelo app", "o texto deve citar o total de clientes".
- gobr: `entregue para gestor` / `pelos canais govendas() e whatsapp("ruptura_vendedor_template1")` (PDF p.52)

## G. Tags (corpus não tem exemplo; o manual não mostra a sintaxe do bloco)

### Tag de contexto e tag nomeada
- chave: 03-secoes/09-01-tags.md#Gatilhos de tags de contexto
- faz: marca clientes por gatilho (tem rotas, cidades, ramo, produtos, fornecedores, feedbacks...). Tag = `@nometag`, minúsculas e números.
- no texto: "marcar os clientes que tem produto sugerido para usar depois nos filtros".
- gobr: sem exemplo de bloco no manual; forma da tabela: `tem rotas` (PDF p.59); tag `@ruptura` (PDF p.62)

### Filtros de produtos e de feedbacks para tag
- chave: 03-secoes/09-01-tags.md#Filtros de produtos
- faz: filtros de produto (em ruptura, mais vendidos, primeira compra...) e de feedback (último atendimento, N atendimentos).
- no texto: "produtos em ruptura para o cliente", "reclamação que apareceu 2 vezes nos últimos 5 atendimentos".
- gobr: `em ruptura` / `nos ultimos <<N>> atendimentos` (PDF p.60)

## Fora do manual (não mapear para chave)
- `no maximo` / `no minimo` depois de frequência `do historico`: o manual só documenta limite para frequência fixa (PDF p.48); usada no corpus, não documentada.
- `sem venda` e `sem vendas` isolados: o manual documenta só `sem venda ou prospects` (PDF p.26); uso isolado não documentado.

## Sem entrada (tópicos de manual/ que não são regra)
- 01-conceitos.md, 02-invariantes.md, 03-mapa.md, CORRECOES_MANUAL.md: material de apoio, não descreve regra.
- 03-secoes/10-gramatica.md: gramática e tipos básicos; transversal, entregue sempre ao gerador.
