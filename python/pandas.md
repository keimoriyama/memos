
# pandas

[公式ドキュメント](https://pandas.pydata.org/)

## データの概要の表示

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

## 文字を特定の数字に変換する

`replace`を使って変換する。

以下の例では`data`の中の`Sex`の列の`male`と`female`を`0`と`1`に変換している

```test.py
data['Sex'].replace(['male', 'female'], [0, 1], inplace=True)
```