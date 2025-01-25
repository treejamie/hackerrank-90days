#!/bin/python3
import math
import os
import random
import re
import sys



def divisibleSumPairs2(n, k, ar):
    """
    This is a O(n) version using a map as a lookup table

    There was a few videos about this, but I struggled to get the underlying logic
    so here I battled it out on paper until I got the very basic algo working.

    What I can say is that I've never once, since 1998 had to use something like this
    in any application I've built. That's either saying more about me than it is the test :) 

    """
    # set the values up
    db = {}
    results = []

    # iterate over ar
    for value in ar:
        # get the mod first
        mod = value % k

        # now get the complement
        # but if mod is zero, use zero instead
        comp = 0 if mod == 0 else k - mod

        # if the complement is in the db as a value, append the value of it to results
        hit = db.get(comp)
        if hit is not None:
            results.append(hit)

        # add the mod into the db, default to one, but
        try:
            db[mod]
            db[mod] += 1
        except KeyError:
            db[mod] = 1

    return sum(results)



def divisibleSumPairs1(n, k, ar):
    """
    I don't think the O n squared is going to win me any friends.
    """
    # the results
    results = []

    # now do the loop
    for i in range(0, len(ar)):

        for j in range(i + 1, len(ar)):

            # this is the main part of the functions
            if (ar[i] + ar[j]) % k == 0:
                results.append((i, k))

    return len(results)
        


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
        "w1/6_divisible_pairs_data_set_test_19.txt",
        "w1/6_divisible_pairs_data_set_on.txt",
        "w1/6_divisible_pairs_data_set_example.txt",
    ]

    # get the input becasue now I am setup to handle the hidden test cases
    n, k, ar, expected = parse_input(possible_inputs[0])

    # and now get the result
    #result = divisibleSumPairs1(n, k, ar)
    result = divisibleSumPairs2(n, k, ar)

    try:
        assert result == expected
        print("yep")
    except AssertionError:
        print ("nope")
        print ("expected: ", expected)
        print ("got: ", result)
