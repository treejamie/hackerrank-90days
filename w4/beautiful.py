import sys



def isBeautiful(left, remaining, maybe_beautiful):
    """
    returns True if a number is beatiful
    """
    # base case - remaining is now empty
    if len(remaining) == 0:
        return maybe_beautiful

    # next to the head is the neck
    right = remaining.pop(0)

    # if left  + 1 == right, it is beautiful
    if left + 1 == right:
        maybe_beautiful = True
        return isBeautiful(right, remaining, maybe_beautiful)
    
    # base case - number is fugly
    else:
        # nope, return nope
        return False


def slicer(s, pattern):
    """given a string and a pattern return a list of integers sliced up into the pattern"""
    return [
        int(
            s[ p[0] :p[1] ]
        ) for p in pattern
    ]


def buildslice(strategy, i=0, slices=None):
    # make slices a local list
    if slices is None:
        slices = []

    # base case - strategy is empty
    if len(strategy) == 0:
        return slices

    # make the left and the right
    s = strategy.pop(0)
    left = i
    right = i +s 

    # append the result
    slices.append( (left, right) )

    # and now
    return buildslice(strategy, right, slices)


def whichslice():
    pass


def separateNumbers(s):
    pass

        


tests = {
    "buildslice": [
        [
            [1, 2, 2],
            [(0, 1), (1, 3), (3, 5)],
            "test one"
        ],
        [
            [1],
            [(0, 1)],
            "test one point five"
        ],
        [
            [4, 5],
            [(0, 4), (4, 9)],
            "test two"
        ],
    ],
    "slicer": [
        [
            "1234",
            [(0, 1), (1, 2), (2, 3), (3, 4)],
            [1, 2, 3, 4],
            "test one"
        ],
        [
            "10111213141516",
            [(0, 2), (2, 4), (4, 6), (6, 8), (8, 10), (10, 12), (12, 14)],
            [10, 11, 12, 13, 14, 15, 16],
            "test two"
        ],
        [
            "999910000",
            [(0, 4), (4, 9)],
            [9999, 10000],
            "test three"
        ]
    ],
    "isBeautiful": [
        [
            1, [2, 3, 4], False,
            True,
            "test one"
        ],
        [
            0, [21, 34, 44], False,
            False,
            "test one"
        ]
    ],
    "separateNumbers": [
        [
            [ '1234', '91011', '99100', '101103', '010203', '13', '1' ],
            [ ("YES",  1), ("YES", 9), ("YES", 99), ("NO",), ("NO",), ("NO",), ("NO",) ],
            "test one"
        ],
    ],
}


skips = [
    {"separateNumbers": 0}
]


for func, tests in tests.items():

    for test in tests:

        # parts
        name = test.pop()
        expected = test.pop()

        # skip things if we're skipping them
        for skip in skips:
            for f, t in skip.items():

                if f == func:
                    if t == 0 or t == name:
                        continue

                # we are not skipping, so call the function with the args
                result = locals()[func](*test)
                try:
                    assert result == expected
                    print("✅: SUCCESS ({2}) - {1} expected and {0} result".format(
                        result,
                        expected,
                        func
                    ))
                except AssertionError:
                    msg = "🛥️ FAILBOAT {3} {0} :\n\texpected: {2}\n\tresult: {1} ".format(
                        name,
                        result,
                        expected,
                        func
                    )
                    sys.exit(msg)