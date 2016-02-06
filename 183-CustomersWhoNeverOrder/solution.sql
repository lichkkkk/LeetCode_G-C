SELECT C.Name
FROM Customers C LEFT JOIN Orders O
ON C.ID = O.CustomerID
WHERE O.ID is NULL

SELECT C.Name
FROM Customers C
WHERE C.ID NOT IN (
	SELECT CustomerID
	FROM Orders
)

SELECT C.Name
FROM Custoemrs C
WHERE NOT EXISTS (
	SELECT 1
	FROM Orders
	WHERE C.ID = Orders.CustoemrID
)
