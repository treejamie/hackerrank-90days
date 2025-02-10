import sys
import math


def sockMerchant(n, ar):

    # iterate over the array and make a dictionary
    socks = {}
    for x in ar:
        if x in socks:
            socks[x] += 1
        else:
            socks[x] = 1
    
    # we can now sort the dictionarys into counts pairs
    pairs = []
    for k,v in socks.items():
        pairs.append(math.floor(v / 2))

    return sum(pairs)
        





tests = [
    [
        9,
        [10, 20, 20, 10, 10, 30, 50, 10, 20],
        3,
        "test one"
    ],
    [
        10,
        [1, 1, 3, 1, 2, 1, 3, 3, 3, 3],
        4,
        "test two"
    ]
]

target = sockMerchant

for test in tests:
    name = test.pop()
    expected = test.pop()
    result = target(*test)

    try:
        assert result == expected
        print("✅: SUCCESS - {1} expected and {0} result".format(
            result,
            expected,
        ))
    except AssertionError:
        msg = "🛥️ FAILBOAT {0} :\n\texpected: {2}\n\tresult: {1} ".format(
            name,
            result,
            expected,
        )
        sys.exit(msg)
