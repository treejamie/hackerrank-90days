defmodule HackerRank.W1.SparseArrayTest do
  use ExUnit.Case
  alias HackerRank.Test.Helper
  alias HackerRank.W1.SparseArray
  #doctest HackerRank.W1.SparseArray


  @pattern ~w"w1/tc/7_*.txt"

  test "run the tests" do
    Helper.test_all(@pattern, &parse_args/1, &parse_expected/1 )
    |> Enum.each(fn [[strings, queries], expected] ->
      assert SparseArray.challenge(strings, queries) == expected
    end)
  end


  def parse_args(raw) do
    # get the data out of a list
    # get the strings
    [take | list] = raw
    take = String.to_integer(take)
    strings = Enum.take(list, take)

    # get the queries
    [take | list ] = Enum.drop(list, take)
    queries = Enum.take(list, String.to_integer(take))

    # done
    [strings, queries]
  end

  def parse_expected(raw) do
    # Just need to convert the list of strings to integers
    Enum.map(raw, &String.to_integer/1)
  end

end
