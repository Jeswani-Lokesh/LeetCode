# Write your MySQL query statement below


-- select * from Users
-- where mail like '%@%.com';
SELECT user_id, name, mail
FROM Users
WHERE REGEXP_LIKE(
    mail,
    '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$',
    'c'
);