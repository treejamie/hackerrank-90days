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
  @spec challenge([String.t()], [String.t()]) :: [integer()]
  def challenge(strings, queries) do
    queries
    |> Enum.map(fn query ->
        # r = Regex.compile!("^#{query}$")
        # Enum.count(strings, fn s -> Regex.match?(r, s) end)
        # Regexs work, but the above regex is effectively checking equality
        # So instead, just compare strings. Same thing, faster result.
        Enum.count(strings, fn s -> s == query end)
      end)
  end

end
