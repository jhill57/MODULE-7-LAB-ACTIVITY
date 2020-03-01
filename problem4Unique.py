def appendlist (lst):
    y = []
    for i in lst:
        if i not in y:
            y.append (i)
    return y
thelist = (1,3,3,3,6,2,3,5)
result = appendlist(thelist)
print (result)
