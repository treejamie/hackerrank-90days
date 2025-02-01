import sys


def countingValleys(steps, path):
    print(steps, path)



if __name__ == "__main__":

    def parse_input(fname):
        with open(fname) as fp:
            steps = fp.readline().strip()
            data = fp.readline().strip()
        
        return steps, data


    inputs = {
        "w2/valleys/tc0.txt": 1,
        "w2/valleys/tc1.txt": 2,
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