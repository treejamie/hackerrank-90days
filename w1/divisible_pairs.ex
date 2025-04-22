defmodule HackerRank.W1.DivisibleSumPairs do
  @moduledoc """
  Divisible Sum Pairs - Challenge 6, Week 1.
  <https://www.hackerrank.com/challenges/three-month-preparation-kit-divisible-sum-pairs/problem>
  """

  @doc """
  Count the number of (i, j) index pairs such that i < j and the sum of arr[i] + arr[j] is divisible by a given integer k.

  ## Parameters

  - _n (integer): The count of items in the supplied array (unused)
  - k (integer): the integer to be used as the divisor
  - ar (list[integers]): the array of integers to work on

  Returns:
  - integer: the number of pairs that are divisible by k

  Example:
    iex> DivisibleSumPairs.challenge(6, 5, [1, 3, 2, 6, 1, 2])
    2
  """

  @spec challenge(integer(), integer(), list(integer())) :: integer()
  def challenge(_n, k, arr) do
    # This is a recursy' thing
    count_pairs(k, arr, %{}, 0)
  end

  # Tail recursive
  defp count_pairs(_k, [],_fmap, count), do: count
  defp count_pairs(k, arr, fmap, count) do
    # get the value
    [value | rest] = arr

    # get the mod
    mod = rem(value, k)

    # get the complement or zero if mod is zero
    comp = if mod == 0, do: 0, else: k - mod

    # increment count by the frequency of the complement
    count =
      case Map.get(fmap, comp) do
        nil -> count
        hit -> count + hit
      end

    # update the frequency map
    fmap = Map.update(fmap, mod, 1, &(&1 + 1))

    # now go again
    count_pairs(k, rest, fmap, count)

  end
end
