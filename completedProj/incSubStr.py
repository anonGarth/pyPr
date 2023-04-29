"""
incSubStr.py
Garth Shaw
4/27/2023

Given an unsorted list, find the longest increasing substring possible. not considering negative values bc that sounds hard
"""
from typing import List

def searchList(numList: List) -> int: #return a tuple for no reason other than i just learned how to use them so i think its fun
    length = 0 #chatGPT pointed out that these vars are confusing. should be current length and lastNumber. but oh well.
    highestLen = 0
    highestNum = numList[0]
    for x in numList:
        if(x > highestNum): #we know that it counted
            length += 1
            highestLen = length
            highestNum = x
        elif(x <= highestNum):
            length = 0
            highestNum = 0
    return highestLen


aList = [5,1,2,19,60,61,19]
length  = searchList(aList)
print(length)


