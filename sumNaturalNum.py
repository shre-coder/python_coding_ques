# Find the Sum of Natural Numbers using the Python Program.

num = int(input("Enter a number here: "))

if num < 0:
    print("pleasse enter positive number")

else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1

print(sum)
