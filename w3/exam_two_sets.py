import sys


"""
Two arrays of integers.

1. The elements of the first array are all factors of the integer being considered.
2. The "integer being considered" is a factor of all elements of the second array.


Factor is a an integer that divides into a whole number without a remainder.

2 is a factor of 4, 6, 8, 10, 12, etc
3 is a factor of 3, 6, 9, 12, 15, etc
4 is a factor if 4, 8, 12, 16, 20, etc

The function should return the number of integers that are between the sets.

--- three hours later

Ok, this one perplexed me and I had to break out ChatGPT to understand it. If only the
question was phrased as find the lowest common multiple of items in a then the greatest
common divider of things in b and then count the intersection of the two.

Luckily, the MITx course has just been over recursive gcd algos using euclidian methods and
lcm algos, so it was just really a case of busting those out.

"""
from functools import reduce

def gcd(a, b):
    # the base case
    if b == 0:
        return a
    
    # done
    return gcd(b, a % b)

def gcd_array(a):
    return reduce(gcd, a)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_array(a):
    return reduce(lcm, a)


def getTotalX(a, b):
    # 1 - compute the lowest common multiple of A
    lcm_a = lcm_array(a) 

    # 2 - compute the highest common denomentaor of B
    gcd_b = gcd_array(b)

    # 3 - find the common numbers between multiples of lcm of A and the gcd factors of B
    count = 0
    for x in range(lcm_a, gcd_b + 1, lcm_a):   # this is a nice use of range. start at lcm_a, go all the way up to gcd_b + 1, and go up in multiples of lcm_a
        if gcd_b % x == 0:
            count += 1

    return count



tests = [
    [
        [2, 6],
        [24, 36],
        2,
        "test zero"
    ],
    [
        [2, 4],
        [16, 32, 96],
        3,
        "test one"
    ],
    [
        [3, 4],
        [24, 48],
        2,
        "test two"
    ]
]


target = getTotalX

skip_tests = [
]

for test in tests:
    name = test.pop()
    expected = test.pop()
    result = target(*test)

    if name in skip_tests:
        continue

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
