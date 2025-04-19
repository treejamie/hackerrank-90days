defmodule HackerRank.W1.TimeConversionTests do
  use ExUnit.Case
  alias HackerRank.Test.Helper
  alias HackerRank.W1.TimeConversion

  @pattern ~w"w1/tc/3_*.txt"

  test "run the tests" do
    Helper.test_all(@pattern, &parse_args/1, &parse_expected/1 )
    |> Enum.each(fn [args, expected] ->
      assert TimeConversion.challenge(args) == expected
    end)
  end

  def parse_args([raw]), do: raw
  def parse_expected([raw]), do: raw

end
