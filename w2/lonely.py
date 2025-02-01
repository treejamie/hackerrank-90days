import sys


def lonelyinteger(a):
    # first off, if there is only 1 item in the array, that's the answer
    if len(a) == 1:
        return a[0]

    # theres more than one thing so lets' do that then
    # if we comprehend into a dict, then new ones through a keyerror, but
    # then resulting ones don't. So if we make new keys have a value of false
    # and existing keys have a value of true, then all that needs to be done at
    # the end is find the false key
    groups = {}
    for maybe_billy_no_mates in a:

        # build the dictionary
        try:
            groups[maybe_billy_no_mates]
            groups[maybe_billy_no_mates] = True
        except KeyError:
            groups[maybe_billy_no_mates] = False
    
    # now find billy no mates
    for k, v in groups.items():
        if v == False:
            billy_no_mates = k
            break

    # return billy no mates
    return billy_no_mates



if __name__ == "__main__":

    def parse_input(fname):
        with open(fname) as fp:
            total = fp.readline()
            data = fp.readline()
            ints = [int(x) for x in data.split()]
        
        return ints


    inputs = {
        "w2/lonely/tc0.txt": 1,
        "w2/lonely/tc1.txt": 2,
        "w2/lonely/tc2.txt": 2,
    }

    for k, v in inputs.items():
        s, expected = parse_input(k), v
        x = lonelyinteger(s)

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