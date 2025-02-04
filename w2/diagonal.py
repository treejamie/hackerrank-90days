import sys



def diagonalDifference(arr):

    # now many rows?
    rows = len(arr)

    # calculate left hand index
    l_idx = [x for x in range(rows)]
    r_idx = [x for x in range(rows)]
    r_idx.reverse()

    # sum lists
    l_sum = []
    r_sum = []

    # iterate over the list
    for i, row in enumerate(arr):
        l_sum.append(
            row[l_idx[i]]
        )
        r_sum.append(
            row[r_idx[i]]
        )

    # return the result
    return abs(sum(r_sum) - sum(l_sum))


if __name__ == "__main__":

    def parse_input(fname):
        with open(fname) as fp:
            # first one is the total
            _total = fp.readline().strip()

            # define the data
            data = []

            # now read in the arrays
            for line in fp.readlines():
                data.append(
                    [int(x) for x in line.split()]
                )

        return data


    inputs = {
        "w2/diagonal/tc_0.txt": 15,
        "w2/diagonal/tc_2.txt": 52,
    }

    for k, v in inputs.items():
        s = parse_input(k)
        expected = v
        x = diagonalDifference(s)

        # assert
        try:
            assert x == expected
            print("✅: success {0} - {1} expected and {2} received".format(
                s,
                expected,
                x
            ))
        except AssertionError:
            msg = "❌: error in {0}:\n\texpected: {1}\n\treceived: {2} ".format(
                s,
                expected,
                x
            )
            sys.exit(msg)