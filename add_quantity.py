import sqlite3

dbname = 'edit.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('SELECT * FROM vending_info')

a = cur.fetchall()

drink_name = []
for b in a:
    print("飲み物:{} 金額:{} 個数:{}".format(b[0],b[1],b[2]))

while True:
    drink = input("どの飲み物の個数を変更しますか？:")
    cur.execute("select * from vending_info where name = ? ",(drink,))
    c = cur.fetchone()
    try:
        if c == None:
            print("入力した飲み物は存在しないため、初めから入力してください。")
        else:
            count = int(input("何本追加しますか？"))
            newcount = c[2]
            new = int(count) + int(newcount)
            cur.execute("update vending_info set quantity = ? where name = ?",(new,drink))
            print("{}が{}本になりました。".format(drink,new))
            print("メニューに戻ります。")
            import menu
            break
    except ValueError:
        print("もう一度入力してください")

conn.commit()

cur.close()
conn.close()
