# Python Program to Check Prime Number
# A prime number is a number that can only be divided by itself and 1 without remainders.

num = int(input("Enter the number: "))

if num == 1:
    print("it is not a prime number")
for i in range(2, num):
    if num % i == 0:
        print(num, " is not a Prime number")
        break
else:
    print(num, " is Prime number")
