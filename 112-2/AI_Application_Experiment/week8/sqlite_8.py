import sqlite3

conn = sqlite3.connect("test.sqlite")

for i in conn.execute("SELECT * FROM contact where id >= 190"):
    print(i) # tuple


conn.close()


