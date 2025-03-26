"""
A password is strong if it satisfies the following criteria:

* Its length is at least 6.
* It contains at least one digit.
* It contains at least one lowercase English character.
* It contains at least one uppercase English character.
* It contains at least one special character. The special characters are: !@#$%^&*()-+

"""
import sys


def minimum_number(pwlength: int, password: str) -> int:
    """
    O(n) - this could be O(1) if I looped over it just once.
    """
    # from the task
    min_length = 6
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    # split up the password into a list
    password.split()

    # now check everything - except length
    total_numbers = 0 if len([x for x in password if x in numbers]) > 0 else 1
    total_lowercase = 0 if len([x for x in password if x in lower_case]) > 0 else 1
    total_uppercase = 0 if len([x for x in password if x in upper_case]) > 0 else 1
    total_special = 0 if len([x for x in password if x in special_characters]) > 0 else 1

    # so now we know how many characters we have to add, do length seperately at the end
    total = total_numbers + total_lowercase + total_uppercase + total_special

    # add total onto current length and see if we have anymore to add
    total_length = 0 if pwlength + total >= min_length else min_length - pwlength - total

    # now return that total
    return total + total_length



tests = [
        [
            3,
            "Ab1",
            3,
            "test 0"
        ],
        [
            11,
            "#HackerRank",
            1,
            "test 1"
        ]
]

target = minimum_number

skip_tests = [
    # "test one",
    # "test two",
    # "test three"
]


for test in tests:
    # parts
    name = test.pop()
    expected = test.pop()
    result = target(*test)

    # skip tests
    if name in skip_tests:
        continue

    # do the things
    try:
        assert result == expected
        print(f"✅: ({target.__name__}) SUCCESS - {expected} expected and {result} result")
    except AssertionError:
        MSG = f"🛥️ ({target.__name__})FAILBOAT {name} :\n\texpected: {expected}\n\tresult: {result}"
        sys.exit(MSG)
