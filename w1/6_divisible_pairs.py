#!/bin/python3



import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


def blackBoxFunction(ar, k, n):
    # the results
    results = []

    # n has a constraint of 2 < n < 100
    if not 2 <= n <= 100:
        return results

    # k has a constraint of 1 < k < 100
    if not 1 <= k <= 100:
        return results


    for a_idx, i_value in enumerate(ar):
        # constraint that 1 < ar[i] < 100
        if not 1 <= i_value <= 100:
            continue

        for b_idx, j_value in enumerate(ar):
            # the constraints

            # this is the main part of the functions
            if i_value < j_value and ((i_value + j_value) % k) == 0:
                results.append((a_idx, b_idx))

    return results
        


def divisibleSumPairs(n, k, ar):
    # Write your code here
    result = blackBoxFunction(ar, k, n)

    return len(result)


def parse_input(fpath):
    # read the file and assign the things
    with open(fpath) as f:
        l1 = f.readline()
        l2 = f.readline()
        l3 = f.readline()

    # build the data
    n, k = [int(x) for x in l1.split()]
    ar = [int(x) for x in l2.split()]
    expected = int(l3.split()[0])

    return n, k, ar, expected


if __name__ == '__main__':

    possible_inputs = [
        "w1/6_divisible_pairs_data_set.txt",
        "w1/6_divisible_pairs_data_set_test_1.txt",
        "w1/6_divisible_pairs_data_set_test_2.txt",
        "w1/6_divisible_pairs_data_set_test_6.txt",
        "w1/6_divisible_pairs_data_set_test_19.txt"
    ]

    # get the input becasue now I am setup to handle the hidden test cases
    n, k, ar, expected = parse_input(possible_inputs[3])

    # and now get the result
    result = divisibleSumPairs(n, k, ar)

    try:
        assert result == expected
        print("yep")
    except AssertionError:
        print ("nope")
        print ("expected: ", expected)
        print ("got: ", result)
