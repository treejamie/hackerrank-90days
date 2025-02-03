import sys




def countingValleys2(steps, path):
    """
    Count D as -1 and U as +1.
    Valleys is the amount of times the counter ticks beneath zero minus 1
    """
    path_ints = [-1 if x == "D" else + 1 for x in path]

    # now, we start at zero and mutate an abstract concept of elevation
    elevation = 0

    # make a list of elevation based moves
    path_count = [] 
    valleys = 0
    #
    # and then you went in the garage to move.
    # is valleys the total amount of times you go into the lowest number
    #
    #
    for i, move in enumerate(path_ints):

        # first move always zero
        if i == 0:
            path_count.append(0)
        else:
            path_count.append(path_ints[i - 1] + move)

    # now we have a path count, so go over
    height = max(path_count)
    depth = min(path_count)
    print(path_count)
    print(height)
    print(depth)
    
    # elevation += move

    # if elevation < 0 and move > 0:
    #     valleys +=1 


    # valleys can be zero but not less than that
    #return valleys - 1 if valleys -1 > 0 else 0


def countingValleys3(steps, path):
    print(path)
    # we start at zero
    altitude = 0

    # define a journey to store moves
    journey = []

    # and now iterate through the steps
    for i, move in enumerate(path):
        match move:
            case "D":
                step = (altitude, altitude - 1)
                journey.append(step)
                altitude -= 1
            case "U":
                step = (altitude, altitude + 1)
                journey.append(step)
                altitude += 1
    
    print(journey)

    # is this just a case of cancelling moves?
    

def countingValleys(steps, path):
    # read the spec! sea level is magical.
    valleys = 0
    altitude = 0

    # go over the steps
    for p in path:
        # if we're going down, shift altitude 
        if p == 'D':
            altitude -= 1
        else:
            # key part: we're coming out of a valley
            # if altitude is -1 and we're coming up
            if altitude == -1:
                valleys +=1
            
            # increment altitude
            altitude +=1

    # return the valleys
    return valleys


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