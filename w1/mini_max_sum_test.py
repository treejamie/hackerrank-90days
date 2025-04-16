"""
Tests for mini_max_sum
"""
from pathlib import Path
from test import testutils
from w1.mini_max_sum import mini_max_sum



class MiniMaxSumTest(testutils.TestCase):
    """
    Mini max sum test cases
    """
    @classmethod
    def setUpClass(cls):
        """Get all the matching test case files"""
        cls.tcs = sorted(Path("w1/tc").glob("2_*.txt"))

    def test_mini_max_sum(self):
        """(W1/2): Mini Max Sum"""
        # iterate over our testcases
        for tc in self.tcs:
            # use a subtest scope
            with self.subTest(tc=tc):
                # read in the lines
                lines = list(self.read_lines(Path(tc)))

                # args: line 1 - but it needs splitting up and turning into a list of ints
                args = [int(value) for value in lines[0].split()]

                # expected: line 3 - also needs splitting up into ints
                expected = [int(value) for value in lines[2].split()]

                # it returns what we expect
                self.assertEqual(mini_max_sum(args), expected)
