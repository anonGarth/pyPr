"""
Rock paper scissors!

4/5/2023
Garth Shaw
"""

import random


flag = True
while flag:

    print("Please input either an r, p, or s for your choice. I promise i wont cheat.")

    usrChoice = input()
    comChoice = random.randint(1,3) #1 is rock, 2 is paper, 3 is scissors


    if (usrChoice == "r"): #im not checking if the if statements are correct. they seem good
        if(comChoice == 1):
            print("tie!")
        elif(comChoice == 2):
            print("I choose paper, you lose!")
        else:
            print("I choose scissors, you win!")
    elif(usrChoice == "p"):
        if(comChoice == 1):
            print("I choose rock, you win!")
        elif(comChoice ==2):
            print("tie!")
        else:
            print("I choose scissors, you lose!")
    elif(usrChoice == "s"):
        if(comChoice == 1):
            print("I choose rock, you lose!")
        elif(comChoice == 2):
            print("I choose paper, you win!")
        else:
            print("tie!")

    print("would you like to play again? 1 for yes")
    answer = int(input())
    if(answer != 1):
        flag = False






