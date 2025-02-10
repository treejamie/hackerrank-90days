import sys


def twoArrays(k, A, B):
    # Write your code here
    pass


tests = [
    [
        10,
        [2, 1, 3],
        [7, 8, 9],
        "YES"
    ]
]
target = twoArrays

for test in tests:
    expected = test.pop()
    result = target(*test)

    try:
        assert result == expected
        print("✅: SUCCESS - {1} expected and {0} result".format(
            result,
            expected,
        ))
    except AssertionError:
        msg = "🛥️ FAILBOAT:\n\texpected: {1}\n\tresult: {0} ".format(
            result,
            expected,
        )
        sys.exit(msg)
