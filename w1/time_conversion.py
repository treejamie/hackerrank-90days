"""
Time Conversion - Challenge 3 - Week 1
"""
from datetime import datetime

# default to not printing
PRINT = False


def time_conversion(s:str) -> str:
    """
    Takes a 12 hour AM/PM string and returns it military time.

    Parameters:
        s (str): A 12 hour AM/PM string
    
    Returns:
        str: A military formatted time

    Example:
        >>> time_conversion('07:05:45PM')
    """
    # first get it from a string into a datetime
    # note: gotcha when parsing the hour - 12 hour parse - not 24!
    dt = datetime.strptime(s, '%I:%M:%S%p')

    # now remake it as the expected format
    result = datetime.strftime(dt, '%H:%M:%S')

    # return the result
    return result
