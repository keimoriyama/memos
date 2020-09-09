# python のメモ

## 競技関連

### ファイルを開く

`with open`を使う

`mode`の引数は以下の通り

| 引数  |        意味        |
| :---: | :----------------: |
|   r   | 読み込み専用で開く |
|   w   | 書き込み専用で開く |
|   x   |  新規作成用で開く  |

```test.py
# pathは開くファイルに対するパス
# colはリストで空白区切りでリストに一行づつ追加する
with open(path, mode = 'r') as f:
    for file_list in f:
        col.append(file_list.split())
```

### 読み込みと書き込み

|     関数     |                意味                |
| :----------: | :--------------------------------: |
|    read()    | ファイル全体を文字列として読み込む |
| readlines()  | ファイル全体をリストとして読み込む |
|  readline()  |     ファイルを一行づつ読み込む     |
|   write()    |     ファイルに文字列を書き込む     |
| writelines() |  リストの内容をファイルに書き込む  |


### 空白区切りの入力について

`1 2 3`みたいに空白区切りの入力を受け取るときの処理。

下の例では map 関数を使って入力を空白で区切ったあとに int 型にキャストしてる

```a.py
D,T,S = map(int, input(データの可視化)

matplotlibよりも簡単に可視化できるらしい.split())
```

### map 関数

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

## kaggle 関連

### pandas

[公式ドキュメント](https://pandas.pydata.org/)

#### データの概要の表示

`Pandas Profiling`を使うと便利（実行に時間がかかる場合がある）

```pd_prof.py
# モジュールのインポート
import pandas as pd
import pandas_profiling
# csvデータの読み込み
train = pd.read_csv('../input/titanic/train.csv')
# 概要の表示
train.profile_report()
```

#### 文字を特定の数字に変換する

`replace`を使って変換する。

以下の例では`data`の中の`Sex`の列の`male`と`female`を`0`と`1`に変換している

```test.py
data['Sex'].replace(['male', 'female'], [0, 1], inplace=True)
```

### 機械学習アルゴリズム

#### ロジスティック回帰

```clf.py
# モジュールのインポート
from sklearn.linear_model import LogisticRegression
# （）の中はハイパーパラメータ
# ロジスティック回帰のオブジェクトを作成
clf = LogisticRegression(penalty='l2', solver='sag', random_state=0)
# 学習する
clf.fit(X_train, y_train)
# 予測する(予測する結果はy_predに代入される)
y_pred = clf.predict(X_test)
```

### matplotlib(データの可視化)

[公式ドキュメント](https://matplotlib.org/)

#### ヒストグラムの描画

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

### seaborn(データの可視化)

matplotlib よりも簡単に可視化できるらしい

[公式ドキュメント](https://seaborn.pydata.org/)

```
import seaborn as sns
# dataには描画もとのデータを入れる
# xのデータに対してhueのデータの集計を取る
sns.countplot(x='SibSp',hue='Survived', data = train)
plt.legend(loc= 'upper right', title = 'survived')
```
