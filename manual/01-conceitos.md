# Conceitos comerciais expressáveis pelo GoBR

Inventário, em linguagem de negócio, do que uma regra comercial de atendimento pode pedir: quem é selecionado (critérios de seleção) e como o atendimento acontece (parâmetros de atendimento). Serve para classificar cada parte de um pedido. Páginas pela numeração impressa do manual v0.89.0.

## Critérios de seleção
### tempo_sem_comprar
Tempo desde a última compra, com a empresa ou com um vendedor, e ritmo de compra do cliente (p.22-24, p.29-31).
- "Comprou nos últimos 7 dias, com qualquer vendedor." (p.23)
- "Última compra entre 31 e 60 dias atrás." (p.24)
- "Está há mais de 90 dias sem comprar." (p.22)
- "Comprou no ano passado e ainda não comprou neste ano." (p.23, p.34)
- "Sem compra entre 61 e 90 dias." (p.31)
- "Está fora do ritmo de compra calculado para ele." (p.29)
- "Ritmo histórico do cliente acima de 30 dias." (p.29; o manual não diz se o histórico é de compras ou de visitas)
### tempo_sem_visita
Tempo desde a última visita ou atendimento, presencial ou remoto (p.24, p.31-32).
- "Sem visita há mais de 30 dias." (p.16, p.24)
- "Visitado pelo representante externo na semana passada." (p.32)
- "Teve atendimento remoto nos últimos 5 dias." (p.31)
- "Sem contato nas últimas 3 vezes em que foi agendado." (p.31)
### estagio_relacionamento
Fase do cliente na relação de compra (p.22-23, p.29).
- "Prospect, que nunca fez pedido." (p.23)
- "Cliente com uma única compra com o vendedor." (p.23)
- "Cliente ativo; cliente inativo." (p.22)
- "Cliente reativado, que voltou a comprar depois de parado." (p.29)
- "Ex-prospect que fez a primeira compra com o vendedor." (p.29)
### carteira
Vínculo do cliente com vendedor ou equipe (p.8-17).
- "Clientes da carteira fixa dos televendas." (p.15)
- "Clientes do campo parados há mais de 90 dias, repassados aos televendas." (p.9)
- "Carteira em que o cliente também pode aparecer em outra." (p.9)
- "Clientes que sobraram depois das carteiras anteriores." (p.12)
Também cobre: carteira acessível, carteira de ruptura pré-calculada e portfólio do vendedor (p.15).
### situacao_financeira
Pendência em aberto, crédito disponível, limite de crédito (p.24-25).
- "Cliente adimplente; cliente inadimplente." (p.24)
- "Sem crédito disponível." (p.24)
- "Limite de crédito de pelo menos 5 mil reais." (p.24)
- "Crédito disponível abaixo de 199 reais." (p.25)
Também cobre: percentual de crédito em relação ao limite (p.25).
### situacao_cadastro
Situação e idade do cadastro do cliente (p.27, p.31-32).
- "Cadastrado há pelo menos 60 dias." (p.32)
- "Cadastro excluído; cliente bloqueado para atendimento." (p.27)
- "Cadastrado a partir de uma data." (p.32)
- "Empresa ativa, suspensa, inapta ou baixada na Receita Federal." (p.27)
- "Cliente elegível: não excluído, ativo e liberado para agendar." (p.32)
### valor_cliente
Faturamento, ticket médio, curva, número de compras (p.25, p.28, p.31-32).
- "Cliente curva A." (p.28)
- "Ticket médio acima de 5 mil reais." (p.25)
- "Faturou mais de 25 mil reais no ano." (p.25)
- "Média mensal de faturamento entre 10 e 15 mil reais." (p.25)
- "Queda de faturamento acima de 20%." (p.32)
- "Pelo menos 5 compras com o vendedor." (p.31)
Também cobre: incluir clientes de valor desconhecido (p.25).
### localizacao
Cidade, bairro, estado, nome da rota (p.26).
- "Clientes de Goiânia." (p.26)
- "Clientes de São Paulo e de Minas Gerais." (p.26)
- "Fora do bairro tal." (p.26)
- "Rota cujo nome começa com tal texto." (p.26)
### agenda_rota
Presença em agenda e datas de rota (p.25-26, p.32-33).
- "Já está na agenda de hoje." (p.25)
- "Não esteve na agenda nos últimos 5 dias." (p.26)
- "Tem rota programada nos próximos 2 dias." (p.33)
- "Teve rota no mês anterior." (p.32)
- "Cliente marcado como não agendável." (p.26)
- "Elegível e marcado para entrar em rota." (p.32)
### segmento
Ramo, tipo de cliente, classificação, grupo auxiliar (p.26-28, p.30).
- "Cliente do ramo de atividade de código 12." (p.28)
- "Cliente filial; cliente principal." (p.27)
- "Pessoa física; pessoa jurídica." (p.27)
- "Pertence ao grupo auxiliar de clientes tal." (p.30)
- "CNAE da Receita cujo nome começa com tal texto." (p.27)
Também cobre: CNAE por identificador (p.27); rótulo de classificação e nota do cliente (p.27).
### periodo_vigencia
Em que dias ou períodos a regra vale (p.18-21).
- "Só na primeira semana do mês." (p.19)
- "Às segundas e quartas." (p.18-19)
- "No segundo semestre." (p.20)
- "A partir do dia 12 de cada mês." (p.19)
- "Em dias úteis, de hora em hora a partir das 7h (só alertas)." (p.18, p.21)
### identificacao
Seleção por código ou identificador (p.6, p.28).
- "Vendedores de códigos 1020 e 1021." (p.6)
- "Clientes de códigos específicos." (p.28)
- "Rotas de código 4, 7 e 14." (p.28)
- "Tipo de cobrança ou de pagamento por identificador." (p.28)

## Parâmetros de atendimento
Como o cliente selecionado é atendido (p.38-45). Valem para clientes sem ajuste manual (p.38).
### intervalo_atendimento
Intervalo entre atendimentos: fixo por período ou em dias; a partir de data de referência; calculado pelo histórico de visitas; herdado do vendedor (com acréscimo ou redução), de qualquer vendedor, ou da média de ativos ou inativos; alternativas em cascata; remoção (p.41, p.43-45).
- "Atender toda semana." (p.43)
- "Usar o intervalo do vendedor; sem ele, o de qualquer vendedor; sem nenhum, 35 dias." (p.41)
- "Intervalo calculado pelo histórico de visitas." (p.44)
- "Intervalo fixo, mas nunca maior que uma semana." (p.44; limite documentado só para intervalo fixo)
### dias_preferidos
Preferência por dia da semana, de 0 (não visitar) a 3 (prioritário) (p.38-42).
- "Preferência na segunda e na terça." (p.39)
- "Prioridade alta na segunda, baixa na terça." (p.40)
- "Preferência nos dias úteis." (p.41)
- "Dias pelo histórico de visitas; sem histórico, dias úteis." (p.42)
Sem preferência declarada: segunda a sexta com valor 1, fim de semana 0 (p.39).
### restricao_semana
A partir de qual semana do mês, ou até qual, o cliente pode aparecer na agenda (p.42, p.45).
- "Só a partir da segunda semana do mês." (p.42)
### roteirizacao
Incluir o cliente na otimização de rota presencial; sem indicação, não entra (p.43).
### rigidez
Marcar o atendimento como fixo: restrição mais rígida no uso do intervalo e da preferência pelo gerador de agendas; sem indicação, não é fixo (p.43).
### retirada_agenda
Marcar o cliente para não aparecer na agenda; exclui intervalo e preferência na mesma regra (p.40).
### conflito_canais
Evitar que televendas e campo atendam o mesmo cliente no mesmo dia; refinável por rota ou pasta (p.42).
### limpeza
Remover os ajustes automáticos já aplicados aos clientes, antes de reaplicar (p.43).

## Não expressável
Conferido nas seções de filtros (6), parâmetros (7), alertas (8) e tags (9).
- Limite de atendimentos por período ("no máximo 30 atendimentos por dia", "15 clientes por semana por vendedor"). Nenhum recurso limita contagem: a comparação com o volume parametrizado (p.30, p.50) não impõe teto; o teto de intervalo (p.44) limita dias entre atendimentos; o limite de vendedores e clientes do alerta (p.48-49) só afeta a exibição; tags não têm gatilho de volume (p.55).
- Condições sobre o vendedor, como poucos ou muitos clientes, ou supervisor com poucos vendedores (p.7, não implementado).
- Retirar cliente de uma carteira diretamente; a saída só acontece pela ordem das carteiras (p.16). Tirar da agenda é possível (retirada_agenda, p.40).
- Passar por cima do ajuste manual feito pelo usuário (p.38).
- Misturar, num mesmo conjunto de regras, ajustes de atendimento e alertas (p.47).
- Teto ou piso sobre intervalo calculado pelo histórico: o manual só documenta limites para intervalo fixo (p.44).
