import sys

def birthday(s, d, m):
    # results
    results = 0

    # now iterate
    for i, _ in enumerate(s):
        # what is the target
        target = s[i:i + m]

        # does it add up to the amount
        if sum(target) == d:
            results += 1

    # return the results
    return results


tests = [
    [
        [1,2,1,3,2],
        3,
        2,
        2,
        "test one"
    ],
    [
        [1,1,1,1,1,1],
        3,
        2,
        0,
        "test two"
    ],
    [
        [4],
        4,
        1,
        1,
        "test three"
    ]
]
target = birthday

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
        msg = "🛥️ FAILBOAT {0} :\n\texpected: {1}\n\tresult: {2} ".format(
            name,
            result,
            expected,
        )
        sys.exit(msg)
