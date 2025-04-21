defmodule HackerRank.W1.CamelCaseTests do
  use ExUnit.Case
  alias HackerRank.Test.Helper
  alias HackerRank.W1.CamelCase
  doctest HackerRank.W1.CamelCase

  @pattern "w1/tc/5_*txt"

  @tag :unit
  test "run the tests" do
    Helper.test_all(@pattern, &parse_args/1, &parse_expected/1 )
    |> Enum.flat_map(fn [inputs, outputs] -> Enum.zip(inputs, outputs) end)
    |> Enum.each(fn {args, expected} ->
      assert CamelCase.challenge(args) == expected
    end)
  end

  def parse_args(raw), do: raw
  def parse_expected(raw), do: raw
end
