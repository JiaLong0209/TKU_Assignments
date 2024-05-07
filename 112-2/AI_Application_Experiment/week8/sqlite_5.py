
import sqlite3

conn = sqlite3.connect("test.sqlite")
for i in range(200):
    conn.execute(f"DELETE FROM contact WHERE id = {i}")
conn.commit()
conn.close()


