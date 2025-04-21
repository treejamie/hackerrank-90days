defmodule HackerRank.W1.BreakingRecordsTests do
  use ExUnit.Case
  alias HackerRank.Test.Helper
  alias HackerRank.W1.BreakingRecords
  doctest HackerRank.W1.BreakingRecords

  @pattern ~w"w1/tc/4_*.txt"

  test "run the tests" do
    Helper.test_all(@pattern, &parse_args/1, &parse_expected/1 )
    |> Enum.each(fn [args, expected] ->
      assert BreakingRecords.challenge(args) == expected
    end)
  end

  def parse_args([_, raw]) do
    # now turn in to Integers
    raw |> String.split(" ") |> Enum.map(&String.to_integer/1)
  end
  def parse_expected([raw]) do
    raw |> String.split(" ") |> Enum.map(&String.to_integer/1)
  end

end
