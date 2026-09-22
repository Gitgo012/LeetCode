# Write your MySQL query statement below
#self join
select distinct(w1.id) 
from Weather w1 
join Weather w2 
on w1.temperature>w2.temperature 
and w1.recordDate=DATE_ADD(w2.recordDate, INTERVAL 1 DAY);