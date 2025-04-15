"""
Plus Minus - Challenge 1 - Week 1
https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem 
"""
from typing import List

# default to not printing
PRINT = False


def plus_minus(arr: List[int]) -> List[str]:
    """
    We get a list of integers, we return a list of three floats.
    Each represents the ratio of positive/negative/zero numbers in arr.
    [positive_ratio, negative_ratio, zero_ratio]
    
    Parameters:
       arr (List[int]): A list of integers

    Returns:
        arr (List[str]): A list of three floats rounded to six decimal places.

    Example:
        >>> plus_minus([-4, 3, -9, 0, 4, 1])
        [0.500000, 0.333333, 0.166667]
    """
    # the total amount of items in the array
    arr_len = len(arr)

    # positive values total and then as a ratio
    p = len([x for x in arr if x > 0]) / arr_len
    fmt_p = format(p, '6f')

    # negative values
    n = len([x for x in arr if x < 0]) / arr_len
    fmt_n = format(n, '6f')

    # zero values
    z = len([x for x in arr if x == 0]) / arr_len 
    fmt_z = format(z, '6f')

    # build the answers and print them out
    answers = [fmt_p, fmt_n, fmt_z]

    # if we are printing, print
    if PRINT:
        for answer in answers:
            print(answer)

    # return the answer because reasons
    return answers
