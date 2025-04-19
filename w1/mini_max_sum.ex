defmodule  Hackerrank.W1.MiniMaxSum do
  @moduledoc """
  Mini Max Sum – Challenge 2 – Week 1
  <https://www.hackerrank.com/challenges/three-month-preparation-kit-mini-max-sum/problem>
  """

  @doc """
  Calculates the minimum and maximum values obtainable by summing exactly
  four of five integers. Optionally prints the result as space-separated values.

  ## Parameters
    - `arr`: a list of integers

  ## Returns
    - a list with two integers: `[min_sum, max_sum]`

  ## Examples

      iex> mini_max_sum([1, 2, 3, 4, 5])
      [10, 14]
  """
  @spec challenge([integer()]) :: [integer()]
  def challenge(arr) do
    # sort the array
    arr = Enum.sort(arr)

    # slice the mins and sum
    [
      Enum.take(arr, 4) |> Enum.sum(),
      Enum.drop(arr, 1) |> Enum.sum()
    ]
  end

end
