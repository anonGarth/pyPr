"""
blackjack.py
4/14/2023
Garth Shaw

Ideally, id like to make a program that plays blackjack with the user over the command line. Id like it to play normally, be
multiplayer, and keep track of how many chips the user has won or lost. classes might be helpful here.

Ill have to keep track of a deck which might be difficult: nvm found a cool library to handle all of that
"""


from playingcards import Card, CardCollection, Deck

print("Would you like to play Blackjack? Enter 1 to play")

playAgain = int(input())
while(playAgain == 1): #main game loop: allows the user to quit after 


    gameDeck = Deck() #gen a deck of cards
    gameDeck.shuffle() #shuffle the deck

    playerHand = gameDeck.draw_n(2)
    dealerHand = gameDeck.draw_n(2)

    #check if either player has blackjack

    if(playerHand)






    print("would you like to play again?")
    playAgain = int(input())






