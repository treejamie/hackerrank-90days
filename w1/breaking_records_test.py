"""
Tests for Breaking Records
"""
import unittest
from pathlib import Path
from test import testutils
from w1.breaking_records import breaking_records



class BreakRecordsTest(unittest.TestCase):
    """
    Breaking records test cases
    """
    tcs = [
        "w1/tc/4_0.txt",
        "w1/tc/4_1.txt"
    ]

    def test_breaking_records(self):
        """(W1/4): Breaking Records"""
        for tc in self.tcs:
            # read in the lines
            lines = list(testutils.read_lines(Path(tc)))

            # args is lines[1], lines[0] is a count and is not needed
            args = [int(value) for value in lines[1].split()]

            # expected is lines[3]
            expected = [int(value) for value in lines[3].split()]

            # we get what we expected
            self.assertEqual(breaking_records(args), expected)
