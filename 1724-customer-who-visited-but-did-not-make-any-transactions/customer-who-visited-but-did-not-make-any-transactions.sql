select v.customer_id as customer_id,count(*) as count_no_trans
from Visits as v
left join(
    select visit_id,transaction_id
    from Transactions
    group by visit_id
) t
on t.visit_id=v.visit_id
where t.transaction_id is null and t.visit_id is null
group by v.customer_id
