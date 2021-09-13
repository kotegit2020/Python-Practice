d1={'a':1}
d2={'b':2}
#print({**d1,**d2})
d1.update(d2)
print(d1)
#print(d2)
d2.update(d1)
print(d2)