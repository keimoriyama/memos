# elixir のーと

# 1 章

## 対話環境の起動

`iex`コマンドを叩くと起動できる

### ヘルプの引き方

`iex`コマンドで`h`を叩くとヘルプのドキュメントが開かれる

特定のモジュールのヘルプを開くには関数`h()`の引数にヘルプを見たいモジュールを入れる

例.IO モジュールのヘルプを見る

```h.ex
h(IO)
````

#### 変数の型を参照する

`i`コマンドの後に変数を指定するとその変数の情報が表示される

例:

```e.ex
iex(8)> i 4
Term
  4
Data type
  Integer
Reference modules
  Integer
Implemented protocols
  IEx.Info, Inspect, List.Chars, String.Chars
iex(9)> i "int"
Term
  "int"
Data type
  BitString
Byte size
  3
Description
  This is a string: a UTF-8 encoded binary. It's printed surrounded by
  "double quotes" because all UTF-8 encoded code points in it are printable.
Raw representation
  <<105, 110, 116>>
Reference modules
  String, :binary
Implemented protocols
  Collectable, IEx.Info, Inspect, List.Chars, String.Chars
```

### 拡張子について

`.ex`と`.exs`の 2 つがある。`.ex`はバイトコードに変換されて実行されることを意図している。`.exs`はソースレベルで解釈される。（スクリプトレベル）

例としては、アプリケーションの拡張子は`.ex`、テストファイルの拡張子は`.exs`になっている。

### コンパイルと実行

プログラムの実行

```
elixir [ファイル名]
```

`iex`の中でも実行できる

[]は c ヘルパーの戻り値で、モジュールの名前のリストが入る。

```h.ex
iex(1)> c "hello.ex"
Hello world
[]
```

## 2 章

### パターンマッチ

#### パターンマッチとは

```h.ex
iex(2)> a = 3
3
iex(3)> a + 1
4
```

これは、`a`に 3 を代入して 1 を足すという意味ではない

elixir においては`=`はマッチ演算子と言われる。

マッチ演算子においては、左辺と右辺を等しくする方法を見つければ成功になる。

#### 少し深ぼる

```h.ex
iex(5)> list = [1, 2, 3]
[1, 2, 3]
iex(6)> [a, b, c] = list
[1, 2, 3]
iex(7)> a
1
iex(8)> b
2
iex(9)> c
3
```

`=`演算子において Elixir は左辺と右辺を等しくする。

`list`は`[1,2,3]`が入っていて、それは`[a,b,c]`についてマッチできるので上のような実行結果になる。

#### やってみよう

```
iex(10)> a = [1,2,3]
[1, 2, 3]
iex(11)> a = 4
4
iex(12)> 4 = a
4
iex(13)> [a,b] = [1,2,3]
** (MatchError) no match of right hand side value: [1, 2, 3]

iex(13)> a = [[1,2,3]]
[[1, 2, 3]]
iex(14)> [a] = [[1,2,3]]
[[1, 2, 3]]
iex(15)> a
[1, 2, 3]
iex(16)> [[[a]]] = [[1,2,3]]
** (MatchError) no match of right hand side value: [[1, 2, 3]]
```

### `_`で値を無視する

```t.ex
iex(16)> [1,_,_] = [1,2,3]
[1, 2, 3]
iex(17)> [1,_,_] = [1,"dog","cat"]
[1, "dog", "cat"]
```

上の例では、1さえマッチすれば`_`によって他は無視される

### 変数の束縛は一回のみ（ただしマッチ中に限る）

一度マッチされた変数はずっとその値を保持し続ける

```
iex(18)> [a,a] = [1,1]
[1, 1]
iex(19)> a
1
# 1にマッチさせた後に、2にマッチさせようとするとエラーになる
iex(20)> [a,a] = [1,2]
** (MatchError) no match of right hand side value: [1, 2]

iex(20)> [a,a] = [3,1]
** (MatchError) no match of right hand side value: [3, 1]
```

変数は続くマッチの中で、新しい値に束縛できる

```
iex(24)> a = 1
1
iex(25)> [1, a, 3] = [1, 2, 3]
[1, 2, 3]
iex(26)> a
2
```

#### やってみよう

(2)

```
iex(29)> [a,b,a] = [1,2,3]
** (MatchError) no match of right hand side value: [1, 2, 3]

iex(29)> [a,b,a] = [1,1,2]
** (MatchError) no match of right hand side value: [1, 1, 2]

iex(29)> [a,b,a] = [1,2,1]
[1, 2, 1]
```

(3)

```
iex(33)> [a,b,a] = [1,2,3]
** (MatchError) no match of right hand side value: [1, 2, 3]

iex(33)> [a,b,a] = [1,1,2]
** (MatchError) no match of right hand side value: [1, 1, 2]

iex(33)> a = 1
1
iex(34)> ^a = 2
** (MatchError) no match of right hand side value: 2

iex(34)> ^a = 1
1
iex(35)> ^a = 2 - a
1
```

## 3章


