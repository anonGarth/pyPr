"""
sumPair.py
Garth Shaw
4/26/2023

Given a list, add them up and see if they add up to a target value
"""




from typing import List, Tuple

def findSum(numbers: List[int], targetVal: int) -> Tuple[int,int]:

    for x in numbers:
        for y in numbers:
            if((x + y) == targetVal):
                return(x,y)

aList = [1, 3, 19, 20, 200, 2, 9, 10, 2, -5, 16]
myTuple = findSum(aList,220)
print(myTuple)
