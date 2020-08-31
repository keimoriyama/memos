# 競技関連

よくわからんけど wa になったときには変数の有効桁数を疑うと良い

多倍長整数を使うときには、'boost'ライブラリを使うとよさげ（計算時間がかかるけど）

python で書き換えると AC できることがある

for 文できつそうなときには再帰関数を用いる方法を考える。

## アルゴリズム

### 深さ優先探索

迷路のスタートからゴールまで到達可能かどうかの判定

```dfs.cpp
//mazeは迷路の入っている変数,visitedは訪問フラグ
void dfs(int i, int j){
    //迷路の外または壁のとき
  if(i >= H || j >= W || i < 0 || j < 0 || maze[i][j] == '#')
    return;
    //すでに訪問済みのとき
  if(visited[i][j] == 1)
    return;
  visited[i][j] = 1;
  //隣接するすべての点に対して探索をおこなう
  dfs(i+1,j);
  dfs(i,j+1);
  dfs(i-1,j);
  dfs(i,j-1);
}
```

### 幅優先探索

キューを使う。

無向グラフ(重み無し)において、スタートからゴールへの最短路を求めたりできる

重みがある場合にはダイクストラ法等を使う

1. スタート地点をキューに入れる

2. キューが空になるまで以下を繰り替えす

3. キューから点を一つ取り出す

4. その点と隣接する未訪問かつグラフ内の点をキューに入れて、その点に訪問済みフラグを立てる

5. 2 に戻る

以下、サンプルプログラム。

`queue_x` と　`queue_y`は迷路のなかの点の x 座標と y 座標

`R`と`C`は迷路の端の点

```a.cpp
//キューがからになるまで
  while(!queue_x.empty() && !queue_y.empty()){
    int x,y;
    //点を一つ取り出す
    x = queue_x.front();
    y = queue_y.front();
    queue_x.pop(); queue_y.pop();
    for(int i = 0; i < 4; i++){
      //迷路の中の点のときにキューに入れる
      if(x+dx[i] >= 0 && x+dx[i] < R && y+dy[i] >= 0 && y+dy[i] < C &&
          c.at(x+dx[i]).at(y+dy[i]) == 1 && visited.at(x+dx[i]).at(y+dy[i]) == 0){
        queue_x.push(x+dx[i]);
        queue_y.push(y+dy[i]);
        //訪問済みフラグを立てる
        visited.at(x+dx[i]).at(y+dy[i]) = visited.at(x).at(y) + 1;
      }
    }
  }
```
