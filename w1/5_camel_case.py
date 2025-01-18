input="""
S;V;iPad
C;M;mouse pad
C;C;code swarm
S;C;OrangeHighlighter
"""

input2="""
C;V;can of coke
S;M;sweatTea()
S;V;epsonPrinter
C;M;santa claus
C;C;mirror
"""
input3="""
S;M;sweatTea()
"""

def to_camel_case(target):
    # this is a bit easier
    return target.title().replace(" ", "")


def from_camel_case(target):
    # this will a little involved
    _processed = ""

    # break it up into a list with underscores ahead of caps
    t = list(map(lambda x: '_' + x.lower() if x.isupper() else x, target))

    # do this one in a forloop to make it easier to read
    for i, c in enumerate(t):
        if c.startswith("_"):
            _processed += c.replace("_", "")  if i == 0 else c.replace("_", " ")
        else:
            _processed += c

    # all done
    return _processed


def to_method(target, operation="C"):
    # slice off the head, make the tail, glue it all back together again
    # if there are alread parens and we would have added them, return
    if target[-2:] == "()" and operation == "C":
        return target

    # if the operation was a split, return the variable form
    if operation == "S":
        return to_variable(target)

    # no more edge cases, do the thing
    return "{0}()".format(to_variable(target))


def to_variable(target):
    if target[-2:] == "()":
        target = target.replace("()", "")

    head, *tail = target
    return "{0}{1}".format(head.lower(), "".join(tail))


def _transform(operation, transformation, target):
    # strip any space from target, just to ensure we are getting nice clean input
    target = target.strip()

    # this will be the returned string
    _processed = ""

    # operate first
    match operation:
        # split a word from camelCase
        case "S":
            _processed = from_camel_case(target)

        # combine words together
        case "C":
            _processed = to_camel_case(target)
        # life isn't always smooth
        case "_":
            raise Exception("unknown operation")
    
    # transform second
    match transformation:
        case "M":
            _processed = to_method(_processed, operation)
        case "C":
            pass
        case "V":
           _processed = to_variable(_processed, operation)
        # sometimes things break
        case "_":
            raise Exception("unknown transformation")

    # done - return the processed strong
    return _processed


def make_the_case(input):
    # read the lines into a list because lists are awesome
    parts = [x.strip() for x in input.split("\n") if x != ''] 

    # split the parts into tokens
    tokens = [y.split(";") for y in parts]
    
    # transform the tokens, use the args operator to our advantage
    transformed = [_transform(*t) for t in tokens]

    # now returned the transformed
    return transformed


    # NOTE: I could have used a triply nested list comprehension
    #       but I am trying to make friends - not show off. Plus
    #       someone in the future may not understand the triple
    #       nesting and introduce a bug.




if __name__ == "__main__":
    print(make_the_case(input3))