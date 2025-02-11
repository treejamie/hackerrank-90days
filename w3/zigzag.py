"""
I don't like the silly challenges of fix lines because

1. If was broken in the way it was, fixing it would likley involve rewriting it to be less fragile
2. The "can only change X lines" is like pinning the tail on the donkey. There are multiple versions that pass the initial test, but that won't get accepted.
3. There's nicer ways to write it.

"""

import itertools
 

def findZigZagSequenceOriginal(a, n):
    # ok, sorting it makes sense, easy wins on first half.
    a.sort()

    # now we need the middle of the array
    mid = int(n/2)

    # now we can swap out the middle and the end, we have the apex
    a[mid], a[n-1] = a[n-1], a[mid]

    # now define the start and the end points
    st = mid + 1
    ed = n - 2

    # now enter a loop where we swap out the left for right and move inwards
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    # as I am doing my own test runners, return the value instead
    # now print it out in a bizzare funky manner, why not ' '.join(n)?
    # for i in range (n):
    #     if i == n-1:
    #         print(a[i])
    #     else:
    #         print(a[i], end = ' ')
    #
    # if we returned the thing we could assert, but no, we're leaving the evidence in stdout.
    # not sure why, but this isn't my rodeo - I'm just riding the horse
    return [x for x in a]



def findZigZagSequenceJC(a, n):
    """
    Much nicer - easily readable, no messy whiles and less to go wrong
    """
    # 1. sort it - lovely
    a.sort()

    # 2. calculate the middle of a
    middle = int(n/2)

    # 3. pop the apex value from the end
    apex = a.pop()

    # 4. slice into left and right which is reversed to give use the zag to the zig
    left = a[ 0 : middle ]
    right = sorted(a[ middle : n ], reverse=True)

    # 5. we have the parts, let's make our zigzag. 
    return [x for x in itertools.chain(left, [apex], right)]


    

#
#
# In a very real sense, a big part of these challenges is actuall
# figuring out custom

if __name__ == "__main__":

    def parse_input(fname):

        # define a list to hold the tests
        tests = []

        # read the file in
        with open(fname) as fp:
            total_tests = fp.readline()

            # define a test
            test = []

            # now iterate over the rest of file
            for i, line in enumerate(fp.readlines()):

                # if this is the first line then the test it is the count of the array
                if i % 2 == 0:
                    test.append(int(line.strip()))
                else:
                    test.append([int(x) for x in line.split()])
                    tests.append(test)
                    test = []
        
        return tests

    def parse_results(fname):
        # somewhere to store the results
        results = []

        # read the file in
        with open(fname) as fp:
            for line in fp.readlines():
                results.append(
                    [int(x.strip()) for x in line.split()]
                )
        # and done, return the results
        return results


    inputs = {
        "w3/testdata/zigzag_tc0_result.txt": "w3/testdata/zigzag_tc0.txt",
        "w3/testdata/zigzag_tc6_result.txt": "w3/testdata/zigzag_tc6.txt",
    }

    total_tests = 0

    for result, testcase in inputs.items():
        results = parse_results(result)
        tests = parse_input(testcase)

        for i in range(len(tests)):
            # what both functions should return in order to pass
            result = results[i]
            
            n = tests[i][0] # length of a
            a = tests[i][1] # the array

            result_hr = findZigZagSequenceOriginal(a, n)
            result_jc = findZigZagSequenceJC(a, n)
            
            assert result == result_hr
            assert result == result_jc

            total_tests += 1

print(total_tests, " tests ran")
