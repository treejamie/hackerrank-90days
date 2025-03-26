"""
You will be given a list of integers ($arr) and a single integer $k.

Create sublists of length $k from elements of $arr such that unfairness is minimised.

unfairness of a sublist ($x) is calculated as max($x) - min($x)

"""
import sys


def minimumNumber(n: int, password: str) -> int:
    """
    You don't need to calculate all the permutations.

    Sorting the array list is enough so that the values are optimised
    to remove the need for calculating max(x) - min(x). This uses python
    internal timsort which is O(n log n).  The loop is O(n), which makes
    the sort the most intensive complexity.

    So we have an O(n log(n)) complexity.
    
    """
    return 1







tests = [
        [
            3,
            "Ab1",
            3,
            "test 0"
        ],
        [
            11,
            "#HackerRank",
            1,
            "test 1"
        ]

 
]

target = minimumNumber

skip_tests = [
    # "test one",
    # "test two",
    # "test three"
]


for test in tests:
    # parts
    name = test.pop()
    expected = test.pop()
    result = target(*test)

    # skip tests 
    if name in skip_tests:
        continue

    # do the things
    try:
        assert result == expected
        print(f"✅: ({target.__name__}) SUCCESS - {expected} expected and {result} result")
    except AssertionError:
        msg = f"🛥️ ({target.__name__})FAILBOAT {name} :\n\texpected: {expected}\n\tresult: {result} "
        sys.exit(msg)