"""
functions.py
Garth Shaw
4/9/2023

Ask user for number, find if prime.
use functions to get input AND provide a default argument
"""

def getInput(question = "Please input a number"): #default value
    return int(input(question))

def isPrime(num):
    for x in range(2,num):
        if(num%x == 0): #we know it isnt prime
            return False
    return True


while(True):
    number = getInput() #default
    myBool = isPrime(number)
    print(myBool)


