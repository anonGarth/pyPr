import string

def checkPassword(password: string) -> bool:
    upperFlag = False
    lowerFlag = False
    numFlag = False
    charFlag = False

    tPassword = password.replace(" ", "")

    if(len(tPassword) < 8):
        return False

    for x in tPassword:
        if(upperFlag and lowerFlag and numFlag and charFlag):
            return True
        elif(x in string.ascii_uppercase):
            upperFlag = True
        elif(x in string.ascii_lowercase):
            lowerFlag = True
        elif(x in string.digits):
            numFlag = True
        elif(x in string.punctuation):
            charFlag = True
    return False


testPass = "Ga5#bbbbbbbbbbbb" #Correct
testPass2 = "      HELL   OO APPleaaa234$ $" #remove whitesace example
#testPass3 = ":LKAJS:LGKHALJKLJSHGDFLJKHGAK2345" #missing lowercase
#testPass4 = "jahghagWERT234" #missing punctuation

print(checkPassword(testPass2))
#print(checkPassword(testPass2))
#print(checkPassword(testPass3))
#print(checkPassword(testPass4))