myset = {"amma","nanna","veda"}
#print(myset)
myset.add("koti")
print(myset)
myset1 = {"anusha", "swapna","koti"}
#myset1.intersection_update(myset)
#print(myset1)
#myset2=myset1.intersection(myset)
#print(myset2)
myset3=myset.union(myset1)
print(myset3)
myset3.symmetric_difference_update(myset)
#myset4=myset3.intersection(myset)
print(myset3)












"""
myset2.add("sravani")
print(myset2)
myset.update(myset1)
print(myset)
myset.remove("nanna")
print(myset)
"""