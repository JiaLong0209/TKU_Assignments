import sqlite3

conn = sqlite3.connect("test.sqlite")

datas = [[12,'xu-jialong', '093400234'], [15, 'xu', '5106498']]


for i in datas:
    print(i)
    conn.execute(f"UPDATE contact SET name ='{i[1]}', tel ='{i[2]}' WHERE id='{i[0]}'")


conn.commit()
conn.close()
