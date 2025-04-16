"""
Tests for sparse array
"""

from pathlib import Path
from test import testutils
from w1.sparsearray import sparsearray


class DivisibleSumPairsTests(testutils.TestCase):
    """
    Tests for divisible sum parirs
    """

    glob_pattern = "w1/tc/7_*.txt"

    def test_sparse_array(self):
        """(W1/7): Sparse Array Tests"""
        for tc in self.tcs:

            # use a subtest scope
            with self.subTest(tc=tc):
                # read in the lines
                lines = list(self.read_lines(Path(tc)))

                # this is very "slicy"
                # string size, strings, query size, queries
                string_size = int(lines[0])
                strings = lines[ 1 : string_size + 1]

                # now get the query size which is at index string_size + 1
                query_size = int(lines[string_size + 1])
                queries = lines[ string_size + 2 : string_size + 2 + query_size]

                # now get the answers, which need to be in the form [a, b, c]
                # first find the empty line ''
                # add one and then you have position to slice at
                # next slice that off the lines
                # use that slice as the basic for a list comprehension
                # comprehend it out into a slist of integers
                # et voila - answers
                answers = [int(x) for x in lines[ lines.index('') + 1 :] ]

                # now test
                self.assertEqual(sparsearray(strings, queries), answers)



