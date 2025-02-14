import sys
import string



def pangram(maybe_pangram):
    # lowercase it and remove spaces
    maybe_pangram = [x.lower() for x in maybe_pangram if x != ' ']

    # make a dictionary of the counts
    counts = {k: 0 for k in string.ascii_lowercase}

    # now iterate through the maybe_pangram and count hits
    for x in maybe_pangram:
        counts[x] += 1

    # now make a list from the counts and use that to assess truthiness
    match all([v for v in counts.values()]):
        case True:
            return 'pangram'
        case _:
            return 'not pangram'




if __name__ == "__main__":

    def parse_input(fname):
        with open(fname) as fp:
            maybe_pangram = fp.readline().strip()
        
        return maybe_pangram


    inputs = {
        "w2/pangrams/tc0.txt": "pangram",
        "w2/pangrams/tc1.txt": "not pangram",
    }

    for k, v in inputs.items():
        s = parse_input(k)
        expected = v
        x = pangram(s)

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