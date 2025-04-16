"""
Tests for camel case
"""

from pathlib import Path
from test import testutils
from w1.camel_case import camel_case


class CamelCaseTests(testutils.TestCase):
    """
    Camel case test cases
    """

    @classmethod
    def setUpClass(cls):
        """Get all the matching test case files"""
        cls.tcs = sorted(Path("w1/tc").glob("5_*.txt"))

    def test_camel_case(self):
        """(W1/5): Camel Case"""
        # get the test data
        for tc in self.tcs:

            # use a subtest scope
            with self.subTest(tc=tc):
                # read in the lines
                lines = list(self.read_lines(Path(tc)))

                # problems are everyline up to the blank line, solutions are everything after
                # however, this challenge works by reading the stdin, feeding it into the
                # function printing to stdout. If correct it moves onto the next word. First
                # order of business is to split out the problems and the solutions.
                split_at = lines.index("")
                problems = lines[:split_at]
                solutions = lines[split_at + 1:]

                # now bundle into pairs of [{problem1, solutions1}, {problem2, solutions2}]
                test_data = []
                for problem, solution in zip(problems, solutions):
                    test_data.append((problem, solution))

                # now we can test
                # print(test_data)
                for data in test_data:
                    result = camel_case(data[0])
                    # print(data[1], result)
                    self.assertEqual(data[1], result)

