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
        to_date(date, 'DD/MM/YYYY') >= '2021-01-01'  -- Considera qualquer atividade após dezembro
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
        WHEN users_in_december = 0 THEN 0  -- Evitar divisão por zero
        ELSE (CAST(retained_users_january AS FLOAT) / users_in_december) 
    END AS retention_rate_ratio
FROM 
    retencao;
