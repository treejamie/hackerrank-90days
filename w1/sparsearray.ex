defmodule HackerRank.W1.SparseArray do
  @moduledoc """
  Sparse Arrays - Challenge 7, Week 1.
  <https://www.hackerrank.com/challenges/three-month-preparation-kit-sparse-arrays/problem>
  """

  @doc """
  Return a list of counts for how often each query appears in the input strings.

  ## Parameters:
      strings (list[str]): a list of strings
      queries (list[str]): a list of queries

  ## Returns:
      list[int]: counts for how often each query appears in the input strings.

  ## Example:
      iex> SparseArray.challenge(["aba", "baba", "aba", "xzxb"], ["aba", "xzxb", "ab"])
      [2, 1, 0]

  """
  @spec challenge(list(integer()), list(integer())):: list(integer)
  def challenge(strings, queries) do
    IO.inspect(strings)
    IO.inspect(queries)
    [1 ]

  end
end
