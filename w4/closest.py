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

    # get the pairs into a dictionary with the difference as the value
    diff_dict = {p: abs(p[0] - p[1]) for p in pairs}

    # sort the values into a list
    vals = sorted([x for x in diff_dict.values()])

    # now return the key for the values
    for k, v in diff_dict.items():
        if v == vals[0]:
            return list(k)


#
#

def closest_in(fname):
    with open(fname) as fp:
        total = fp.readline()
        return [int(x.strip()) for x in fp.readline().split()]

def closest_out(fname):
    with open(fname) as fp:
        return [int(x.strip()) for x in fp.readline().split()]

tests = {
    "get_pairs": [
        [
            [1, 2, 7, 1000],
            [(1, 2), (2, 7), (7, 1000)],
            "even"
        ],
        [
            [1, 2, 3, 4, 5],
            [(1, 2), (2, 3), (3, 4), (4, 5)],
            "odd"
        ]
    ],
    "closest_numbers": [
        [
            [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854],
            [-20, 30],
            "HR tc0"
        ],
        [
            {"transformer": closest_in, "fname": "w4/tc/closest4_in.txt"},
            {"transformer": closest_out, "fname": "w4/tc/closest4_out.txt"},
            "HR tc4"
        ]
    ],
}

skips = [
    {"closest_numbers": 1}
]

for func, tests in tests.items():

    for i, test in enumerate(tests):
        # run?
        run = True

        # parts
        name = test.pop()
        expected = test.pop()

        # if test[0] or test [1] is a dict with "transformer as a key", transform.
        if "transformer" in test[0]:
            test[0] = test[0]["transformer"](test[0]["fname"])

        if "transformer" in expected:
            expected = expected["transformer"](expected["fname"])

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
            print("✅: SUCCESS ({2} #{4} {3}) - {1} expected and {0} result".format(
                result,
                expected,
                func,
                name,
                i
            ))
        except AssertionError:
            msg = "🛥️ FAILBOAT #{3} {4} {0} {0} :\n\texpected: {2}\n\tresult: {1} ".format(
                name,
                result,
                expected,
                func,
                i
            )
            sys.exit(msg)