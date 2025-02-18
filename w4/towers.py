import sys




def tower_breakers(n, m):
    """
    Players play optimally.
    Player one always starts.
    Player loses if there are no more moves.
    
    So basically -  if all the towers are height of one, or number of towers is one, player one wins.
    """
    if n % 2 == 0 or m == 1:
        return 2
    else:
        return 1


tests = {
    "tower_breakers": [
        [
            1,
            7,
            1,
            "HR TC 1"
        ],
    ],
}

skips = [
    {"tower_breakers": 2}
]

for func, tests in tests.items():

    for i, test in enumerate(tests):
        # run?
        run = True

        # parts
        name = test.pop()
        expected = test.pop()


        # if test[0] or test [1] is a dict with "transformer as a key", transform.

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
        print(*test)
        result = locals()[func](*test)

        truncate_at = 10

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