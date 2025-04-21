"""
Breaking the Records - Challenge 4, Week 1.
https://www.hackerrank.com/challenges/three-month-preparation-kit-breaking-best-and-worst-records/problem
"""
from typing import List


def breaking_records(scores: List[int]) -> List[int]:
    """
    Given a list of scores for season of games, return

    Parameters:
        scores (List[int]): A list of integeres

    Returns: 
        List[int]: Numbers of times records have been broken.
                   [0] is for breaking most points records,
                   [1] is for breaking least points records.
    
    Example:
        >>> breaking_records([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
        [4, 0]
    """
    # keep track of the counts of breaks for min score and max score
    min_b = max_b =0

    # start off with 0 for max and min counts
    mx = mn = scores[0]

    for score in scores[1:]:

        if score > mx:
            mx = score
            max_b += 1

        elif score < mn :
            mn = score
            min_b += 1

    # all done
    return [max_b, min_b]
