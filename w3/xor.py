import sys

def strings_xor(s, t):
    """
    I had heard about and used XOR once before. I didn't understand it then.

    However, this challenge wasn't complex in terms of completion, it
    simply took from a more advanced topic.

    So here's the deal.
    This function gives two strings

    10101: which is 21
    00101: which is 5

    This function expects to return 
    10000: which is 16

    So basically this challenge is to subtract s from t.
    
    which would be as simple as

    result = int(s, 2) ^ int(t, 2)
    return bin(result)[2:]

    However, the challenge is that a maxium of three lines can be edited.

    result = int(s, 2) ^ int(t, 2)
    return bin(result)[2:]
    
    """

    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'    # we're appending to the strings, not assigning them repeatedly 
        else:
            res += '1'

    return res




tests = [
    [
        "10101",
        "00101",
        "10000",
        "test one"
    ],
]
target = strings_xor

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
        msg = "🛥️ FAILBOAT {0} :\n\texpected: {2}\n\tresult: {1} ".format(
            name,
            result,
            expected,
        )
        sys.exit(msg)
