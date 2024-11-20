from datetime import datetime, timedelta
import random

# Function to generate random dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Base for randomization
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

# Extend Customer_Payment_Details_Report data
extended_customer_payment_details = customer_payment_details[:]
customers = ["Alice Smith", "Bob Johnson", "Carol Williams", "David Green", "Eva Brown", "Frank Harris", "Gina White", 
             "Henry Black", "Ivy Davis", "Jake Wilson"]
statuses = ["Paid", "Partially Paid", "Unpaid"]

for i in range(4, 21):
    customer = random.choice(customers)
    invoice_id = 1000 + i
    payment_amount = round(random.uniform(500.00, 5000.00), 2)
    payment_date = random_date(start_date, end_date).strftime("%Y-%m-%d")
    payment_status = random.choice(statuses)
    extended_customer_payment_details.append([customer, str(invoice_id), str(payment_amount), payment_date, payment_status])

# Extend Expense_Report data
extended_expense_report = expense_report[:]
employees = ["John Doe", "Jane Smith", "Michael Brown", "David Johnson", "Alice Thompson", "Eve Wilson", "Franklin White"]
descriptions = ["Travel Expenses", "Office Supplies", "Marketing Campaign", "Employee Benefits", "Equipment Purchase", "Training Costs"]
expense_types = ["Capital Expense", "Operational Expense"]

for i in range(4, 21):
    employee = random.choice(employees)
    description = random.choice(descriptions)
    expense_amount = round(random.uniform(100.00, 1500.00), 2)
    expense_date = random_date(start_date, end_date).strftime("%Y-%m-%d")
    expense_type = random.choice(expense_types)
    extended_expense_report.append([employee, description, str(expense_amount), expense_date, expense_type])

# Extend Income_Report data
extended_income_report = income_report[:]
sources = ["Customer Payment", "Service Income", "Donation", "Investment Income", "Consulting Services", "Software Licenses"]

for i in range(4, 21):
    source = random.choice(sources)
    income_amount = round(random.uniform(1000.00, 10000.00), 2)
    received_date = random_date(start_date, end_date).strftime("%Y-%m-%d")
    responsible_employee = random.choice(employees)
    income_category = "Sales Income" if source == "Customer Payment" else "Other Income"
    extended_income_report.append([source, str(income_amount), received_date, responsible_employee, income_category])

# Print the data
extended_customer_payment_details, extended_expense_report, extended_income_report
