# Write your MySQL query statement below
select d.name as Department, e.name as Employee, e.salary as Salary
from Employee as e
join Department as d
on e.departmentId =d.id
join(
    select departmentId, max(salary) as max_salary
    from employee
    group by departmentId 
) m
on m.departmentId=e.departmentId
where e.salary=max_salary
