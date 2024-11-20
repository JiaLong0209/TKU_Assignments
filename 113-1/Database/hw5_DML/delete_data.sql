
USE FinanceDB;
GO

-- Employee
-- Expense
-- Income
-- Customer
-- Invoice
-- Payment

select * from Employee, Expense where Employee.id = Expense.employee_id

-- delete from Employee where Employee.id > 5
