# 学習データの分割をして学習する

複数回、データセットの分割の方法を変化させて学習させる。（train と valid データの分割の場所を変える）

データセットを分割するときには、課題設定やデータの特徴を意識するのが重要。Kfold では何も考慮しない。

気をつけること

- データセット内に時系列性はないか

- データセット内にグループが存在しないか

## KFold

```a.py
from sklearn.model_selection import KFold

y_preds = []
models = []
oof_train = np.zeros(((len(X_train),)))
# n_splitsで分割数を指定する（今回は５）
cv = KFold(n_splits=5, shuffle=True, random_state = 0)
categorical_features = ['Embarked', 'Pclass', 'Sex']

params = {
    'objective':'binary',
    'max_bin': 427,
    'learning_late': 0.05,
    'num_leaves' : 79
}

for fold_id, (train_index, valid_index) in enumerate(cv.split(X_train)):
    X_tr = X_train.loc[train_index, :]
    X_val = X_train.loc[valid_index,:]
    y_tr = y_train[train_index]
    y_val = y_valid[valid_index]

    lgb_train = lgb.Dataset(X_tr, y_tr,
                       categorical_feature=categorical_features)
    lgb_eval = lgb.Dataset(X_val, y_val, reference = lgb_train,
                      categorical_feature = categorical_features)

    model = lgb.train(params, lgb_train,
                 valid_sets=[lgb_train, lgb_eval],
                 verbose_eval = 10,
                 num_boost_round=10000,
                 early_stopping_rounds=10)
    # 学習に使われなかったfoldのことをout of fold(oof)という。oofに対する予測結果をoof_trainに格納する
    oof_train[valid_index] = \
    model.predict(X_val, num_iteration=model.best_iteration)
    y_pred = model.predict(X_test, num_iteration=model.best_iteration)

    y_preds.append(y_pred)
    models.append(model)
```

# 機械学習アルゴリズム

## ロジスティック回帰

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

## ランダムフォレスト

`n_estimators`は木の数

`max_depth`は木の深さ

```forest.py
# モジュールのインポート
from sklearn.ensemble import RandomForestClassifier
# オブジェクトの作成
clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state = 0)
```