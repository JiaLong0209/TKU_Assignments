
-- insert
USE FinanceDB2;
GO


--- Tables
INSERT INTO Employee (name, position, email, phone, address, hire_date) VALUES
('Alice Johnson', 'Finance Manager', 'alice.johnson@company.com', '123-456-7890', '123 Green St, Springfield', '2018-04-23'),
('Bob Smith', 'Accountant', 'bob.smith@company.com', '988-654-3210', '456 Blue Ave, Metropolis', '2018-06-15'),
('Charlie Davis', 'Financial Analyst', 'charlie.davis@company.com', '555-123-4567', '789 Skyline Rd, Gotham', '2019-11-01'),
('Diana Roberts', 'Payroll Specialist', 'diana.roberts@company.com', '444-567-8901', '101 Nova Plaza, Star City', '2021-02-10'),
('Evan Wilson', 'Budget Coordinator', 'evan.wilson@company.com', '777-777-7777', '202 Vertex Way, Central City', '2022-07-20'),
('Linus', 'Budget Coordinator', 'linux@company.com', '787-777-7777', '203 Vertex Way, Central City', '2022-08-19'),
('Arch Linux', 'Budget Coordinator', 'archlinux@company.com', '987-777-7777', '204 Vertex Way, Central City', '2022-09-19'),
('Garuda Linux', 'Budget Coordinator', 'archlinux2@company.com', '987-773-7777', '284 Vertex Way, Central City', '2022-09-20') ;
GO

DECLARE @i INT = 0;
WHILE @i <= 8
BEGIN
    UPDATE Employee
    SET department_id = (@i % 3)+1
    WHERE id = @i+1;
    SET @i = @i + 1;
END;
GO

INSERT INTO Department (name, budget) VALUES
('Finance', 100000),
('Development', 200000),
('Analysis', 50000);
GO

UPDATE Department SET manager_id = 1 WHERE id = 1;
UPDATE Department SET manager_id = 2 WHERE id = 2;
UPDATE Department SET manager_id = 3 WHERE id = 3;


INSERT INTO Expense (employee_id, amount, description, date)
VALUES
(1, 1200.50, 'Office Supplies Purchase', '2024-10-10 10:00:00'),
(2, 500.00, 'Travel Reimbursement', '2024-10-12 15:30:00'),
(3, 1500.75, 'Team Building Event', '2024-10-15 09:00:00'),
(4, 800.00, 'Conference Registration', '2024-10-16 14:45:00'),
(5, 200.00, 'Miscellaneous Expenses', '2024-10-18 11:15:00'),
(3, 12000.00, 'Team Building Event', '2024-10-15 09:00:00'),
(1, 50000.00, 'Office Supplies Purchase', '2024-10-12 15:30:00');
GO


INSERT INTO Income (employee_id, amount, source, date, description)
VALUES
(1, 3000.00, 'Customer Payment', '2024-10-02 14:00:00', 'Quarterly Subscription Payment'),
(2, 1500.00, 'Donation', '2024-10-10 11:00:00', 'Charity Donation'),
(3, 500.00, 'Other', '2024-10-11 14:00:00', 'Tax Refund'),
(3, 500.00, 'Other', '2024-10-11 14:00:00', 'Tax Refund'),
(4, 7500.00, 'Customer Payment', '2024-10-11 12:00:00', 'Annual Contract Payment'),
(2, 30000.00, 'Other', '2024-10-11 14:00:00', 'Tax Refund'),
(1, 60000.00, 'Donation', '2024-10-8 11:00:00', 'Charity Donation'),
(5, 1000.00, 'Other', '2024-10-14 13:30:00', 'Government Subsidy');
GO

INSERT INTO Customer (name, email, phone, address)
VALUES
('GreenTech Ltd.', 'contact@greentech.com', '1234567890', '123 Green St, Springfield'),
('BlueCorp Inc.', 'info@bluecorp.com', '9876543210', '456 Blue Ave, Metropolis'),
('Skyline Solutions', 'sales@skyline.com', '5551234567', '789 Skyline Rd, Gotham'),
('Nova Enterprises', 'support@nova.com', '4445678901', '101 Nova Plaza, Star City'),
('Linus', 'ILoveLinux@linux.com', '7777777777', '106 Nova Plaza, Star City'),
('Neovim', 'ILoveNeovim@nvim.com', '6666666666', '99 Nova Plaza, Star City'),
('Vertex Dynamics', 'hello@vertex.com', '3334567890', '202 Vertex Way, Central City');
GO

INSERT INTO Invoice (customer_id, amount, date, due_date)
VALUES
(1, 3000.00, '2024-10-01 12:00:00', '2024-10-15 12:00:00'),
(2, 1500.00, '2024-10-05 09:00:00', '2024-10-20 09:00:00'),
(3, 5000.00, '2024-10-07 15:00:00', '2024-10-21 15:00:00'),
(4, 7500.00, '2024-10-08 10:00:00', '2024-10-22 10:00:00'),
(5, 2500.00, '2024-10-09 11:30:00', '2024-10-23 11:30:00'),
(1, 15000.00, '2024-10-11 10:00:00', '2024-10-30 10:00:00'),
(3, 11000.00, '2024-10-12 15:00:00', '2024-10-21 15:00:00');
GO

INSERT INTO Payment (invoice_id, amount, date)
VALUES
(1, 3000.00, '2024-10-02 14:00:00'),
(2, 1000.00, '2024-10-06 16:00:00'),
(3, 5000.00, '2024-10-10 10:00:00'),
(4, 7500.00, '2024-10-11 12:00:00'),
(6, 5000.00, '2024-10-10 10:00:00'),
(6, 8000.00, '2024-10-10 10:00:00'),
(5, 1500.00, '2024-10-12 11:00:00');
GO

INSERT INTO Invoice (customer_id, amount, date, due_date)
VALUES
(3, 30000.00, '2024-10-13 15:00:00', '2024-10-21 15:00:00'),
(5, 12000.00, '2024-10-13 15:00:00', '2025-9-21 15:00:00');
GO



INSERT INTO Payment (invoice_id, amount, date)
VALUES
(8, 23000.00, '2024-11-02 14:00:00'),
(3, 4000.00, '2024-10-02 14:00:00'),
(9, 10000.00, '2024-11-02 14:00:00'),
(9, 1000.00, '2024-12-02 14:00:00');
GO


---
