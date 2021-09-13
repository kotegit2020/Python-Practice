"""
details = "this is {tup[0]} from {tup[1]} and working for {tup[2]}"
tup = ("koti", "bangalore", "legato")
#print(tup[0])
print(details)
print(details.format(tup[0]))

from platform import python_version
print(python_version) 

#original = [['a','b'],['a','c'],['a','d']]
original = (('a','b'),('c','d'))
transpose = zip(*original)
print(list(transpose))
#print(list(zip(*original)))



def product(a,b):
    return a*b
def add(a,b):
    return a+b
b = True
print((product if b else add)(5,6))
if b:
     b = False
     b=b-1
else:
     print("exit from the loop")

a=[1,2,3,4]
b=a
print(a)
print(list(a))
print(b.copy())
print(b)
"""




























