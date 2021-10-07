#!python3 

"""
##### Task 1
Ask the user to enter an integer.
Print the multiplication tables up to 12 for that number
using a for loop instead of a while loop.
(2 points)

inputs:
int number

outputs:
multiples of that number

example:
Enter number:4
4 8 12 16 20 24 28 32 36 40 44 48
"""

import math 
num = int(input("Enter a number: "))
print(num, num*2, num*3, num*4, num*5, num*6, num*7, num*8, num*9, num*10, num*11, num*12)