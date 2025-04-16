"""
Tests for Time Conversion
"""
from pathlib import Path
from test import testutils
from w1.time_conversion import time_conversion



class TimeConversionTest(testutils.TestCase):
    """
    Time conversion test cases
    """

    glob_pattern = "w1/tc/3_*.txt"

    def test_time_conversion(self):
        """(W1/3): Time Conversion"""
        for tc in self.tcs:
            # use a subtest scope
            with self.subTest(tc=tc):
                # read in the lines
                lines = list(self.read_lines(Path(tc)))

                # args: line 1 - but it needs splitting up and turning into a list of ints
                args = lines[0].strip()

                # expected: line 3 - also needs splitting up into ints
                expected = lines[2].strip()

                # it returns what we expect
                self.assertEqual(time_conversion(args), expected)
