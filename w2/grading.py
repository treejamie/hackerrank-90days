import sys



def gradingStudents(grades):
    """
    If the difference between grade and next multiple
    of 5 is less than 3 round the grade up.
    If less than 38, NO OP
    """
    # ensure they are ints
    grades = [int(grade) for grade in grades ]

    # make a list for processed grades
    processed = []

    #iterate through the grades, dong the thing
    for grade in grades:
        # work out the rounded
        rounded = round(grade / 5) * 5
        round_up = all([
                grade > 37,             # above 37 only
                rounded > grade,        # if rounded < grade, we don't round down
                (rounded - grade) < 3   # only if the distance is > 3 
        ])
        # operations
        if round_up:
            processed.append(rounded)
        else:
            processed.append(grade)
    
    return processed




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
        x = gradingStudents(s)

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