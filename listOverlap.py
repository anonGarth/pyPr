"""
listOverlap.py
Garth Shaw
4/9/2023



Given two lists(gen them randomly), return a new list that contains only the elements that are present in both lists
WITHOUT DUPLICATES IN THE NEW LIST AND USE LIST COMPREHENSION

"""

import random
listA = [random.randrange(1,20) for x in range(10)] #fill list a with 20 numbers 1 through 19
listB = [random.randrange(1,20) for x in range(10)]
finalList = [x for x in set(listA) if x in listB]
print(finalList)
