WITH contas_ativas AS (
    SELECT 
        to_date(entry_date, 'DD/MM/YYYY') AS entry_date,  -- Convertendo para date
        account_id,
        final_price
    FROM 
        premium_accounts_by_day
    WHERE 
        final_price > 0
),
primeiros_7_dias AS (
    SELECT DISTINCT 
        to_date(entry_date, 'DD/MM/YYYY') AS entry_date  -- Convertendo para date
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
                        AND a2.entry_date = (f.entry_date + INTERVAL '7 days')  -- A data já está em date
GROUP BY 
    f.entry_date
ORDER BY 
    f.entry_date;
