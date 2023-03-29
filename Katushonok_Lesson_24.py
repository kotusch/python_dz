#ДЗ на пятницу. Создайте таблицу в БД, заполните минимум 10-ю записями. Половину записей удалите (DELETE),
# вторую измените (с помощью UPDATE). Точное количество записей вы не знаете, поэтому код должен быть универсальным -
# для любого количества записей в таблице.

import sqlite3, random
conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()


cursor.execute(''' CREATE TABLE IF NOT EXISTS table_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER) ''')
cursor.execute(''' INSERT INTO table_2(col_1, col_2) VALUES (?,?) ''', (random.randint(1,2), random.randint(1,2)))
cursor.execute(''' INSERT INTO table_2(col_1, col_2) VALUES (?,?) ''', (random.randint(1,2), random.randint(1,2)))
cursor.execute(''' INSERT INTO table_2(col_1, col_2) VALUES (?,?) ''', (random.randint(1,2), random.randint(1,2)))
cursor.execute(''' INSERT INTO table_2(col_1, col_2) VALUES (?,?) ''', (random.randint(1,2), random.randint(1,2)))
cursor.execute(''' INSERT INTO table_2(col_1, col_2) VALUES (?,?) ''', (random.randint(1,2), random.randint(1,2)))
cursor.execute(''' INSERT INTO table_2(col_1, col_2) VALUES (?,?) ''', (random.randint(1,2), random.randint(1,2)))
cursor.execute(''' INSERT INTO table_2(col_1, col_2) VALUES (?,?) ''', (random.randint(1,2), random.randint(1,2)))
cursor.execute(''' INSERT INTO table_2(col_1, col_2) VALUES (?,?) ''', (random.randint(1,2), random.randint(1,2)))
cursor.execute(''' INSERT INTO table_2(col_1, col_2) VALUES (?,?) ''', (random.randint(1,2), random.randint(1,2)))
cursor.execute(''' INSERT INTO table_2(col_1, col_2) VALUES (?,?) ''', (random.randint(1,2), random.randint(1,2)))
cursor.execute(''' INSERT INTO table_2(col_1, col_2) VALUES (?,?) ''', (random.randint(1,2), random.randint(1,2)))
cursor.execute(''' INSERT INTO table_2(col_1, col_2) VALUES (?,?) ''', (random.randint(1,2), random.randint(1,2)))
conn.commit()

cursor.execute('''SELECT * FROM table_2''')
k = cursor.fetchall()

for i in k:
    l_bd = len(k)
    if i[0] - 1 < l_bd / 2:
        cursor.execute('''DELETE FROM table_2 WHERE id=?''', (i[0],))
        conn.commit()
    else:
        cursor.execute('''UPDATE table_2 SET col_1= col_1 + 2, col_2=5 WHERE id=?''', (i[0],))
        conn.commit()

cursor.execute('''SELECT * FROM table_2''')
k = cursor.fetchall()
for i in k:
    print(*i)
conn.close()
