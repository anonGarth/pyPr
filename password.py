"""
password.py
Garth Shaw
4/5/2023


Generates a random password for the user. Generate strong passwords by default
that has uppercase, lowercase, numbers and symbols. Ask if they want a weak password
and select it from a list

"""
import random
weakPass = ["1234", "5280", "hello", "book"]

def genPass():
    newPassword = ""



    return newPassword

    


print("Input 1 for a strong password, 2 for a weak password and any other number to quit the program")

flag = True
while flag:
    mode = int(input())
    if(mode == 1):#strong passwords
        newPassword = genPass()
        print(newPassword)
    elif(mode ==2):#weak passwords
        choice = random.randrange(0,4)
        print("your weak password is: ")
        print(weakPass[choice])
    else:
        flag = False
    
