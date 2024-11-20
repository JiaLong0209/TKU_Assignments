
USE FinanceDB;
GO

INSERT INTO Employee (name, position, hire_date)
VALUES
('Alice Johnson', 'Finance Manager', '2018-04-23'),
('Bob Smith', 'Accountant', '2018-06-15'),
('Charlie Davis', 'Financial Analyst', '2019-11-01'),
('Diana Roberts', 'Payroll Specialist', '2021-02-10'),
('Evan Wilson', 'Budget Coordinator', '2022-07-20');

INSERT INTO Expense (employee_id, amount, description, date)
VALUES
(1, 1200.50, 'Office Supplies Purchase', '2024-10-10 10:00:00'),
(2, 500.00, 'Travel Reimbursement', '2024-10-12 15:30:00'),
(3, 1500.75, 'Team Building Event', '2024-10-15 09:00:00'),
(4, 800.00, 'Conference Registration', '2024-10-16 14:45:00'),
(5, 200.00, 'Miscellaneous Expenses', '2024-10-18 11:15:00');

INSERT INTO Income (employee_id, amount, source, date, description)
VALUES
(1, 3000.00, 'Customer Payment', '2024-10-02 14:00:00', 'Quarterly Subscription Payment'),
(2, 1500.00, 'Donation', '2024-10-10 11:00:00', 'Charity Donation'),
(3, 500.00, 'Other', '2024-10-11 14:00:00', 'Tax Refund'),
(4, 7500.00, 'Customer Payment', '2024-10-11 12:00:00', 'Annual Contract Payment'),
(5, 1000.00, 'Other', '2024-10-14 13:30:00', 'Government Subsidy');

INSERT INTO Customer (name, email, phone, address)
VALUES
('GreenTech Ltd.', 'contact@greentech.com', '1234567890', '123 Green St, Springfield'),
('BlueCorp Inc.', 'info@bluecorp.com', '9876543210', '456 Blue Ave, Metropolis'),
('Skyline Solutions', 'sales@skyline.com', '5551234567', '789 Skyline Rd, Gotham'),
('Nova Enterprises', 'support@nova.com', '4445678901', '101 Nova Plaza, Star City'),
('Vertex Dynamics', 'hello@vertex.com', '3334567890', '202 Vertex Way, Central City');

INSERT INTO Invoice (customer_id, amount, date, due_date)
VALUES
(1, 3000.00, '2024-10-01 12:00:00', '2024-10-15 12:00:00'),
(2, 1500.00, '2024-10-05 09:00:00', '2024-10-20 09:00:00'),
(3, 5000.00, '2024-10-07 15:00:00', '2024-10-21 15:00:00'),
(4, 7500.00, '2024-10-08 10:00:00', '2024-10-22 10:00:00'),
(5, 2500.00, '2024-10-09 11:30:00', '2024-10-23 11:30:00');

INSERT INTO Payment (invoice_id, amount, date)
VALUES
(1, 3000.00, '2024-10-02 14:00:00'),
(2, 1000.00, '2024-10-06 16:00:00'),
(3, 5000.00, '2024-10-10 10:00:00'),
(4, 7500.00, '2024-10-11 12:00:00'),
(5, 1500.00, '2024-10-12 11:00:00');

