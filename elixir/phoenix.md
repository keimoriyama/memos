# Phoenixのめも

サンプルプロジェクトとして`my-app`を作りました。

## 10/21

apiを作ろう

### router.ex

ルータ用のファイル。

今回は`localhost:4000/api/test`に`get`と`post`を定義した。

`MyAppWeb.JsonController`を定義したあとに、`hello`と`res`を定義する。

`get`を受け取ると`hello`関数が発火する。

`post`を受け取ると`res`関数が発火する。

```a.ex
defmodule MyAppWeb.Router do
  use MyAppWeb, :router

# piplineで設定する
  pipeline :api do
  # jsonを受け取る設定
    plug :accepts, ["json"]
  end
  # Other scopes may use custom stacks.
  # routerにapiを適用
  scope "/api", MyAppWeb do
    pipe_through :api
    # JsonController内でhello関数を呼び出す(helloはアトム)
    # これはcontrollersの中のJsonControllerを呼び出す
    get "/test", JsonController, :hello
    post "/test", JsonController, :res
  end
end
```

```module.ex
# MyAppWebの中にJsonControllerを定義する
defmodule MyAppWeb.JsonController do
  # これはコントローラーである
  use MyAppWeb, :controller
  # _を前につけると変数を使用しないという意味になる
  def hello(conn, _params) do
    json(conn, %{
      msg: "HELLO"
    })
  end
  # postを受け取るやつ
  def res(conn, params) do
    json(conn, %{
      # paramsにJsonが入力されるのでその中のnumの値を返す
      msg: params["num"]
    })
  end
end
```