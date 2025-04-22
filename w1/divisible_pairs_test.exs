defmodule HackerRank.W1.DivisibleSumPairsTests do
  use ExUnit.Case
  alias HackerRank.Test.Helper
  alias HackerRank.W1.DivisibleSumPairs
  doctest HackerRank.W1.DivisibleSumPairs


  @pattern "w1/tc/6_*txt"

  test "run the tests" do
    Helper.test_all(@pattern, &parse_args/1, &parse_expected/1 )
    |> Enum.each(fn [[n, k, arr], expected] ->
       assert DivisibleSumPairs.challenge(n, k, arr) == expected
    end)
  end

  def parse_args(raw) do
    # convert raw from a string ints seperated by spaces
    [[n, k], arr] =
      raw
      |> Enum.map(&String.split/1)
      |> Enum.map(fn args -> Enum.map(args, &String.to_integer/1) end)
    [n, k, arr]
  end

  def parse_expected(raw) do
    Enum.map(raw, &String.to_integer/1) |> List.first
  end

end
