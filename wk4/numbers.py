import sys

def pickingNumbers1(a):
    # sort it first
    # a.sort()

    # set variabls up
    i = 0
    l = len(a) - 1
    ml = 1
    subs = []

    # now loop
    while i <= l:
        # this the end? (beautiful friend, the end...)
        if i ==  l:
            subs.append(ml)  # bank the current max length cos the party is over
            ml = 1
            break

        # is next thing less than one?
        if a[i + 1] - a[i] <= 1:
            ml += 1          # increment the max length
        else:
            # nope, we reached the end of the streak
            subs.append(ml)  # bank it
            ml = 1           # reset the length
        
        # increment the index
        i += 1

    # le done
    return max(subs)


def in_bounds(x, arr_in, arr_out):
    # base case is that there no arr_in left
    if len(arr_in) == 0:
        return arr_out
    
    # now we want everything in the array within abs(1)
    a = []
    for y in arr_in:
        if abs(x - y) <= 1:
            a.append(y)
    
    # append a onto array_out
    arr_out.append(a)
    
    # now pop off the end and call again
    return in_bounds(arr_in.pop(), arr_in, arr_out)


def subarrays(x, a_in, a_out):
    
    # define distance
    distance = x + 1

    # get everything within distance of the target
    z = list(filter(lambda y: y <= distance, a_in))

    # append it to the a_out
    a_out.append(z)

    # remove everything from a_in that is in a_out
    foo = [x for x in a_in if x not in z]

    # the base case
    if len(foo) == 0:
        return a_out

    # now call the function again
    return subarrays(foo[0], foo, a_out)
    


def pickingNumbers(a):
    """
    Subarrays of a that are less than 1 int away from each other.

    categorised as a frequency counting problem
    """
    #  sort the array
    a.sort()

    # get the first
    start = a[0]

    # convert everthing into subarrays 
    subs = subarrays(start, a, [])

    # call max on a list comprehension of len(x) in subs and that is our answer
    return max([len(x) for x in subs])




tests = [
    [
        [4, 6, 5, 3, 3, 1],
        3,
        "test one"
    ],
    [
        [1, 2, 2, 3, 1, 2],
        5,
        "test two"
    ]
]

target = pickingNumbers

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
        print("✅: SUCCESS - {1} expected and {0} result".format(
            result,
            expected,
        ))
    except AssertionError:
        msg = "🛥️ FAILBOAT {0} :\n\texpected: {2}\n\tresult: {1} ".format(
            name,
            result,
            expected,
        )
        sys.exit(msg)
