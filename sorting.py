"""
sorting.py
4/8/2023
Garth Shaw 

Write functions that implement a sorting algorithim. multiple sorting algorithms can be implemented. Maybe even time them?


this is to hard, come back to it later
"""
import random

############FUNCTIONS##############

def bubbleSort(aList): #return a sorted list
    n = len(aList)
    swapped = False

    for i in range(n-1):
        for j in range(0,n-i-1):
            if aList[j] > aList[j + 1]:
                swapped = True
                aList[j], aList[j+1] = aList[j+1], aList[j]
        
        if not swapped:
                return
    



############USE FUNCTIONS##############


