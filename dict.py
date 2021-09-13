from typing import AsyncGenerator


mydict = {
    "name" : "koti",
    "age" : 29,
    "relation" : "son"
}
for x,y in mydict.items():
    print(x,y)

"""
print(mydict.items())
mydict.update({"name":"koteswar"})
print(mydict)

print(mydict["name"])
print(len(mydict))
print(mydict.get("age"))
print(mydict.keys())
mydict["sex"]="male"
print(mydict)
print(mydict.values())
""" 

