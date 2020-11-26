# matplotlib(データの可視化)

[公式ドキュメント](https://matplotlib.org/)

## とりあえず描画する

ランダムなデータを10個用意して、折れ線グラフで表示する

```a.py
from matplotlib import pyplot as plt
from random import randint
# x,yはともにリスト
x = list(range(10))
y = [randint(1, 100) for _ in x]

plt.plot(x, y)
plt.show()
```

## 2つのグラフを重ねて表示する

```a.py
from matplotlib import pyplot as plt
from random import randint

x = list(range(10))
y1 = [randint(1, 100) for _ in x]
y2 = [randint(1, 100) for _ in x]

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
```

# 2つのグラフを別々に表示する

縦に分ける。`add_subplot`の引数には`縦のプロットエリアの数`、`横のプロットエリアの数`、`描画するプロットエリア番号`の順番に指定する。

```a.py
from matplotlib import pyplot as plt
from random import randint

x = list(range(10))
y1 = [randint(1, 100) for _ in x]
y2 = [randint(1, 100) for _ in x]

fig = plt.figure()

ax = fig.add_subplot(2, 1, 1)
ax.plot(x, y1)
ax = fig.add_subplot(2, 1, 2)
ax.plot(x, y2)
plt.show()
```

## ヒストグラムの描画

`matploglib.pyplot'の`hist`を使う

`bins` は表示するヒストグラムの棒の数

`alpha` はヒストグラムの透明度

```plot.py
# モジュールのインポート
import matplotlib.pyplot as plt
# trainデータの中で、Survivedが0の年齢をヒストグラムに表示している
# drpona()で欠損値を除いている
# 重ねて表示するので、histを2回呼んでいる
plt.hist(train.loc[train['Survived'] == 0, 'Age'].dropna(), bins = 30,alpha = 0.5, label = '0')
# trainデータの中で、Survivedが1の年齢をヒストグラムに表示している
plt.hist(train.loc[train['Survived'] == 1, 'Age'].dropna(), bins = 30,alpha = 0.5, label = '1')
# 縦軸と横軸の設定
plt.xlabel('Age')
plt.ylabel('count')
# ラベルを貼る
plt.legend(title='Survived')
```
