# Find & Calculate Square Root Program in Python

# Solution-1: (Using Exponentiation)

# num = 64
# num1 = int(input("Enter a number here: "))
# sr = num1 ** (1 / 2)
# print("Square root of given number is: ", sr)

# Solution-2 (Using Math Module)
import math

num = int(input("Enter a number here: "))
sr = math.sqrt(num)
print("The square root of given number is: ", sr)
