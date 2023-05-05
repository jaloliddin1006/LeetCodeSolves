# Write your MySQL query statement below
select name , sum(amount)  as balance 
from users 
inner join transactions on users.account = transactions.account 
group by transactions.account 
having  balance > 10000;