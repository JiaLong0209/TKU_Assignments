import sqlite3

conn = sqlite3.connect("test.sqlite")

# datas = [[12,'jialong', '08934234'], [15, 'xu', '325106498']]
datas = [[i, f"n_{i}", f"09-{str(i)*3}"] for i in range(100, 200)]


for i in datas:
    print(i)
    conn.execute(f"insert into contact (id, name, tel) values ({i[0]}, '{i[1]}', '{i[2]}')")


conn.commit()
conn.close()




