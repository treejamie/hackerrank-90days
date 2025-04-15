"""
The hello.py tests
"""
import unittest
from pathlib import Path
from test import testutils
from w1.plus_minus import plus_minus


class PlusMinusTest(unittest.TestCase):
    """
    Ensure everything works as expected
    """

    tcs = [
        "w1/tc/1_0.txt",
        "w1/tc/1_1.txt",
        "w1/tc/1_2.txt",
    ]

    def test_plus_minus(self):
        # iterate over our testcases
        for tc in self.tcs:
            # read in the lines
            lines = [line for line in testutils.read_lines(Path(tc))]

            # args: line 2 - but it needs splitting up and turning into a list of ints
            args = [int(value) for value in lines[1].split()]

            # expected: lines 4,5,6
            expected = lines[3:6]

            # it returns what we expect
            self.assertEqual(plus_minus(args), expected)
