SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1

SELECT DISTINCT a.Email
FROM Person a LEFT JOIN Person b
ON a.Email = b.Email
WHERE a.ID <> b.ID
