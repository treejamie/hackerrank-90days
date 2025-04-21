"""
Helpers for testing
"""
import unittest
from typing import ClassVar, Iterator
from pathlib import Path


class TestCase(unittest.TestCase):
    """
    The common base for tests
    """

    # holds the globbed' paths for a given TestCase
    tcs: ClassVar[list[Path]]
    glob_pattern: ClassVar[str] = "w1/tc/*.txt"

    @classmethod
    def setUpClass(cls):
        """Get all the matching test case files"""
        # Path.glob is lazy, so wrap in list to get iteration ready paths...
        cls.tcs = list(Path().glob(cls.glob_pattern))

    def read_lines(self, path: Path) -> Iterator[str]:
        """
        Reads the lines from a file at path and returns a generator of stripped lines

        Parameters:
            path (Path): the path of a given file

        Returns:
            IAn iterator containing the contents of the file at path
        
        Examples:
            Assuming the file at path has two lines: foo,bar
            read_lines(path/to/foo/bar)
            >>>["foo", "bar"]
        """
        with path.open() as f:
            for line in f:
                yield line.rstrip('\n')  # or .strip() if you want to trim all whitespace
