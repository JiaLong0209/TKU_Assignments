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

CREATE VIEW CustomerFinancialOverview AS
    SELECT 
        cus.id AS CustomerID,
        cus.name AS CustomerName,
        ISNULL(SUM(inv.amount), 0) AS TotalInvoicedAmount,
        ISNULL(SUM(pay.amount), 0) AS TotalPaidAmount,
        ISNULL(SUM(inv.amount), 0) - ISNULL(SUM(pay.amount), 0) AS OutstandingAmount
    FROM 
        Customer cus
    LEFT JOIN 
        Invoice inv ON cus.id = inv.customer_id
    LEFT JOIN 
        Payment pay ON inv.id = pay.invoice_id
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
