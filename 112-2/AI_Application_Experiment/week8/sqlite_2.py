
import sqlite3

conn = sqlite3.connect("test.sqlite")

cur = conn.cursor()

str= """CREATE TABLE IF NOT EXISTS contact ('id' INTEGER PRIMARY KEY NOT NULL, 'name' TEXT NOT NULL, 'tel' TEXT NOT NULL) """

cur.execute(str)
conn.commit()
conn.close()




