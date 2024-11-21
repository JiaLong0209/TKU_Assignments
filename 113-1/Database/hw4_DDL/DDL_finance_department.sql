-- DDL 

CREATE DATABASE FinanceDB;
GO

USE FinanceDB;
GO

CREATE TABLE Employee (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255) NOT NULL,
    hire_date DATETIME
    
);

CREATE TABLE Expense (
    id INT IDENTITY(1,1) PRIMARY KEY,
    employee_id INT,
    amount DECIMAL(30, 10) NOT NULL,
    description VARCHAR(255) DEFAULT 'General Expense',
    date DATETIME NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES Employee(id)
);

CREATE TABLE Income (
    id INT IDENTITY(1,1) PRIMARY KEY,
    employee_id INT,
    source NVARCHAR(50) DEFAULT 'Other',
    amount DECIMAL(30, 10) NOT NULL,
    date DATETIME NOT NULL,
    description VARCHAR(255) DEFAULT 'Income Description',
    FOREIGN KEY (employee_id) REFERENCES Employee(id)
);

CREATE TABLE Customer (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE Invoice (
    id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(30, 10) NOT NULL,
    date DATETIME NOT NULL,
    due_date DATETIME NOT NULL,
    status NVARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES Customer(id)
);

CREATE TABLE Payment (
    id INT IDENTITY(1,1) PRIMARY KEY,
    invoice_id INT,
    amount DECIMAL(30, 10) NOT NULL,
    date DATETIME NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES Invoice(id)
);


