import sys



def is_beautiful(left, remaining, maybe_beautiful):
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
        return is_beautiful(right, remaining, maybe_beautiful)
    
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


def build_slice(strategy, i=0, slices=None): # change the slices to an empty list and side effects creep in.
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
    return build_slice(strategy, right, slices)


def get_strategy(s, left, segments=None):

    # beware the default arg mutation issue
    if segments is None:
        segments = []
    
    # Base case -  string is empty, return the built segments
    if not s:
        return segments

    # try different segment lengths
    for length in range(1, len(s) + 1):
        current_part = s[:length]         # Take the first 'length' characters
        if current_part.startswith("0"):  # No leading zeros allowed
            continue
        
        current_num = int(current_part)  # Convert to an integer

        # If this is the first number, accept it and recurse
        if left is None or current_num == left + 1:
            result = get_strategy(s[length:], current_num, segments + [length])
            if result:  # If we found a valid sequence, return it
                return result

    return None  # No valid sequence found



def separate_numberss(s):

    # get strategies
    strategy = get_strategy(s, None)

    # if strategy is None: no
    if strategy is None:
        return ("NO", )

    # reset beautiful
    beautiful = False

    # and now iterate over the strategy
    slices = build_slice( strategy )

    # make the numbers
    numbers = slicer(s, slices)

    # is it beautiful?
    left = numbers.pop(0)
    beautiful = is_beautiful(left, numbers, False)

    # now do the output
    if beautiful and left != 0:
        return ("YES", left)
    else:
        return ("NO", )



tests = {
    "get_strategy": [
        [
            "1234567891011",
            None,
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
            "test one"
        ],
        [
            "00000000000000000000000000000000", 
            None,
            None,
            "test two"
        ],

    ],
    "build_slice": [
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
    "is_beautiful": [
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
    "separate_numberss": [
        [
            "1234",
            ("YES", 1),
            "test one"
        ],
        [
            "91011",
            ("YES", 9),
            "test two"
        ],
        [
            "99910001001",
            ("YES", 999),
            "test three"

        ],
        [  
            "010203",
            ("NO", ),
            "test four"
        ],
        [
            "99910001001",
            ("YES", 999 ),
            "test five"
        ]
    ],
}

skips = [

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