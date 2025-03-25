import sys



def anagram(s):
    # base case - if len(s) is odd, return -1
    if len(s) % 2 == 1:
        return -1

    # first determine where is halfway
    half = len(s) // 2

    # split s into two list
    a = sorted([x for x in s[:half]])

    b = sorted([x for x in s[half:]])
    print(a)
    print(b)

    # assume we replace everything
    count = half

    # iterate over a and as x and if x is in a, reduce the count
    for x in b:
        if x in a:
            count -= len([y for y in a if y == x])

    print(count)
    return count





tests = [
    [
        "abccde", 
        2,
        "test 1"
    ],
    # [
    #     "abc", 
    #     -1,
    #     "test 2"
    # ],
    # [
    #     "aaabbb",
    #     3,
    #     "test 3"
    # ],
    # [
    #     "asdfjoieufoa",
    #     3,
    #     "test 15a"
    # ],
    [
        "fdhlvosfpafhalll",
        5,
        "test 15b"
    ],
    # [
    #     "mvdalvkiopaufl",
    #     5,
    #     "test 15b"
    # ],
]

target = anagram

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
        print(f"✅: ({target.__name__}) SUCCESS - {expected} expected and {result} result")
    except AssertionError:
        msg = f"🛥️ ({target.__name__})FAILBOAT {name} :\n\texpected: {expected}\n\tresult: {result} "
        sys.exit(msg)