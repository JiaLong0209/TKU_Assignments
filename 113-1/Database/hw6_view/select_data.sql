-- Tables:
-- Employee
-- Expense
-- Income
-- Customer
-- Invoice
-- Payment

USE FinanceDB;
GO

select TABLE_NAME from INFORMATION_SCHEMA.TABLES

select TABLE_NAME, COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS

select * from Employee, Expense where Employee.id = Expense.employee_id

select name "Employee Name", employee_id, amount, date, [description] 
    from Income, Employee  
    where (amount between 2000 and 10000) and (Income.employee_id = Employee.id)

select * from Customer where [address] like '%City'

select * from Customer, Invoice where Customer.id = Invoice.customer_id

select name "Customer_Name", Invoice.id "Invoice_Id", amount, date, status  
    from Customer, Invoice 
    where Customer.id = Invoice.customer_id

select Invoice.id "Invoice_Id", Payment.date, due_date, Payment.amount 
    from Invoice, Payment 
    where Invoice.id = Payment.invoice_id

select SUM(amount) "Sum of Expense" from Expense

select SUM(amount) "Sum of Income" from Income



-- delete from Employee where Employee.id > 5
-- delete from Payment where id > 0
-- delete from Invoice where id > 0
