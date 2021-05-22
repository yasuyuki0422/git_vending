import sqlite3
import sys
import os


dbname = 'edit.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('SELECT * FROM vending_info')
a = cur.fetchall()

drink_name = []
for b in a:
    print("飲み物:{} 金額:{} 個数:{}".format(b[0],b[1],b[2]))
c = cur.fetchone()

while True:
    try:
        drinks = input("飲み物を選択してください。")
        cur.execute("select * from vending_info where name = ? ", (drinks,))
        drink = cur.fetchone()
        quantity_1 = int(drink[2])
        if quantity_1 != 0:
            print("{}の在庫数は{}個です。".format(drinks, quantity_1))
            quantity_2 = int(drink[1])
            break
        else:
            print("在庫が足りません。")
            break
    except TypeError:
        print("文字で入力してください")


while True:
    try:
        count = int(input("何本購入しますか?:"))
        if quantity_1 >= count:
            someprice = quantity_2 * count
            print("合計金額は{}円になります".format(someprice))
            some_count = quantity_1 - count
            cur.execute("update vending_info set quantity = ? where name = ?",(some_count,drinks))
            conn.commit()
            break
        else:
            print("申し訳ありません。在庫切れです。")
    except ValueError:
        print("数値で入力してください")

while True:
    try:
        money = int(input("投入金額を入力してください："))
        if money < someprice:
            print("投入金額が足りません")
            totalprice_1 = someprice - money
            try:
                money2 = int(input(str(totalprice_1) + "円が不足しているためお金を入れてください："))
                if money2 == totalprice_1:
                    print(drinks + "の購入ができました！")
                    some_count = quantity_1 - count
                    break
                elif money2 < totalprice_1:
                    print("投入金額が不足しております")
                    totalprice_1 -= money2
                else:
                    print("購入できました")
                    print("お釣りは" + str(money2 - (totalprice_1) ) + "円です")
                    some_count = quantity_1 - count
                    break

            except ValueError:
                print("数値を入力してください")

        elif int(money) > someprice:
            print(drinks + "を購入しました！")
            print("お釣りは" + str(money - someprice) + "円です")
            some_count = quantity_1 - count
            break

        else:
            print(drinks + "を購入しました！")
            some_count = quantity_1 - count
            cur.execute("update vending_info set quantity = ? where name = ?",(some_count,drinks))
            break

    except ValueError:
        print("数値で入力してください")


while True:
    choice = input("購入を続けますか？YESorNO：")
    if choice == "YES":
        os.system("clear")
        break
    elif choice == "NO":
        print("ありがとうございました")
        sys.exit()
    else:
        print("YESorNOを入力してください")

conn.commit()

cur.close()
conn.close()


# 1 動作確認をする→OK

# 1 クラス化する
# 2 終わったら動作確認をする
