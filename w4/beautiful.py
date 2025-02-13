import sys

{
    4: [2, 1],
    5: [3, 2, 1],
    6: [3, 2, 1],
    7: [4, 3, 2, 1],
    8: [4, 3, 2, 1],
    9: [4, 3, 2, 1],
    10: [5, 4, 3, 2, 1],
}


def split(l, left, right):
    return l[left:right]

def separateNumbers(s):
    # need somewhere to stash the stuff
    out = []

    # iterate
    for item in s:
        work = [int(x) for x in item[:]]
        i = 0
        while len(work) >= i + 1:
            left_idx = i
            right_idx = left_idx + 1 if left_idx + 1 <= (len(work) - 1) else left_idx
            print(left_idx)
            print(right_idx)

            if work[left_idx] + 1 == work[right_idx]:
                print("yes")
            
            i += 1

        


tests = [
    [
        [ '1234', '91011', '99100', '101103', '010203', '13', '1' ],
        [ ("YES",  1), ("YES", 9), ("YES", 99), ("NO",), ("NO",), ("NO",), ("NO",) ],
        "test one"
    ]
]


targets = [
    separateNumbers,
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
