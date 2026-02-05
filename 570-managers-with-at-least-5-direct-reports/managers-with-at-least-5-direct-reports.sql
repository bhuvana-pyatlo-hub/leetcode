# Write your MySQL query statement below
select e.name
from Employee as e
join
(
    select managerId 
    from Employee
    group by managerId
    having count(*)>=5
) as t
on e.id=t.managerId
