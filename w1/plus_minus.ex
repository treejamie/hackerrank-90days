defmodule Hackerrank.W1.PlusMinus do
  @doc """
  The challenge function.
  """
  def ratio(list, length), do: Enum.count(list) / length

  def format(float) do
    :io_lib.format("~.6f", [float])
    |> List.to_string()
  end

  def challenge(arr) do

    # length is accessed a few times
    length = Enum.count(arr)

    # postive, negative and zero - I could have done this in a more
    # terse manner, but I think clear code is better than clever code.
    positive =
      Enum.filter(arr, &(&1 > 0))
      |> ratio(length)
      |> format()
    negative =
      Enum.filter(arr, &(&1 < 0))
      |> ratio(length)
      |> format()
    zero =
      Enum.filter(arr, &(&1 == 0))
      |> ratio(length)
      |> format()

    # the solution
    [positive, negative, zero]

    # the challenge expects to to be printed
    # Enum.each([positive, negative, zero], fn x -> IO.inspect(x) end)

  end
end
