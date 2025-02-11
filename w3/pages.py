import sys

def pageCount(n, p):
    """
    ok, this is essentially an exercise in counting tuples.

    7 pages, page 5 - 1 flip from back.
    7 pages, page 2 - 1 flip from front.
    
    0 3 - (0, 1)
    1 2 - (2, 3)
    2 1 - (4, 5)
    3 0 - (6, 7)
    """
    pass

    # front index
    # this one has no pre-calc shenanigans because of the zero index
    if p % 2 == 1:
        front = (p - 1) / 2
    else:
        front = p / 2

    # back index
    # first we do n / 2
    back_index = n / 2

    # now it is mostly the same as front
    if p % 2 == 1:
        back = back_index - ((p - 1) / 2)
    else:
        back = back_index - (p / 2)

    # now return the minimum from front and back
    return int(min([front, back]))


    # back index
    print(n, p)




tests = [
    [
        [6, 2],
        1,
        "test one"
    ],
    [
        [5, 4],
        0,
        "test two"
    ],

]

target = pageCount

skip_tests = [
    # "test one",
    # "test two",
    # "test three"
]


for test in tests:
    # parts
    name = test.pop()
    expected = test.pop()
    args = test.pop()
    result = target(*args)

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
        msg = "🛥️ FAILBOAT {0}:\n\texpected: {2}\n\tresult: {1} ".format(
            name,
            result,
            expected,
        )
        sys.exit(msg)
