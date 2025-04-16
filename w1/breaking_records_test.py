"""
Tests for Breaking Records
"""
from pathlib import Path
from test import testutils
from w1.breaking_records import breaking_records



class BreakRecordsTest(testutils.TestCase):
    """
    Breaking records test cases
    """
    glob_pattern = "w1/tc/4_*.txt"

    def test_breaking_records(self):
        """(W1/4): Breaking Records"""
        for tc in self.tcs:

            # use a subtest scope
            with self.subTest(tc=tc):
                # read in the lines
                lines = list(self.read_lines(Path(tc)))

                # args is lines[1], lines[0] is a count and is not needed
                args = [int(value) for value in lines[1].split()]

                # expected is lines[3]
                expected = [int(value) for value in lines[3].split()]

                # we get what we expected
                self.assertEqual(breaking_records(args), expected)
