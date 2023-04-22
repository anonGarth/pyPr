"""
given a list (or rand gen one)
Write one line of Python that takes this list and makes a new list that has only the even elements of this list in it.

Garth Shaw
4/5/2023
"""

#gen new list
import random
nums = [random.randrange(1,50) for x in range(10)] #this is one of the tricky lines
print(nums)


newNums = [x for x in nums if x%2 == 0] #another of those tricky lines

""" This is what the list comprehension above is equal to
newNums = []
for x in nums:
    if(x%2 == 0):
        newNums.append(x)
"""

print(newNums)






