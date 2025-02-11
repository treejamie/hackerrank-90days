"""
I don't like the silly challenges of fix lines because

1. If was broken in the way it was, fixing it would likley involve rewriting it to be less fragile
2. The "can only change X lines" is like pinning the tail on the donkey. There are multiple versions that pass the initial test, but that won't get accepted.
3. There's nicer ways to write it.

"""
def findZigZagSequence(a, n):
    # ok, sorting it makes sense, easy wins on first half.
    a.sort()

    # now we need the middle of the array
    mid = int(n/2)

    # now we can swap out the middle and the end, we have the apex
    a[mid], a[n-1] = a[n-1], a[mid]

    # now define the start and the end points
    st = mid + 1
    ed = n - 2

    # now enter a loop where we swap out the left for right and move inwards
    while(st <= ed):
        print(st, ed)
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    # now print it out in a bizzare funky manner, why not ' '.join(n)?
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    
    # if we returned the thing we could assert, but no, we're leaving the evidence in stdout.
    # not sure why, but this isn't my rodeo - I'm just riding the horse.return
    return



test_cases = 1 # int(input())
for cs in range (test_cases):
    a = [1, 2, 3, 4, 5, 6, 7]  # int(input())
    n = 7 # list(map(int, input().split()))
    findZigZagSequence(a, n)


    for x in [1, 2, 3, 7, 6, 5, 4]:
        print(x, end=' ')
    print()
