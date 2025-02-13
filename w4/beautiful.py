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

    # a zero could only ever be on the left because logically 1 would be next
    if right == 0:
        return False

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
    x = [
        int(
            s[ p[0] :p[1] ]
        ) for p in pattern
    ]
    return x


def buildslice(strategy, i=0, slices=None): # change the slices to an empty list and side effects creep in.
    # make slices a local list
    if slices is None:                      # If slices is a list, rather than none, then the frames point to
        slices = []                         # the same list over all function calls. Rather than get back correct
                                            # results eg ([[1]], [[1], [1,1]]) they end up getting mysteriously
                                            # appended eg ([[1], [1], [1, 1]]). Neat. The solution is to use
                                            # an immutable default value and then set the mutable version inside
                                            # the function so the list is scoped to the function. I imagine
                                            # this is the kind of thing that people complain about in certain circles.

    # base case - strategy is empty
    if len(strategy) == 0:
        return slices

    # make the left and the right
    s = strategy.pop(0)
    left = i
    right = i + s 

    # append the result
    slices.append( (left, right) )

    # and now
    return buildslice(strategy, right, slices)


def get_strategy(length):
    """
    There has to be a way to calculate this on the fly,
    perhaps I will do that, and this data can be turned
    into a data structure. For now, it is a hard coded ting'
    """
    # make sure it is an int
    length = int(length)

    # dreaming of generating this programattically
    table = {
        1: [
            [1]
        ],
        2: [
            [1, 1],
        ],
        3: [
            [1, 1, 1,],
            [1, 2]
        ],
        4: [
            [1, 1, 1, 1],
            [1, 1, 2],
            [2, 2]
        ],
        5: [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 2],
            [1, 2, 2],
            [2, 3]
        ],
        6: [
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 2],
            [1, 1, 2, 2],
            [2, 2, 2],
            [3, 3]
        ],
        7: [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 2],
            [1, 1, 1, 2, 2],
            [1, 2, 2, 2],
            [2, 2, 3],
            [3, 4],
        ],
        8: [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 2],
            [1, 1, 1, 1, 2, 2],
            [1, 1, 2, 2, 2],
            [2, 2, 2, 2],
            [4, 4],
        ],
        9: [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 2],
            [1, 1, 1, 1, 1, 2, 2],
            [1, 1, 1, 2, 2, 2],
            [1, 2, 2, 2, 2],
            [4, 5],
        ],
        10: [
            [1, 1, 1, 1, 1, 1, 1, 1, 2],
            [1, 1, 1, 1, 1, 1, 2, 2],
            [1, 1, 1, 1, 2, 2, 2],
            [1, 1, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [5, 5],
        ],
        11: [
            [1, 1, 1, 1, 1, 1, 1, 2, 2],
            [1, 1, 1, 1, 1, 2, 2, 2],
            [1, 1, 1, 2, 2, 2, 2],
            [1, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 3],
            [3, 4, 4],
            [5, 6],
        ],
        12: [
            [1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
            [1, 1, 1, 1, 2, 2, 2, 2],
            [1, 1, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3],
            [4, 4, 4],
            [6, 6],
        ],
    }
    return table[length]


def separateNumbers(s):
    # stash the results
    results = []

    # iterate over the things
    for x in s:
        # get strategies
        strategies = get_strategy( len(x) )

        # reset beautiful
        beautiful = False

        # and now iterate over the strategy
        for strategy in strategies:
            slices = buildslice( strategy )

            # make the numbers
            numbers = slicer(x, slices)

            # is it beautiful?
            left = numbers.pop(0)
            beautiful = isBeautiful(left, numbers, False)

            # number would only be beautiful once, so break if True
            if beautiful:
                break

        # now do the output
        if beautiful and left != 0:
            #print("YES {0}".format(left))
            results.append(("YES", left))
        else:
            #print("NO")
            results.append(("NO", ))

    # print it for HR
    return results



tests = {
    "get_strategy": [
        [
            1, 
            [[1]],
            "test one"
        ],
        [
            5, 
            [ [1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [2, 3] ],
            "test two"
        ],

    ],
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
        [
            ['010203'],
            [("NO", )],
            "test two"
        ],
        [
            ['99910001001', '7891011', '9899100', '999100010001'],
            [ ("YES", 999), ("YES", 7), ("YES", 98), ("NO",) ],
            "test three"
        ]
    ],
}

skips = [
    {"separateNumbers": None}
]

for func, tests in tests.items():

    for test in tests:
        # run?
        run = True

        # parts
        name = test.pop()
        expected = test.pop()

        # skip things if we're skipping them
        for skip in skips:
            for f, t in skip.items():
                if f == func:
                    if t == 0 or t == name:
                        run = False

        # do the continue here
        if not run:
            continue

        # we are not skipping, so call the function with the args
        result = locals()[func](*test)

        # and do the feedback
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