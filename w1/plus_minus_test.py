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

    glob_pattern = "w1/tc/1_*.txt"

    def test_plus_minus(self):
        """(W1/1): Plus Minus"""
        # iterate over our testcases
        for tc in self.tcs:
            # use a subtest scope
            with self.subTest(tc=tc):
                # read in the lines
                lines = list(self.read_lines(Path(tc)))

                # args: line 2 - but it needs splitting up and turning into a list of ints
                args = [int(value) for value in lines[1].split()]

                # expected: lines 4,5,6
                expected = lines[3:6]

                # it returns what we expect
                self.assertEqual(plus_minus(args), expected)
