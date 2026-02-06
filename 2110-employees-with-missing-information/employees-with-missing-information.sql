SELECT e1.employee_id
FROM Employees e1
LEFT JOIN Salaries s1
ON e1.employee_id = s1.employee_id
WHERE s1.employee_id IS NULL

UNION

SELECT s2.employee_id
FROM Employees e2
RIGHT JOIN Salaries s2
ON e2.employee_id = s2.employee_id
WHERE e2.employee_id IS NULL
ORDER BY employee_id;
