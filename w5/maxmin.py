"""
You will be given a list of integers ($arr) and a single integer $k.

Create sublists of length $k from elements of $arr such that unfairness is minimised.

unfairness of a sublist ($x) is calculated as max($x) - min($x)

"""
import sys


def maxMin(k: int, arr: list[int]) -> int:
    """
    You don't need to calculate all the permutations.

    Sorting the array list is enough so that the values are optimised
    to remove the need for calculating max(x) - min(x). This uses python
    internal timsort which is O(n log n).  The loop is O(n), which makes
    the sort the most intensive complexity.

    So we have an O(n log(n)) complexity.
    
    """

    # sort it - O(n log(n)) - this is the "cheat"
    arr.sort()

    # now that it is sorted make an initial calculation
    maximally_fair = arr[k - 1] - arr[0]

    # and now iterate over the rest of the arr
    for i in range(1, len(arr) - k + 1):

        # calculate this unfairness
        unfairness  = arr[i + k - 1] - arr[i]

        # set the maximally_fair value if unfairness is less than current maximally fair
        if unfairness < maximally_fair:
            maximally_fair = unfairness
    
    # and we're done
    return maximally_fair







tests = [

    [
        3,
        [10, 100, 300, 200, 1000, 20, 30],
        20,
        "test 1"
    ],
    [
        4,
        [1, 2, 3, 4, 10, 20, 30, 40, 100, 200],
        3,
        "test 2"
    ],

 
]

target = maxMin

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