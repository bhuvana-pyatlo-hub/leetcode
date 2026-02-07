select u.name as name, t.balance as balance
from Users as u
join(
    select account ,sum(amount) as balance 
    from Transactions
    group by account 
    having balance>10000

) t
on u.account=t.account

