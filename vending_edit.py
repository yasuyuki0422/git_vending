print("1 自動販売機飲み物個数追加機能")
print("2 自動販売機飲み物種類追加機能")
print("3 自動販売機飲み物種類削除機能")

while True:
    a = input("メニューから選んでください（1or2or3）：")
    if a == "1":
        b = print("自動販売機飲み物個数追加機能")
        import add_quantity
        break
    elif a == "2":
        c = print("自動販売機飲み物種類追加機能")
        import add_type
        break
    else:
        d =print("自動販売機飲み物種類削除機能")
        import delete_type
        break
