import sys


def countingValleys(steps, path):
    """
    Count D as -1 and U as +1.
    Valleys is the amount of times the counter ticks beneath zero minus 1
    """
    path_ints = [-1 if x == "D" else + 1 for x in path]

    # now, we start at zero and mutate an abstract concept of elevation
    elevation = 0
    valleys = 0
    for move in path_ints:
        elevation += move

        if elevation < 0 and move > 0:
            valleys +=1 

    # valleys can be zero but not less than that
    return valleys - 1 if valleys -1 > 0 else 0



if __name__ == "__main__":

    def parse_input(fname):
        with open(fname) as fp:
            steps = fp.readline().strip()
            data = fp.readline().strip()
        
        return steps, data


    inputs = {
        "w2/valleys/tc0.txt": 1,
        "w2/valleys/tc1.txt": 2,
        "w2/valleys/tc2.txt": 0,
        "w2/valleys/tc4.txt": 1,
        "w2/valleys/tc5.txt": 1,
    }

    for k, v in inputs.items():
        steps, path = parse_input(k)

        expected = v
        x = countingValleys(steps, path)

        # assert
        try:
            assert x == expected
            print("✅: success {0} - {1} expected and {2} received".format(
                path,
                expected,
                x
            ))
        except AssertionError:
            msg = "❌: error in {0}:\n\texpected: {1}\n\treceived: {2} ".format(
                path,
                expected,
                x
            )
            sys.exit(msg)