"""
Camel Case - Challenge 5, Week 1.
https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem
"""

import sys


# set to true if for hackerrank submission
PRINT=False


def camel_case(token: str) -> str:
    """
    A program that creates or splits Java style Camel Case variable, method, and class names.

    parameters:
        token (str): a semi-colon seperated string containing configuration and a target string
                    C: combine, S: seperate
                    M: methdod, C: class, V: variable

    returns:
        str: a camel case string coverted for variable, method or class name configuration

    examples"
        >>> camel_case('C;V;can of coke')
        'canOfCoke'
        >>> camel_case('S;M;sweetTea()')
        'sweet tea'
        >>> camel_case('C;C;mirror')
        'Mirror'
        >>> camel_case('C;M;santa claus')
        'santaClaus()'
    """
    # split into operation [C|S], variant[M|C|V] and string
    operation, variant, target = token.split(';')

    # C is to combine
    # In the case of a combine operation, the words will be a space-delimited
    # list of words starting with lowercase letters that you need to combine
    # into the appropriate camel case String. Methods should end with an empty
    # set of parentheses to differentiate them from variable names.
    if operation == 'C':

        # split on spaces and rejoin as TitleCase
        result = ''.join([t.title() for t in target.split()])

        # v is a variable, so lowercase first item
        if variant == 'V':
            result = result[0].lower() + result[1:]
        
        # m is method, so we need parenthesis and a lowercase start
        if variant == 'M':
            if result[-2:] != '()':
                result = f'{result}()'
                result = result[0].lower() + result[1:]

    # S is to split
    # in the case of a split operation, the words will be a camel case method,
    # class or variable name that you need to split into a space-delimited list
    # of words starting with a lowercase letter.
    elif operation == 'S':

        # split on uppercase letters and add spaces
        result = ''.join(
            map(lambda x: ' ' + x.lower() if x.isupper() else x, target)
        )

        # if first character is a space, remove it
        if result[0] == ' ':
            result = result[1:]

        # M is a method, so ensure we have parenthesis
        if result[-2:] == '()':
            result = result.replace('()', '')
    
    # if we're on HackerRank, print it
    if PRINT:
        print(result)

    # all done, return result
    return result


# HackerRank made you write all of the runner for this one as well.
# that doesn't seem all that 'basic'
if __name__ == '__main__' and PRINT:
    for line in sys.stdin.readlines(): 
        camel_case(line.strip())
