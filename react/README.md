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
