CREATE TABLE [Employee] (
  [id] integer PRIMARY KEY IDENTITY(1, 1),
  [name] varchar(255) NOT NULL,
  [position] varchar(255) NOT NULL,
  [hire_date] date
)
GO

CREATE TABLE [Expense] (
  [id] integer PRIMARY KEY IDENTITY(1, 1),
  [employee_id] integer,
  [amount] decimal(30,10) NOT NULL,
  [description] varchar(255) DEFAULT 'General Expense',
  [date] datetime NOT NULL
)
GO

CREATE TABLE [Income] (
  [id] integer PRIMARY KEY IDENTITY(1, 1),
  [employee_id] integer,
  [source] enum(Customer Payment,Donation,Other) DEFAULT 'Other',
  [amount] decimal(30,10) NOT NULL,
  [date] datetime NOT NULL,
  [description] varchar(255) DEFAULT 'Income Description'
)
GO

CREATE TABLE [Payment] (
  [id] integer PRIMARY KEY IDENTITY(1, 1),
  [invoice_id] integer,
  [amount] decimal(30,10) NOT NULL,
  [date] datetime NOT NULL
)
GO

CREATE TABLE [Invoice] (
  [id] integer PRIMARY KEY IDENTITY(1, 1),
  [customer_id] integer,
  [amount] decimal(30,10) NOT NULL,
  [date] datetime NOT NULL,
  [due_date] datetime NOT NULL,
  [status] enum(Pending,Paid,Overdue) DEFAULT 'Pending'
)
GO

CREATE TABLE [Customer] (
  [id] integer PRIMARY KEY IDENTITY(1, 1),
  [name] varchar(255) NOT NULL,
  [email] varchar(255) UNIQUE NOT NULL,
  [phone] varchar(20) NOT NULL,
  [address] varchar(255) NOT NULL
)
GO

EXEC sp_addextendedproperty
@name = N'Column_Description',
@value = 'foreign key',
@level0type = N'Schema', @level0name = 'dbo',
@level1type = N'Table',  @level1name = 'Expense',
@level2type = N'Column', @level2name = 'employee_id';
GO

EXEC sp_addextendedproperty
@name = N'Column_Description',
@value = 'foreign key',
@level0type = N'Schema', @level0name = 'dbo',
@level1type = N'Table',  @level1name = 'Income',
@level2type = N'Column', @level2name = 'employee_id';
GO

EXEC sp_addextendedproperty
@name = N'Column_Description',
@value = 'foreign key',
@level0type = N'Schema', @level0name = 'dbo',
@level1type = N'Table',  @level1name = 'Payment',
@level2type = N'Column', @level2name = 'invoice_id';
GO

EXEC sp_addextendedproperty
@name = N'Column_Description',
@value = 'foreign key',
@level0type = N'Schema', @level0name = 'dbo',
@level1type = N'Table',  @level1name = 'Invoice',
@level2type = N'Column', @level2name = 'customer_id';
GO

ALTER TABLE [Expense] ADD FOREIGN KEY ([employee_id]) REFERENCES [Employee] ([id])
GO

ALTER TABLE [Income] ADD FOREIGN KEY ([employee_id]) REFERENCES [Employee] ([id])
GO

ALTER TABLE [Payment] ADD FOREIGN KEY ([invoice_id]) REFERENCES [Invoice] ([id])
GO

ALTER TABLE [Invoice] ADD FOREIGN KEY ([customer_id]) REFERENCES [Customer] ([id])
GO
