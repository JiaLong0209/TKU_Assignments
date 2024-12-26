import pyodbc

server = 'localhost,1433'
database = 'master'  # Replace 'master' with your database name
username = 'sa'
password = 'Password1234'
driver = '{ODBC Driver 17 for SQL Server}'  # Ensure this driver is installed

try:
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    cursor = conn.cursor()
    
    # Execute a test query
    cursor.execute("SELECT Name FROM sys.Databases")
    for row in cursor.fetchall():
        print(row)
    
    conn.close()

except Exception as e:
    print(f"Error: {e}")

