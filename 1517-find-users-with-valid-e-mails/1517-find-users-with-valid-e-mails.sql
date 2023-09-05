# Write your MySQL query statement below
SELECT *
FROM Users
WHERE mail REGEXP '^[a-zA-Z][_a-zA-Z0-9.-]*@leetcode\\.com$';