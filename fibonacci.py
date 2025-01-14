# Fibonacci Sequence
# The Fibonacci sequence is a series of numbers where each number is the sum of the two numbers that come before it:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, …

a = 0
b = 1
num = int(input("Enter a number to obtain fibonacci sequence: "))

if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, num):
        c = a + b
        a = b
        b = c
        print(c)
