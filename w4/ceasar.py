import sys
import string




def caesarCipher(s: str, k: int) -> str:
    # k is the shift, but don't assume it is less than 26.
    k = k % 26

    # make a rosetta stone for the shift using a dict and iterating over string.ascii_lowercase & uppercase
    rs = {}
    chars = string.ascii_lowercase
    for i, char in enumerate(chars):
        rs[char] = chars[(i + k) % 26]

    chars = string.ascii_uppercase
    for i, char in enumerate(chars):
        rs[char] = chars[(i + k) % 26]

    # now translate it
    result = []
    for x in s:
        if x in rs:
            result.append(rs[x])
        else:
            result.append(x)
    
    # and done
    return "".join(result)




tests = [
    [
        "middle-Outz", 
        2,
        "okffng-Qwvb",
        "test one"
    ],
    [
        "Always-Look-on-the-Bright-Side-of-Life",
        5,
        "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj",
        "test two"
    ]
]

target = caesarCipher

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