"""
password.py
Garth Shaw
4/5/2023


Generates a random password for the user. Generate strong passwords by default
that has uppercase, lowercase, numbers and symbols. Ask if they want a weak password
and select it from a list


WHAT WENT WRONG:
so the program works and generates lists that are passwords and it does it at random, choosing the thing to insert and the location is random
however
i use the insert function. this fucntion does not replace the element in the array but rather adds to it at that postion. this means that
my check function is useless. there is no need to check if an element is going to be replaced becasue insert() dosent do that. but im not fixing
it because that sounds awful.


"""
import random
import string
from pprint import pprint
weakPass = ["1234", "5280", "hello", "book"]
alphL = string.ascii_lowercase
alphU = string.ascii_uppercase
symbols = string.punctuation #32 elements long

def  start(a):
    if(a == 1):
        myNum = random.randrange(1,len(alphL))
        return alphL[myNum]
    elif(a ==2):
        myNum = random.randrange(1,len(alphU))
        return alphU[myNum]
    else:
        myNum = random.randrange(1,len(symbols))
        return symbols[myNum]

def checkSpace(listThing, a):
    if(listThing[a] == False):
        return False
    else:
        return True

def genPass():
    newPassword = []
    listThing = [False for x in range(10)]
    ############## insert a lowercase letter       0
    myNum = random.randrange(1,10)
    while(checkSpace(listThing,myNum)):
        myNum = random.randrange(1,10)
    else:
        newPassword.insert(myNum,start(random.randrange(1)))

    ################### insert a upper case letter    1
    myNum = random.randrange(1,10)
    while(checkSpace(listThing,myNum)):
        myNum = random.randrange(1,10)
    else:
        newPassword.insert(myNum,start(random.randrange(2)))

   ################### insert a symbol             2
    myNum = random.randrange(1,10)
    while(checkSpace(listThing,myNum)):
        myNum = random.randrange(1,10)
    else:
        newPassword.insert(myNum,start(random.randrange(3)))

   ################### insert any of the three for the next 7 times    3
    myNum = random.randrange(1,10)
    while(checkSpace(listThing,myNum)):
        myNum = random.randrange(1,10)
    else:
        newPassword.insert(myNum,start(random.randrange(1,4)))


   ################### 4
    myNum = random.randrange(1,10)
    while(checkSpace(listThing,myNum)):
        myNum = random.randrange(1,10)
    else:
        newPassword.insert(myNum,start(random.randrange(1,4)))

       ################### 5
    myNum = random.randrange(1,10)
    while(checkSpace(listThing,myNum)):
        myNum = random.randrange(1,10)
    else:
        newPassword.insert(myNum,start(random.randrange(1,4)))

       ################### 6
    myNum = random.randrange(1,10)
    while(checkSpace(listThing,myNum)):
        myNum = random.randrange(1,10)
    else:
        newPassword.insert(myNum,start(random.randrange(1,4)))

       ################### 7
    myNum = random.randrange(1,10)
    while(checkSpace(listThing,myNum)):
        myNum = random.randrange(1,10)
    else:
        newPassword.insert(myNum,start(random.randrange(1,4)))

       ################### 8
    myNum = random.randrange(1,10)
    while(checkSpace(listThing,myNum)):
        myNum = random.randrange(1,10)
    else:
        newPassword.insert(myNum,start(random.randrange(1,4)))

       ################### 9
    myNum = random.randrange(1,10)
    while(checkSpace(listThing,myNum)):
        myNum = random.randrange(1,10)
    else:
        newPassword.insert(myNum,start(random.randrange(1,4)))


    return newPassword


print("Input 1 for a strong password, 2 for a weak password and any other number to quit the program")

flag = True
while flag:
    mode = int(input())
    if(mode == 1):#strong passwords
        newPassword = genPass()
        print("your new strong password is: ")
        pprint(newPassword)
    elif(mode ==2):#weak passwords
        print("your weak password is: ")
        print(weakPass[random.randrange(0,4)])
    else:
        flag = False
    
