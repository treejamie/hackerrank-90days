import sys



def countingSort(arr):
    # make the counting array
    count_list = [0 for _ in arr]

    # now do the count
    for val in arr:
        count_list[val] +=1 

    # and done 
    return count_list
    




if __name__ == "__main__":

    def parse_input(fname):
        with open(fname) as fp:
            _ = fp.readline()
            data = fp.readline()
            expected = fp.readline()
            print(data)

        data = [int(x) for x in data.split()]
        expected = [int(x) for x in expected.split()]
        return data, expected


    inputs = [
        "w2/counting/tc0.txt",
        "w2/counting/tc1.txt"
    ]

    for i in inputs:
        s, expected = parse_input(i)
        x = countingSort(s)

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