
# LightGBM

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
