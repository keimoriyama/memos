# 学習データの分割をして学習する

複数回、データセットの分割の方法を変化させて学習させる。（train と valid データの分割の場所を変える）

データセットを分割するときには、課題設定やデータの特徴を意識するのが重要。Kfold では何も考慮しない。

気をつけること

- データセット内に時系列性はないか

- データセット内にグループが存在しないか

## sklearn.model_selection

### train_test_split

リストの中身を割合に応じてテストデータと開発データに分割する

```a.py
from sklearn.model_selection import train_test_split
# 開発データと訓練データを7:3に分ける
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 0)
```

### Kfold

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
    
    # lightBGMの訓練
    lgb_train = lgb.Dataset(X_tr, y_tr,
                       categorical_feature=categorical_features)
    lgb_eval = lgb.Dataset(X_val, y_val, 
                            reference = lgb_train,
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

## sklearn.preprocessing

### StandardScaler

データを正規化する

```a.py
from sklearn.preprocessing import StandardScaler
# オブジェクトの生成
sc = StandardScaler()
# モデルを作成する
sc.fit(X_train)
# 正規化する
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
```

# 機械学習アルゴリズム

## sklearn.linear_model

### Perceptron

パーセプトロンのアルゴリズム

```a.py
from sklearn.linear_model import Perceptron
# オブジェクトを作る
ppn = Perceptron(eta0=0.1, random_state=0, shuffle=True)
# データに適合させる
ppn.fit(X_train_std, y_train)
```

### LogisticRegression

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

## sklearn.ensemble

### RandomForestClassifier

`n_estimators`は木の数

`max_depth`は木の深さ

```forest.py
# モジュールのインポート
from sklearn.ensemble import RandomForestClassifier
# オブジェクトの作成
clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state = 0)
```

## skelarn.metrics

### accuracy_score

モデルの性能指標の一つで正解率を計算してくれる

```a.py
from sklearn.metrics import accuracy_score
# y_testは正解データ、y_predはモデルの予測データ
# accuracy_score(y_test, y_pred)で正解率の計算
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))
```