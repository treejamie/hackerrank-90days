import sys

def kangaroo(x1, v1, x2, v2):
    return "PLLOP"




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
