
select users.name as NAME, 
    sum(transactions.amount)  as BALANCE 
from users 
right join transactions on users.account = transactions.account 
group by transactions.account 
having sum(transactions.amount)>10000;