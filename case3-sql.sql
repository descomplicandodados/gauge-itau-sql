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
