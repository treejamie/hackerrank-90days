defmodule Hackerank.W1.MiniMaxSumTests do

  use ExUnit.Case
  alias Hackerrank.Test.Helper
  alias Hackerrank.W1.MiniMaxSum

  @pattern "w1/tc/2_*.txt"

  test "run the tests" do
    Helper.test_all(@pattern, &parse_args/1, &parse_expected/1 )
    |> Enum.each(fn [args, expected] ->
      assert MiniMaxSum.challenge(args) == expected
    end)
  end

  def parse_args(raw) do
    # get the data out of a list
    [raw] = raw

    # now split it
    String.split(raw, " ")
    |> Enum.map(&String.to_integer/1)
  end

  def parse_expected(raw) do
    # in this challange the raw data is already correct - a list of floaty-strings
    # get the data out of a list
    [raw] = raw

    # now split it
    String.split(raw, " ")
    |> Enum.map(&String.to_integer/1)
  end

end
