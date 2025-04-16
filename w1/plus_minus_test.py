"""
Tests for plus_minus
"""
from pathlib import Path
from test import testutils
from w1.plus_minus import plus_minus


class PlusMinusTest(testutils.TestCase):
    """
    Ensure everything works as expected
    """

    @classmethod
    def setUpClass(cls):
        """Get all the matching test case files"""
        cls.tcs = sorted(Path("w1/tc").glob("1_*.txt"))

    def test_plus_minus(self):
        """(W1/1): Plus Minus"""
        # iterate over our testcases
        for tc in self.tcs:
            # read in the lines
            lines = list(self.read_lines(Path(tc)))

            # args: line 2 - but it needs splitting up and turning into a list of ints
            args = [int(value) for value in lines[1].split()]

            # expected: lines 4,5,6
            expected = lines[3:6]

            # it returns what we expect
            self.assertEqual(plus_minus(args), expected)
