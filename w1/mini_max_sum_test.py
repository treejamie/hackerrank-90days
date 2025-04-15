"""
Tests for mini_max_sum
"""
import unittest
from pathlib import Path
from test import testutils
from w1.mini_max_sum import mini_max_sum



class MiniMaxSumTest(unittest.TestCase):
    """
    Mini max sum test cases
    """
    tcs = [
        "w1/tc/2_0.txt",
        "w1/tc/2_1.txt",
        "w1/tc/2_14.txt",
    ]

    def test_mini_max_sum(self):
        """Testing Mini Max Sum - Challenge 2 - Week 1"""
        # iterate over our testcases
        for tc in self.tcs:
            # read in the lines
            lines = list(testutils.read_lines(Path(tc)))

            # args: line 1 - but it needs splitting up and turning into a list of ints
            args = [int(value) for value in lines[0].split()]

            # expected: line 3 - also needs splitting up into ints
            expected = [int(value) for value in lines[2].split()]

            # it returns what we expect
            self.assertEqual(mini_max_sum(args), expected)
