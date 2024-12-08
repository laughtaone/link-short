# link-short

# 概要
- 入力された任意のURLを4文字のアルファベットに短縮するPythonプログラムです。
- 「ノートやプリント上に手書きでリンクを書くのは辛い」という課題を解決するためのプライベート用プログラムです。
- ブランチ名「developer」上の`shorted_link_db.txt` に登録されているURLは、開発者が実際に短縮したURLです。これにより、開発者がこのリポジトリのブランチと4文字のアルファベットを教えるだけで、教えたいURLを簡単に共有できるようになってます。

# 仕組み
次の4つのPythonファイルをプロジェクトのディレクトリ下で各自実行することで、概要で述べた機能を実現しています：
| ファイル名            | 機能                                                | 詳細                                              |
|-----------------------|-----------------------------------------------------|---------------------------------------------------|
| `long_to_short.py`     | 任意のURL→4文字のアルファベットに変換する           | ユーザーが入力したURLを短縮し、4文字のアルファベット形式に変換します。 |
| `short_to_long.py`     | 4文字のアルファベット→登録されているURLに変換する   | 短縮されたURL（4文字のアルファベット）を入力すると、対応する元のURLを返します。 |
| `delete_link.py`       | 登録済みのリンクを削除する                          | 登録された短縮URLを削除する機能を提供します。      |
| `shorted_link_db.txt`  | 短縮URLと元URLの対応を記録するデータベースファイル   | 「4文字のアルファベット@登録したURL」という形式でURLの対応を保存します。 |


# 実行方法
次のコマンドをルートディレクトリ下で実行：
```
python3 <実行したいPythonファイル名>
```
※ `shorted_link_db.txt` はテキストファイルなので、実行してもエラーになります。
