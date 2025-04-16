"""
Divisible Sum Pairs - Challenge 6, Week 1.
https://www.hackerrank.com/challenges/three-month-preparation-kit-divisible-sum-pairs/problem
"""
from typing import List


def divisible_sum_pairs(n: int, k: int, ar: List[int] ) -> int:
    """
    Count the number of index pairs (i, j) such that i < j and (ar[i] + ar[j]) is divisible by k.

    Note: An O(n2) solution will timeout and fail. Using a frequency map is O(n), which passes.

    Parameters:
        n (int): the length of the array `ar`
        k (int): the integer to be used as the divisor
        ar (List[int]): an array of integers
    
    Returns:
        int: the number of pairs that are divisible by K
    
    Examples:
        >>> divisible_sum_pairs(6, 5, [1, 3, 2, 6, 1, 2])
        2
    """
    # setup
    fmap = {}
    match_counts = []

    # iterate over ar
    for value in ar:
        # get the mod first
        mod = value % k

        # now get the complement, but if mod is zero, use zero instead
        comp = 0 if mod == 0 else k - mod

        # if the complement is in the fmap as a value, append the value of it to match_counts
        hit = fmap.get(comp)
        if hit is not None:
            match_counts.append(hit)

        # update the frequency map.
        fmap[mod] = fmap.get(mod, 0) + 1

    return sum(match_counts)
