import sys

def rotateLeftSlice(d, arr):
    """
    I am feeling drawn towards recursive solutions,
    but I think this could be done with a slice.
    """
    return arr[d:] + arr[:d]  # A one liner



def rotateLeftRecurse(total_moves, arr, move=1):
    """
    I felt cheated that the above was a one liner, so here's
    a recursive solution. 
    """

    # pop at zero and append
    x = arr.pop(0)
    arr.append(x)

    # base case: total moves is equal to move
    if total_moves == move:
        return arr

    # and return this function
    return rotateLeftRecurse(total_moves, arr, move + 1)




tests = [
    [
        4,
        [1, 2, 3, 4, 5],
        [5, 1, 2, 3, 4],
        "test one"
    ],

]

targets = [
    rotateLeftSlice,
    rotateLeftRecurse
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
