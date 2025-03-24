import sys


def minimumAbsoluteDifference(arr: list) -> int:
    """
    Return the minimum absolute different from elements in an array.
    This one is closer to O(1) but to be fair, I'm not 100% on my big O stuff
    as of the time of writing
    """
    # first sort it.
    arr.sort()

    # now that it is sorted, we know that pairs are grouped together
    # so we don't need to iterate over the loop twice - this is the 
    # performance boost. This is the trick.

    # calulate minimum difference on the first two elements.
    md = arr[1] - arr[0]

    # now go through the array comparing i with  i - 1, but start at 2
    # because we've just compared arr[0] and arr[1] above
    for i in range(2, len(arr)):
        x = arr[i] - arr[i - 1]
        if x < md:
            md = x

    # done
    return md




def minimumAbsoluteDifferenceOn2(arr: list) -> int:
    """
    Return the minimum absolute difference from elements in an array
    O(n2) - works on all but three test cases.  This is a solution,
    but it is not optimal.
    """
    # store the minium difference
    mindiff = None

    # we have to iterate over the array twice.
    for i in arr:
        for j in arr:
            d = abs(i - j)
            if d == 0:
                continue
            elif (mindiff is None or d < mindiff):
                mindiff = d
    
    # return the mindiff
    return mindiff




tests = [
    [
        [3, 7, 0],
        3,
        "test one"
    ],
    [
        [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75],
        1,
        "test two"
    ]
]

target = minimumAbsoluteDifference

skip_tests = [

    # "test one",
    # "test two",
    # "test three"
]


for test in tests:
    # parts
    name = test.pop()
    expected = test.pop()
    result = target(*test)

    # skip tests 
    if name in skip_tests:
        continue

    # do the things
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
