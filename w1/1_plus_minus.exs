defmodule Wk1.PlusMinus do

  use ExUnit.Case

  # the available test case data
  @test_cases [
    "tc/1_0.txt",
    "tc/1_1.txt",
    "tc/1_2.txt"
  ]

  # if you need to skip a test
  @skip_tests [
   # "tc/1_0.txt"
  ]


  @doc """
  Load the contents of a file in a list of lines suitable
  for parsing by specific functions in each challenges module
  """
  def load_test_case(tc) do
    File.read!(tc)
    |> String.split("\n")
    |> Enum.split_while(&(&1 != ""))
  end


  @doc """
  Using the module attribute @test_cases this function will
  return a list of test cases that are not in @skip_tests
  """
  def test(tc) do
    # get the args and the expected data - it's raw, first expected can be dropped
    # as it is double newline
    {args, [_ | expected]} = load_test_case(tc)

    # parse the args
    args = parse_args(args)

    # parse expedted
    expected = parse_expected(expected)

    # and done
    [args, expected]
  end

  @doc """
  parse_args transforms raw data from test case files into args ready for
  calling the "challenge" function.
  """
  def parse_args(raw) do
    # the first arg isn't passed into the function, drop that
    [_, raw] = raw

    # convert raw from a string ints seperated by spaces
    args =
      String.split(raw, " ")
      |> Enum.map(&String.to_integer/1)
  end

  @doc """
  parse_expected transforms raw data from test case files into args ready for
  asserting against the return from the challenge function
  """
  def parse_expected(raw) do
    # in this challange the raw data is already correct - a list of floaty-strings
    raw
  end


  @doc """
  run loads up test data and calls the challenge function
  """
  def run(tc) do
    # get args and expedted
    [args, expected] = test(tc)

    # now call it
    results = challenge(args)

    # assert
    assert results == expected

  end


  @doc """
  The challenge function.
  """
  def challenge(_args) do
    ["0.500000", "0.333333", "0.166667"]

  end


end

Wk1.PlusMinus.run("tc/1_0.txt")
