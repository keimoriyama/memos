# Oputina

[公式ドキュメント](https://optuna.readthedocs.io/en/stable/index.html)

ハイパーパラメータをチューニングしてくれるライブラリ。

チューニングしたいハイパーパラメータを`trial.suggest_int`を使って最適なパラメータにする

```a.py
# optunaを用いてハイパーパラメータをチューニングするための関数
def objective(trial):
    # max_binとnum_leavesをチューニングする
    params = {
        'objective':'binary',
        # 範囲は255~500
        'max_bin':trial.suggest_int('max_bin',255,500),
        'learning_rate':0.05,
        # 範囲は32~128
        'num_leaves':trial.suggest_int('num_leaves',32,128),
    }
    # モデルを訓練する
    lgb_train = lgb.Dataset(X_train,y_train,categorical_feature = categorical_features)
    lgb_eval = lgb.Dataset(X_valid, y_valid, categorical_feature= categorical_features)
    model = lgb.train(params, lgb_train,
                        valid_sets=[lgb_train, lgb_eval],
                     verbose_eval=10,
                     num_boost_round=1000,
                     early_stopping_rounds=10)
    y_pred_valid = model.predict(X_valid,num_iteration=model.best_iteration)
    # 損失の計算（なるべく小さくしたい）
    score = log_loss(y_valid, y_pred_valid)
    return score
```

optuna オブジェクトを作って、`optimize`メソッドを使って最適化する。

```a.py
# オブジェクトの作成
study = optuna.create_study(sampler=optuna.samplers.RandomSampler(seed = 0))
# 最適化する（試行回数は40回）
study.optimize(objective, n_trials = 40)
# 結果の表示
study.best_params
```