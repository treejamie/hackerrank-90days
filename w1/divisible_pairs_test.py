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
        cls.tcs = sorted(Path("w1/tc").glob("5_*.txt"))


    def test_divisible_sum_pairs(self):
        """(W1/6): Divisible Sum Pairs"""
        for tc in self.tcs:

            # use a subtest scopeV
            with self.subTest(tc=tc):
                pass