import sqlite3

conn = sqlite3.connect("test.sqlite")


cursor = conn.cursor()

str= """
create table if not exists table01 \
    ('id' integer primary key not null,
     'name' text not null,
     'tel' text not null)
"""
cursor.execute(str)


for i in range(2, 10):
    insert_exe = f"insert into table01 values({i},'David', '02-1253235')"
    cursor.execute(insert_exe)

conn.commit()

conn.close()


