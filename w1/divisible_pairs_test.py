"""
Tests for divisible pairs
"""

from pathlib import Path
from test import testutils
from w1.divisible_pairs import divisible_sum_pairs


class DivisibleSumPairsTests(testutils.TestCase):
    """
    Tests for divisible sum parirs
    """

    @classmethod
    def setUpClass(cls):
        """Get all the matching test case files"""
        cls.tcs = sorted(Path("w1/tc").glob("6_*.txt"))


    def test_divisible_sum_pairs(self):
        """(W1/6): Divisible Sum Pairs"""
        for tc in self.tcs:

            # use a subtest scopeV
            with self.subTest(tc=tc):

                # get the lines
                lines = list(self.read_lines(tc))

                # n, k is lines[0]
                n, k = [int(x) for x in lines[0].split()]

                # ar is lines[1]
                ar = [int(x) for x in lines[1].split()]

                # result is lines[3]
                result = int(lines[3])

                # ok, do it
                self.assertEqual(divisible_sum_pairs(n, k, ar), result)