select e1.employee_id
from Employees as e1

where manager_id not in (
    select employee_id
    from Employees 
) and e1.salary<30000
order by e1.employee_id asc

 


