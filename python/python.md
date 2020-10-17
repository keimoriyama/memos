# ファイルを開く

`with open`を使う

`mode`の引数は以下の通り

| 引数 |        意味        |
| :--: | :----------------: |
|  r   | 読み込み専用で開く |
|  w   | 書き込み専用で開く |
|  x   |  新規作成用で開く  |

```test.py
# pathは開くファイルに対するパス
# colはリストで空白区切りでリストに一行づつ追加する
with open(path, mode = 'r') as f:
    for file_list in f:
        col.append(file_list.split())
```

# 読み込みと書き込み

|     関数     |                意味                |
| :----------: | :--------------------------------: |
|    read()    | ファイル全体を文字列として読み込む |
| readlines()  | ファイル全体をリストとして読み込む |
|  readline()  |     ファイルを一行づつ読み込む     |
|   write()    |     ファイルに文字列を書き込む     |
| writelines() |  リストの内容をファイルに書き込む  |

# 空白区切りの入力について

`1 2 3`みたいに空白区切りの入力を受け取るときの処理。

下の例では map 関数を使って入力を空白で区切ったあとに int 型にキャストしてる

```a.py
D,T,S = map(int, input().split())
```

# map 関数

[python3.8.5 公式ドキュメント](https://docs.python.org/ja/3/library/functions.html)より

> map(function, iterable, ...)
> function を、結果を返しながら iterable の全ての要素に適用するイテレータを返します。

```
>>> i = '1 3 4 5 6'
# 文字列iを空白について分割したあと、int型に変換する処理をした。
>>> print(map(int, i.split()))
<map object at 0x1065d5d60>
# listにする
>>> print(list(map(int,i.split())))
[1, 3, 4, 5, 6]

```