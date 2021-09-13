
"""
lst = [10,40,30,20,50]
def minIndex(lst):
 return(min(range(len(lst)),key=lst.__getitem__))
def maxIndex(lst):
 return(max(range(len(lst)),key=lst.__getitem__))
print("minimum index is:", minIndex(lst))
print("maximum index is:", maxIndex(lst))
"""

import sys
print(sys.executable)
