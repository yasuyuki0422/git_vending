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
    delete = str(input("どの飲み物を削除しますか？:"))
    cur.execute("select * from vending_info where name = ? ",(delete,))
    c = cur.fetchone()

    if c != None:
        cur.execute("delete from vending_info where name = ?",(delete,))
        cur.execute("select * from vending_info")
        print("{}が削除されました。".format(delete,))
        print("メニューに戻ります。")
        import menu
        break
    else:
        print("選択した飲み物は存在しません。")


conn.commit()

cur.close()
conn.close()
