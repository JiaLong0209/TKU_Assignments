
USE FinanceDB2;
GO

-- USE master ;  
-- GO  


-- USE master
-- GO

-- DROP DATABASE Finance;

-- delete from Employee where Employee.id > 5
-- delete from Payment where id > 0
-- delete from Invoice where id > 0

-- DROP table Department

TRUNCATE table Payment 
-- TRUNCATE table Invoice 

-- TRUNCATE table Customer 
DELETE from Invoice

TRUNCATE table Invoice 

DBCC CHECKIDENT ('Invoice', RESEED, 0);
DBCC CHECKIDENT ('Payment', RESEED, 0);


EXEC sp_MSForEachTable 'ALTER TABLE ? NOCHECK CONSTRAINT ALL'
EXEC sp_MSForEachTable 'TRUNCATE TABLE ?'
EXEC sp_MSForEachTable 'ALTER TABLE ? CHECK CONSTRAINT ALL'


