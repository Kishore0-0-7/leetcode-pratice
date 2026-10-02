# Write your MySQL query statement below
select d.name as Department,e.name as Employee,e.salary 
from employee e
join department d
on e.departmentID=d.id
where (e.departmentId,e.salary) in (
    select departmentId,max(salary) from employee
    group by departmentId
);