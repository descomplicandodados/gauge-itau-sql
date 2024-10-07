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
        user_id  -- Incluindo user_id aqui
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
