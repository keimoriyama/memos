# matplotlib(データの可視化)

[公式ドキュメント](https://matplotlib.org/)

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
