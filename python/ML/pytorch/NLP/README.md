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
