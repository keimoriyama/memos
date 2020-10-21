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
