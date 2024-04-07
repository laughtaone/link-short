# このプログラムは、long_to_short.pyによって生成された4文字の文字列を、元のリンクに戻すプログラム

import webbrowser

# データベースを読み込み
with open('shorted_link_db.txt') as reader:
    content = reader.read()

# データベースを読み込み、リストに格納
torima_list = content.split("\n")
short_url_list = []
original_url_list = []
for torima in torima_list:
    original_url_list.append(torima.split("@")[1])  # リンク
    short_url_list.append(torima.split("@")[0])     # 短縮文字列

def stol():
    while True:
        url = str(input("短縮文字列を入力→  "))
        if url in short_url_list:
            break
        else:
            print("!!!!!!!!!!!!!!!!エラー!!!!!!!!!!!!!!!!")
            if len(url) == 4 and url not in short_url_list:
                if url[0].isupper()==True and url[1].islower()==True and url[2].isupper()==True and url[3].islower()==True:     # 大小大小
                    print(f"エラー原因：未登録\n正しい短縮文字列を入力してください。\n")
                else:     # 大小大小以外
                    print(f"エラー原因：フォーマットに適合していない\n正しい短縮文字列を入力してください。\n")
            elif len(url) != 4:
                print(f"エラー原因：4文字でない\n4文字の正しい短縮文字列を入力してください。\n")
            else:
                print("エラー原因：不明なエラー\n確認の上、再度入力してください。")

    url_index = short_url_list.index(url)
    print(f"\n{url} の元URL\n" + "==========================================================\n" +  original_url_list[url_index] + "\n==========================================================\n")

    print('デフォルトのブラウザで開きます')
    webbrowser.open(original_url_list[url_index], new=1, autoraise=True)

stol()