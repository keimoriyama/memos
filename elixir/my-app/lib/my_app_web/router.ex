defmodule MyAppWeb.Router do
  use MyAppWeb, :router
# 　これはブラウザの設定
#   pipeline :browser do
#     plug :accepts, ["html"]
#     plug :fetch_session
#     plug :fetch_flash
#     plug :protect_from_forgery
#     plug :put_secure_browser_headers
#   end

# piplineで設定する
  pipeline :api do
    plug :accepts, ["json"]
  end

  # scope "/", MyAppWeb do
  #   # routerに対して設定を適用する
  #   pipe_through :browser

  #   get "/", PageController, :index
  # end

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
