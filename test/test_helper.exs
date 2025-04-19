defmodule HackerRank.Test.Helper do
  @moduledoc """
  A set of utilities for testing the Elixir HackerRank challenges
  """

  @doc """
  Loads and parses all test cases matching the given glob pattern.

  For each file, applies the provided argument and expected result functions,
  returning a list of {args, expected} tuples ready for testing.
  """
  def test_all(pattern, arg_fn, exp_fn) do
    Path.wildcard(pattern)
    |> Enum.map( fn tc -> get_args_expected(tc, arg_fn, exp_fn) end)
  end

  @doc """
  get_args_expected returnsUsing the module attribute @test_cases this function will
  return a list of test cases that are not in @skip_tests
  """
  def get_args_expected(tc, arg_fn, exp_fn) do
    # get the args and the expected data - it's raw, first expected can be dropped
    # as it is a blank line that delineates args from expected data.

    tc_path = Path.join([File.cwd!, tc])

    {args, [_ | expected]} =
       File.read!(tc_path)
        |> String.split("\n")
        |> Enum.split_while(&(&1 != ""))

    # parse the args
    args = arg_fn.(args)

    # parse expedted
    expected = exp_fn.(expected)

    # and done
    [args, expected]
  end

end
