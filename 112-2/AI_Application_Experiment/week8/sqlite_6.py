
import sqlite3

conn = sqlite3.connect("test.sqlite")

for i in conn.execute("SELECT * from contact"):
    print(i) # tuple


conn.close()


