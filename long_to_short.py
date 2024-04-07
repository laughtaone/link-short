# このプログラムは、リンクを4文字の文字列に短縮するプログラム
# 生成される文字列はここでしか意味を持たない
# 生成できる文字列の最大個数：456973個

import random

upper_list = [chr(i) for i in range(65, 91)]    # 大文字(26字)
lower_list = [chr(i) for i in range(97, 123)]   # 小文字(26字)

# 読み込み
with open('shorted_link_db.txt') as reader:
    content = reader.read()

torima_list = content.split("\n")
short_url_list = []
original_url_list = []
for torima in torima_list:
    original_url_list.append(torima.split("@")[1])
    short_url_list.append(torima.split("@")[0])

if len(short_url_list) != len(original_url_list):
    print("データベースに不整合があります。\n開発者に連絡してください。")
    exit()
if len(short_url_list) == 456973:
    print("データベースが最大個数に達しました。\n開発者に連絡してください。")
    exit()




def ltos():
    while True:
        url = str(input("\nリンクを入力→  "))
        if url.count("http://") > 1 or url.count("https://") > 1 or url.count("www.") > 1:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!エラー!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"エラー原因：{url} はURLが2回以上ペーストされています。正しいURLを入力してください。\n")
            continue
        elif url=="cancel":
            exit()
        else:
            break

    if url not in original_url_list:
        while True:
            short_url_str = random.choice(upper_list) + random.choice(lower_list) + random.choice(upper_list) + random.choice(lower_list)   # 4文字
            if ((short_url_str).lower()).count("sex") != 1 and ((short_url_str).lower()).count("porn") != 1 and ((short_url_str).lower()).count("fuck") != 1 and short_url_str not in short_url_list:   # 不適切な文字列が含まれない＆使用済みの文字列ではない
                break


        with open('shorted_link_db.txt', 'a') as writer:
            writer.write("\n" + short_url_str + "@" + url)

        print(f"\n{url} の短縮文字列\n" + "=============================\n          " +  short_url_str + "\n=============================\n")

    else:
        url_index = original_url_list.index(url)
        print(f"\n{url} の短縮文字列(既に短縮済みのURL)\n" + "=============================\n          " +  short_url_list[url_index] + "\n=============================\n")


ltos()
