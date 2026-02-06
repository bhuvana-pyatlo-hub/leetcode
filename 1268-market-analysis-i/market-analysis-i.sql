select u.user_id as buyer_id ,u.join_date,coalesce(t.orders_in_2019,0) as orders_in_2019
from Users as u
left join(
    select  buyer_id,count(*) as orders_in_2019
    from Orders
    where year(order_date) =2019
    group by buyer_id
) t
on u.user_id=t.buyer_id


