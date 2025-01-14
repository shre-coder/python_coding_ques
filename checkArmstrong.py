# An Armstrong number is a number that is equal to the sum of its own digits, each raised to the power of the number of digits in the number. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

num = int(input("Enter a number here: "))
order = len(str(num))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    cube = digit**order
    sum = sum + cube
    temp //= 10

if sum == num:
    print("It is an armstrong number.")
else:
    print("It is not a armstrong number.")
