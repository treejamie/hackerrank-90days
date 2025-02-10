import sys

def maximumPerimeterTriangle(sticks):

    # first, sort the array
    sticks.sort(reverse=True)

    solved = False
    while not solved:

        # slice off the largest three and sort them
        maybe = sticks[:3]

        # if we have a dengenerate, pop off from sticks and try again        
        if maybe[0] == maybe[1] + maybe[2] or maybe[1] + maybe[2] < maybe[0]:
            if len(sticks) > 3:
                sticks.pop(0)
                continue
            else:
                return [-1]

        

        # we have a solution
        solved = maybe

    # return the triangle
    return sorted(maybe)



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
    ],
    [
        [3, 9, 2, 15, 3],
        [2, 3, 3],
        "test four"
    ],
    [
        [9, 2015, 5294, 58768, 285, 477, 72, 13867, 97, 22445, 48, 36318, 764, 8573, 183, 3270, 81, 1251, 59, 95094],
        [72, 81, 97],
        "test five"
    ],
]

target = maximumPerimeterTriangle

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
