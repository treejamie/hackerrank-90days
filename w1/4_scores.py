

def breakingRecords(scores):
    """
    scores: list of all scores over a season of games

    returns: a list of two items where:
      [0] is amount of times highscore was broken
      [1] is amount of times lowscore was broken
    """
    # keep track of the low and high scores.
    hc = [] # note: final high count is this list length
    lc = [] # note: final low count is the count of this list

    # so that we can keep track of the things processes
    processed = []

    # iterate over the scores
    for s in scores:
        # max min are functions of what is processed
        try:
            _mx = max(processed)
        except ValueError:
            # zero is not class as a high score so if the score
            # was zero, count it as processed and continue on.
            processed.append(s)
            continue

        try:
            _mn = min(processed)
        except ValueError:
            _mn = 0

        # count the highs and lows 
        if s > _mx:
            hc.append(s)

        if s < _mn:
            lc.append(s)
        
        # value was processesed, so append it
        processed.append(s)


    # done, return the count
    return [
        len(hc),
        len(lc)
    ] 
    

# the scores
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

# call the function
r = breakingRecords(scores)

# the result
print(r)