# C++の基礎勉強用のメモ

競技プログラミングで使ったテクとか、c++の基本文法をつかったときにメモをかいておく

## 文法関連

### bit 演算

フラグ管理をするときとかに便利
シフト演算をつかうと i 番目の bit が立っている状態を`(1 << i)`と表す。これを使って i 番目の bit の状態を調べる

|       演算       |                                          結果                                          |
| :--------------: | :------------------------------------------------------------------------------------: |
|  bit & (1 << i)  | i 番目の bit が立っているかどうかの確認（立っている場合 1，立っていない場合 0 になる） |
| bit ｜= (1 << i) |                             bit の i 番目のフラグを立てる                              |

#### 2 進数のまま出力する

`std::bitset`を用いる。

```
// 変数bitを8bit表記で標準出力する
cout << bitset<8>(bit) << endl;
```

### vector

可変長配列的なやつ

```test.cpp
#include <vector>
// 大きさNの1次元ベクトルを用意する(型はint)
vector<int> A(N);
//i番目の要素にアクセスして0を代入する
A.at(i) = 0
```

### 二次元 vector

```vector.cpp
//宣言のしかた
vector<vector<要素の型>> 変数名(要素数1, vector<要素の型>(要素数2, 初期値));
vector<vector<要素の型>> 変数名(要素数1, vector<要素の型>(要素数2));  // 初期値を省略
// 具体例：int型の2次元配列(3×4要素の)の宣言
// 縦に３個、横に４個のベクトルの宣言
vector<vector<int>> data(3, vector<int>(4));
//(i,j)番目の要素にアクセスする
data.at(i).at(j) = 0;
```

### 範囲 for 文

vector のすべての要素に対して for 文を実行する

```for.cpp
for ( for-range-declaration : for-range-initializer ) statement
```

for-range-declaration に変数を宣言して、そこに for-range-initializer の内容が start()から end()まで代入される。

### continue

continue 以下の処理を飛ばす処理。

```continue.cpp
  for(int v = 1; v < n; v++){
    if(seen[v])continue;
    if(dfs(G, v))++count;
  }
```

### キューを使う

```que.cpp
#include <iostream>
//ライブラリのインクルード
#include <queue>

int main()
{
//キューの定義
  std::queue<int> que;

  // 要素を追加
  que.push(1);
  que.push(2);
  que.push(3);
  //que.empty()はキューが空のときに１、空じゃないときに0を返す
  while (!que.empty()) {
    std::cout << que.front() << " "; // 先頭要素を参照する
    que.pop(); // 先頭要素を削除
  }
}
```
