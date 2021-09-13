class myclass:
 def __init__(self,lname,fname):
    self.lname = lname 
    self.fname = fname
 def printname(self):
  print("my name is " +self.lname, self.fname)

class student(myclass):
 def __init__(self,lname, fname, rollnum):
     print("this is child class display")
     self.rollnum = rollnum

x = student("karthik", "number1", 2001)
#x.printname()
print(x.rollnum)


#y = myclass("koti","eleswaram")
#y.printname()
#print(myclass("koti", "eleswaram"))
#print(myclass("koti", "eleswaram").printname())



