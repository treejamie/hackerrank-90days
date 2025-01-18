from functools import reduce


def _sum(x):
    """sums up the contexts of iterable x"""
    # note: many ways to do this, let's do the fancy pants
    # functional method, because this is a formal interview
    return reduce(lambda a, b: a + b, x)



def sortAndPop(arr, reverse=False):
    """Given an array, sort it, then pop last value and return array"""
    x = sorted(arr, reverse=reverse)
    x.pop()
    return x


def miniMaxSum(arr):
    """a function for a job interview"""
    # make two sets to process
    minArr = sortAndPop(arr)
    maxArr = sortAndPop(arr, reverse=True)
    
    # handle that off to be summed
    minValue = _sum(minArr)
    maxValue = _sum(maxArr)
    
    # normally that would be sent off to a custom function
    output = "{0} {1}".format(minValue, maxValue)
    print(output)


# call the function and experience the joy
miniMaxSum([1, 2, 3, 4, 5,])