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
    # keep track of the low and high scores.
    hc = [] # note: final high count is this list length
    lc = [] # note: final low count is the count of this list

    # so that we can keep track of the things processes
    processed = []

    # iterate over the scores
    for s in scores:
        # max min are functions of what is processed
        try:
            _mx = max(processed)
        except ValueError:
            # zero is not class as a high score so if the score
            # was zero, count it as processed and continue on.
            processed.append(s)
            continue

        try:
            _mn = min(processed)
        except ValueError:
            _mn = 0

        # count the highs and lows
        if s > _mx:
            hc.append(s)

        if s < _mn:
            lc.append(s)
        
        # value was processesed, so append it
        processed.append(s)


    # done, return the count
    return [
        len(hc),
        len(lc)
    ]