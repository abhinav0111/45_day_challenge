def printDups(s):
    l = list(s)
    for i in l:
        if l.count(i) > 1:
            print(i, " count is ", l.count(i))


printDups('geeksforgeeks')
