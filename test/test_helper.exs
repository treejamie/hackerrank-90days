defmodule Hackerrank.Tests.Helper do



  @doc """
  Load the contents of a file in a list of lines suitable
  for parsing by specific functions in each challenges module
  """
  def load_test_case(tc) do
    IO.inspect File.cwd!
    File.read!(tc)
    |> String.split("\n")
    |> Enum.split_while(&(&1 != ""))
  end

  @doc """
  get_args_expected returnsUsing the module attribute @test_cases this function will
  return a list of test cases that are not in @skip_tests
  """
  def get_args_expected(tc) do
    # get the args and the expected data - it's raw, first expected can be dropped
    # as it is a blank line that delineates args from expected data.

    tc_path = Path.join([File.cwd!, tc])

    {args, [_ | expected]} =
       File.read!(tc_path)
        |> String.split("\n")
        |> Enum.split_while(&(&1 != ""))

    # parse the args
    # args = parse_args(args)

    # parse expedted
    # expected = parse_expected(expected)

    # and done
    [args, expected]
  end


end
