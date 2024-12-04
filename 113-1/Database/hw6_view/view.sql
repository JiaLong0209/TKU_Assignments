-- Tables:
-- Employee
-- Expense
-- Income
-- Customer
-- Invoice
-- Payment

USE FinanceDB;
GO


CREATE VIEW TotalExpensesByEmployee AS
    SELECT 
        e.id AS EmployeeID,
        e.name AS EmployeeName,
        ISNULL(SUM(exp.amount), 0) AS TotalExpenseAmount
    FROM 
        Employee e
    LEFT JOIN 
        Expense exp ON e.id = exp.employee_id
    GROUP BY 
        e.id, e.name;
GO

CREATE VIEW TotalIncomeByEmployee AS
    SELECT 
        e.id AS EmployeeID,
        e.name AS EmployeeName,
        ISNULL(SUM(inc.amount), 0) AS TotalIncomeAmount
    FROM 
        Employee e
    LEFT JOIN 
        Income inc ON e.id = inc.employee_id
    GROUP BY 
        e.id, e.name;
GO

CREATE VIEW TotalRecordsByEmployee AS
SELECT 
    e.id AS EmployeeID,
    e.name AS EmployeeName,
    ISNULL((SELECT COUNT(*) FROM Income inc WHERE inc.employee_id = e.id), 0) AS TotalIncomeCount,
    ISNULL((SELECT SUM(inc.amount) FROM Income inc WHERE inc.employee_id = e.id), 0) AS TotalIncomeAmount,
    ISNULL((SELECT COUNT(*) FROM Expense exp WHERE exp.employee_id = e.id), 0) AS TotalExpenseCount,
    ISNULL((SELECT SUM(exp.amount) FROM Expense exp WHERE exp.employee_id = e.id), 0) AS TotalExpenseAmount
FROM 
    Employee e;
GO



-- CREATE VIEW CustomerFinancialOverview AS
--     SELECT 
--         cus.id AS CustomerID,
--         cus.name AS CustomerName,
--         ISNULL(SUM(inv.amount), 0) AS TotalInvoicedAmount,
--         ISNULL(SUM(pay.amount), 0) AS TotalPaidAmount,
--         ISNULL(SUM(inv.amount), 0) - ISNULL(SUM(pay.amount), 0) AS OutstandingAmount
--     FROM 
--         Customer cus
--     LEFT JOIN 
--         Invoice inv ON cus.id = inv.customer_id
--     LEFT JOIN 
--         Payment pay ON inv.id = pay.invoice_id
--     GROUP BY 
--         cus.id, cus.name;
-- GO

-- CREATE VIEW CustomerFinancialOverview AS
--     SELECT 
--         cus.id AS CustomerID,
--         cus.name AS CustomerName,
--         ISNULL(SUM(inv.amount), 0) AS TotalInvoicedAmount,
--         ISNULL(
--             (SELECT SUM(p.amount) 
--              FROM Payment p 
--              JOIN Invoice inv_sub ON p.invoice_id = inv_sub.id 
--              WHERE inv_sub.customer_id = cus.id), 
--             0
--         ) AS TotalPaidAmount,
--         ISNULL(SUM(inv.amount), 0) - ISNULL(
--             (SELECT SUM(p.amount) 
--              FROM Payment p 
--              JOIN Invoice inv_sub ON p.invoice_id = inv_sub.id 
--              WHERE inv_sub.customer_id = cus.id), 
--             0
--         ) AS OutstandingAmount
--     FROM 
--         Customer cus
--     LEFT JOIN 
--         Invoice inv ON cus.id = inv.customer_id
--     GROUP BY 
--         cus.id, cus.name;
-- GO

CREATE VIEW CustomerFinancialOverview AS
    SELECT 
        cus.id AS CustomerID,
        cus.name AS CustomerName,
        ISNULL(SUM(inv.amount), 0) AS TotalInvoicedAmount,
        ISNULL(SUM(p.TotalPaidAmount), 0) AS TotalPaidAmount,
        ISNULL(SUM(inv.amount), 0) - ISNULL(SUM(p.TotalPaidAmount), 0) AS OutstandingAmount
    FROM 
        Customer cus
    LEFT JOIN 
        Invoice inv ON cus.id = inv.customer_id
    LEFT JOIN (
        SELECT invoice_id, SUM(amount) AS TotalPaidAmount FROM Payment GROUP BY invoice_id
    ) p ON inv.id = p.invoice_id
    GROUP BY 
        cus.id, cus.name;
GO

CREATE VIEW CustomerInvoiceStatusSummary AS
    SELECT 
        cus.id AS CustomerID,
        cus.name AS CustomerName,
        COUNT(inv.id) AS TotalInvoices,
        COUNT(CASE WHEN inv.status = 'Pending' THEN inv.id END) AS PendingInvoices,
        COUNT(CASE WHEN inv.status = 'Overdue' THEN inv.id END) AS OverdueInvoices,
        COUNT(CASE WHEN inv.status = 'Paid' THEN inv.id END) AS PaidInvoices
    FROM 
        Customer cus
    LEFT JOIN 
        Invoice inv ON cus.id = inv.customer_id
    GROUP BY 
        cus.id, cus.name;
GO

CREATE VIEW PendingInvoices AS
    SELECT 
        inv.id AS InvoiceID,
        cus.name AS CustomerName,
        inv.amount AS InvoiceAmount,
        inv.due_date AS DueDate,
        inv.status AS InvoiceStatus
    FROM 
        Invoice inv
    INNER JOIN 
        Customer cus ON inv.customer_id = cus.id
    WHERE 
        inv.status = 'Pending';
GO

CREATE VIEW OverdueInvoices AS
    SELECT 
        inv.id AS InvoiceID,
        cus.name AS CustomerName,
        inv.amount AS InvoiceAmount,
        inv.due_date AS DueDate,
        inv.status AS InvoiceStatus
    FROM 
        Invoice inv
    INNER JOIN 
        Customer cus ON inv.customer_id = cus.id
    WHERE 
        inv.status <> 'Paid' AND inv.due_date < GETDATE();
GO

CREATE VIEW PaymentDetailsByInvoice AS
    SELECT 
        inv.id AS InvoiceID,
        cus.name AS CustomerName,
        pay.id AS PaymentID,
        pay.amount AS PaymentAmount,
        pay.date AS PaymentDate
    FROM 
        Invoice inv
    INNER JOIN 
        Customer cus ON inv.customer_id = cus.id
    INNER JOIN 
        Payment pay ON inv.id = pay.invoice_id;
GO
