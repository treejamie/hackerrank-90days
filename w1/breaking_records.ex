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
  @spec challenge([integer()]) :: [integer()]
  def challenge(scores) do
    # calculate the minimum and maximum records
    process_scores(scores, [], [], [])
  end

  def process_scores([current | rest], processed, min_b, max_b) do

    # get the max value in processed, if there is no value
    # add the current to procesed and recurse.
    mx = Enum.max(processed, fn -> :nil end)
    if mx == :nil do
      process_scores(rest, [current | processed], min_b, max_b)
    end

    # get the minimum value in processed, and fallback to zero
    mn = Enum.min(processed, fn -> 0 end)

    # now process everything
    cond do
      current > mx ->
        process_scores(rest, [current| processed] , min_b, [current| max_b])

      current < mn ->
        process_scores(rest, [current| processed], [ current | min_b] , max_b)

      true ->
        process_scores(rest, [current | processed] , min_b, max_b)
    end
  end

  def process_scores([], _processed, min_b, max_b) do
    [length(max_b), length(min_b)]
  end
end
