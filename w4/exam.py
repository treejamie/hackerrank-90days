import sys
from collections import Counter



def anagram(s):
    # O(n2) timed out
    # This approach is O(n)
    # base case - if len(s) is odd, return -1
    if len(s) % 2 == 1:
        return -1

    # first determine where is halfway
    half = len(s) // 2

    # split s into two lists - not sets - sets don't have duplicates
    s1 = [x for x in s[:half]]
    s2 = [x for x in s[half:]] # slicing

    # make two counters
    c1 = Counter(s1)
    c2 = Counter(s2)

    # the difference
    diff = c1 - c2

    # answer is the sum of the values
    return sum(diff.values())




tests = [
    [
        "abccde", 
        2,
        "test 1"
    ],
    # [
    #     "abc", 
    #     -1,
    #     "test 2"
    # ],
    # [
    #     "aaabbb",
    #     3,
    #     "test 3"
    # ],
    # [
    #     "asdfjoieufoa",
    #     3,
    #     "test 15a"
    # ],
    [
        "fdhlvosfpafhalll",
        5,
        "test 15b"
    ],
    # [
    #     "mvdalvkiopaufl",
    #     5,
    #     "test 15b"
    # ],
]

target = anagram

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