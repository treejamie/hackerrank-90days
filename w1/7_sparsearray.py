import sys

def matchstrings(strings, queries):
    
    pass


    return 0


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

if __name__ == "__main__":
    
    # the data to work with
    datasets = [
        "w1/7_sparsearray_data_1.txt",
        "w1/7_sparsearray_data_2.txt",
        "w1/7_sparsearray_data_3.txt",
    ]

    # iterate
    for x in datasets:
        # parse
        scount, strings, qcount, queries = parse(x)

        # run
        result = matchstrings(strings, queries)

        # assert
        try:
            assert result == qcount
            print("✅: success {0} - {1} expected. {2} received".format(
                x,
                qcount,
                result
            ))
        except AssertionError:
            msg = "❌: error in {0} - {1} expected. {2} received".format(
                x,
                qcount,
                result
            )
            sys.exit(msg)
