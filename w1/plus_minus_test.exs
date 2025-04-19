defmodule Hackerank.W1.PlusMinusTest do

  use ExUnit.Case
  alias Hackerrank.Test.Helper
  alias Hackerrank.W1.PlusMinus

  @pattern "w1/tc/1_*.txt"

  test "run the tests" do
    Helper.test_all(@pattern, &parse_args/1, &parse_expected/1 )
    |> Enum.each(fn {_label, args, expected} ->
      assert PlusMinus.challenge(args) == expected
    end)
  end

  def parse_args(raw) do
    # the first arg isn't passed into the function, drop that
    [_, raw] = raw

    # convert raw from a string ints seperated by spaces
    String.split(raw, " ")
    |> Enum.map(&String.to_integer/1)
  end

  def parse_expected(raw) do
    # in this challange the raw data is already correct - a list of floaty-strings
    raw
  end

end
