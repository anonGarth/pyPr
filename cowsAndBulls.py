"""
cowsAndBulls.py
4/15/23
Garth Shaw

Play the cows and bulls game. generate a random number and ask the user to guess it. for every digit that the user guesses correctly,
give them a cow. if they get the number right but the place wrong, they have a bull. print this out after every guess. keep asking until
they guess the number right.
"""

import string
import random

def calc(number, guess):
    cowCount = 0
    bullCount = 0
    for x in number:
        for y in guess:
            #Check if they got a cow
            if (number.index(x) == guess.index(y) and x == y): #getting closer: works if there arent duplicates of a number. if num is 5566 and guess is 5757 it will return 4 cows instead of 2
                cowCount += 1
                print(cowCount)




print("would you like to play Cows and Bulls? Enter a one to play")
controlVar = int(input())

while(controlVar == 1):
    number = str(random.randint(1, 9999)) #give us a random int between 1 and 9999
    print(number)

    guessed = False
    while(guessed == False):
        print("Please guess a number")
        guess = input()
        if(guess == number):
            print("you guessed the number!")
            guessed = True
        else:
            calc(number, guess)




    print("would you like to play again? enter a one if so")
    controlVar = int(input())
    