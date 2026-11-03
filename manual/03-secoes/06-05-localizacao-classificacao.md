# Filtros de localização e classificação (manual 6.5, p.26-28)

Filtros de texto aceitam as operações `igual`, `diferente`, `contém`, `inicia com`.

| Filtro | Descrição |
|---|---|
| `nome da cidade igual("cidade1", "cidade2")` | clientes na cidade |
| `nome do bairro diferente(...)` | bairro diferente do informado |
| `uf do estado contém("SP", "MG")` | UF contém o texto |
| `nome da rota inicia com(...)` | nome da rota começa com o texto |
| `conteudo da nota igual(...)` | conteúdo da nota igual a um dos valores |
| `nome da nota contém(...)` | nome da nota contém um dos textos |
| `o rótulo diferente(...)` | rótulo de classificação diferente de todos os valores |
| `cnae igual(...)` | id do CNAE mapeado pelo Govendas igual a um dos ids |
| `cnae da receita igual(...)` | id do CNAE da Receita Federal igual a um dos ids |
| `cnae do erp igual(...)` | id do CNAE mapeado no ERP igual a um dos ids |
| `nome do cnae da receita inicia com(...)` | nome do CNAE da Receita começa com um dos textos |
| `status na receita federal definido como ativa` | empresa ativa na Receita |
| `status na receita federal definido como suspensa` | suspensa |
| `status na receita federal definido como inapta` | inapta |
| `status na receita federal definido como baixada` | baixada |
| `pessoa fisica` | só pessoa física (CPF) |
| `pessoa juridica` | só pessoa jurídica (CNPJ) |
| `cliente principal` | registro é o cliente principal (não é filial) |
| `cliente filial` | registro é filial |
| `excluidos` / `não excluidos` | marcado / não marcado como excluído do sistema |
| `bloqueados` / `não bloqueados` | bloqueado / não bloqueado para atendimento |
| `tem coordenada confiavel` | geolocalização validada |
| `não tem coordenada confiavel` | geolocalização ausente ou não confiável |
