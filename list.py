"""
Generate a random list of numbers 10 long.
Print out any number from that list that is less than some other nuber

4/4/2023
Garth Shaw
"""

import random

myList = []
for i in range(0,10): #create a random list of numbers
    myList.append(random.randint(0,50))

print(myList)

print("What should the value be less than?")
lowVal = int(input())

for x in myList: #now, loop through list and if element at x is less than 20 it gets printed again
    if(x < lowVal):
        print(x)
