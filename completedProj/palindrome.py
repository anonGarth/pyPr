"""
Given a word, determine if its a palindrome

4/5/2023
Garth Shaw
"""

""" Process / psuedocode

1. get word
2. flip word
    create new str var
    add letters to it starting from the end
3. compare input and flipped word

"""

word = input()
word.lower()
newWord = ""
for x in word: #for every letter in word
    #print(x)
    newWord = x + newWord #set new word equal to x put in front of new word

if(newWord == word):
    print("word is a palindrome")
else:
    print("word is NOT a plaindrome")