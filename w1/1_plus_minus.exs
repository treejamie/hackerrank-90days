defmodule Wk1.PlusMinus do

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
  def test() do
    # build the args and get the expected data from the test cases.
    @test_cases
    |> Enum.filter(fn test -> test not in @skip_tests end)
    |> Enum.map(&load_test_case/1)
    |> Enum.map(fn {a, b} -> {a, Enum.reject(b, &(&1 == ""))} end)
    |> Enum.map(&compare/1)
  end

  @doc """
  Each test case will have specific data structures and so parse
  needs to live in the same place as each challenge.
  """
  def parse_args(raw) do
    # get it into args and expected

    IO.inspect raw
    {raw, :args}
  end

  def run(arr) do
    IO.inspect arr
    # return this array for now
    arr
  end

  def compare(tc) do
    {args, expected } = tc

    parse_args(args)
    IO.inspect args
    IO.inspect expected
  end



end

Wk1.PlusMinus.test()
