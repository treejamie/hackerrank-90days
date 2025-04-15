defmodule Hackerank.W1.PlusMinus do

  use ExUnit.Case
  alias Hackerrank.Tests.Helper
  alias Hackerrank.W1.PlusMinus

  defp parse_args(raw) do
    # the first arg isn't passed into the function, drop that
    [_, raw] = raw

    # convert raw from a string ints seperated by spaces
    String.split(raw, " ")
    |> Enum.map(&String.to_integer/1)
  end


  defp parse_expected(raw) do
    # in this challange the raw data is already correct - a list of floaty-strings
    raw
  end

  test "tc/1_0.txt" do
    # get the raw data from the file
    [raw_args, raw_expected] = Helper.get_args_expected("w1/tc/1_0.txt")

    # now parse them into the data we need for this challenge
    args = parse_args(raw_args)
    expected = parse_expected(raw_expected)

    # run the challenge
    result = PlusMinus.challenge(args)

    # did it match what it should?
    assert result == expected

  end
  test "tc/1_1.txt" do
    # get the raw data from the file
    [raw_args, raw_expected] = Helper.get_args_expected("w1/tc/1_1.txt")

    # now parse them into the data we need for this challenge
    args = parse_args(raw_args)
    expected = parse_expected(raw_expected)

    # run the challenge
    result = PlusMinus.challenge(args)

    # did it match what it should?
    assert result == expected

  end

  test "tc/1_2.txt" do
    # get the raw data from the file
    [raw_args, raw_expected] = Helper.get_args_expected("w1/tc/1_2.txt")

    # now parse them into the data we need for this challenge
    args = parse_args(raw_args)
    expected = parse_expected(raw_expected)

    # run the challenge
    result = PlusMinus.challenge(args)

    # did it match what it should?
    assert result == expected

  end

end
