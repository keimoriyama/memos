defmodule Greeter do

    def for(name, greeting) do
        fn
        (^name) -> "#{greeting} #{name}"
        (_) -> "I dont know you"
        end
    end

end
