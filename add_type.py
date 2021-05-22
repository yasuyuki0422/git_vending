import sqlite3

dbname = 'edit.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('SELECT * FROM vending_info')

a = cur.fetchall()

drink_name = []
for b in a:
    print("飲み物:{} 金額:{} 個数:{}".format(b[0],b[1],b[2]))


drink = str(input("新規で飲み物を追加してください:"))
cur.execute("select * from vending_info where name = ?",(drink,))
c = cur.fetchone()

while True:
    try:
        price = int(input("価格をいくらにしますか？"))
        break
    except ValueError:
        print("数値で入力してください。")


while True:
    try:
        count = int(input("本数をいくつにしますか？"))
        break
    except ValueError:
        print("数値で入力してください。")


cur.execute("insert into vending_info values (?,?,?)", (drink, price, count))
conn.commit()

print("{}、{}円、{}本を追加しました。".format(drink, price, count))
print("メニューに戻ります。")
import menu



conn.commit()

cur.close()
conn.close()

