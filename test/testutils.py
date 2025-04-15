"""
Helpers for testing
"""
from pathlib import Path
from typing import Iterator

def read_lines(path: Path) -> Iterator[str]:
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
