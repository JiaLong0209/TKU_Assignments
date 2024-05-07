
import sqlite3

conn = sqlite3.connect("test.sqlite")

rows = conn.execute("SELECT * from contact").fetchall()
print(rows)

conn.close()


