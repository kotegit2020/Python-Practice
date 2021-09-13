str1 = "koti"
mydict = { }
for x in str1:
    if x.lower() in mydict:
        mydict[x.lower()] += 1
    else:
        mydict[x.lower()] = 1

print(mydict)
