import sys

def maximumPerimeterTriangle(sticks):
    pass
    return []


tests = [
    [
        [1, 1, 1, 3, 3],
        [1,3,3],
        "test one"
    ],
    [
        [1, 2, 3],
        [-1],
        "test two"
    ],
    [
        [1, 1, 1, 2, 3, 5],
        [1,1,1],
        "test three"

    ]
]
target = maximumPerimeterTriangle

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
