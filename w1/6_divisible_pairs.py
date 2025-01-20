#!/bin/python3
import math
import os
import random
import re
import sys



def divisibleSumPairs1(n, k, ar):
    # the results
    results = []

    # now do the loop
    for i in range(0, len(ar)):

        for j in range(i + 1, len(ar)):

            # this is the main part of the functions
            if (ar[i] + ar[j]) % k == 0:
                results.append((i, k))

    return results
        



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
    result = divisibleSumPairs1(n, k, ar)
    # result = divisibleSumPairs2(n, k, ar)

    try:
        assert result == expected
        print("yep")
    except AssertionError:
        print ("nope")
        print ("expected: ", expected)
        print ("got: ", result)
