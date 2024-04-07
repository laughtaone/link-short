# このプログラムは、long_to_short.pyによって生成された4文字の文字列を指定して、その文字列と文字列に対応するリンクをデータベースから削除するプログラム


# データベースを読み込み
with open('shorted_link_db.txt') as reader:
    content = reader.read()

# データベースを読み込み、リストに格納
torima_list = content.split("\n")
if len(torima_list)==1 and torima_list[0] == "":
    print("データベースに登録されているリンクはありません。\nプログラムを終了します。\n")
    exit()
else:
    short_url_list = []
    original_url_list = []
    for torima in torima_list:
        original_url_list.append(torima.split("@")[1])  # リンク
        short_url_list.append(torima.split("@")[0])     # 短縮文字列


def delete_link():
    print("!!!!!!!!!このプログラムは、4文字の文字列から該当するリンクを含めて、データベースから削除するプログラムです。!!!!!!!!!\n")

    while True:
        del_agree = str(input("このまま削除の作業を続ける場合は「continue」、キャンセルする場合は「cancel」を入力してください。　"))
        if del_agree == "cancel":
            print("\nキャンセルしました。\n")
            exit()
        elif del_agree == "continue":
            break
        else:
            print("!!!!!!!!!!!!!!!!エラー!!!!!!!!!!!!!!!!")
            print(f"エラー原因：「{del_agree}」は不正な入力です。\n「continue」または「cancel」を入力してください。\n")

    while True:
        while True:
            del_str = str(input("削除したい4文字の短縮文字列を入力→  "))
            if del_str in short_url_list:
                while True:
                    del_confirm = str(input(f"削除する内容は次のようになります。\n\n - 削除する短縮文字列：{del_str}\n - 削除する短縮文字列に対応するリンク：{original_url_list[short_url_list.index(del_str)]}\n\nこれで良い場合は「ok」、キャンセルする場合は「cancel」を入力してください。　"))
                    if del_confirm == "ok":
                        del_index = short_url_list.index(del_str)
                        break
                    elif del_confirm == "cancel":
                        print("\nキャンセルしました。\n")
                        break
                    else:
                        print("!!!!!!!!!!!!!!!!エラー!!!!!!!!!!!!!!!!")
                        print(f"エラー原因：「{del_confirm}」は不正な入力です。\n「ok」または「cancel」を入力してください。\n")
                if del_confirm == "ok":  # del_confirmが"ok"でループを抜けた場合、del_strのループも抜ける
                    break
            else:
                print("!!!!!!!!!!!!!!!!エラー!!!!!!!!!!!!!!!!")
                if len(del_str) == 4 and del_str not in short_url_list:
                    if del_str[0].isupper()==True and del_str[1].islower()==True and del_str[2].isupper()==True and del_str[3].islower()==True:     # 大小大小
                        print(f"エラー原因：未登録\n正しい短縮文字列を入力してください。\n")
                    else:     # 大小大小以外
                        print(f"エラー原因：フォーマットに適合していない\n正しい短縮文字列を入力してください。\n")
                elif len(del_str) != 4:
                    print(f"エラー原因：4文字でない\n4文字の正しい短縮文字列を入力してください。\n")
                else:
                    print("エラー原因：不明なエラー\n確認の上、再度入力してください。")

        with open('shorted_link_db.txt', 'w') as writer:
            for i in range(len(short_url_list)):
                if i != del_index:  # 削除するインデックス以外の場合
                    if i == 0 or writer.tell() == 0:
                        # ファイルの先頭では改行を入れない
                        writer.write(short_url_list[i] + "@" + original_url_list[i])
                    else:
                        # それ以外の場合は、改行を入れてから書き込む
                        writer.write("\n" + short_url_list[i] + "@" + original_url_list[i])

        print("\n\n\n削除が完了しました。\n")
        print(f" - 削除した短縮文字列：{del_str}")
        print(f" - 削除した短縮文字列に対応するリンク：{original_url_list[del_index]}\n")


delete_link()