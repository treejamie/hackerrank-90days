import sys

def migratoryBirds(arr):
    # make a dictionary
    burds = {} # yes, I know birds isn't spelled with a u, but it is more fun that way.

    # next iterate over and count them up
    for burd in arr:
        if burd in burds:
            burds[burd] += 1
        else:
            burds[burd] = 1

    # now find their max
    frekwunt_burd = None    # for some reason this challenge feels like a fun one to play with words
    frekwunt_kownt = 0      # for some reason this challenge feels like a fun one to play with words
    for burd, count in burds.items():

        # this is the edge case where burd id > existing one
        if count == frekwunt_kownt: 
            if frekwunt_burd > burd:
                frekwunt_kownt = count
                frekwunt_burd = burd

        elif count > frekwunt_kownt:
            frekwunt_kownt = count
            frekwunt_burd = burd
    
    return frekwunt_burd



tests = [
    [
        [1, 4, 4, 4, 5, 3],
        4,
        "test one"
    ],
    [
        [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4],
        3,
        "test two"
    ]
]
target = migratoryBirds

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
