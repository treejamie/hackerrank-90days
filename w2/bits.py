import sys



def flippingBits(n):
    print(n)



if __name__ == "__main__":

    def parse_input(fname):
        with open(fname) as fp:
            _ = fp.readline()
            raw = fp.readlines()

        # make the data
        data = {
            'grades': [],
            'expected': []
        }
        mode = 'grades'
        for x in raw:
            cleaned = x.strip()

            if cleaned == '-':
                mode = 'expected'
            else:
                data[mode].append(int(cleaned))

        return data['grades'], data['expected']


    inputs = [
        "w2/grading/tc0.txt"
    ]

    for i in inputs:
        s, expected = parse_input(i)
        x = flippingBits(s)

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