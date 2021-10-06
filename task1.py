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
n = float(input("Enter a number: "))
m = int(n) * 12
n = int(n)
for x in range(n, (m + 1)):

    if x % n == 0:

        print(x)