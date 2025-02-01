import sys

def parse_input(f):
    with open(f) as fp:
        s = fp.readline()
    return s.strip()


def mars_exploration(s):
    # we expect chunks of three, so split it up
    # into chunks of three that we can count diffs on
    chunks = []
    for i, x in enumerate(s):
        # if not an iteration of three, skip.
        if i % 3 != 0:
            continue

        # make the slices
        l = i
        r = i + 3
        
        # add to the chunks
        chunks.append((s[l:r]))
    
    # now iterate over chunks and count differences
    diffs = 0
    for chunk in chunks:
        for i, char in enumerate("SOS"):
            if chunk[i] != char:
                diffs += 1

    return diffs




if __name__ == "__main__":
    
    inputs = {
        "w2/mars/mars_1.txt": 3,
        "w2/mars/mars_2.txt": 1,
        "w2/mars/mars_3.txt": 0,
        "w2/mars/mars_tc3.txt": 12 
    }

    for k, v in inputs.items():
        s, expected = parse_input(k), v
        x = mars_exploration(s)

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




