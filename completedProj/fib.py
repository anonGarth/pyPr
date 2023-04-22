"""
fib.py
4/14/23
Garth Shaw

ask the user for a number of fibonachi numbers to generate, then print a list of them to the console
"""

print("How many fib numbers would you like me to generate?")

num = int(input()) #number of fib numbers to calc

if num == 0:   
    fibNums = []
elif num == 1:
    fibNums = [1]
elif num == 2:
    fibNums = [1,1]
elif num > 2:
    fibNums = [1, 1]
    i = 1
    while i < (num - 1):
        fibNums.append(fibNums[i] + fibNums[i - 1])
        i += 1

print(fibNums)
