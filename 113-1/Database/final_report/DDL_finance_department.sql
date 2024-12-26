-- DDL 

CREATE DATABASE FinanceDB2;
GO

USE FinanceDB2;
GO

-- ALTER TABLE Employee
-- ADD department_id INT;

-- ALTER TABLE Employee
-- ADD FOREIGN KEY (department_id) REFERENCES Department(id);


CREATE TABLE Employee (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    hire_date DATETIME,
    department_id INT NULL
);
GO

-- Create the Department table after Employee
CREATE TABLE Department (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    manager_id INT NULL,
    budget DECIMAL(30, 10) NOT NULL DEFAULT 0.0,
    FOREIGN KEY (manager_id) REFERENCES Employee(id) ON DELETE SET NULL
);
GO

-- Add the foreign key constraint for Employee
ALTER TABLE Employee
ADD CONSTRAINT FK_Employee_Department FOREIGN KEY (department_id) REFERENCES Department(id);
GO

-- Expense Table
CREATE TABLE Expense (
    id INT IDENTITY(1,1) PRIMARY KEY,
    employee_id INT,
    amount DECIMAL(30, 10) NOT NULL,
    description VARCHAR(255) DEFAULT 'General Expense',
    date DATETIME NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES Employee(id)
);
GO

-- Income Table
CREATE TABLE Income (
    id INT IDENTITY(1,1) PRIMARY KEY,
    employee_id INT,
    source NVARCHAR(50) DEFAULT 'Other',
    amount DECIMAL(30, 10) NOT NULL,
    date DATETIME NOT NULL,
    description VARCHAR(255) DEFAULT 'Income Description',
    FOREIGN KEY (employee_id) REFERENCES Employee(id)
);
GO

-- Customer Table
CREATE TABLE Customer (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL
);
GO


-- Invoice Table
CREATE TABLE Invoice (
    id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(30, 10) NOT NULL,
    date DATETIME NOT NULL,
    due_date DATETIME NOT NULL,
    status NVARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES Customer(id)
);
GO

-- Payment Table
CREATE TABLE Payment (
    id INT IDENTITY(1,1) PRIMARY KEY,
    invoice_id INT,
    amount DECIMAL(30, 10) NOT NULL,
    date DATETIME NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES Invoice(id)
);
GO