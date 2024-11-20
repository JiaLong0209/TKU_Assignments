import csv
import pandas as pd

# Sample data size 5 for each report

# Expense_Report.csv data
expense_report_data = [
    ["Employee_ID", "Expense_ID", "Expense_Amount", "Expense_Description", "Expense_Date"],
    ["E001", "EXP001", "1500.00", "Office Supplies", "2024-03-15"],
    ["E002", "EXP002", "2000.00", "Travel Expenses", "2024-04-10"],
    ["E003", "EXP003", "500.00", "Marketing Campaign", "2024-05-01"],
    ["E004", "EXP004", "1200.00", "Equipment Purchase", "2024-06-20"],
    ["E005", "EXP005", "800.00", "Employee Benefits", "2024-07-15"],
]


# Income_Report.csv data
income_report_data = [
    ["Income_Source", "Received_Date", "Employee_ID", "Income_Amount"],
    ["Customer Payment", "2024-01-15", "E001", "5000.00"],
    ["Service Income", "2024-02-20", "E002", "3000.00"],
    ["Consulting Services", "2024-03-10", "E003", "2500.00"],
    ["Donation", "2024-04-05", "E004", "1500.00"],
    ["Investment Income", "2024-05-12", "E005", "4000.00"],
]

# Customer_Payment_Details_Report.csv data
customer_payment_data = [
    ["Customer_ID", "Invoice_ID", "Payment_Amount", "Payment_Date", "Payment_Status"],
    ["C001", "INV001", "1500.00", "2024-01-10", "Paid"],
    ["C002", "INV002", "2000.00", "2024-02-15", "Partially Paid"],
    ["C003", "INV003", "1800.00", "2024-03-20", "Unpaid"],
    ["C004", "INV004", "2500.00", "2024-04-25", "Paid"],
    ["C005", "INV005", "3000.00", "2024-05-30", "Unpaid"],
]

# Saving to CSV files
with open('./Expense_Report_sample.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(expense_report_data)

with open('./Income_Report_sample.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(income_report_data)

with open('./Customer_Payment_Details_Report_sample.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(customer_payment_data)

