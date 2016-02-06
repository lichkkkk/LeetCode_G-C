SELECT E.Name
FROM Employee E LEFT JOIN Employee M
ON E.ManagerID = M.ID
WHERE E.Salary > M.Salary
