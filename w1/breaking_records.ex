defmodule HackerRank.W1.BreakingRecords do
  @moduledoc """
  Breaking the Records - Challenge 4, Week 1.
  <https://www.hackerrank.com/challenges/three-month-preparation-kit-breaking-best-and-worst-records/problem>
  """
  @doc """
  Given a list of scores for a season of games, returns how many times records were broken.

  ## Parameters

    - `scores`: a list of integers representing game scores

  ## Returns

    - A two-element list:
      - `[0]` is the number of times the max score record was broken
      - `[1]` is the number of times the min score record was broken

  ## Example

      iex> breaking_records([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
      [4, 0]
  """
  @spec breaking_records([integer()]) :: [integer()]
  def challenge(scores) do
    [1,2]
  end

end
