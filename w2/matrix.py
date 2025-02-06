import sys



def flippingMatrix(matrix):
    """
    Ok, this is the deal.
    
    a   b   b   a
    b   c   c   b
    b   c   c   b
    a   b   b   a
    """

    # so we don't need to actually flip the matrix, 
    # just return the largest values in the mirror.

    n = len(matrix)
    s = 0

    # this iterates over the rows
    for i in range(n//2):

        # this iterates over the rows
        for j in range(n//2):

            # max does all the heavy lifting
            s += max(
                matrix[i][j],
                matrix[i][n-j-1],
                matrix[n-i-1][j],
                matrix[n-i-1][n-j-1],
                )
    return s


if __name__ == "__main__":

    def parse_input(fname):
        with open(fname) as fp:
            # first one is the total
            q = fp.readline().strip()
            n = fp.readline().strip()

            # define the data
            data = []

            # now read in the arrays
            for line in fp.readlines():
                data.append(
                    [int(x) for x in line.split()]
                )

        return q, n, data


    inputs = {
        "w2/matrix/tc0.txt": 414,
    }

    for k, v in inputs.items():
        q, n, s = parse_input(k)
        expected = v
        x = flippingMatrix(s)

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