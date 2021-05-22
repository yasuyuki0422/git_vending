import sqlite3

dbname = 'edit.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('INSERT INTO vending_info(name,price,quantity) values("コーラ",160,10)')
cur.execute('INSERT INTO vending_info(name,price,quantity) values("ペプシ",150,10)')
cur.execute('INSERT INTO vending_info(name,price,quantity) values("レッドブル",200,10)')
cur.execute('INSERT INTO vending_info(name,price,quantity) values("コーヒー",120,10)')

conn.commit()

cur.close()
conn.close()


