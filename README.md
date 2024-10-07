# CASES TESTE SQL

Após a descrição dos cases abaixo, haverá o tutorial de como executar os arquivos.
Arquivos com os scritps python e explicações
- load.py
- cases_sql.py

# CASE 1
Encontre a data da atividade e a pe_description das instalações com o nome 'STREET CHURROS' e com uma pontuação inferior a 95 pontos.
Tabela: los_angeles_restaurant_health_inspections

# CASE 2
Escreva uma consulta que calcule a diferença entre os maiores salários encontrados nos departamentos de marketing e engenharia. Exiba apenas a diferença absoluta entre os salários.
Tabelas: db_employee, db_dept

# CASE 3
Encontre os detalhes de cada cliente, independentemente de o cliente ter feito um pedido. Exiba o primeiro nome, o sobrenome e a cidade do cliente junto com os detalhes do pedido. Ordene os registros com base no primeiro nome do cliente e nos detalhes do pedido em ordem ascendente.
Tabelas: customers, orders

# CASE 4
Você recebeu um conjunto de dados que fornece o número de usuários ativos por dia por conta premium. Uma conta premium terá uma entrada para cada dia em que for premium. No entanto, uma conta premium pode ser temporariamente descontada e considerada não paga, o que é indicado por um valor de 0 na coluna final_price para um determinado dia. Descubra quantas contas premium pagas em um determinado dia ainda são premium e pagas 7 dias depois. Exiba a data, o número de contas premium e pagas naquele dia, e o número de quantas dessas contas ainda são premium e pagas 7 dias depois. Como você só tem dados para um período de 14 dias, inclua apenas as primeiras 7 datas disponíveis no resultado.
Tabela: premium_accounts_by_day
premium_accounts_by_day

# CASE 5
Encontre a taxa de retenção mensal de usuários para cada conta separadamente para dezembro de 2020 e janeiro de 2021. A taxa de retenção é a porcentagem de usuários ativos que uma conta retém durante um determinado período de tempo. Neste caso, assuma que o usuário é retido se ele/ela permanecer usando o aplicativo em qualquer mês futuro. Por exemplo, se um usuário esteve ativo em dezembro de 2020 e tem atividade em qualquer mês futuro, considere-o retido para dezembro. Você pode assumir que todas as contas estão presentes em dezembro de 2020 e janeiro de 2021. Sua saída deve conter o ID da conta e a taxa de retenção de janeiro de 2021 dividida pela taxa de retenção de dezembro de 2020. 
Tabela: sf_events

# CASE 6
Selecione o client_id mais popular com base na contagem do número de usuários que têm pelo menos 50% de seus eventos da seguinte lista: 'video call received', 'video call sent', 'voice call received', 'voice call sent'.
Tabela: fact_events

## Pré-requisitos

Antes de começar, você precisará ter o docker instalado na sua máquina:

- [Docker](https://docs.docker.com/get-docker/)

# Requisitos

- Greenlet
- Numpy
- Pandas
- Psycopg2-binary
- Python-dateutil
- Pytz
- Six
- SQLAlchemy
- Typing_extensions
- Tzdata

# Como executar

- Clone o repositório para sua máquina local
```
git clone git@github.com:descomplicandodados/gauge-itau-sql.git
```
- Navegue até a pasta do projeto
```
cd gauge-itau-sql
```
- Execute os comandos
```
docker build -t gauge-itau-sql .
```

```
docker run --rm gauge-itau-sql
```

# Funcionamento
O script load.py é responsável por criar as tabelas dentro do banco de dados, o scritp cases_sql.py é responsável por executar as querys e salvar o resultado delas localmente no formato CSV atendendo cada um dos Cases do teste.