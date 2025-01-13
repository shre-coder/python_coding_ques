# Find the Largest Among Three Numbers
num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))

if num1 > num2:
    if num1 > num3:
        print("Num1 is the largest of three numbers.")
    else:
        print("Num3 is the largest of three numbers.")
elif num2 > num1:
    if num2 > num3:
        print("Num2 is the largest of three numbers.")
    else:
        print("Num3 is the largest of three numbers.")
