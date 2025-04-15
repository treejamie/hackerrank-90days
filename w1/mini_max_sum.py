"""
Mini Max Sum - Challenge 2 - Week 1
https://www.hackerrank.com/challenges/three-month-preparation-kit-mini-max-sum/problem
"""
from typing import List

# default to not printing
PRINT = False


def mini_max_sum(arr: List[int]) -> List[int]:
    """
    Calculates the minimum and maximum values obtainable by summing exactly
    four of five integers. Optionally prints the result as space-separated values.

    Parameters:
       arr (List[int]): A list of integers

    Returns:
        List[int]: A list of two integers
    
    Example:
        >>> mini_max_sum([1, 2, 3, 4, 5,]) 
        [10, 14]
    """

    # sort the array
    arr = sorted(arr)

    # sum a slice of min and max
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])

    # printing?
    if PRINT:
        print(f"{min_sum} {max_sum}")

    # all done, return
    return [min_sum, max_sum]
