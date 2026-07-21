# Write your MySQL query statement below
select user_id, email
from users
where email REGEXP '^[a-zA-Z0-9_]+@[a-zA-Z]+\\.com$'
ORDER BY user_id ASC;