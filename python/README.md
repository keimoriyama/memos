# python のメモ

## 競技関連

### ファイルを開く

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
D,T,S = map(int, input().split())
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

#### ランダムフォレスト

`n_estimators`は木の数

`max_depth`は木の深さ

```forest.py
# モジュールのインポート
from sklearn.ensemble import RandomForestClassifier
# オブジェクトの作成
clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state = 0)
```

#### LightGBM

LightGBM を使う前に

1. 学習用、検証用に学習用データセットを分割（過学習予防）

```a.py
# 分割するためのモジュールをインポート
from sklearn.model_selection import train_test_split
# trainとvalidに分ける
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size = 0.3, random_state = 0, stratify=y_train)
```

2. カテゴリ変数をリスト形式で宣言する

LightGBM に何をカテゴリ変数として扱ってほしいかを教えるために必要

```a.py
categorical_features = ['Embarked', 'Pclass', 'Sex']
```

```lgb.py
# モジュールのインポート
import lightgbm as lgb
# 学習データと評価データの設定
lgb_train = lgb.Dataset(X_train, y_train,
                       categorical_feature=categorical_features)
# 評価データは訓練データをreferenceにする必要がある
lgb_eval = lgb.Dataset(X_valid, y_valid, reference = lgb_train,
                      categorical_feature = categorical_features)
# 訓練用のパラメータ
params = {
    'objective':'binary'
}
# valid_setsには評価用のデータ
# verbose_evalには何回ごとに結果を出力するかを指定（early_stoppingに引っかかったときも表示してくれる
# num_boost_roundは最大実行回数
# early_stopping_roundsは精度が向上しなかった場合に打ち切る回数（今回は10回）
model = lgb.train(params, lgb_train,
                 valid_sets=[lgb_train, lgb_eval],
                 verbose_eval = 10,
                 num_boost_round=10000,
                 early_stopping_rounds=10)

y_pred = model.predict(X_test, num_iteration= model.best_iteration)
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

## 研究関連

### seq2seq などを動かす前にやること

1. 学習データの用意

   いうまでもない。テキストデータを単語別に分けてあげる。

2. 単語に対応する ID を用意して辞書にする

下の例では、0 番目のデータにパディング文字を追加し、`input_data`か`output_data`から、まだ辞書に存在しない単語を探してその単語を辞書に割り当てる

```dict.py
#　文字に対してIDを割り当てる
char2id = {}
# 長さを揃えるためのパディング文字を追加
char2id.update({"<pad>": 0})
# input_dataとoutput_dataのすべての要素に対して単語を検索する
for input_chars, output_chars in zip(input_data, output_data):
    # input_dataの単語の中で辞書にないものがあれば
    for c in input_chars:
        if not c in char2id:
            # 辞書に追加
            char2id[c] = len(char2id)
    # 同じ処理をoutput_dataに対して行う
    for c in output_chars:
        if not c in char2id:
            char2id[c] = len(char2id)
```

3. 単語を ID に変換する

```convert.py
# 変換先のリストの用意
input_id_data = []
output_id_data = []
# input_dataとoutput_dataについて単語をIDに変換した
for input_chars, output_chars in zip(input_data, output_data):
    # 変換する（内包表記で該当する単語IDに変換する）
    input_id_data.append([char2id[c] for c in input_chars])
    output_id_data.append([char2id[c] for c in output_chars])
```

4. 全体の大きさを合わせる（最も長い文字の長さに全体の大きさを合わせる感じ）

```a.py
# 系列の長さの最大値を取得。この長さに他の系列の長さをあわせる
max_in_len = 0
max_out_len = 0
for input_d, out_d in zip(input_id_data, output_id_data):
    #パディングするためのリストを一時的に取っておく
    index_datasets_in_tmp.append(input_d)
    index_datasets_out_tmp.append(out_d)
    # 長さの最大値の計算(入力、出力それぞれについて計算する)
    if max_in_len < len(input_d):
        max_in_len = len(input_d)
    if max_out_len < len(out_d):
        max_out_len = len(out_d)

# 系列の長さを揃えるために短い系列にパディングを追加
index_datasets_input = []
index_datasets_out = []
# tmpデータの内容について
for title in index_datasets_in_tmp:
    # 一番長い文章との差を計算して、padding文字で埋める
    for i in range(max_in_len - len(title)):
        title.insert(0, 0)  # 前パディング
    # データセットをpaddingした文字で追加する
    index_datasets_input.append(title)

for title in index_datasets_out_tmp:
    for i in range(max_out_len - len(title)):
        title.insert(0, 0)  # 前パディング
    index_datasets_out.append(title)
```

5. テストデータと訓練データに分割する

`scikit-learn`の`train_test_split`関数を使う。これはリストのデータを`train_size`の割合で分割してくれる

```split.py
train_x, test_x, train_y, test_y = train_test_split(
    index_datasets_input, index_datasets_out, train_size=0.7)
```
