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
  def challenge([]), do: [0, 0]
  def challenge([first | rest]), do: process_scores(rest, first, first, 0, 0)


  defp process_scores([], _min, _max, min_b, max_b), do: [max_b, min_b]

  defp process_scores([s | rest], min, max, min_b, max_b) do
    cond do
      s > max ->
        process_scores(rest, min, s, min_b, max_b + 1)
      s < min ->
        process_scores(rest, s, max, min_b + 1, max_b)
      true ->
        process_scores(rest, min, max, min_b, max_b)
    end
  end
end
