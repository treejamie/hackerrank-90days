import sys

import re



def parse(fname):
    # read the file into a bunch of arrays
    with open(fname) as fp:
        # we know first line is a count, so just get that
        scount = fp.readline().strip()

        # the reset
        content = fp.readlines()

    strings = []
    queries = []

    # iterate over content and create gubbins, until we get a qcount
    # we know that we're working with strings, so use the same loop
    # and define a target we can switch at the right time
    target = strings

    for x in content:
        # strip it into a workable thing
        int_or_string = x.strip()
        
        # int or string?
        try:
            y = int(int_or_string)

            # we have the query count
            qcount = y
            
            # switch the target
            target = queries
            
        except ValueError:
            target.append(int_or_string)

    # and done
    return scount, strings, qcount, queries


def matchstrings1(strings, queries):
    """
    Let us just do an O(n2) first. We win no friends, but we do get a tick.
    """

    # somewhere to stash the results
    results = []

    # iterate
    for q in queries:

        # the regex is dynamic, so precompile it
        regex = re.compile(r'^{0}$'.format(q))

        # get the matches
        matches = [re.match(regex, s) for s in strings]

        # filter out the Nones
        result = len([m for m in matches if m is not None])

        # append to the results
        results.append(result)
    
    # and return the results
    return results




if __name__ == "__main__":
    
    # the data to work with
    datasets = {
        "w1/7_sparsearray_data_1.txt": [2, 1, 0],
        "w1/7_sparsearray_data_2.txt": [1, 0, 1],
        "w1/7_sparsearray_data_3.txt": [1, 3, 4, 3, 2],
    }

    # iterate
    for fname, expected_results in datasets.items():
        # parse
        scount, strings, qcount, queries = parse(fname)

        # run
        results = matchstrings1(strings, queries)

        # assert
        try:
            assert results == expected_results
            print("✅: success {0} - {1} expected and {2} received".format(
                fname,
                expected_results,
                results
            ))
        except AssertionError:
            msg = "❌: error in {0}:\n\texpected: {1}\n\treceived: {2} ".format(
                fname,
                expected_results,
                results
            )
            sys.exit(msg)



