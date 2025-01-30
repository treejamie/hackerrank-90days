import sys

def parse_input(f):
    with open(f) as fp:
        s = fp.readline()
    return s.strip()


def mars_exploration(s):
    # the answer is the count of characters that are not S or O
    return len([x for x in s if x not in ['S', 'O']])




if __name__ == "__main__":
    
    inputs = {
        "w2/mars_1.txt": 3,
        "w2/mars_2.txt": 1,
        "w2/mars_3.txt": 0 
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




