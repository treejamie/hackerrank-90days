import sys

def pickingNumbers(a):
    # sort it first
    a.sort()

    # set variabls up
    i = 0
    l = len(a) - 1
    ml = 1
    subs = []

    # now loop
    while i < l:
        # is next thing less than one?
        if a[i + 1] - a[i] <= 1:
            # this the end? (beautiful friend, the end...)
            if i + 1 ==  l:
                subs.append(ml)  # bank the current max length cos the party is over
            else:
                ml += 1   # increment the max length
        else:
            # nope, we reached the end of the streak
            subs.append(ml)  # bank it
            ml = 1           # reset the length
        
        # increment the index
        i += 1
    
    return max(subs)
    


tests = [
    [
        [4, 6, 5, 3, 3, 1],
        4,
        "test one"
    ],
    [
        [1, 2, 2, 3, 1, 2],
        5,
        "test two"
    ]
]

target = pickingNumbers

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
