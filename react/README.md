# React の学習メモです

## docker に環境を作る

1. `Dockerfile`を書く

ベースイメージは`node`を使う

```Dockerfile
FROM node:latest

WORKDIR /usr/src/app
```

2. `docker-compose.yml`を書く

```a.yml
version: "3"
services:
  node:
    build:
    # Dockerfileのディレクトリとかを指定する
      context: .
      dockerfile: Dockerfile
    # Dockerイメージの中のディレクトリを指定
    volumes:
      - ./:/usr/src/app
    # reactのプログラムの実行
    command: sh -c "cd react-sample && npm start"
    # 開放するポートの指定
    ports:
      - "3000:3000"
    # これがないとなんかアクセスできない
    stdin_open: true
```

3. コマンドを叩く

- イメージを作る

```
docker-compose build
```

`create-react-app`をインストールして、`react-sample`っていうプロジェクトを作る

```
docker-compose run --rm node sh -c “npx create-react-app react-sample"
```

コンテナを起動する

起動したときに`command`のコマンドが実行される

```
docker-compose up
```

## React とは

js のライブラリ

`コンポーネント`と呼ばれる部品で UI を組み立てる

React には色々な種類のコンポーネントがある。

以下の例では`React.Component`を使って、新しいコンポーネントの`ShoppngList`を作っている。

コンポーネントは`props`と呼ばれるパラメータを受け取り、`render`メソッドを通して、表示するビューを返す。

```test.js
// React.Componentの継承
class ShoppingList extends React.Component {
  // ここで、ビューを返す
  render() {
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}</h1>
        <ul>
          <li>Instagram</li>
          <li>WhatsApp</li>
          <li>Oculus</li>
        </ul>
      </div>
    );
  }
}
```

### データを props 経由で渡す

親コンポーネントである Board から子コンポーネントである Square に値を渡すようにする

```a.js
// Squareコンポーネント
class Square extends React.Component {
  render() {
    //propsの値を表示するようにしている
    return <button className="square">{this.props.value}</button>;
  }
}

// Boardコンポーネント
class Board extends React.Component {
  //Squareコンポーネントのpropsには引数iを設定する
  renderSquare(i) {
    return <Square value={i} />;
  }

  render() {
    // renderSquareに1を渡す
    <div>
      {this.renderSquare(1)}
    </div>
  }
}
```

## インタラクティブなコンポーネントを作る

```a.js
class Square extends React.Component {
  render() {
    return (
      // onClickを追加して、ボタンが押されたときのアクションを指定する
      <button
        className="square"
        onClick={() => {
          alert("pushed");
        }}
      >
        {this.props.value}
      </button>
    );
  }
}
```

## コンポーネントの状態の管理

`state`を指定することでコンポーネントが状態を管理することができる。

```a.js
class Square extends React.Component {
  // propsの設定（コンストラクタを使います）
  constructor(props) {
    // propsを親オブジェクトとして設定する
    super(props);
    // stateの設定（valueの初期値はnull)
    this.state = {
      value: null,
    };
  }
  render() {
    return (
      <button
        className="square"
        // ボタンが押されたときstateのvalueにXを設定する
        onClick={() => {
          this.setState({ value: "X" });
        }}
      >
      // stateの内容を表示（Nullは空白）
        {this.state.value}
      </button>
    );
  }
}
```

## state のリフトアップ

複数の子要素からデータを集めたり、2 つの子コンポーネントにデータをやりとりさせたいときには、親コンポーネントで共有の`state`を宣言する必要がある。

親コンポーネントは`props`を使うことで子に情報を渡すことができる。これで、子コンポーネント間や、親との間で同期できるようになる。

## immutability の重要性

`Board`コンポーネントの`handleClick`では、一回配列の複製を作成したあとに、その複製を編集してもとの配列に反映させた

### これを行うことの利点

- 複雑な機能が簡単に実装できる
- 変更の検出
- React の再レンダータイミングの決定
