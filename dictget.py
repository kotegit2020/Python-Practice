from operator import itemgetter

d={'a':1,'c':5,'b':4}
print(sorted(d.items(),key=itemgetter(1)))
#print(d.get('a',4))
#print(sorted(d,key=d.get))

