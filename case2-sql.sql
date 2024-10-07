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
    ) AS salary_difference
