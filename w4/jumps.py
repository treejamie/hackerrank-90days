import sys

def kangaroo(x1, v1, x2, v2):
    """
    This is a lowest common multiplier question
    
    two roos'

    1 starts at position X (x1) with velocity V(v1)
    2 starts at position X (x2) with velocity V(v2)

    The question is, can they ever arrive at the same place at the same time?

    It could be brute forced and then check for membership, but that is dumb.

    """
    # if the one behind is not faster, NO. Logic.
    if (x1 < x2 and v2 > v1) or (x2 < x1 and v1 > v2):
        return "NO"

    # this is the math bit 
    # if the distance between out two roo's "mod" the v2 - v1 is zero, they're gonna meet
    if (x1 - x2) % (v2 - v1) == 0:
        return "YES"

    # nope
    return "NO"



tests = [
    [
        0,
        3,
        4,
        2,
        "YES",
        "test one"
    ],
    [
        0,
        2,
        5,
        3,
        "NO",
        "test two"
    ],
]

targets = [
    kangaroo,
]

# if you wanted to skip tests this where you do that
skip_tests = [
    # "test one",
    # "test two",
    # "test three"
]

for test in tests:
    # parts
    name = test.pop()
    expected = test.pop()
    

    for target in targets:
        result = target(*test)

        # skip tests 
        if name in skip_tests:
            continue

        # do the things
        try:
            assert result == expected
            print("✅: SUCCESS ({2}) - {1} expected and {0} result".format(
                result,
                expected,
                target.__name__
            ))
        except AssertionError:
            msg = "🛥️ FAILBOAT {3} {0} :\n\texpected: {2}\n\tresult: {1} ".format(
                name,
                result,
                expected,
                target.__name__
            )
            sys.exit(msg)
