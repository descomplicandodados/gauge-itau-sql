from sqlalchemy import create_engine
import pandas as pd

# Configurações de conexão
DATABASE_URL = "postgresql://admin:admin@db:5432/mydatabase"

# Criar o motor de conexão
engine = create_engine(DATABASE_URL)

# Dicionário para armazenar os nomes dos DataFrames e suas respectivas consultas
queries = {
    "case1": """
        SELECT activity_date, pe_description
        FROM public.los_angeles_restaurant_health_inspections
        WHERE facility_name = 'STREET CHURROS' AND score < 95;
    """,
    "case2": """
        SELECT 
            ABS(
                (SELECT MAX(salary) 
                 FROM db_employee 
                 WHERE department_id = (SELECT id FROM db_dept WHERE department = 'marketing')
                ) - 
                (SELECT MAX(salary) 
                 FROM db_employee 
                 WHERE department_id = (SELECT id FROM db_dept WHERE department = 'engineering')
                )
            ) AS salary_difference;
    """,
    "case3": """
        SELECT 
            c.first_name, 
            c.last_name, 
            c.city, 
            o.order_date, 
            o.order_details, 
            o.total_order_cost
        FROM 
            customers c
        LEFT JOIN 
            orders o ON c.id = o.cust_id
        ORDER BY 
            c.first_name ASC, 
            o.order_details ASC;
    """,
    "case4": """
        WITH contas_ativas AS (
            SELECT 
                to_date(entry_date, 'DD/MM/YYYY') AS entry_date,
                account_id,
                final_price
            FROM 
                premium_accounts_by_day
            WHERE 
                final_price > 0
        ),
        primeiros_7_dias AS (
            SELECT DISTINCT 
                to_date(entry_date, 'DD/MM/YYYY') AS entry_date
            FROM 
                premium_accounts_by_day
            ORDER BY 
                entry_date
            LIMIT 7
        )
        SELECT 
            f.entry_date,
            COUNT(DISTINCT a.account_id) AS contas_ativas_pagas,
            COUNT(DISTINCT a2.account_id) AS contas_ativas_pagas_7_dias_depois
        FROM 
            primeiros_7_dias f
        LEFT JOIN 
            contas_ativas a ON f.entry_date = a.entry_date
        LEFT JOIN 
            contas_ativas a2 ON a.account_id = a2.account_id 
                            AND a2.entry_date = (f.entry_date + INTERVAL '7 days')
        GROUP BY 
            f.entry_date
        ORDER BY 
            f.entry_date;
    """,
    "case5": """
        WITH usuarios_ativos_dezembro AS (
            SELECT 
                account_id,
                user_id
            FROM 
                sf_events
            WHERE 
                to_date(date, 'DD/MM/YYYY') >= '2020-12-01' 
                AND to_date(date, 'DD/MM/YYYY') < '2021-01-01'
        ),
        usuarios_ativos_futuro AS (
            SELECT 
                DISTINCT account_id,
                user_id
            FROM 
                sf_events
            WHERE 
                to_date(date, 'DD/MM/YYYY') >= '2021-01-01'
        ),
        retencao AS (
            SELECT 
                d.account_id,
                COUNT(DISTINCT d.user_id) AS users_in_december,
                COUNT(DISTINCT f.user_id) AS retained_users_january
            FROM 
                usuarios_ativos_dezembro d
            LEFT JOIN 
                usuarios_ativos_futuro f ON d.account_id = f.account_id AND d.user_id = f.user_id
            GROUP BY 
                d.account_id
        )
        SELECT 
            account_id,
            CASE 
                WHEN users_in_december = 0 THEN 0
                ELSE (CAST(retained_users_january AS FLOAT) / users_in_december) 
            END AS retention_rate_ratio
        FROM 
            retencao;
    """,
    "case6": """
        WITH contagen_eventos AS (
            SELECT 
                user_id,
                client_id,
                COUNT(*) AS total_events,
                SUM(CASE WHEN event_type IN ('video call received', 'video call sent', 'voice call received', 'voice call sent') THEN 1 ELSE 0 END) AS eventos_esperados
            FROM 
                fact_events
            GROUP BY 
                user_id, client_id
        ),
        usuarios_qualificados AS (
            SELECT 
                client_id,
                user_id
            FROM 
                contagen_eventos
            WHERE 
                eventos_esperados >= total_events * 0.5
        )
        SELECT 
            client_id,
            COUNT(DISTINCT user_id) AS user_count
        FROM 
            usuarios_qualificados
        GROUP BY 
            client_id
        ORDER BY 
            user_count DESC
        LIMIT 1;
    """
}

# Executar as consultas e salvar os resultados em arquivos CSV
for case_name, query in queries.items():
    try:
        with engine.connect() as connection:
            results = pd.read_sql(query, connection)
            # Salvar os resultados em um arquivo CSV
            results.to_csv(f"{case_name}.csv", index=False)
            print(f"Resultados de {case_name} salvos em {case_name}.csv")

    except Exception as e:
        print(f"Erro ao executar a consulta {case_name}: {e}")
