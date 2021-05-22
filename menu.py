print("１：自動販売機購入機能")
print("２：自動販売機編集")
print("３：自動販売機を終了")

while True:
    a = input("メニューから選んでください（１or２or３）：")
    if a == "1":
        print("自動販売機の購入機能に移ります")
        import vending_machine_class
        break
    elif a == "2":
        print("自動販売機編集に移ります")
        import vending_edit
        break
    elif a == "3":
        print("自動販売機を終了いたします。")
        print("ご利用ありがとうございました。")
        break

    else:
        print("１か２の番号を選択してください")

