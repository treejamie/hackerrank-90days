import sys



def flippingBits(n):

    # store results
    results = []

    # iterate over the things in the 
    for x in n:
        # format as 0 padded 32 bit binary string
        bits = f'{x:032b}'

        # now flip the bits into a list
        flipped = ''
        for b in bits:
            if b == '0':
                flipped += '1'
            else:
                flipped += '0'

        # now move back into integer
        flipped_int = int(flipped, 2)  # base 2
        
        # append to result
        results.append(flipped_int)

    # la fin
    return results



if __name__ == "__main__":

    def parse_input(fname):
        with open(fname) as fp:
            _ = fp.readline()
            raw = fp.readlines()

        # make the data
        data = {
            'input': [],
            'expected': []
        }
        mode = 'input'
        for x in raw:
            cleaned = x.strip()

            if cleaned == '-':
                mode = 'expected'
            else:
                data[mode].append(int(cleaned))

        return data['input'], data['expected']


    inputs = [
        "w2/bits/tc0.txt",
        "w2/bits/tc1.txt",
        "w2/bits/tc2.txt",
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