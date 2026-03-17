-- Total Spend per Customer
SELECT Customer_ID, SUM(Amount) AS Total_Spend
FROM Transactions
GROUP BY Customer_ID;

-- High Risk Customers
SELECT *
FROM Customers
WHERE Credit_Score < 580;

-- Loan Default Rate
SELECT Loan_Status, COUNT(*) AS Count
FROM Loans
GROUP BY Loan_Status;