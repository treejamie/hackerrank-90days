import sys

def get_pairs(arr: list, pairs: None | list = None) -> list:
    # if pairs was none, make it a list
    if pairs is None:
        pairs = []
    
    # pop off the first thing
    left = arr.pop(0)

    # base case - nothing left to pair with
    if len(arr) == 0:
        return pairs
    
    # make the pair
    pairs.append((left, arr[0]))

    # recurse thyself
    return get_pairs(arr, pairs)


def closest_numbers(arr:list) -> list:
    # sort 
    arr.sort()

    # to pairs
    pairs = get_pairs(arr)

    return 1


tests = {
    "get_pairs": [
        [
            [1, 2, 7, 1000],
            [(1, 2), (2, 7), (7, 1000)],
            "#1"
        ],
        [
            [1, 2, 3, 4, 5],
            [(1, 2), (2, 3), (3, 4), (4, 5)],
            "#2"
        ]
    ],
    "closest_numbers": [
        [
            [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854],
            [-20, 30],
            "#1"
        ]
    ],
}

skips = [
    {"closest_numbers": 0}
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
            print("✅: SUCCESS ({2} {3}) - {1} expected and {0} result".format(
                result,
                expected,
                func,
                name
            ))
        except AssertionError:
            msg = "🛥️ FAILBOAT {3} {0} {0} :\n\texpected: {2}\n\tresult: {1} ".format(
                name,
                result,
                expected,
                func
            )
            sys.exit(msg)