from datetime import datetime


s = "07:05:45PM"

def timeConversion(s):
    # Write your code here
    # first get it from a string into a datetime
    # note: gotcha when parsing the hour - 12 hour parse - not 24!
    dt = datetime.strptime(s, "%I:%M:%S%p")

    # now remake it as the expected format
    result = datetime.strftime(dt, "%H:%M:%S")
    
    # return the result
    return result



if __name__ == "__main__":
    timeConversion(s)
