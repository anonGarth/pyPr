
"""" 
4/3/23
Garth Shaw
charInput.py

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

"""

print("Please input your name and age")
print("age: ")
age = int(input())

print("name: ")
name = input()


birth = 2023 - age #stops working 2024
hunYear = birth + 100

print("OK {name}, you will be 100 years old in the year {hunYear}".format(name=name, hunYear = hunYear))