"""
Sparse Arrays - Challenge 7, Week 1.
https://www.hackerrank.com/challenges/three-month-preparation-kit-sparse-arrays/problem
"""
import re
from typing import List


def sparsearray(strings: List[str], queries: List[str]) -> List[int]:
    """
    Return a list of counts for how often each query appears in the input strings.

    Parameters:
        strings (List[str]): a list of strings
        queries (List[str]): a list of queries
    
    Returns:
        List[int]: counts for how often each query appears in the input strings.
    
    Examples:
        >>> sparsearray(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab'])
        [2, 1, 0]

    """

    # somewhere to stash the results
    results = []

    # iterate
    for q in queries:

        # the regex is dynamic, so precompile it
        regex = re.compile(r'^{0}$'.format(q))

        # get the matches
        matches = [re.match(regex, s) for s in strings]

        # filter out the Nones
        result = len([m for m in matches if m is not None])

        # append to the results
        results.append(result)

    # and return the results
    return results
