"""
removeDupFromList.py
Garth Shaw
4/7/23

write a function that, given a list, removes any duplicates. Maybe overload the functions to accept, numbers, chars and strings?
no thats stupid, everything is a string
"""

def removeDup(a):

    aList = []
    for x in a:
         if(x not in aList):
            aList.append(x)

    return aList
            

            



myList = ["a","b","a","b","c","a", "b", "z", "a", "c"]
finalList = []
print(myList)
finalList = removeDup(myList)
print(finalList)