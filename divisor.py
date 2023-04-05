"""
4/4/2023
Garth Shaw

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
"""
print("Please input a number and I will find the divisors")
usrNum = int(input())

print("divisors: ")
for x in range(1,usrNum):
    if(usrNum % x == 0):
        print(x)