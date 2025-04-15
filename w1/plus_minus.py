"""
This is the first challenge of week 1.

https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem

Given an array of integers, calculate the ratios of its elements that are
positive, negative, and zero. Print the decimal value of each fraction on a
new line with 6 places after the decimal.
*/
"""




def _format_ratio(x):

    return format(x, '6f')
    


def plusMinus(arr):
    # the total amount of items in the array
    l = len(arr)
        
    # positive values total and then as a ratio
    p = len([x for x in arr if x > 0]) / l
    fmt_p = _format_ratio(p)            

    # negative values
    n = len([x for x in arr if x < 0]) / l
    fmt_n = _format_ratio(n)

    # zero values
    z = len([x for x in arr if x == 0]) / l
    fmt_z = _format_ratio(z)

    # build the answers and print them out
    answers = [fmt_p, fmt_n, fmt_z]
    
    for answer in answers:
        print(answer)

    # return the answer because reasons
    return answer



# call it
plusMinus([-4, 3, -9, 0, 4, 1])