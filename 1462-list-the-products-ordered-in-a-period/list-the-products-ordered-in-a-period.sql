select p.product_name as product_name, t.unit as unit
from Products as p
join
(select product_id,sum(unit) as unit
from Orders

where year(order_date) = 2020 and month(order_date) =2
group by product_id
)as t
on p.product_id=t.product_id
where t.unit>=100