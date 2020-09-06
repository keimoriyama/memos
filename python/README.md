# python のメモ

## 空白区切りの入力について

`1 2 3`みたいに空白区切りの入力を受け取るときの処理。

下の例では map 関数を使って入力を空白で区切ったあとに int 型にキャストしてる

```a.py
D,T,S = map(int, input().split())
```

## map 関数

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

## pandas

### 文字を特定の数字に変換する

`replace`を使って変換する。

以下の例では`data`の中の`Sex`の列の`male`と`female`を`0`と`1`に変換している

```test.py
data['Sex'].replace(['male', 'female'], [0, 1], inplace=True)
```
