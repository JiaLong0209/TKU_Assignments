import sqlite3

conn = sqlite3.connect("test.sqlite")

for i in conn.execute("""
             SELECT * FROM contact
             WHERE name LIKE '%15%' AND tel LIKE '%11%'
              """):
    print(i)

conn.close()



